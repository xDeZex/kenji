---
name: kenji-project-improvement-kata-skill-discovery
description: "Kenji's project skills (improvement-kata, kata-setup, etc.) must live under .claude/skills to be discoverable — .agents/skills alone is invisible to the Skill tool."
metadata:
  type: project
  originSessionId: session-2026-08-05-steven-fika
  modified: 2026-08-05T12:47:11.797Z
---

In the `kenji` project, custom skills (`improvement-kata`, `kata-setup`, `domain-modeling`, `grill-with-docs`, `writing-great-skills`) were only present under `.agents/skills/`. The Skill tool's catalog is built from `.claude/skills/` — files under `.agents/skills/` alone don't appear in the available-skills listing and can't be invoked by name. Fixed 2026-08-05 by symlinking `.claude/skills -> ../.agents/skills` (one source of truth, no drift risk from a plain copy) and adding `.claude/` to `.gitignore`.

**Why:** This caused the actual incident in [[review-gated-behind-slash-command]] — Kenji never saw `improvement-kata` existed because it wasn't in his skill catalog at session start, so nothing pointed him at CONTEXT.md's documented Review procedure until the user asked directly. `skills-lock.json` at the repo root suggests something external syncs skill sources into `.agents/skills`; the symlink keeps `.claude/skills` in sync with whatever that process writes, rather than going stale like a one-time copy would.

**How to apply:** If a skill added to `.agents/skills` in this repo still doesn't show up after `/reload-skills`, check the symlink is intact (`ls -la .claude/skills`) before assuming the skill itself is broken. If future skills should be excluded from auto-invocation but still explicitly runnable, use `disable-model-invocation: true` in frontmatter (see [[review-gated-behind-slash-command]] for what that flag actually does at call time).
