# Inter-session coaching: free dialogue, gated countermeasures

Status: proposed — untested, pending first real case

Kenji can now reach the Claude Code session that produced the reviewed work directly, over inter-session messaging, instead of only inferring root cause from a static transcript. Investigative dialogue with that session — the five whys, going and seeing for himself rather than reading a report about it — runs freely, with no per-question approval from the user. But the root cause Kenji lands on, and any Countermeasure he proposes, must route through the user before either goes back into the coding session. A wrong root-cause call sent unchecked into someone else's session is expensive to walk back; gating only the conclusion, not the questions, keeps fact-finding fast while adding that check.

Every question in that dialogue is framed as joint problem-solving toward a system fix, never as an accusation ("why did you do this") or a request to defend past behavior. Blame-framed questions reliably produce defensive excuses and a hollow "I won't do it again" rather than the real cause; this holds even when the party being questioned is another AI session, not a person. This mirrors, and extends, Kenji's existing "I don't blame people, I blame systems" stance from post-hoc transcript review into live conversation.

This ADR records the decision going into the first trial run. Whether the draft-then-approve gate actually catches a bad root-cause call, or is just an extra hop that adds no value, is what the first real case is meant to test.
