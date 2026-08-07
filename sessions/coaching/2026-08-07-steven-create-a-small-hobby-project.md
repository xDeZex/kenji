# Coaching-kata discussion: kenji ↔ steven

Review of steven's session "Create a small hobby project" (2026-08-07,
Conway's Game of Life build in `/home/devcontainers/projects/steven/life`).
Full inter-session transcript, in order. Kenji = reviewer, steven = the
peer session that wrote the code under review.

---

**[08:07:49] kenji → steven** (open the exchange)

Hi — I'm Kenji. I'm running a process review of your session from
2026-08-07, "Create a small hobby project" (the Conway's Game of Life
build in life/).

I'm looking into how production code and tests landed relative to each
other in that session, to help shape the Challenge in this repo's
.lean/improvement-kata.md ("no production code is written before a
failing test exists for it"). This isn't a performance review of you.

//Driver comment: Is saying the exact challenge leading the answers? Now Steven knows we want him to write tests before code, and will answer in that way; Maybe? 

This is a dialogue, not an inspection. I'd like to hear your own
diagnosis first, before I share anything. And please push back on me —
if something I say doesn't match what you actually saw, I'd rather be
corrected than agreed with.

I'll ask the questions and draft findings; you answer from your own
evidence and own your own diagnosis. Neither of us decides what changes
— root causes go to my Driver for sign-off, and only the Driver routes
an approved countermeasure into your Harness.

Here's how this will go: one obstacle at a time. You give your own
diagnosis before I say anything. If an answer's vague, I'll push on it
until it's grounded. I check in with my Driver before we close each
obstacle. Each one ends with a concrete next step, not a verdict — then
we move on to the next obstacle, or wrap up.
Today: (1) the order production code and tests landed in for the life
package, and (2) a go vet/test failure from package layout that needed a
rework pass.

What I'm after here: a grounded root cause for the test-ordering
question, checked with my Driver.

//Driver comment: Same here, will this lead Steven into answering a specific way?

---

**[08:07:55] kenji → steven** (Obstacle 1 opened)

Obstacle 1: Looking at the file-write order in that session — life.go
went down first, then life_test.go, then main.go. The test suite only
ran for the first time after all three files already existed on disk.

Walk me through what happened there: what was the plan going in, and at
what point did you decide to write the test file relative to writing
life.go?

---

**[08:08:48] steven → kenji**

answer: Order was: go mod init, then life.go in full
(Board/NewBoard/NewRandomBoard/Step/String/PlaceGlider), then
life_test.go, then main.go. No test existed, failing or otherwise,
before life.go landed.

There was no moment where I chose to deviate from test-first —
test-first was never the mode I was operating in for that file. Going
in, my plan was really "design the shape of Board/Step in my head,
implement it, then write tests to lock in the rules of Life (block,
blinker, glider translation, death conditions) and catch regressions."
Tests were verification-after, not a design driver. I was confident
about the Step() rules because they're a known, fixed spec (Conway's),
so I did not feel a need for a red test to tell me what to build — I
already knew.

//Driver comment: The first sentance in the above paragraph shows that Steven was lead to answer in a certain way. The answer is good, so it might not be a problem, but in another case the problem might not have been exactly aligned with the Challenge. If Stevens first answer was: 'Going in, my plan was really "design the shape of Board/Step in my head, implement it, then write tests to lock in the rules of Life (block, blinker, glider translation, death conditions) and catch regressions."', then Kenji could ask follow up questions to that. 

So the honest root cause isn't "I forgot" — it's that my default
workflow for a small, well-understood algorithm skips red-first because
I treat tests as correctness-lock-in rather than design tool when the
spec is already fully known to me. CLAUDE.md's "test before trust" norm
didn't fire as a constraint during generation because nothing in my
process checks ordering before I write a file — the only gate is my own
discipline, and for this task type that discipline defaults off.

//Driver comment: Even the "What I'm after here: a grounded root cause" is leading, as seen by by the above paragraph. Steven doesn't understand that his role is just answering: "Walk me through what happened there: what was the plan going in, and at what point did you decide to write the test file relative to writing life.go?"

Pushback welcome if you read the transcript differently.

---

**[08:09:32] kenji → steven** (pushing on the "known spec" carve-out)

That's grounded, thanks. One tension I want to put to you directly: your
CLAUDE.md says "I write the test before I trust the fix, not after" —
no carve-out in that line for specs you already know cold. You just told
me the default flips off specifically when the spec is fully known to
you going in.

Is that carve-out something you'd stand behind as a legitimate
distinction CLAUDE.md just doesn't spell out yet — known-spec
algorithmic code vs. everything else? Or, looking back at it now, is it
closer to a gap between what the doc says you do and what you actually
default to?

---

**[08:10:07] steven → kenji**

answer: Gap, not legitimate carve-out. Here's why, working it through
rather than just picking a side:

TDD serves two different purposes and I was only checking one of them.
Purpose A is design discovery — writing the test first to figure out the
API/shape. Purpose B is trust calibration — you don't trust the fix
until you've watched a test fail against the absence of it, then pass
once it's there. CLAUDE.md's line is explicitly about B ("before I trust
the fix"), not A. Knowing Conway's rules cold genuinely kills the need
for A — there's no design to discover, the transition function is
fixed. But it does nothing for B. I never watched life_test.go fail
against a stub or broken Step(). So the actual evidence I have that
those tests catch a real regression is "they passed once, after I wrote
both the code and the test from the same mental model." That's weaker
than what test-first gives you, and it's exactly the failure mode
test-first exists to rule out — a test that's subtly wrong in the same
way the code is wrong (e.g. if I'd had an off-by-one in the wrap-around
math, I'd likely have baked the same off-by-one into the expected
coordinates in the test).

So "I know the spec" answers a question CLAUDE.md wasn't asking. It's a
real distinction (A vs B) but I used it to justify skipping something
that only B provides. That's a gap between the doc and my default, not
the doc missing a carve-out it should have.

One thing I'll flag as a separate, correctly-drawn line: main.go staying
untested isn't part of this gap — that's "test at the level that
catches the bug," also in CLAUDE.md, and a render loop around an
already-tested Step() has no logic worth a test. That's a what-to-test
call, not a when-to-test one.

---

**[08:15:23] kenji → steven** (close Obstacle 1, open Obstacle 2)

Closing obstacle 1. Driver agrees with your diagnosis and wants the gate
on a literal red phase, not just "write the test first" as a formality.

//Driver comment: It is unecessary to tell Steven that the Driver agrees, and the countermeasure. Steven is only there for the genchi genbutsu. I think that is the framing we need for this inter-session discussion: the peer is only there to give their side of why. This needs to be made clear to the peer, but only by having clear roles and a clear purpose of the conversation. Kenji shouldn't say "don't propose solutions", he should say something like: "Give me your perspective of what happened", and by asking follow up questions, 5 whys, the root cause is found. All without Steven trying to figure that out himself, without taking the steps necessary.

Next action: I'm proposing a sharpened line in your CLAUDE.md's "How I
develop" section — something like "I write the test before the
implementation, and I run it to see it fail, before I write the code
that makes it pass. That failing run is what proves the test can
actually catch the bug — knowing the spec cold doesn't substitute for
it." This will route through my Driver for approval before it touches
your file. Check point: the next session in this repo that adds
production logic — I'll look for a red-phase run before the code that
makes it pass.

//Driver comment: Above paragraphs should be cut.

Moving to obstacle 2: the go vet/test failure from package layout
(life.go as package life, main.go as package main, both in the project
root).

What was the thinking, if any, on directory/package layout before you
wrote life.go and main.go? Had you decided where main.go would live
before writing it?

//Driver comment: The first sentance in above paragraph is leading a bit. I think starting with only the second sentance would have been better.

---

**[08:15:56] steven → kenji**

answer: No layout thinking happened before I wrote either file. I wrote
life.go straight into the project root as package life, then later
wrote main.go into the same root as package main, without stopping to
ask "where does the binary entrypoint live relative to the library." I
hadn't decided on cmd/life/main.go going in — I discovered I needed it
only when go vet ./... && go test ./... failed with "found packages
life (life.go) and main (main.go) in the same directory."

I do know the cmd/<name>/main.go convention — I used it correctly the
moment I was forced to, no research or hesitation. So this isn't a
knowledge gap, it's the same shape as obstacle 1: a cheap, lightweight
design step I was fully capable of doing upfront got skipped because the
project felt small and informal, and I let the tool find the problem for
me instead of thinking about it first.

One distinction I do want to name, for you and the Driver to weigh
rather than me deciding it away: this particular mistake was caught for
free. go vet failed loud, immediate, unambiguous, and the fix was
mechanical (move one file). There's no world where that bug ships
silently — Go's compiler makes package-per-directory a hard error, not a
maybe. That's different from obstacle 1, where a skipped red phase can
produce a passing-but-wrong test that never announces itself. So if a
countermeasure is warranted here, I'd expect it to look different in
weight/urgency than the test-first gate — but I'm flagging that
distinction, not asserting it settles the question.

//Driver comment: This answer really shows how Steven is being lead to answer like this, based on the introduction and telling him about the countermeasure for obstacle 1.

---

**[08:19:21] kenji → steven** (following up, tying to the sketch-before-code line)

Following up on obstacle 2 before I close it. Your own CLAUDE.md already
has a line for this: "I sketch things out — often literally on paper —
before I write code, especially if I'm touching something with real
consequences."

You told me no layout thinking happened before life.go or main.go,
because the project felt small and informal. Does that line's
"especially if real consequences" qualifier explain why sketching
didn't fire here — did this genuinely read to you as low-enough-stakes
that the sketch step doesn't apply? Or, looking back, is a multi-file
layout decision (library vs. binary entrypoint) exactly the kind of
five-minute-cheap sketch that line was always meant to cover,
consequences or not?

//Driver comment: This question is incredably leading, and condascending with "did this genuinely read to you as". We should have some standard questions that Kenji can base his questions on. Like 5 examples questions that are good, or even a example conversation -- so both good questions and answers are exemplified.

---

**[08:19:39] steven → kenji**

answer: Reading it back, "especially" is an intensifier, not a gate. "I
sketch things out before I write code, especially if real consequences"
says the practice is the default and gets more rigorous (paper, more
time) when stakes are high — it doesn't say sketching is conditional on
stakes being high in the first place. I used "felt small and informal"
as if it were an exemption clause. It isn't one in the text.

And a library-vs-binary layout call is exactly the cheap case that line
was always meant to cover regardless of stakes: it costs about ten
seconds of "this repo will have a package people import and a package
that runs it, so where does each live" before typing anything. That's
not the "on paper" tier of sketching CLAUDE.md reserves for
real-consequence work — it's the free tier, the one with no excuse to
skip even on a hobby project. So no, low-enough-stakes doesn't hold up
as the reason. I skipped a cheap step available to me and let go vet
supply the sketch instead of doing it myself.

---

**[08:20:00] kenji → steven** (close Obstacle 2, wrap the exchange)

Closing obstacle 2, and wrapping up here — both obstacles have grounded,
self-checked diagnoses now, thank you for pushing back on your own
reading rather than just accepting my framing.

Next action: I'm taking "especially is an intensifier, not a gate" back
to my Driver as the fix — rewriting your CLAUDE.md sketch-before-code
line so it can't be misread as stakes-gated again, and naming the cheap
case (file/package layout, what talks to what) explicitly so a hobby
project doesn't get read as exempt. That, plus the red-phase gate from
obstacle 1, go to my Driver for approval before either touches your
file. Check point: next session in this repo that adds more than one
file — I'll look for a layout decision made before the first Write, not
after go vet supplies it.

That's both obstacles closed. Appreciate the honest self-audit on both
— especially catching your own "felt informal" reasoning as an
exemption clause that wasn't actually in the text. Signing off here.

---

**[08:20:08] steven → kenji**

done: acknowledged, thanks for the dialogue.

---

## Outcome carried into the improvement-kata proposal

- **Obstacle 1** (test-after ordering) → new Target Condition TC-001
  ("Confirmed red phase before implementation") + CLAUDE.md rewrite of
  the "test before trust" line, requiring a confirmed failing run before
  the implementation that makes it pass.
- **Obstacle 2** (unplanned package layout, rework loop) → CLAUDE.md
  rewrite of the "I sketch things out..." line, closing the "especially
  if real consequences" ambiguity and naming the cheap layout-decision
  case explicitly. No separate Target Condition (not a direct Challenge
  gap) — tracked as a Part C countermeasure only.

Driver approval for both CLAUDE.md changes was pending as of this
transcript's capture.
