# Kata Format — `.lean/improvement-kata.md`

This file lives in the Target Repo and is the single source of truth for the team's improvement work on that repo. Kenji reads and writes it during every Review.

## File structure

```markdown
# Improvement Kata — <repo name>

## Challenge

<One sentence: what does AI-assisted coding look like in this repo when it's working well?>

## Harness

<Brief prose describing the engineering setup around the AI model in this repo. List the available levers — instruction files, config, user behavior — and note the typical review flow.>

## Target Conditions

### TC-001: <short title>

**Status**: active
**Set**: YYYY-MM-DD
**Check window**: <target date or "by session N">
**Criterion**: <What must be consistently observable in a future session for this condition to be considered met? One specific, checkable sentence.>

#### Experiments

| Date | Hypothesis | Countermeasure | Outcome |
|------|------------|----------------|---------|
| YYYY-MM-DD | <what we expected to happen> | <the change applied and where> | <what was observed in the next session> |
```

## Rules

- **Harness**: Update when the engineering setup changes — new instruction files, new tools, changed approval behaviour.
- **Challenge**: Changes rarely. Only update it when the team's fundamental direction has shifted — not in response to a single session.
- **IDs**: Sequential and never reused. The next condition is TC-002, TC-003, and so on. Scan the file for the highest existing ID before writing a new one.
- **Criterion**: Must be specific enough to check without interpretation. "Fewer mistakes" fails. "Definition of done stated in Turn 1 in at least 3 of the next 4 sessions" passes.
- **Check window**: Required on every new Target Condition. Without it, conditions stay open forever.
- **Experiments**: Append-only. Never edit or delete a past experiment row — the record of what failed is part of the learning.
- **Status transitions**: `active` → `met` (when criterion is satisfied by session evidence) → `standardized` (when the improvements are written into standard work). Use `abandoned` if the condition is no longer worth pursuing; record why in a final experiment row.
