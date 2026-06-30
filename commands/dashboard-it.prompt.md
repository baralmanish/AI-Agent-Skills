---
agent: agent
description: Build an interactive dashboard from the provided context
tools:
  - search/codebase
  - edit/editFiles
  - search
  - execute/runInTerminal
  - execute/getTerminalOutput
  - read/terminalLastCommand
  - read/terminalSelection
---
Use the skill definition at ./skills/dashboard-it/SKILL.md.
Apply it to the user request below and generate the final artifacts.
If key details are missing, ask one concise follow-up question before proceeding.

User input:
${input}
