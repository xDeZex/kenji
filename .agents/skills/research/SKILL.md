---
name: research
description: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user or you wants something researched.
---

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Check `docs/references/INDEX.md` and `docs/research/INDEX.md` first — if an entry already covers this, stop and point to it instead of re-researching.
2. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it.
3. Pick the entry's home: a reusable engineering practice feeding a Countermeasure goes in `docs/references/`, following `docs/references/ENTRY-FORMAT.md`; everything else — API behavior, tool docs, one-off factual questions — goes in `docs/research/`, following `docs/research/ENTRY-FORMAT.md`. 
4. Report back the file's path.
