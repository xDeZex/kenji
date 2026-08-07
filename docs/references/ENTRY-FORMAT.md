# Practice Reference — Entry Format

Entries live in `docs/references/`, one file per entry: `docs/references/<slug>.md`. `docs/references/INDEX.md` lists every entry — update it whenever one is added.

Create an entry lazily — only when a live obstacle needs a practice this file doesn't already cover. Check `INDEX.md` first; don't duplicate an existing entry under a new slug.

This is the counterpart to the general research (`docs/research/`): use it for findings on Countermeasures.

## Template

```md
# {Practice title}

**Situation**: {the pattern or problem this addresses — concrete, not abstract}
**Practice**: {the established practice itself, stated plainly}
**Source**: {an external citation (doc, standard, book — with enough detail to find it again) OR "Driver, YYYY-MM-DD" when the Driver supplied or confirmed it directly}
**Added**: YYYY-MM-DD, during review of {Target Repo} (or theme of current session)

{Optional: one line on tradeoffs, or when this practice doesn't apply.}
```

## Rules

- **Never an unsourced heuristic.** A Practice Reference entry without a citation is a Countermeasure in disguise — the Source field is what tells them apart.
- **Global, not per-repo.** One shared library — a practice that's true in one Target Repo is true in another.
- **Tied to a real obstacle.** No pre-populated categories — an entry exists because a real obstacle in a real Review needed it.
- **Check the agent-specific angle before stopping at the general source.** Many practices read differently for an AI coding agent than for a human programmer — sometimes from the same author. When researching, check whether the practice's source, or another credible one, has written specifically about the agent case; if so, cite both and note where they diverge. If nothing agent-specific exists, the general source stands alone — but check before assuming that's true.
