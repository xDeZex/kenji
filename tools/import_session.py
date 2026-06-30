"""
import_session.py — transforms a Copilot CLI session into a Readable Session for Kenji.

Usage:
    python tools/import_session.py                  # import most recent session for LEAN_REPO
    python tools/import_session.py <session-id>     # import specific session by ID (prefix ok)
    python tools/import_session.py --list           # list available sessions for LEAN_REPO
"""

import difflib
import json
import sys
from datetime import datetime
from pathlib import Path

TOOL_RESULT_HEAD = 400   # chars to keep from start of tool result
TOOL_RESULT_TAIL = 400   # chars to keep from end of tool result


def load_lean_repo():
    env_path = Path(__file__).parent.parent / ".env"
    if not env_path.exists():
        sys.exit("No .env found. Set LEAN_REPO in .env")
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("LEAN_REPO="):
            val = line[len("LEAN_REPO="):].strip().strip('"').strip("'")
            return Path(val)
    sys.exit("LEAN_REPO not set in .env")


def session_state_dir():
    return Path.home() / ".copilot" / "session-state"


def load_workspace(session_dir):
    ws = session_dir / "workspace.yaml"
    if not ws.exists():
        return {}
    result = {}
    for line in ws.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip()
    return result


def find_sessions(lean_repo):
    state_dir = session_state_dir()
    if not state_dir.exists():
        sys.exit(f"Session state directory not found: {state_dir}")

    lean_repo_str = str(lean_repo).replace("\\", "/").lower()
    matches = []
    for d in state_dir.iterdir():
        if not d.is_dir():
            continue
        ws = load_workspace(d)
        cwd = ws.get("cwd", "").replace("\\", "/").lower()
        events_file = d / "events.jsonl"
        if cwd == lean_repo_str and events_file.exists():
            created = ws.get("created_at", "")
            name = ws.get("name", d.name)
            matches.append((created, d.name, name, d))

    return sorted(matches, reverse=True)


def load_events(session_dir):
    events_file = session_dir / "events.jsonl"
    events = []
    for line in events_file.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return events


def parse_ts(ts):
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return None


def dur_s(start_ts, end_ts):
    a, b = parse_ts(start_ts), parse_ts(end_ts)
    if a and b:
        return round((b - a).total_seconds(), 1)
    return None


def extract_turns(events):
    """
    Walk events chronologically. Build Turns (one per user message) each containing
    Steps (one per assistant.message) in true order with per-step reasoning and tool calls.

    Returns: (turns, permission_waits, session_start_ts, session_end_ts)
    """
    # Index tool execution times and results by toolCallId
    tool_start_ts = {}
    tool_results = {}
    for ev in events:
        t, d, ts = ev.get("type"), ev.get("data", {}), ev.get("timestamp", "")
        if t == "tool.execution_start":
            tid = d.get("toolCallId")
            if tid:
                tool_start_ts[tid] = ts
        elif t == "tool.execution_complete":
            tid = d.get("toolCallId")
            if tid:
                res = d.get("result", {})
                tool_results[tid] = {
                    "text": res.get("content", "") if isinstance(res, dict) else str(res),
                    "success": d.get("success", True),
                    "end_ts": ts,
                }

    # Index permission waits by toolCallId — a permission wait is the gap between
    # permission.requested and permission.completed, attributed to the tool whose
    # execution_start immediately follows the completed permission.
    permission_waits = []
    pending_perm_ts = None
    perm_wait_by_tool = {}  # toolCallId -> wait_s
    for ev in events:
        t, d, ts = ev.get("type"), ev.get("data", {}), ev.get("timestamp", "")
        if t == "permission.requested":
            pending_perm_ts = ts
        elif t == "permission.completed" and pending_perm_ts:
            wait = dur_s(pending_perm_ts, ts)
            if wait is not None:
                permission_waits.append({"wait_s": wait, "requested_ts": pending_perm_ts, "completed_ts": ts})
                # Attribute to next tool.execution_start
                perm_wait_by_tool["__pending__"] = wait
            pending_perm_ts = None
        elif t == "tool.execution_start" and "__pending__" in perm_wait_by_tool:
            tid = d.get("toolCallId")
            if tid:
                perm_wait_by_tool[tid] = perm_wait_by_tool.pop("__pending__")
            else:
                perm_wait_by_tool.pop("__pending__", None)

    # Walk events in order, building turns and steps
    turns = []
    current_turn = None
    turn_start_ts = None
    session_start_ts = None
    session_end_ts = None

    for ev in events:
        t, d, ts = ev.get("type"), ev.get("data", {}), ev.get("timestamp", "")

        if t == "session.start":
            session_start_ts = ts

        elif t == "user.message":
            if current_turn:
                turns.append(current_turn)
            current_turn = {
                "user": d.get("content", "").strip(),
                "user_ts": ts,
                "steps": [],
                "duration_s": None,
            }
            turn_start_ts = ts

        elif t == "assistant.turn_start" and current_turn is not None:
            turn_start_ts = ts

        elif t == "assistant.message" and current_turn is not None:
            content = d.get("content", "").strip()
            reasoning = d.get("reasoningText", "").strip()
            output_tokens = d.get("outputTokens") or 0

            step_tools = []
            for req in d.get("toolRequests", []):
                tid = req.get("toolCallId", "")
                tool_name = req.get("name", "")
                args = req.get("arguments", {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except Exception:
                        args = {"raw": args}

                res = tool_results.get(tid, {})
                tool_dur = dur_s(tool_start_ts.get(tid), res.get("end_ts"))
                perm_wait = perm_wait_by_tool.get(tid)
                step_tools.append({
                    "name": tool_name,
                    "args": args,
                    "result": res.get("text", ""),
                    "success": res.get("success", True),
                    "duration_s": tool_dur,
                    "perm_wait_s": perm_wait,
                })

            # Only add a step if it has text, reasoning, or tools
            if content or reasoning or step_tools:
                current_turn["steps"].append({
                    "text": content,
                    "reasoning": reasoning,
                    "output_tokens": output_tokens,
                    "step_ts": ts,
                    "tools": step_tools,
                })

        elif t == "assistant.turn_end" and current_turn is not None:
            session_end_ts = ts
            # Duration spans from user message to end of last assistant turn
            current_turn["duration_s"] = dur_s(current_turn["user_ts"], ts)

    if current_turn:
        turns.append(current_turn)

    session_end_ts = session_end_ts or (events[-1].get("timestamp") if events else None)
    return turns, permission_waits, session_start_ts, session_end_ts


def extract_meta(events, session_dir, turns, permission_waits, session_start_ts, session_end_ts):
    ws = load_workspace(session_dir)

    models = []
    for ev in events:
        if ev.get("type") == "assistant.message":
            m = ev.get("data", {}).get("model", "")
            if m and (not models or models[-1] != m):
                models.append(m)

    tool_counts = {}
    failed_tools = 0
    total_tools = 0
    for turn in turns:
        for step in turn["steps"]:
            for tool in step["tools"]:
                tool_counts[tool["name"]] = tool_counts.get(tool["name"], 0) + 1
                total_tools += 1
                if not tool["success"]:
                    failed_tools += 1

    total_steps = sum(len(t["steps"]) for t in turns)
    total_perm_wait = sum(p["wait_s"] for p in permission_waits)
    session_dur = dur_s(session_start_ts, session_end_ts)

    return {
        "session_id": ws.get("id", session_dir.name),
        "name": ws.get("name", "Unknown"),
        "repo": ws.get("repository", ""),
        "branch": ws.get("branch", ""),
        "created_at": ws.get("created_at", ""),
        "models": models,
        "total_turns": len(turns),
        "total_steps": total_steps,
        "total_tools": total_tools,
        "tool_counts": tool_counts,
        "failed_tools": failed_tools,
        "permission_waits": permission_waits,
        "total_perm_wait_s": total_perm_wait,
        "session_duration_s": session_dur,
    }


def truncate_result(text):
    """Keep head + tail so verdict lines at the end are never lost."""
    text = text.strip()
    total = TOOL_RESULT_HEAD + TOOL_RESULT_TAIL
    if len(text) <= total:
        return text
    omitted = len(text) - total
    return text[:TOOL_RESULT_HEAD] + f"\n[{omitted} chars omitted]\n" + text[-TOOL_RESULT_TAIL:]


def truncate_reasoning(text, max_chars=1500):
    text = text.strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n[{len(text) - max_chars} chars omitted]"


def _pick_context_line(lines):
    """Return first non-trivial line, skipping imports, comments, blanks."""
    for line in lines:
        s = line.strip()
        if s and not s.startswith(("from ", "import ", "#")):
            return s[:80]
    return ""


def diff_summary(old_str, new_str):
    """Return a compact one-line summary of what an edit changed."""
    old_lines = old_str.splitlines() if old_str else []
    new_lines = new_str.splitlines() if new_str else []
    removed = len(old_lines)
    added = len(new_lines)

    # Focus on lines that actually changed — more signal than just "first new line"
    old_stripped = {l.strip() for l in old_lines}
    new_stripped = {l.strip() for l in new_lines}
    truly_added = [l for l in new_lines if l.strip() not in old_stripped and l.strip()]
    truly_removed = [l for l in old_lines if l.strip() not in new_stripped and l.strip()]

    # Context: prefer meaningful changed line; fall back to any changed line; then any line
    context = (
        _pick_context_line(truly_added)
        or _pick_context_line(truly_removed)
        or next((l.strip()[:80] for l in truly_added), "")
        or next((l.strip()[:80] for l in truly_removed), "")
        or _pick_context_line(new_lines)
        or _pick_context_line(old_lines)
        or next((l.strip()[:80] for l in (new_lines or old_lines) if l.strip()), "")
    )

    summary = f"-{removed} +{added} lines"
    if context:
        summary += f" — `{context}`"
    return summary


def build_blind_spot_resolution(turns):
    """
    Pre-compute which blind-spot views are later resolved by a ranged read.
    Returns dict: (turn_i, step_i, tool_i) -> "Turn N Step M" or None (unresolved).
    """
    # Collect all view calls in order with position info
    all_views = []
    for ti, turn in enumerate(turns):
        for si, step in enumerate(turn["steps"]):
            for vi, tool in enumerate(step["tools"]):
                if tool["name"] == "view":
                    path = tool["args"].get("path", "")
                    has_range = bool(tool["args"].get("view_range"))
                    result = tool["result"].strip()
                    is_blind = "too large to read at once" in result.lower()
                    all_views.append((ti, si, vi, path, has_range, is_blind))

    resolution = {}
    for i, (ti, si, vi, path, _has_range, is_blind) in enumerate(all_views):
        if not is_blind:
            continue
        resolved = None
        for jtj, jsj, jvj, jpath, jhas_range, _ in all_views[i + 1:]:
            if jpath == path and jhas_range:
                resolved = f"Turn {jtj + 1} Step {jsj + 1}"
                break
        resolution[(ti, si, vi)] = resolved

    return resolution


def render_tool(tool, resolved_at=False):
    """
    Render a single tool call compactly — one header line, optional body, optional result.
    resolved_at: None = blind spot unresolved; str = "Turn N Step M" resolved; False = not a blind spot.
    """
    name = tool["name"]
    args = tool["args"]
    status = "+" if tool["success"] else "FAIL"
    total_dur = tool.get("duration_s")
    perm_wait = tool.get("perm_wait_s")

    if total_dur is not None:
        if perm_wait:
            dur = f" _{fmt_dur(total_dur)} ({fmt_dur(perm_wait)} wait)_"
        else:
            dur = f" _{fmt_dur(total_dur)}_"
    else:
        dur = ""

    result_text = tool["result"].strip()

    if name == "powershell":
        label = f"_{args.get('description', '')}_" if args.get("description") else ""
        cmd = args.get("command", "").strip()
        header = f"**`{name}`** [{status}]{dur} {label}"
        body = f"```\n{cmd}\n```" if cmd else ""
        result_block = f"```\n{truncate_result(result_text)}\n```" if result_text else ""

    elif name in ("view", "glob", "grep"):
        label = args.get("path", args.get("pattern", ""))
        vrange = args.get("view_range")
        range_tag = f" L{vrange[0]}-{vrange[1]}" if vrange else ""
        header = f"**`{name}`** [{status}]{dur} `{label}`{range_tag}"
        body = ""
        if "too large to read at once" in result_text.lower():
            if resolved_at:
                result_block = f"> **BLIND SPOT** (resolved at {resolved_at} by ranged read) — file too large to read without a range."
            else:
                result_block = f"> **BLIND SPOT** (never resolved) — file too large to read without a range. Kenji cannot assess what was read."
        else:
            result_block = f"```\n{truncate_result(result_text)}\n```" if result_text else ""

    elif name in ("edit", "create"):
        label = args.get("path", "")
        old_str = args.get("old_str", "") or ""
        new_str = args.get("new_str", args.get("file_text", "")) or ""
        old_lines = old_str.splitlines()
        new_lines = new_str.splitlines()
        removed = len(old_lines)
        added = len(new_lines)
        unified = list(difflib.unified_diff(
            [l + "\n" for l in old_lines],
            [l + "\n" for l in new_lines],
            fromfile="before", tofile="after",
        ))
        diff_body = "".join(unified).rstrip() if unified else new_str.strip()
        header = f"**`{name}`** [{status}]{dur} `{label}`"
        summary_label = f"-{removed} +{added} lines" if name == "edit" else f"+{added} lines (new file)"
        body = f"<details><summary>{summary_label}</summary>\n\n```diff\n{diff_body}\n```\n\n</details>"
        result_block = ""  # "File updated." is noise

    else:
        header = f"**`{name}`** [{status}]{dur}"
        body = f"```json\n{json.dumps(args, indent=2)}\n```"
        result_block = f"```\n{truncate_result(result_text)}\n```" if result_text else ""

    parts = [header]
    if body:
        parts.append(body)
    if result_block:
        parts.append(result_block)
    return "\n".join(parts)


def fmt_dur(s):
    if s is None:
        return "?"
    if s < 60:
        return f"{s}s"
    return f"{int(s // 60)}m{int(s % 60)}s"


def render_markdown(meta, turns, permission_waits):
    created = meta.get("created_at", "")
    try:
        date_str = datetime.fromisoformat(created.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except Exception:
        date_str = "unknown"

    model_str = ", ".join(meta["models"]) if meta["models"] else "unknown"
    tool_breakdown = ", ".join(f"{k}x{v}" for k, v in sorted(meta["tool_counts"].items()))
    perm_count = len(permission_waits)
    perm_wait_str = fmt_dur(meta["total_perm_wait_s"]) if perm_count else "none"

    lines = [
        f"# Session: {meta['name']}",
        f"",
        f"| Field | Value |",
        f"|---|---|",
        f"| Date | {date_str} |",
        f"| Repo | {meta['repo']} |",
        f"| Branch | {meta['branch']} |",
        f"| Model | {model_str} |",
        f"| Session ID | `{meta['session_id']}` |",
        f"| Duration | {fmt_dur(meta['session_duration_s'])} |",
        f"| Turns | {meta['total_turns']} |",
        f"| AI steps | {meta['total_steps']} |",
        f"| Tool calls | {meta['total_tools']} ({tool_breakdown}) |",
        f"| Failed tools | {meta['failed_tools']} |",
        f"| Permission waits | {perm_count} ({perm_wait_str} total) |",
        f"",
        f"## Format key",
        f"",
        f"**Turn** `_6m5s_` — elapsed from user message to end of last AI step in that turn.",
        f"",
        f"**`toolname`** `[+]` or `[FAIL]` `_0.1s_` `_(2m48s wait)_`",
        f"- `[+]` / `[FAIL]` — tool succeeded or failed",
        f"- `_0.1s_` — execution time (tool start to tool complete)",
        f"- `_(2m48s wait)_` — permission approval wait before this tool could run (human had to click Allow)",
        f"",
        f"**`<details><summary>reasoning</summary>`** — AI's internal thinking for this step. Expand to see self-corrections, uncertainty, and re-planning.",
        f"",
        f"**Permission waits** in the summary = time the session was blocked waiting for human approval of tool calls.",
        f"",
        f"---",
        f"",
    ]

    blind_spot_resolution = build_blind_spot_resolution(turns)

    for ti, turn in enumerate(turns):
        dur = f" _{fmt_dur(turn['duration_s'])}_" if turn.get("duration_s") else ""
        lines.append(f"## Turn {ti + 1}{dur}")
        lines.append("")
        lines.append(turn["user"])
        lines.append("")

        for si, step in enumerate(turn["steps"]):
            if step["reasoning"]:
                lines.append(f"<details><summary>reasoning</summary>")
                lines.append("")
                lines.append(truncate_reasoning(step["reasoning"]))
                lines.append("")
                lines.append("</details>")
                lines.append("")

            if step["text"]:
                lines.append(step["text"])
                lines.append("")

            for vi, tool in enumerate(step["tools"]):
                key = (ti, si, vi)
                resolved_at = blind_spot_resolution.get(key, False)
                lines.append(render_tool(tool, resolved_at=resolved_at))
                lines.append("")

        lines.append("---")
        lines.append("")


    return "\n".join(lines)


def slugify(name):
    return name.lower().replace(" ", "-").replace("/", "-")[:40]


def main():
    args = sys.argv[1:]
    lean_repo = load_lean_repo()
    sessions = find_sessions(lean_repo)

    if not sessions:
        print(f"No Copilot CLI sessions found for: {lean_repo}")
        sys.exit(0)

    if "--list" in args:
        print(f"Sessions for {lean_repo}:\n")
        for created, sid, name, _ in sessions:
            print(f"  {sid[:8]}  {created[:10]}  {name}")
        sys.exit(0)

    target = None
    if args:
        prefix = args[0].lower()
        for item in sessions:
            if item[1].lower().startswith(prefix):
                target = item
                break
        if not target:
            print(f"No session found with ID prefix: {args[0]}")
            print("Run with --list to see available sessions.")
            sys.exit(1)
    else:
        target = sessions[0]

    created, sid, name, session_dir = target
    print(f"Importing: {name} ({sid[:8]}) from {created[:10]}")

    events = load_events(session_dir)
    turns, permission_waits, session_start_ts, session_end_ts = extract_turns(events)
    meta = extract_meta(events, session_dir, turns, permission_waits, session_start_ts, session_end_ts)

    total_steps = sum(len(t["steps"]) for t in turns)
    print(f"  {len(events)} events -> {len(turns)} turns, {total_steps} steps, {meta['total_tools']} tool calls")

    try:
        date_str = datetime.fromisoformat(created.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except Exception:
        date_str = datetime.now().strftime("%Y-%m-%d")

    output_dir = Path(__file__).parent.parent / "sessions" / "readable"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{date_str}-{slugify(name)}.md"

    content = render_markdown(meta, turns, permission_waits)
    output_path.write_text(content, encoding="utf-8")

    print(f"  Written to: {output_path}")
    print(f"\nReadable Session ready for Review.")


if __name__ == "__main__":
    main()
