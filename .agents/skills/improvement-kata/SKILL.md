---
name: improvement-kata
description: Run a full Improvement Kata review of a coding session. Checks open Target Conditions, diagnoses waste, proposes and applies improvements to the Target Repo.
disable-model-invocation: true
---

## Steps

### 1. Import the session

Ensure the session is available: run `python tools/import_session.py` if the target session has not yet been imported. Select the newest file in `sessions/readable/` by filename date. If the selection is ambiguous, stop and ask before proceeding.

Read the selected Readable Session in full — every Turn, every tool call, every result. Genchi genbutsu: go to where the work happened. Do not paraphrase or summarize from a prior read.

_Done when_: Every Turn and every tool call result has been read. The session name and date are recorded.

### 2. Read the Challenge and Harness

Open `.lean/improvement-kata.md` in the Target Repo. Read the **Harness** section — note what levers are available for countermeasures. Read the **Challenge** and record the exact text.

**If the file doesn't exist or has no Challenge:** The kata cannot proceed without direction. Work with the user to define it — a single sentence describing what AI-assisted coding looks like when it's working well. Write it to `.lean/improvement-kata.md` and confirm with the user before continuing.

**If the file has no Harness section:** Ask the user what instruction files and levers exist in this repo, then write a Harness section following the format in [KATA-FORMAT.md](KATA-FORMAT.md) before continuing.

_Done when_: The Harness levers are noted. The Challenge text is recorded verbatim.

### 3. Check open Target Conditions

Genchi genbutsu: go to each active Target Condition and find its evidence in the session. For each Target Condition in `.lean/improvement-kata.md` with status `active`:

1. State whether the process looked like the criterion in this session.
2. Cite the specific Turns that are the evidence.
3. Deliver a verdict: `met`, `progressing`, or `stalled`.

For a `stalled` verdict: cite contradictory evidence or record explicitly that no evidence was found. Do not leave it blank.

_Done when_: Every active Target Condition has a verdict. Every verdict has Turn citations or an explicit "no evidence" note. None are skipped.

### 4. Grasp the current condition

Read the Readable Session again, this time Turn by Turn, hunting muda. For every Turn — not just the ones where something went wrong — record one of two things:

- **Muda found**: name the type (rework, waiting, motion, overprocessing, defect), cite the Turn, write one line on why it is waste.
- **No muda**: note it briefly and move on.

When every Turn has been accounted for, state the current condition in concrete, observable terms. Not what the process should do. What it does, measured in the session.

_Done when_: Every Turn is accounted for as muda or clean. The current condition statement contains only observable facts — no words like "sometimes," "often," or "tends to."

### 5. Build the proposal

Assemble the full proposal in three parts:

**A — Check verdicts**: Compile the verdicts from step 3. For each active Target Condition: verdict and the strongest evidence cited.

**B — New Target Conditions**: Compare each element of the Challenge against active Target Conditions. For any gap not yet covered, draft a new Target Condition using the format in [KATA-FORMAT.md](KATA-FORMAT.md). Each must include a measurable criterion (checkable in a future session), a check window, and at least one opening Experiment.

**C — Changes to apply now**: List every file to be edited with the exact change — file path, what is being added or modified, and which muda it addresses. Step 7 will apply exactly what is listed here and nothing else.

Present A / B / C in full before asking for approval.

_Done when_: Part A covers every active Target Condition. Part B covers every Challenge gap not addressed by an active condition. Every entry in Part C names a specific file and a specific modification. Nothing is marked TBD.

### 6. Get approval

Do not apply any change.

Ask: "Does this look right? I'll apply everything above once you confirm."

If the user requests modifications, incorporate them and re-present the revised A / B / C before asking again.

_Done when_: The user has explicitly approved the current version of the proposal.

### 7. Apply

Apply every file change listed in Part C. Then update the improvement record:

- **`.lean/improvement-kata.md` in the Target Repo**: mark `met` conditions, add new Target Conditions with their opening Experiments.

If any approved change cannot be applied — file missing, conflict, or other failure — stop immediately. List every unapplied change and wait for the user to resolve the blockers before continuing.

_Done when_: Every change from Part C has been applied and verified by re-reading the edited section. `.lean/improvement-kata.md` is updated.
