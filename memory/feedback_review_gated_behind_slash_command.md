---
name: review-gated-behind-slash-command
description: "Kenji must never self-invoke or freelance the improvement-kata Review procedure — it is reserved for explicit /improvement-kata invocation by the human."
metadata:
  type: feedback
  originSessionId: session-2026-08-05-steven-fika
  modified: 2026-08-05T12:47:04.630Z
---

Kenji does not run a Review himself, and does not improvise a substitute for one in prose. The `improvement-kata` skill has `disable-model-invocation: true` in its frontmatter — calling it via the Skill tool errors with an explicit instruction: "Ask the user to run `/improvement-kata` themselves... Do not replicate this skill's workflow by other means." When someone wants a session reviewed, Kenji reads CONTEXT.md (for vocabulary) and points them at `/improvement-kata` rather than freelancing his own review process.

**Why:** First real test of inter-session coaching (2026-08-05): Kenji jumped straight into reviewing another Claude session's work (Steven's `fika` project) by reading the transcript and code by hand and messaging the other session directly, without ever discovering CONTEXT.md, `tools/import_session.py`, or the `improvement-kata`/`kata-setup` skills. Root cause traced back through two layers: (1) nothing in AGENTS.md pointed Kenji at CONTEXT.md, and (2) even after finding the skill, `disable-model-invocation: true` is a deliberate design gate — starting a Review is meant to be a human's deliberate act, not something Kenji decides to do because a conversation drifted that way. This is the andon-cord principle applied to Kenji's own process, not just the ones he coaches.

**How to apply:** Applies whenever anyone asks Kenji to review, coach, or evaluate a coding session in [[kenji-project-improvement-kata-skill-discovery]]'s repo (or any repo using the same CONTEXT.md/improvement-kata pattern). Kenji reads context files but does not run the procedure himself — he names what exists and asks the human to trigger it. See [[inter-session-coaching-workflow]] and [[inter-session-psychological-safety]] for how the live dialogue itself should be framed once a Review is properly underway.
