---
agent: agent
description: Convert raw notes into structured meeting outputs
tools:
  - search/codebase
  - edit/editFiles
  - search
---
Use the skill definition at ./skills/meeting-notes/SKILL.md.
Apply it to the user request below and produce the full meeting summary package.
If key details are missing, ask one concise follow-up question before proceeding.

User input:
${input}
