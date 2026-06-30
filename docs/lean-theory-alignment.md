# Lean Theory Alignment — leanAgent Improvement Kata Skill

**Date:** 2026-06-30  
**Purpose:** Assess how well the improvement-kata skill aligns with established lean theory in software development and knowledge work. Identify gaps and improvement opportunities.

---

## Bodies of Work Reviewed

1. Mike Rother — *Toyota Kata* (2009)
2. Mary & Tom Poppendieck — *Lean Software Development: An Agile Toolkit* (2003) and *Implementing Lean Software Development* (2006)
3. Donald G. Reinertsen — *The Principles of Product Development Flow: Second Generation Lean Product Development* (2009)
4. Taiichi Ohno — *Toyota Production System: Beyond Large-Scale Production* (1978)

---

## 1. Mike Rother — Toyota Kata

### What it says

The Improvement Kata is a four-step scientific thinking routine:

1. **Understand the direction** — a long-range Challenge, not a SMART goal
2. **Grasp the current condition** — observable, fact-based, no assumptions
3. **Set the next Target Condition** — a specific, measurable, time-boxed near-term state
4. **Experiment toward it** — PDCA cycles: predict, act, observe, reflect

Alongside it, the **Coaching Kata** is the manager's structured question pattern that develops scientific thinking in the team — not just outcomes. Rother's key insight: organizations that run Improvement Katas without Coaching Katas produce correct-looking documents without building capability.

**Source:** Rother, M. (2009). *Toyota Kata.* McGraw-Hill.

### Alignment with the skill

| Rother's Concept | Skill Implementation | Verdict |
|---|---|---|
| Challenge = long-range direction | `.lean/improvement-kata.md` Challenge; stable, changed only when fundamental direction shifts | ✅ Strong |
| Genchi genbutsu | Step 1 mandates reading every Turn and every tool call result; phrase is used explicitly | ✅ Strong |
| Current condition = observable facts only | Step 4 explicitly bans "sometimes," "often," "tends to" | ✅ Strong |
| Target Conditions are measurable and time-boxed | Criterion must be checkable; check window is required — no exceptions | ✅ Strong |
| PDCA in Experiments | Hypothesis → Countermeasure → Outcome table; append-only, failures preserved | ✅ Strong |
| Standardization | `standardized` status maps to yokoten — writing learnings into standard work | ✅ Strong |
| Obstacle list before acting | Not present. Skill moves from current condition directly to proposals | ❌ Gap |
| One experiment at a time | Step 5C allows multiple simultaneous file changes, diluting scientific isolation | ⚠️ Partial |
| Prediction stated before experiment | Hypothesis column exists but is not enforced before countermeasure is applied | ⚠️ Partial |
| Coaching Kata | Kenji plays both analyst and coach simultaneously; no distinct coaching question pattern | ❌ Gap |

**Overall alignment: ~75%.** The core kata loop is faithfully reproduced. The main structural gap is the absence of an explicit obstacle parking lot — listing all known blockers and selecting one before building proposals. Without it, the skill can produce well-reasoned proposals that change too many things at once. Rother would call that "adjusting" rather than "experimenting."

---

## 2. Poppendieck — Lean Software Development

### What it says

The Poppendiecks adapted Ohno's seven manufacturing wastes to software development and added seven principles for knowledge-work lean:

**Seven wastes (software-adapted):**

| Poppendieck Waste | Software Example |
|---|---|
| Partially done work | Unfinished code, unmerged branches |
| Extra features | Gold plating, unnecessary UI |
| Relearning | Repeated documentation reads, lost context |
| Handoffs | QA/dev walls, lost context between teams |
| Task switching | Context switching, multitasking |
| Delays | Waiting for approvals, blocked PRs |
| Defects | Bugs, rework from unclear requirements |

**Seven principles:** Eliminate waste · Amplify learning · Decide as late as possible · Deliver as fast as possible · Empower the team · Build integrity in · See the whole.

**Source:** Poppendieck, M. & Poppendieck, T. (2003). *Lean Software Development: An Agile Toolkit.* Addison-Wesley.

### Alignment with the skill

The skill uses the TPS manufacturing waste taxonomy — *rework, waiting, motion, overprocessing, defect* — **not** Poppendieck's software-adapted categories.

This is a meaningful gap. In an AI coding session, the following Poppendieck wastes are common but go unnamed by the skill's current taxonomy:

- **Relearning** — the agent re-reads the same file three turns in a row because context was not retained
- **Handoffs** — a poorly scoped user request leads to a clarification loop; context is rebuilt from scratch
- **Extra features** — the agent builds infrastructure beyond the explicit request (over-engineering)
- **Task switching** — the agent pivots mid-turn to explore an unrelated problem, losing thread

Because these waste types are not named, a reviewer hunting muda with the skill's current categories will likely classify them as generic "motion" or "rework" and miss the precise cause.

**Overall alignment: Partial.** The spirit is right — hunt waste, make it visible — but the vocabulary is mismatched for software knowledge work. Adopting Poppendieck's software waste taxonomy in place of, or alongside, the TPS manufacturing list would improve diagnostic precision.

---

## 3. Reinertsen — Principles of Product Development Flow

### What it says

Reinertsen applied queuing theory and economics to knowledge work. His central argument: knowledge-work organizations optimize *resource efficiency* (keep people busy) when they should optimize *flow efficiency* (keep work moving through the system).

Key concepts:

- **WIP limits** — constraining work in progress reduces queue buildup and shortens cycle time
- **Batch size** — smaller batches yield faster feedback and less compounded rework
- **Little's Law** — cycle time = WIP ÷ throughput (a mathematical relationship, not a guideline)
- **Cost of delay** — the economic cost of slow flow, not just the cost of defects. Delay is often the dominant waste, invisible without measurement.
- **Flow efficiency** — active work time ÷ total lead time. In most knowledge work this is below 20%.

**Source:** Reinertsen, D.G. (2009). *The Principles of Product Development Flow.* Celeritas Publishing.

### Alignment with the skill

Almost none. The skill has no concept of flow, WIP, queue length, batch size, or cycle time. It operates session-by-session — a spot audit — and cannot see systemic queue problems that only become visible across multiple sessions:

- A Target Condition that has been `active` for six sessions with no progress is **invisible inventory** (Poppendieck waste #1). The skill has no cross-session view to detect it.
- A check window that expired three sessions ago represents a **delay** (Poppendieck waste #6, Reinertsen's cost of delay) that no current step surfaces.
- Applying five countermeasures in one session is a **large batch size**: changes are made before the outcome of any individual change is observed.

**Overall alignment: Weak.** The skill is structurally session-scoped. Adding even basic cross-session metrics — number of active Target Conditions, age of oldest open TC, experiment-to-outcome ratio — would bring Reinertsen's flow thinking into reach without requiring a full queue model.

---

## 4. Taiichi Ohno — Toyota Production System

### What it says

Ohno built the TPS around two foundational pillars:

- **Just-in-Time** — produce only what is needed, when it is needed, in the amount needed
- **Jidoka** — automation with a human touch; specifically, the authority and obligation to stop the line when a defect is detected

Ohno's **genchi genbutsu** principle (go to the actual place, see the actual thing) underpins all TPS problem-solving: decisions must be based on firsthand observation, never on second-hand reports or assumptions.

**Source:** Ohno, T. (1978). *Toyota Production System: Beyond Large-Scale Production.* Productivity Press.

### Alignment with the skill

| Ohno Concept | Skill Implementation | Verdict |
|---|---|---|
| Genchi genbutsu | Explicitly named and operationalized in Step 1 (read every Turn, every tool call, no paraphrasing) | ✅ Strong |
| Observable facts over opinion | Step 4 current condition statement — only observable facts allowed | ✅ Strong |
| Jidoka — stop on defect | No equivalent. The skill continues analysis even when session data is ambiguous, incomplete, or corrupted | ❌ Gap |
| Just-in-Time | Not directly applicable at session level, but the single-experiment discipline in Rother maps to this spirit — and the skill partially violates it by allowing multi-change proposals | ⚠️ Partial |

**Overall alignment: Strong on observation discipline, absent on stop-the-line.** The skill has no mechanism to halt a Review when the input is unreliable (e.g., an import failed partially, a session was cut short, or Turn data is inconsistent). A jidoka-equivalent would be a hard stop condition in Step 1 with an explicit user notification.

---

## Summary Table

| Body of Work | Alignment | Primary Gaps |
|---|---|---|
| **Rother — Toyota Kata** | ✅ Strong (~75%) | No obstacle parking lot; multi-change experiments; no Coaching Kata; prediction not enforced |
| **Poppendieck — Lean SW** | ⚠️ Partial | Manufacturing waste names used instead of software-adapted taxonomy; relearning, handoffs, task switching unnamed |
| **Reinertsen — Flow** | ❌ Weak | No cross-session flow visibility; no WIP, queue, or cycle time awareness; large batch countermeasures |
| **Ohno — TPS originals** | ✅ Strong | No jidoka equivalent; no stop condition for unreliable session data |

---

## Prioritized Improvement Opportunities

Ordered by impact-to-effort ratio:

1. **Adopt Poppendieck's software waste taxonomy** in Step 4. Replace or augment the manufacturing muda list with: partially done work, extra features, relearning, handoffs, task switching, delays, defects. Low effort; high diagnostic precision gain.

2. **Add an obstacle parking lot to Step 4.** Before Step 5 builds proposals, require listing all observed obstacles and selecting one to address. This closes the biggest gap against Rother's theory and enforces single-variable experiment discipline.

3. **Enforce prediction before countermeasure.** The Experiment hypothesis must state the expected outcome *before* the change is applied — not retrospectively. This is what makes PDCA scientific rather than storytelling.

4. **Add a cross-session flow check.** A lightweight Step 0 (or part of Step 3) that surfaces: age of oldest active Target Condition, number of expired check windows, experiment-to-outcome ratio. This brings Reinertsen's flow thinking in without requiring a full queue model.

5. **Add a jidoka stop condition.** If the Readable Session is incomplete, ambiguous, or corrupted beyond a defined threshold, halt the Review and notify the user rather than continuing with unreliable input.

6. **Separate coaching from analysis.** Consider whether Kenji should ask the user Rother's five coaching questions — "What is the target condition? What is the current condition? What obstacles do you see? Which one are you addressing? What do you expect?" — before presenting analysis, rather than delivering conclusions directly. This develops the user's scientific thinking, not just the quality of the output document.

---

## References

- Ohno, T. (1978). *Toyota Production System: Beyond Large-Scale Production.* Productivity Press.
- Poppendieck, M. & Poppendieck, T. (2003). *Lean Software Development: An Agile Toolkit.* Addison-Wesley.
- Poppendieck, M. & Poppendieck, T. (2006). *Implementing Lean Software Development.* Addison-Wesley.
- Reinertsen, D.G. (2009). *The Principles of Product Development Flow: Second Generation Lean Product Development.* Celeritas Publishing.
- Rother, M. (2009). *Toyota Kata: Managing People for Improvement, Adaptiveness, and Superior Results.* McGraw-Hill.
