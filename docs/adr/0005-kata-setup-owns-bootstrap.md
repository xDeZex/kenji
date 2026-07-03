# Kata Setup is a separate skill; improvement-kata delegates to it

Bootstrapping a Target Repo's Challenge and Harness could have stayed inline in improvement-kata's step 2, as a fallback triggered only when the sections are missing. Instead it lives in its own skill, kata-setup, which improvement-kata invokes rather than reimplementing. Keeping the logic in one place means a future change to how Challenge or Harness get drafted happens once, and the setup work can also be run directly ahead of a repo's first Review instead of surfacing reactively mid-Review.
