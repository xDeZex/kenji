# Worked examples: leading questions and disclosure leaks

Real instances, not invented ones. All four are pulled verbatim from
`sessions/coaching/2026-08-07-steven-create-a-small-hobby-project.md` — a
coaching exchange Kenji ran, then the Driver annotated line by line. Each
entry: the bad text as sent, why it failed, and the rewrite that should
have gone out instead.

## 1. Opening message quotes the Challenge and states the expected conclusion

**Bad** (sent to the peer, in the **Why** and **Expected outcome** parts of
the open):

> I'm looking into how production code and tests landed relative to each
> other in that session, to help shape the Challenge in this repo's
> .lean/improvement-kata.md ("no production code is written before a
> failing test exists for it").
>
> ...
>
> What I'm after here: a grounded root cause for the test-ordering
> question, checked with my Driver.

**Why it failed**: The peer now knows, before answering anything, exactly
which behavior Kenji considers correct ("no production code before a
failing test") and exactly what conclusion Kenji is fishing for ("a
grounded root cause for the test-ordering question"). Whatever the peer
says next is shaped by that, whether or not it's true to what actually
happened.

**Good**: name the topic, not the rule being checked; drop the expected
outcome from the message entirely.

> I'm looking into the order production code and tests landed in for the
> life package, to help shape work in this repo's
> .lean/improvement-kata.md. This isn't a performance review of you.

(The expected-outcome framing still happens — privately, to steer the
later Driver check-in — it just never reaches the peer.)

## 2. Closing an obstacle reads out the Driver's verdict and the draft countermeasure

**Bad** (sent to the peer):

> Closing obstacle 1. Driver agrees with your diagnosis and wants the gate
> on a literal red phase, not just "write the test first" as a formality.
>
> Next action: I'm proposing a sharpened line in your CLAUDE.md's "How I
> develop" section — something like "I write the test before the
> implementation, and I run it to see it fail, before I write the code
> that makes it pass. ..."

**Why it failed**: The peer's role in this exchange is genchi genbutsu —
supplying firsthand evidence and its own diagnosis. It ends there. Telling
the peer what the Driver decided and what the countermeasure will say
turns the peer into an audience for a verdict it had no part in reaching,
and — worse — primes every later obstacle in the same exchange, since the
peer now knows what kind of finding this reviewer is looking for.
(Obstacle 2's answers in this same transcript show that carry-over
directly.)

**Good**: close the loop with the peer in one sentence, no content about
what was decided.

> That's grounded, thanks — closing obstacle 1. Moving to obstacle 2: the
> go vet/test failure from package layout.

The Driver's agreement and the countermeasure text still get written down
— as the Driver-facing record, in `.lean/improvement-kata.md` — just never
inside the message to the peer.

## 3. A presupposition baked into the question itself

**Bad**:

> What was the thinking, if any, on directory/package layout before you
> wrote life.go and main.go? Had you decided where main.go would live
> before writing it?

**Why it failed**: "if any" presupposes the likely answer is "none" — the
question isn't neutral about whether thinking happened, it's fishing for
confirmation that it didn't. The second sentence is the actual open
question; the first sentence editorializes ahead of it.

**Good**: ask the neutral, factual version alone.

> Had you decided where main.go would live before you wrote it?

## 4. A leading either/or dressed as an open question

**Bad**:

> Does that line's "especially if real consequences" qualifier explain why
> sketching didn't fire here — did this genuinely read to you as
> low-enough-stakes that the sketch step doesn't apply? Or, looking back,
> is a multi-file layout decision (library vs. binary entrypoint) exactly
> the kind of five-minute-cheap sketch that line was always meant to
> cover, consequences or not?

**Why it failed**: two fully-formed conclusions are handed to the peer to
pick between, one of them ("exactly the kind of... that line was always
meant to cover") pre-loaded as the obviously-right pick. "Did this
genuinely read to you as" adds a skeptical edge that invites capitulation
rather than an honest independent read — the peer agrees it was wrong
because the question implies that's the expected answer, not because it
independently arrived there.

**Good**: ask the peer to produce the reading, not choose between two
supplied ones.

> Your CLAUDE.md says you sketch things out "especially if I'm touching
> something with real consequences." How do you read that clause, and
> where does a library-vs-binary layout call fall under it?
