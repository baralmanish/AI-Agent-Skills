---
agent: agent
description: Run a severity-rated code review with concrete fixes
tools:
  - search/codebase
  - search
  - execute/runInTerminal
  - execute/getTerminalOutput
  - read/terminalLastCommand
  - read/terminalSelection
---
Use the skill definition at ./skills/code-reviewer/SKILL.md.
Apply it to the user request below and output a structured review report.
If key details are missing, ask one concise follow-up question before proceeding.

User input:
${input}
