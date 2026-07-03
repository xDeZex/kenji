---
name: kata-setup
description: Grill out the Challenge and Harness for a Target Repo's .lean/improvement-kata.md, before a Review can run — including when improvement-kata's step 2 finds the file missing or incomplete.
---

## Steps

### 1. Locate the file and classify its state

Read `LEAN_REPO` from `.env` to find the Target Repo. Check `.lean/improvement-kata.md` there and classify into exactly one case:

- **Missing** — no file, or a file with neither a Challenge nor a Harness section.
- **Partial** — exactly one of Challenge or Harness is present.
- **Complete** — both Challenge and Harness are present.

For **Complete**: warn the human that Target Conditions in the file may already reference the current Challenge, and ask for explicit confirmation before continuing. If they decline, stop here.

_Done when_: the case is named, and for Complete, explicit confirmation has been given.

### 2. Grill the Challenge

Ask the human for one sentence: what does AI-assisted coding look like in this repo when it's working well? Do not accept the first answer. Cross-reference it against the Target Repo's actual codebase, README, and instruction files, and against general best practice — where the answer is generic ("write good code") or contradicted by what the repo actually does, push back and ask again. Use [domain-modeling](../domain-modeling/SKILL.md)'s technique for sharpening fuzzy language.

_Done when_: the human has confirmed one concrete, specific sentence.

### 3. Grill the Harness

Inspect the Target Repo for its actual levers — instruction files (`AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `.github/copilot-instructions.md`), CI config, pre-commit hooks, linters. Draft a candidate Harness paragraph from what you find, then grill the human on it: does this match how the team actually works, or does the draft describe configuration nobody follows? Revise until the human confirms it reflects real practice, not aspiration.

_Done when_: the human has confirmed a Harness paragraph that reflects actual, observed practice.

### 4. Write the file

The repo name is the last path segment of `LEAN_REPO`.

Write `.lean/improvement-kata.md`:

- **Missing** case: create `.lean/` if it doesn't exist, then create the file with `# Improvement Kata — <repo name>`, then `## Challenge` and `## Harness` — nothing else. No Target Conditions section.
- **Partial** or **Complete** case: replace only the Challenge and Harness section content. Leave any existing Target Conditions section untouched.

_Done when_: the file has exactly one Challenge section and one Harness section holding the grilled answers, and any pre-existing Target Conditions section is unchanged.
