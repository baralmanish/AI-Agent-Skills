---
name: meeting-notes
description: "Use this skill when the user provides raw meeting notes, a transcript, or a voice memo summary and wants a structured output: clean summary, decisions log, action items with owners and deadlines, and an optional follow-up email draft."
tags: [meetings, productivity, summarization, action-items, team-collaboration]
argument-hint: "Paste your raw meeting notes, transcript, or recording summary"
user-invocable: true
disable-model-invocation: false
---

# Meeting Notes

Transform raw, messy meeting notes or transcripts into a clean, structured summary that a team can act on immediately.

## When to Use

- User pastes raw notes from a meeting, workshop, or standup
- User uploads or pastes a transcript from Zoom, Teams, or similar
- User says "clean up my meeting notes", "summarize this call", "extract action items"
- User needs a follow-up email ready to send to attendees

## Inputs

- **Required:** Raw meeting notes, transcript, or voice memo text
- **Optional via `$ARGUMENTS`:** Meeting type (standup, planning, retrospective, executive sync, client call), attendee names, project context

## Process

### Step 1: Identify Meeting Context

Before structuring, determine:

- **Meeting type**: Standup, planning, retrospective, decision-making, client call, all-hands
- **Key participants**: Who owns outcomes and who needs to be informed
- **Primary purpose**: What was this meeting trying to accomplish?
- **Time frame**: When decisions and actions are due

If the meeting type is ambiguous, infer it from the content tone and structure.

### Step 2: Extract and Categorize Content

Scan the full notes and extract all content into four buckets:

- **Decisions made**: Any conclusions, agreements, or approvals reached
- **Action items**: Tasks with a responsible person and deadline (infer if not stated)
- **Discussion topics**: Key points discussed, context, and rationale
- **Open questions / blockers**: Unresolved items that need follow-up or escalation

### Step 3: Assign Owners and Deadlines

For every action item:

- Assign an owner (use the person mentioned most recently in context, or flag as "TBD" if unclear)
- Set a deadline (use stated due date, or default to "End of this week" if not specified)
- Rate urgency: **High** (blocks others), **Medium** (on track), **Low** (nice-to-have)

### Step 4: Draft the Structured Output

Produce all required sections in order. Do not skip sections — mark them "None" if genuinely empty.

### Step 5: Draft Follow-up Email (if requested or contextually needed)

- Subject: `[Meeting Type] — [Date] Summary & Action Items`
- Audience: All attendees + any relevant stakeholders not in the meeting
- Tone: Professional, concise, forward-looking
- Include: Summary paragraph, decisions, action item table, next meeting date if known

## Decision Rules

- If notes are very sparse (fewer than 5 lines): ask one clarifying question before proceeding
- If a task has no clear owner: mark as "TBD" and flag it explicitly
- If conflicting decisions appear: note both versions and flag for clarification
- If the meeting was clearly a standup: use the compressed standup format (Yesterday / Today / Blockers per person)
- Never invent decisions or tasks that are not supported by the notes

## Quality Criteria (Completion Checks)

Every response must include:

- ✅ Meeting metadata (date if available, type, attendees if mentioned)
- ✅ TL;DR (2–3 sentence executive summary)
- ✅ Decisions log (or "None")
- ✅ Action items table with Owner, Due Date, and Priority
- ✅ Discussion summary (key points, not a transcript)
- ✅ Open questions / blockers (or "None")
- ✅ Follow-up email draft (if 3+ action items or explicitly requested)

## Output Template

---

### Meeting Summary

**Date:** [date or "Not specified"]  
**Type:** [Standup | Planning | Retro | Client Call | Executive Sync | Other]  
**Attendees:** [names or "Not specified"]

**TL;DR:** [2–3 sentence summary of what happened and what was decided]

---

### Decisions Made

| #   | Decision   | Decided By          |
| --- | ---------- | ------------------- |
| 1   | [decision] | [person or "Group"] |

---

### Action Items

| #   | Task   | Owner         | Due Date        | Priority            |
| --- | ------ | ------------- | --------------- | ------------------- |
| 1   | [task] | [name or TBD] | [date or "EOW"] | High / Medium / Low |

---

### Discussion Summary

**[Topic 1]:** [Key points, context, rationale]

**[Topic 2]:** [Key points, context, rationale]

---

### Open Questions & Blockers

| #   | Question / Blocker | Raised By         | Status                   |
| --- | ------------------ | ----------------- | ------------------------ |
| 1   | [item]             | [person or "TBD"] | Unresolved / Needs Owner |

---

### Follow-up Email Draft

**To:** [Attendee names or emails]  
**Subject:** [Meeting Type] — [Date] Summary & Action Items

[Body of email]

---

## Supporting References

This skill includes reference files that govern output format and decision rules:

- **MEETING_TYPES.json** — Per-type output format, required sections, owner/deadline inference rules, follow-up email guidance, and tone by meeting type. Located in `references/`.
- **action-item-tracker.csv** — Downloadable CSV template for tracking action items across multiple meetings. Located in `assets/`.

The AI uses MEETING_TYPES.json to determine which output sections to include, what to skip, and how to format the follow-up email for each meeting type.

---

## Example Invocations

- `"Summarize these meeting notes from our product planning call"`
- `"Extract action items from this Zoom transcript"`
- `"Turn this into a structured summary I can send to the team"`
- `"Here are my standup notes — clean them up"`
