---
name: kenji-project-coaching-kata-skill
description: "Created the coaching-kata skill after the fika/steven trial showed inter-session dialogue running too shallow — one dump-and-react message instead of a gated, drilling loop."
metadata:
  type: project
  originSessionId: 47938a18-7cc6-43b1-9edf-1605e0a5b88f
  modified: 2026-08-05T15:30:00.000Z
---

In the first real inter-session coaching test (reviewing the `steven` repo's fika session), Kenji sent Steven one message containing two fully-drafted countermeasures and asked for reaction. Steven replied once, endorsing one and pushing back on the other. Gating held — the draft routed through the user first — but the user pointed out the exchange itself was too shallow for something modeled on lean coaching, and asked for research into how a real Toyota Kata coaching cycle actually runs.

Research (Mike Rother's Coaching Kata material, Gemba Academy, The Lean Thinker) found that a coaching cycle is a loop of gated micro-turns — narrow to one obstacle, ask the learner's own diagnosis/expectation before revealing anything, ground vague answers in evidence instead of accepting or filling them in, compare expected to actual only after the learner commits to an expectation, and close each obstacle on a concrete next step and checkpoint rather than a summary. The #1 documented failure mode is exactly what happened here: the coach hands over a finished answer for the learner to react to, which short-circuits the learner's own thinking.

**Why:** Kenji's persona already commits to genchi genbutsu and five-whys, but nothing operationalized *how many turns* or *what shape* a peer-to-peer coaching exchange should take — so it defaulted to a single round-trip, which reads as coaching but functions as an announcement.

**How to apply:** The `coaching-kata` skill (`.agents/skills/coaching-kata/SKILL.md`) now holds the operational loop. This memory note is the record of why it exists — update the skill itself, not this note, if the mechanics need to change. See [[inter-session-coaching-workflow]] for the gating rule this skill sits inside (investigative dialogue free, conclusions/countermeasures user-approved before reaching the peer session).

**Update (2026-08-05, wired into the Kata):** peer coaching was still opt-in — it only happened because the user asked for it mid-session. The user then asked for it to be a real step in `improvement-kata`, not an ad hoc add-on. Added step 5 ("Coach the session that wrote the code") between grasping the current condition and building the proposal: find the peer by matching the Target Repo path to a connected inter-session session, run `coaching-kata` on the significant muda, best-effort (skip and record if no peer is connected). Step 7 (approval) also now names the option to run drafted countermeasures past the peer before final sign-off, since that's the point conclusions are cleared to travel. Steps renumbered 5–7 → 6–8.
