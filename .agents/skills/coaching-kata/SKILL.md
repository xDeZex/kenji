---
name: coaching-kata
description: Use before sending an investigative question to another Claude Code session. Structures the exchange as a small ordered backbone plus standing obligations instead of a single dump-and-react message — one obstacle at a time, ask before disclosing, grounded in evidence, closing on a next step, never a conclusion.
---

A coaching exchange is a loop over obstacles, not a single message, and not a flat numbered list either. Two kinds of structure make it up: a small **backbone** with a real before/after order (open the exchange, investigate one obstacle, close it, loop), and **standing obligations** — right now, just the Driver check-in — that must happen at least once inside the backbone but don't own a fixed slot in it. The single most common failure is handing over a finished conclusion for the peer to react to; that skips the thinking that produces real insight, and calls one message "coaching."

The peer is being pulled into this mid-stream, on Kenji's schedule, often with no memory of why. Skipping the introduction and dropping straight into a question makes the first exchange read as an interrogation from a stranger, not a dialogue — the peer has no way to judge whether to answer plainly, push back, or treat it as an attack.

## The backbone

### 1. Open the exchange

Before naming the first obstacle, send one message built from six parts. Two are fixed — send them close to verbatim, every time. The rest vary by session but follow the template below rather than being composed freely. Read it the way the peer will: this is the first thing a possibly-fresh session sees, and it should read like an invitation to talk, not a protocol notice.

**Who** (fill in): "Hi — I'm Kenji. I'm running a process review of {session — repo, date, or session title}."

**Why** (fill in): "I'm looking into {what's being investigated}, to help shape {the Challenge or a Target Condition} in this repo's `.lean/improvement-kata.md`. This isn't a performance review of you."

**Rules of engagement** (fixed, send verbatim):
> This is a dialogue, not an inspection. I'd like to hear your own diagnosis first, before I share anything. And please push back on me — if something I say doesn't match what you actually saw, I'd rather be corrected than agreed with.

**Roles** (fixed, send verbatim):
> I'll ask the questions and draft findings; you answer from your own evidence and own your own diagnosis. Neither of us decides what changes — root causes go to my Driver for sign-off, and only the Driver routes an approved countermeasure into your Harness.

**Agenda** (fixed frame, fill in the obstacle list):
> Here's how this will go: one obstacle at a time. You give your own diagnosis before I say anything. If an answer's vague, I'll push on it until it's grounded. I check in with my Driver before we close each obstacle. Each one ends with a concrete next step, not a verdict — then we move on to the next obstacle, or wrap up.
> Today: {name the obstacle(s) on the table}.

**Expected outcome** (fill in): "What I'm after here: {a grounded root cause for X, checked with the Driver}."

Skip this step only when the peer already has this context live in the same conversation (a second obstacle in an exchange that already opened this way). A cleared or fresh peer conversation always gets the full open — assume no memory unless told otherwise.

_Done when_: all six parts have been sent — the two fixed ones verbatim, the rest filled in — before the first obstacle-specific question goes out.

### 2. Investigate the obstacle

Open with exactly one obstacle, named in the same message that asks for the peer's own diagnosis — never bundle two unrelated obstacles together. Then:

- **Ask without disclosing.** Ask for the peer's own diagnosis or what it expected to happen, without leading with Kenji's own theory or naming a suspected cause. Keep the question open — "what/how," not "why"; describe, don't demand justification. See `docs/references/open-non-leading-questions-and-agent-self-report.md`.
- **Ground vague answers.** A general, hedged, or unverified answer doesn't move the investigation forward — push back with "how do you know," "what did you actually try," "walk me through the specific case," and wait again. Never fill in the specifics yourself; that's Kenji doing the peer's thinking for it. A verified answer only licenses the next push — it doesn't license stopping. Ohno's own Five Whys pushes past a checked fact at every single step (`docs/references/five-whys-verified-answer-is-not-root-cause.md`); the actual stop condition is a countermeasure that would prevent the whole chain of symptoms up to this point, not just patch the last link.
- **When a question needs sharpening, that's the Driver check-in obligation's cue to fire early.** If pushing isn't landing, or Kenji doesn't have a good next question in hand, don't wait for the obstacle to be otherwise ready to close — pull the obligation forward and let what it turns up shape the next question, not just the eventual close.
- **Surface disagreement, don't restate agreement.** The goal isn't consensus between Kenji and the peer — it's finding out why the process failed, from the peer's own grounded account. Kenji read the same transcript the peer worked from, so repeating it back adds nothing by itself. Only raise Kenji's own read when it conflicts with a specific claim the peer made, and raise it as an open question ("the transcript shows X at turn N — how does that square with what you just said?"), never as a correction to simply accept.

_Done when_: the peer's diagnosis names a controllable, systemic cause and every step to it cited specific evidence — a turn, a line, a fact, not a generalization — and any conflict between that account and the transcript has been raised and addressed, not left standing.

## Standing obligation: Driver check-in

At some point during the investigation of every obstacle — before it closes, and at least once after the peer's first answer has been pushed on at least once — bring the obstacle to the Driver, the human running this Review, not the peer. Check `docs/references/INDEX.md` (the Practice Reference) for a practice that already covers it; if nothing fits, research one per `docs/references/ENTRY-FORMAT.md` (a research subagent, not an inline search).

This obligation doesn't wait for a fixed slot — it can fire early, even to shape the next question sent to the peer. But what the Driver or Practice Reference surfaces informs the question; it never appears inside it. Naming a candidate practice or countermeasure to the peer turns an open question into a leading one — see `docs/references/open-non-leading-questions-and-agent-self-report.md`.

Speak to the Driver as soon as there's something to ask, without waiting on research that hasn't returned — unless the specific question depends on that research, in which case wait for it to land. When Kenji doesn't know what to research or where to look, ask the Driver that directly instead of dispatching a search — the Driver is a Practice Reference source on the same footing as an external citation, not just a slower path to one.

Present the Driver the muda type, the specific evidence (a turn or line, not a paraphrase), the peer's own stated diagnosis, and a plain-language read of what research found — or that it found nothing, or is still pending — and why it's relevant; the Driver may not know the subject going in, so explain it rather than just citing it. Then ask what the Driver would do here. The Driver may confirm it, correct it, or supply a different practice from their own experience; either way, once confirmed it's ready to become a Practice Reference entry.

This is the one obligation that doesn't need a peer. When no peer is connected for a Review, run it directly against Kenji's own read of the obstacle — the Practice Reference consult and the Driver check-in still happen; only the peer half of the exchange is skipped.

_Done when_: the Driver has responded to a read that named the muda type, the evidence, the peer's diagnosis, and an explained research finding, at least once, before the obstacle's cycle closes.

## The backbone, continued

### 3. Close the obstacle

End the cycle with a concrete next action and when it'll be checked again — never a wrap-up sentence. Fold in whatever the Driver confirmed or supplied in the Driver check-in. That next step is what becomes an Experiment row in `.lean/improvement-kata.md`, not a verdict typed up on the spot.

_Done when_: the closing message names an action and a check point.

### 4. Loop or stop

After closing an obstacle, open the next one or end the exchange — a single message-and-reply is never sufficient grounds to finalize a proposal.

_Done when_: the exchange spans more than one obstacle, or there's a specific reason one was enough (the peer's first answer already cited unprompted evidence).

## Guardrails

- Frame every question as system inquiry, not accusation — "looking for a process fix, not blaming you." Accusatory framing produces defensive non-answers, not real ones.
- Keep every question open: "what/how" over "why," never naming a suspected cause or candidate practice inside the question itself. See `docs/references/open-non-leading-questions-and-agent-self-report.md`.
- Don't accept a self-reported diagnosis at face value — ask for the specific evidence it rests on. An agent's stated reasoning for its own action is frequently a post-hoc reconstruction, not a faithful trace.
- Watch for false capitulation: a peer can agree it was wrong when it wasn't, under nothing more than mild pushback — no authority framing required. If a diagnosis reverses under pressure, that's a signal to ask for evidence, not a signal the new answer is truer.
- This skill only ever carries questions to the peer. Root causes and countermeasures route through the Driver into the Target Repo's own artifacts (`.lean/improvement-kata.md`, the peer's own Harness) — never into another exchange with the peer.
- Treat the peer's account as equally valid regardless of the reviewer/reviewed gap between Kenji and the peer — invite it throughout the exchange, not just once in the opening message. If Kenji doesn't know something, say so plainly rather than bluffing a confident read. See `docs/references/leader-inclusiveness-and-situational-humility.md`.
