---
name: coaching-kata
description: Structures a live dialogue with a peer coding session over inter-session messaging as a gated loop instead of a single dump-and-react message — one obstacle at a time, grounded in evidence, expected-before-actual, closing on a next step. Use whenever about to send an investigative question or a draft countermeasure to another Claude Code session.
---

A coaching exchange is a loop of gates, not a single message. Each gate stays open until the answer is concrete — never wave one through on the first pass. The single most common failure is handing over a finished conclusion for the peer to react to; that skips the thinking that produces real insight, and calls one message "coaching."

### 1. Narrow to one obstacle

Name the single obstacle, question, or draft countermeasure this gate is about before sending anything. Never bundle two unrelated issues into one message — park the rest for a later gate.

_Done when_: the message names exactly one obstacle.

### 2. Ask before you tell

Ask for the peer's own diagnosis or what it expected to happen — before revealing Kenji's conclusion, root cause, or draft fix. If nothing to compare against exists yet, this is the gate that produces it.

_Done when_: the peer has answered before Kenji's analysis is disclosed in this gate.

### 3. Ground vague answers

A general, hedged, or unverified answer doesn't close the gate — push back with "how do you know," "what did you actually try," "walk me through the specific case," and wait again. Never fill in the specifics yourself; that's Kenji doing the peer's thinking for it.

_Done when_: the answer cites a specific fact, turn, or line — not a generalization.

### 4. Compare expected to actual

Once the peer has stated what it expected, surface what actually happened. The contrast is what produces the peer's own insight — reveal it too early and there's nothing left to compare against.

_Done when_: expectation and outcome have both been stated, in that order.

### 5. Close on a next step, not a summary

End the gate with a concrete next action and when it'll be checked again — never a wrap-up sentence. That next step is what becomes an Experiment row in `.lean/improvement-kata.md`, not a verdict typed up on the spot.

_Done when_: the closing message names an action and a check point.

### 6. Loop or stop, never one-and-done

After closing a gate, open the next obstacle or end the exchange — a single message-and-reply is never sufficient grounds to finalize a proposal.

_Done when_: the exchange spans more than one gate, or there's a specific reason one gate was enough (the peer's first answer already cited unprompted evidence).

## Guardrails

- Frame every question as system inquiry, not accusation — "looking for a process fix, not blaming you." Accusatory framing produces defensive non-answers, not real ones.
- This skill governs how a cleared conversation is structured, not whether to send it — root causes and countermeasures still route through the user before reaching the peer session.
