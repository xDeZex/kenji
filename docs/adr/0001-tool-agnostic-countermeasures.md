# Tool-agnostic countermeasure storage

Countermeasures are stored as PDCA Items in `data/kaizen_backlog.json`, not injected directly into any AI tool's instruction file (e.g., `copilot-instructions.md`, `CLAUDE.md`, or `AGENTS.md`).

This repo is used with multiple AI tools (VS Code Copilot Chat, Claude Code, OpenCode). Coupling Kenji's countermeasures to a single tool's instruction format would make the kaizen process invisible to sessions run in a different tool, and would require migrating all experiments when switching tools. The kaizen backlog is the single source of truth; applying a standardized countermeasure to a specific tool's config is a deliberate, manual act — not automatic.
