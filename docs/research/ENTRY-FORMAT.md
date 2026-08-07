# Research — Entry Format

Entries live in `docs/research/`, one file per entry: `docs/research/<slug>.md`. `docs/research/INDEX.md` lists every entry — update it whenever one is added.

Create an entry lazily — only when a question has actually been researched. Check `INDEX.md` first; don't duplicate an existing entry under a new slug.

This is the general-purpose counterpart to the Practice Reference (`docs/references/`): use it for findings that aren't a reusable engineering practice feeding a Countermeasure — API behavior, tool docs, spec details, one-off factual questions.

## Template

```md
# {Question or topic, stated plainly}

**Finding**: {the answer, stated plainly}
**Source**: {primary source citation — official docs, source code, a spec, a first-party API — with enough detail to find it again}
**Added**: YYYY-MM-DD, during review of {Target Repo} (or theme of current session)

{Optional: one line on caveats, or where the finding stops applying.}
```
