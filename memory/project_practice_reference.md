---
name: kenji-project-practice-reference
description: "Created the Practice Reference (references/) and the Driver domain term after the steven/life trial showed Kenji drafting countermeasures from its own untested guesses or from its own review artifacts instead of real software-engineering practice."
metadata:
  type: project
  originSessionId: session-2026-08-06-coaching-depth-grill
  modified: 2026-08-06T00:00:00.000Z
---

Reviewing the `steven` repo's Conway's Game of Life session, Kenji drafted two countermeasures on the spot: "don't suppress stderr on git commands" (Kenji's own unsourced heuristic) and "defer to `.lean/improvement-kata.md`'s Challenge" (pointing the peer at Kenji's own review artifact, which was never part of the peer's actual Harness — the peer's repo never told it to read that file). The Driver caught both: a countermeasure needs a real source, and that source should never be Kenji's own artifact standing in as an authority the Target Repo is expected to consult.

The Driver also pointed out this is the same gap twice over: Kenji doesn't reliably know what good software-engineering practice looks like, even with a reference to check — and the Driver, running Kenji, knows more about that than Kenji can determine on its own. So the Driver isn't just an approver; the Driver is a source, on the same footing as an external citation.

**Why:** Countermeasure was already a defined term (`CONTEXT.md`), but nothing said where a Countermeasure's content should come from — so Kenji filled that gap with its own pretrained guesses, the same failure mode as an ungrounded Five Whys chain (see [[kenji-project-coaching-kata-skill]]'s 2026-08-06 update).

**How to apply:** `references/` now holds the Practice Reference — a lazily-grown, global catalog (`INDEX.md` + one file per entry, format in `ENTRY-FORMAT.md`). Every entry cites a source: an external reference, or the Driver directly with a date. It grows only when a live obstacle needs a practice it doesn't cover — no pre-populated categories. `coaching-kata`'s gate 6 checks it (researching if nothing fits) before bringing a candidate practice to the Driver; `improvement-kata` step 6C checks it before drafting each Countermeasure. Research for a missing entry is delegated to a subagent (the Agent tool, a specific question with a citation requirement), not run inline in Kenji's own context — same reasoning as forking any open-ended lookup: the search noise isn't worth keeping, only the cited answer is. "Driver" is now a defined term in `CONTEXT.md` — the human running Kenji, both the approver and a Practice Reference source. Update the skills and `CONTEXT.md` themselves if the mechanics need to change, not this note.
