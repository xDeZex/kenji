# Lean Agent

Kenji reviews AI coding sessions and runs structured improvement work to reduce waste and improve the flow of future sessions. The Target Repo is where the work was done — and where the improvement goals and experiments are stored. leanAgent is where Reviews and reports live.

## Language

### Toyota Way

**Genchi Genbutsu** ("go and see the actual thing"):
Decide from firsthand observation of where the work actually happened — never from a summary, a report, or someone else's secondhand account. Governs Kenji's own habit of reading CONTEXT.md and each session in full before acting, and the peer's role in a coaching exchange (see coaching-kata), which supplies its own firsthand account rather than reacting to Kenji's.
_Avoid_: Eyewitness, source, informant

**Five Whys**:
Ask why repeatedly, past the first easy answer, until the cause found is one someone can actually act on — a controllable, systemic cause, not an abstract "root" or a verified fact that still isn't fixable. Never "Five Whos": the question chases the process, never the person.
_Avoid_: Root cause analysis, the five whys technique

**Muda** (waste):
Any activity that consumes effort without adding value the customer would pay for. Kenji hunts Poppendieck's software-adapted seven, not Ohno's manufacturing seven: partially done work, extra features, relearning, handoffs, task switching, delays, defects.
_Avoid_: Inefficiency, the seven wastes (manufacturing sense)

**Jidoka**:
Stop rather than let a defect pass downstream — quality built in, not inspected in after the fact. One of Ohno's two technical pillars alongside Just-in-Time; the authority and obligation to halt sits with whoever is doing the work, not only with leadership above them.
_Avoid_: Automation, stop-the-line (as a generic phrase)

**Just-in-Time**:
Produce only what is needed, when it is needed, in the amount needed — the other of Ohno's two technical pillars, alongside Jidoka. In Kenji's own communication, this means one sharp question or one countermeasure, not a batch of options offered just in case.
_Avoid_: Efficiency, on-demand, lean scheduling

**Kaizen**:
Continuous, incremental improvement, carried out by whoever does the work — never a one-off overhaul. The unit of Kenji's own proposals: a small, testable change to the workflow, checked and tracked rather than declared correct on arrival.
_Avoid_: Improvement (untranslated), optimization, overhaul

**Standardized Work**:
The current best-known way of doing a task, written down as the baseline the next Kaizen measures against. A Countermeasure becomes Standardized Work once it has held up — recorded via a Target Condition's `standardized` status.
_Avoid_: Best practice, convention, the rules

**Hansei**:
Structured, honest self-reflection on a result — including a success, not only a failure — done deliberately rather than left implicit. Precedes Kaizen in Kenji's own close: reflection that doesn't lead to an action is incomplete.
_Avoid_: Retrospective, post-mortem, lessons learned

**PDCA** (Plan-Do-Check-Act):
The cycle Kenji's problem-solving runs through. A Review is Check, an approved Countermeasure applied is Do, and Hansei folding into a next action is Act — a cycle Kenji never leaves sitting on Check.
_Avoid_: The scientific method, plan-do-check-act (spelled out)

**Respect for People**:
One of the Toyota Way's two pillars, alongside Continuous Improvement: engage people to challenge and improve their own work, rather than simply directing them. Grounds Kenji's Five Whys discipline — the fault sought is the system's, not a person's — and the Driver's standing as an equal source in the Practice Reference, not only an approver.
_Avoid_: Psychological safety (as a substitute), empathy, kindness

### Review Process

**Session**:
A recorded AI-assisted coding conversation — the raw transcript of an interaction between a developer and an AI tool (VS Code Copilot Chat, Claude Code, OpenCode, or similar). The primary input for a Review.
_Avoid_: Conversation, history, log

**Review**:
Kenji's structured application of the Improvement Kata to a Session. Checks open Target Conditions against the session evidence, grasps the current process condition, proposes a set of improvements for Driver approval, then applies changes directly and documents any new or updated Target Conditions.
_Avoid_: Analysis, assessment, audit

**Driver**:
The human running Kenji for a given Review. Approves every Countermeasure and Target Condition before it reaches a Target Repo. Also a source Kenji consults for the Practice Reference, on the same footing as an external citation — not only an approver, but someone who may know the better practice outright.
_Avoid_: User, operator, owner

**Challenge**:
The long-range direction for the team's AI-assisted coding practice, defined in the Target Repo. All Target Conditions advance toward the Challenge. Stable across many Reviews; changes only when the team's fundamental goals shift.
_Avoid_: Goal, objective, vision, north star

**Harness**:
The recorded description of the AI engineering environment in a Target Repo — its instruction files, config, and user behavior — kept as a section of `.lean/improvement-kata.md`. Names the levers a Countermeasure can pull. Updated only when that environment actually changes.
_Avoid_: Environment, tooling, setup, config

**Kata Setup**:
The skill that produces the Challenge and Harness sections of `.lean/improvement-kata.md` before a Review can run. Grills the user directly for the Challenge, and inspects the Target Repo before grilling the user for the Harness. Invoked directly ahead of a repo's first Review, or by improvement-kata's step 2 when either section is missing.
_Avoid_: Onboarding, bootstrap, init

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
A small, reversible change applied to address a specific waste pattern. May be a change to developer workflow, AI instruction files, documentation, or process conventions. The action taken in an Experiment. Drawn from the Practice Reference or the Driver — never invented without a source.
_Avoid_: Fix, solution, recommendation, rule

**Practice Reference**:
A lazily-grown catalog of established software-engineering practices, kept in Kenji's own repo at `docs/references/` and shared across every Target Repo — not repo-specific. Consulted before drafting a Countermeasure. Every entry cites a source: either an external reference (docs, a standard, a book) or the Driver directly, dated. Grows one entry at a time, only when a live obstacle needs a practice it doesn't yet cover.
_Avoid_: Best practices doc, knowledge base, playbook

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
