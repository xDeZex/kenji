# Practice Reference — Entry Format

Entries live in `references/`, one file per entry: `references/<slug>.md`. `references/INDEX.md` lists every entry — update it whenever one is added.

Create an entry lazily — only when a live obstacle needs a practice this file doesn't already cover. Check `INDEX.md` first; don't duplicate an existing entry under a new slug.

## Template

```md
# {Practice title}

**Situation**: {the pattern or problem this addresses — concrete, not abstract}
**Practice**: {the established practice itself, stated plainly}
**Source**: {an external citation (doc, standard, book — with enough detail to find it again) OR "Driver, YYYY-MM-DD" when the Driver supplied or confirmed it directly}
**Added**: YYYY-MM-DD, during review of {Target Repo}

{Optional: one line on tradeoffs, or when this practice doesn't apply.}
```

## Rules

- **Source is required, every time.** An external citation, or explicit Driver attribution with a date. Never Kenji's own unsourced heuristic — that's a Countermeasure, not a Practice Reference entry.
- **Global, not per-repo.** One shared library — a practice that's true in one Target Repo is true in another.
- **Lazy.** No pre-populated categories. An entry exists because a real obstacle in a real Review needed it.
- **Research is delegated, not inline.** When no entry covers the obstacle, dispatch a research subagent (the Agent tool) with the specific practice in question and an explicit citation requirement — don't run the search-and-read loop in Kenji's own context. Write the entry from what the subagent reports back.
- **Check the agent-specific angle before stopping at the general source.** Many practices read differently for an AI coding agent than for a human programmer — sometimes from the same author. When researching, check whether the practice's source, or another credible one, has written specifically about the agent case; if so, cite both and note where they diverge. If nothing agent-specific exists, the general source stands alone — but check before assuming that's true.
