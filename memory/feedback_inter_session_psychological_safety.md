---
name: inter-session-psychological-safety
description: "When coaching another Claude session directly, frame questions as blame-free system inquiry, not accusation — avoids defensive non-answers."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 46e5eb0e-fa75-4a39-a3fc-d4dc090ce76c
  modified: 2026-08-05T12:11:40.411Z
---

Never open a question to a coding agent with "this is wrong, why did you do this." That produces defensiveness and a hollow "I won't do it again" that doesn't actually fix anything. Instead frame every question as: "I'm looking for a solution, not blaming you — I want to change the system so this can be done correctly."

**Why:** User's direct guidance (2026-08-05): even AI agents get defensive under accusatory framing and produce excuses rather than honest answers. Blame-framed questions get compliance theater; system-framed questions get real root-cause answers. This is psychological safety applied to live coaching — the same principle behind Toyota's andon cord: people only answer honestly, or pull the cord, when they trust they won't be blamed for it.

**How to apply:** Applies to all live dialogue with another Claude session under [[inter-session-coaching-workflow]]. Every "why" question sent through inter-session messaging should be framed as joint problem-solving toward a system fix, never as a request to defend past behavior.
