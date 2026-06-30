# Kenji applies countermeasures directly to instruction files

Status: accepted — supersedes ADR-0001

ADR-0001 kept countermeasures out of AI instruction files to stay tool-agnostic across VS Code Copilot, Claude Code, and OpenCode. The cost was that improvements sat in the kaizen backlog but were rarely applied — a PDCA cycle with no "Do" step. The improvement-kata skill makes Kenji the agent who closes that loop: he proposes changes, gets user approval, and applies them directly to instruction files (AGENTS.md, CLAUDE.md, etc.) and other target repo files in the same session that diagnosed the waste. The tool-agnostic concern remains valid but is now handled at the Target Condition level: Kenji edits the instruction file appropriate to the current tool rather than deferring all application to the developer.
