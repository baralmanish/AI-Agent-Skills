---
agent: agent
description: Create a personalized weekly meal plan for weight loss
tools:
  - search/codebase
  - edit/editFiles
  - search
  - execute/runInTerminal
  - execute/getTerminalOutput
  - read/terminalLastCommand
  - read/terminalSelection
---
Use the skill definition at ./skills/weekly-meal-planner-weightloss/SKILL.md.
Apply it to the user request below and produce the full meal planning outputs.
If key details are missing, ask one concise follow-up question before proceeding.

User input:
${input}
