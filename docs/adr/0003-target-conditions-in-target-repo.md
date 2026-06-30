# All improvement records live in the Target Repo

The Challenge, all Target Conditions, their Experiments, and the Kaizen Backlog are stored in the Target Repo, not in leanAgent. The only artifact leanAgent retains is Review Reports in `sessions/reports/`.

leanAgent was the original home for all improvement records (the kaizen backlog). Co-locating everything with the work it governs has a decisive advantage: when a developer or AI tool opens the target repo, the improvement goals, history, and backlog are all right there. The kaizen backlog as a separate index in leanAgent was redundant once Target Conditions moved — `.lean/improvement-kata.md` is already the complete record. The only thing that belongs in leanAgent is the session review history.
