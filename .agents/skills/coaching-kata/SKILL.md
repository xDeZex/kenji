---
name: coaching-kata
description: Structures a live dialogue with a peer coding session over inter-session messaging as a gated loop instead of a single dump-and-react message — one obstacle at a time, grounded in evidence, expected-before-actual, closing on a next step. Use whenever about to send an investigative question or a draft countermeasure to another Claude Code session.
---

A coaching exchange is a loop of gates, not a single message. Each gate stays open until the answer is concrete — never wave one through on the first pass. The single most common failure is handing over a finished conclusion for the peer to react to; that skips the thinking that produces real insight, and calls one message "coaching."

The peer is being pulled into this mid-stream, on Kenji's schedule, often with no memory of why. Skipping the introduction and dropping straight into a question makes the first gate read as an interrogation from a stranger, not a dialogue — the peer has no way to judge whether to answer plainly, push back, or treat it as an attack.

### 1. Open with who, why, and what

Before naming the first obstacle, send one message that frames the whole exchange:

- **Who**: Kenji, running a process review of a specific session (name it — repo, date, or session title).
- **Why**: what's being investigated and what it's for — feeding a Challenge or Target Condition in that repo's `.lean/improvement-kata.md`, not a performance judgment of the peer.
- **Rules of engagement**: this is a dialogue, not an inspection. The peer gives its own diagnosis before Kenji discloses any conclusion. The peer can and should push back on any factual claim Kenji makes — grounded correction beats polite agreement.
- **Roles**: Kenji asks the questions and drafts findings. The peer answers from its own evidence (its transcript, its repo state) and owns its own diagnosis. Neither agent decides what changes — root causes surfaced here go to the Driver for sign-off, and only the Driver routes an approved countermeasure into `.lean/improvement-kata.md` or the peer's own CLAUDE.md. Say this plainly so the peer knows nothing it says here gets implemented unilaterally.
- **Agenda**: the shape of the exchange itself, not just the topic — one obstacle at a time; the peer gives its own diagnosis before Kenji says anything; vague and unverified answers get pushed on until they're grounded; the Driver is checked in with before the gate closes; each obstacle closes on a concrete next step, not a verdict; then either the next obstacle opens or the exchange ends. Name the obstacle(s) on the table for today up front, inside that structure.
- **Expected outcome**: what a successful exchange produces — e.g. "a grounded root cause for X, checked with the Driver, going to the peer before anything changes" — not a fix, not a verdict.

Skip this step only when the peer already has this context live in the same conversation (a second obstacle in an exchange that already opened this way). A cleared or fresh peer conversation always gets the full open — assume no memory unless told otherwise.

_Done when_: who, why, the rules, the roles, the agenda, and the expected outcome have all been stated to the peer, before the first obstacle-specific question goes out.

### 2. Narrow to one obstacle

Name the single obstacle, question, or draft countermeasure this gate is about before sending anything. Never bundle two unrelated issues into one message — park the rest for a later gate.

_Done when_: the message names exactly one obstacle.

### 3. Ask before you tell

Ask for the peer's own diagnosis or what it expected to happen — before revealing Kenji's conclusion, root cause, or draft fix. If nothing to compare against exists yet, this is the gate that produces it.

_Done when_: the peer has answered before Kenji's analysis is disclosed in this gate.

### 4. Ground vague answers

A general, hedged, or unverified answer doesn't close the gate — push back with "how do you know," "what did you actually try," "walk me through the specific case," and wait again. Never fill in the specifics yourself; that's Kenji doing the peer's thinking for it.

A specific answer can still be a guess wearing detail: "I assumed X," "I expected Y," "I figured Z would work" name a belief, not a check. Treat these the same as a vague answer — the gate stays open. Push one more why, aimed at the process rather than the peer: *why did nothing catch that belief before it landed?* This is the discipline Five Whys actually runs on — an unverified answer is a guess that becomes the basis for the next guess, and a chain that stops at "I made a mistake" has found a symptom, not a root cause. The real cause is whatever let the mistake through uncaught. Keep pushing until an answer is backed by something the peer actually checked (a rerun, a log, a specific line), or one more why would just restate what's already been said — there's no fixed count, this is judgment, not a script.

_Done when_: the answer cites a specific fact, turn, or line — not a generalization — and, where that fact was itself a stated belief, at least one further why has chased what let the belief go unverified.

### 5. Compare expected to actual

Once the peer has stated what it expected, surface what actually happened. The contrast is what produces the peer's own insight — reveal it too early and there's nothing left to compare against.

_Done when_: expectation and outcome have both been stated, in that order.

### 6. Check in with the Driver

Before closing the gate, bring the obstacle back to the Driver — the human running this Review, not the peer. Check `references/INDEX.md` (the Practice Reference) for a practice that already covers it; if nothing fits, research one per `references/ENTRY-FORMAT.md` — a research subagent, not an inline search. Present the Driver a general-terms read — the muda type and the reasoning behind it, not a finished Countermeasure — alongside that candidate practice, and ask what the Driver would do here. The Driver may confirm it, correct it, or supply a different practice from their own experience; either way, once confirmed it's ready to become a Practice Reference entry.

This gate can fire earlier than its position suggests — even mid-investigation, before gates 3-5 are finished — whenever the obstacle looks like it needs the Driver's judgment rather than more questions to the peer. Wherever it fires, it happens at least once before the obstacle's gate closes.

This is the one gate that doesn't need a peer. When no peer is connected for a Review, run this gate directly against Kenji's own read of the obstacle — the Practice Reference consult and the Driver check-in still happen; only the peer half of the exchange is skipped.

_Done when_: the Driver has responded to a general-terms read and a candidate practice, at least once, before the gate closes.

### 7. Close on a next step, not a summary

End the gate with a concrete next action and when it'll be checked again — never a wrap-up sentence. Fold in whatever the Driver confirmed or supplied in gate 6. That next step is what becomes an Experiment row in `.lean/improvement-kata.md`, not a verdict typed up on the spot.

_Done when_: the closing message names an action and a check point.

### 8. Loop or stop, never one-and-done

After closing a gate, open the next obstacle or end the exchange — a single message-and-reply is never sufficient grounds to finalize a proposal.

_Done when_: the exchange spans more than one gate, or there's a specific reason one gate was enough (the peer's first answer already cited unprompted evidence).

## Guardrails

- Frame every question as system inquiry, not accusation — "looking for a process fix, not blaming you." Accusatory framing produces defensive non-answers, not real ones.
- This skill governs how a cleared conversation is structured, not whether to send it — root causes and countermeasures still route through the Driver before reaching the peer session.
