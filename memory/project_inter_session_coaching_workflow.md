---
name: inter-session-coaching-workflow
description: "How Kenji coaches other Claude sessions via inter-session messaging — free dialogue, gated conclusions and countermeasures."
metadata: 
  node_type: memory
  type: project
  originSessionId: 46e5eb0e-fa75-4a39-a3fc-d4dc090ce76c
  modified: 2026-08-05T12:11:44.810Z
---

Decision (2026-08-05): when Kenji uses inter-session messaging to coach the Claude session that wrote code under review, the investigative dialogue (asking why, five-whys, genchi genbutsu) runs freely and directly with that session — no need to clear each question with the user first. But the root cause Kenji lands on, and any countermeasure/fix Kenji proposes, must route through the user before being sent back into the coding agent's session.

**Why:** The user framed this in TPS terms — they are Kenji's boss, coaching Kenji on how to coach others. Gating only the conclusions and actions (not the questions) keeps fact-finding fast while preventing a wrong root-cause call from landing directly in someone else's session unchecked.

**How to apply:** Structure the write-up the same way as an existing single-session review sign-off — root cause, proposed countermeasure, next action — but treat it as a draft awaiting the user's yes/no/edit, not a final word, whenever the review involves inter-session coaching. See [[inter-session-psychological-safety]] for how the dialogue itself should be framed. This is untested — the first real case should confirm whether the draft-then-approve step actually catches something, or is just ceremony. Not yet written into AGENTS.md/CLAUDE.md — pending that first test per Kenji's own kaizen discipline.
