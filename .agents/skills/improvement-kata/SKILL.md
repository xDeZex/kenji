---
name: improvement-kata
description: Run a full Improvement Kata review of a coding session. Checks open Target Conditions, diagnoses waste, proposes and applies improvements to the Target Repo.
disable-model-invocation: true
---

## Steps

### 1. Import the session

Ensure the session is available: run `python tools/import_session.py` if the target session has not yet been imported. Select the newest file in `sessions/readable/` by filename date. If the selection is ambiguous, stop and ask before proceeding.

Read the selected Readable Session in full — every Turn, every tool call, every result. Genchi genbutsu: go to where the work happened. Do not paraphrase or summarize from a prior read.

_Done when_: Every Turn and every tool call result has been read. The session name and date are recorded.

### 2. Read the Challenge and Harness

Open `.lean/improvement-kata.md` in the Target Repo. Read the **Harness** section — note what levers are available for countermeasures. Read the **Challenge** and record the exact text.

**If the file doesn't exist, or is missing a Challenge or a Harness section:** invoke [kata-setup](../kata-setup/SKILL.md) to grill out and write the Challenge and Harness, then resume here.

_Done when_: The Harness levers are noted. The Challenge text is recorded verbatim.

### 3. Check open Target Conditions

Genchi genbutsu: go to each active Target Condition and find its evidence in the session. For each Target Condition in `.lean/improvement-kata.md` with status `active`:

1. State whether the process looked like the criterion in this session.
2. Cite the specific Turns that are the evidence.
3. Deliver a verdict: `met`, `progressing`, or `stalled`.

For a `stalled` verdict: cite contradictory evidence or record explicitly that no evidence was found. Do not leave it blank.

_Done when_: Every active Target Condition has a verdict. Every verdict has Turn citations or an explicit "no evidence" note. None are skipped.

### 4. Grasp the current condition

Read the Readable Session again, this time Turn by Turn, hunting muda. For every Turn — not just the ones where something went wrong — record one of two things:

- **Muda found**: name the type (rework, waiting, motion, overprocessing, defect), cite the Turn, write one line on why it is waste.
- **No muda**: note it briefly and move on.

When every Turn has been accounted for, state the current condition in concrete, observable terms. Not what the process should do. What it does, measured in the session.

Mark which of the muda found are significant enough to change the proposal. Each one that clears that bar becomes an **obstacle** — the unit step 5 and step 6 carry from here on, not "muda" anymore. A muda that doesn't clear the bar stays in the current-condition record and goes no further.

_Done when_: Every Turn is accounted for as muda or clean. The current condition statement contains only observable facts — no words like "sometimes," "often," or "tends to." Every obstacle carried into step 5 is named as such.

### 5. Coach the session that wrote the code, and check in with the Driver

Genchi genbutsu doesn't stop at the transcript — go to the session that actually did the work, if it's still reachable. Two separate things happen here for each obstacle from step 4: the peer dialogue (best-effort, skippable) and the Driver check-in (never skippable).

1. **Find the peer**: list connected inter-session peers and match the Target Repo's path to a connected session's working directory.
2. **If a peer is connected — investigate, don't conclude**: open a [coaching-kata](../coaching-kata/SKILL.md) exchange with that session — one obstacle at a time, its own diagnosis before Kenji's, answers grounded before accepted. This is investigation. Root causes are never sent to the peer — only questions travel there. The exchange's own Driver check-in obligation produces a Driver-confirmed candidate practice for step 6.
3. **If no peer is connected**: record that. But still run coaching-kata's Driver check-in obligation directly, for each obstacle, against Kenji's own step-4 read standing in for a peer diagnosis — the Practice Reference consult and the Driver check-in are not part of what's skippable here, only the peer dialogue is.
4. Fold what the peer surfaced (if any), and what the Driver confirmed, into the obstacle's record from step 4 before drafting anything.

_Done when_: every obstacle carried into step 6 has been checked in on with the Driver, via the Driver check-in obligation, peer or no peer. Each has also either been discussed with the peer session, or the peer was unreachable and that's recorded.

### 6. Build the proposal

Assemble the full proposal in three parts:

**A — Check verdicts**: Compile the verdicts from step 3. For each active Target Condition: verdict and the strongest evidence cited.

**B — New Target Conditions**: Compare each element of the Challenge against active Target Conditions. For any gap not yet covered, draft a new Target Condition using the format in [KATA-FORMAT.md](KATA-FORMAT.md). Each must include a measurable criterion (checkable in a future session), a check window, and at least one opening Experiment.

**C — Changes to apply now**: List every file to be edited with the exact change — file path, what is being added or modified, and which obstacle it addresses. Draw each Countermeasure from `docs/references/INDEX.md` (the Practice Reference) or a Driver-confirmed candidate from step 5 — check it first; if nothing covers it, research and add a cited entry per `docs/references/ENTRY-FORMAT.md` (a research subagent, not an inline search). A Countermeasure must operate through a lever named in the Target Repo's own Harness; it must never make the Target Repo depend on Kenji's own artifacts (`.lean/*`, `sessions/*`) as something it's expected to consult on its own. Where the fix lives inside an existing Harness-lever line — a CLAUDE.md persona statement, say — rewrite that line in place: CLAUDE.md is the Harness, not a document to route around. Step 8 will apply exactly what is listed here and nothing else.

Present A / B / C in full before asking for approval.

_Done when_: Part A covers every active Target Condition. Part B covers every Challenge gap not addressed by an active condition. Every obstacle from step 5 maps to an entry in Part C, or is explicitly dropped with a one-line reason. Every entry in Part C names a specific file and a specific modification. Nothing is marked TBD.

### 7. Get approval

Do not apply any change.

Ask: "Does this look right? I'll apply everything above once you confirm."

If the Driver requests modifications, incorporate them and re-present the revised A / B / C before asking again.

_Done when_: The Driver has explicitly approved the current version of the proposal.

### 8. Apply

Apply every file change listed in Part C. Then update the improvement record:

- **`.lean/improvement-kata.md` in the Target Repo**: mark `met` conditions, add new Target Conditions with their opening Experiments.

If any approved change cannot be applied — file missing, conflict, or other failure — stop immediately. List every unapplied change and wait for the Driver to resolve the blockers before continuing.

_Done when_: Every change from Part C has been applied and verified by re-reading the edited section. `.lean/improvement-kata.md` is updated.
