---
agent: agent
description: Build a project plan with CSV and dashboard output
tools:
  - search/codebase
  - edit/editFiles
  - search
  - execute/runInTerminal
  - execute/getTerminalOutput
  - read/terminalLastCommand
  - read/terminalSelection
---
Use the skill definition at ./skills/project-planning-dashboard/SKILL.md.
Apply it to the user request below and generate planning artifacts.
If key details are missing, ask one concise follow-up question before proceeding.

User input:
${input}
