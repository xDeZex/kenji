# Lean Agent

Kenji reviews AI coding sessions and runs structured improvement work to reduce waste and improve the flow of future sessions. The Target Repo is where the work was done — and where the improvement goals and experiments are stored. leanAgent is where Reviews and reports live.

## Language

**Session**:
A recorded AI-assisted coding conversation — the raw transcript of an interaction between a developer and an AI tool (VS Code Copilot Chat, Claude Code, OpenCode, or similar). The primary input for a Review.
_Avoid_: Conversation, history, log

**Review**:
Kenji's structured application of the Improvement Kata to a Session. Checks open Target Conditions against the session evidence, grasps the current process condition, proposes a set of improvements for user approval, then applies changes directly and documents any new or updated Target Conditions.
_Avoid_: Analysis, assessment, audit

**Challenge**:
The long-range direction for the team's AI-assisted coding practice, defined in the Target Repo. All Target Conditions advance toward the Challenge. Stable across many Reviews; changes only when the team's fundamental goals shift.
_Avoid_: Goal, objective, vision, north star

**Target Condition**:
The primary unit of improvement work. A concrete, measurable picture of what the process should look like at the next stage — specific enough that a future Review can determine whether it has been reached. Lives in the Target Repo alongside the Challenge. Every Review checks open Target Conditions and may set new ones.
_Avoid_: PDCA Item, goal, milestone, outcome

**Experiment**:
A single PDCA cycle within a Target Condition. Contains a hypothesis (what is expected to happen), a Countermeasure (the change applied), and an outcome (what was actually observed). The atomic sub-unit of a Target Condition. Multiple Experiments may run before a Target Condition is met.
_Avoid_: Test, action item, trial

**Kaizen Backlog**:
The collection of all Target Conditions for a given Target Repo, stored in `.lean/improvement-kata.md` alongside the Challenge and Experiments. The complete improvement record lives in the Target Repo; leanAgent holds only Review Reports.
_Avoid_: Issue tracker, backlog, task list

**Countermeasure**:
A small, reversible change applied to address a specific waste pattern. May be a change to developer workflow, AI instruction files, documentation, or process conventions. The action taken in an Experiment.
_Avoid_: Fix, solution, recommendation, rule

**Check**:
The act of evaluating whether a Target Condition has been reached. Performed during a Review by examining session evidence against the Target Condition's measurable criteria.
_Avoid_: Verification, follow-up, validation

**Session Source**:
The original artifact produced by an AI tool, before any transformation. For Copilot CLI: a directory in `~/.copilot/session-state/` containing `events.jsonl` and `workspace.yaml`. For VS Code Copilot Chat: a manually exported conversation. The input to an Import.
_Avoid_: Raw session, log file, input file

**Import**:
The act of transforming a Session Source into a Readable Session. Kenji invokes an import script as the first step of a Review. The script extracts Turns, tool calls, and metadata from the Session Source and writes a structured file to `sessions/raw/`.
_Avoid_: Export, convert, parse

**Readable Session**:
A preprocessed session file in `sessions/readable/` — the output of an Import, the input to a Review. Structured by Turns and Steps, human-readable, stripped of wire-format noise.
_Avoid_: Raw session, transcript, log

**Turn**:
The atomic unit of a Session: one user message, the AI's reasoning, and all tool calls and results produced in response. Kenji analyzes Sessions turn-by-turn to locate waste patterns.
_Avoid_: Exchange, step, interaction

**Review Report**:
The output of a Review, saved in `sessions/reports/`. Contains the waste diagnosis, new and updated Target Conditions, Experiment outcomes, and the list of changes Kenji applied.
_Avoid_: Output, analysis report, summary

**Target Repo**:
The repository that was the subject of the Session being reviewed. Configured via `LEAN_REPO` in `.env`. Kenji reads context from it (e.g., `CONTEXT.md`, `CLAUDE.md`, `AGENTS.md`) and applies Countermeasures there directly. Also stores the Challenge and all Target Conditions.
_Avoid_: Source repo, project repo, reviewed repo

**Status**:
The lifecycle state of a Target Condition. One of: `active` (experiments running, Target Condition not yet reached), `met` (session evidence confirms the process looks like the Target Condition), `standardized` (the improvements that achieved the Target Condition have been written into standard work), `abandoned` (the Target Condition is no longer worth pursuing).
_Avoid_: State, phase
