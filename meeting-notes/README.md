# Meeting Notes Skill

Transforms raw meeting notes, transcripts, or voice memo summaries into a clean, structured output: decisions log, action items with owners and deadlines, discussion summary, and an optional follow-up email draft.

## Triggers

- "Summarize these meeting notes"
- "Extract action items from this transcript"
- "Clean up my notes from today's call"
- "Turn this into a follow-up email"

## Outputs

1. Meeting metadata (type, date, attendees)
2. TL;DR executive summary (2–3 sentences)
3. Decisions made (table)
4. Action items with owner, due date, and priority (table)
5. Discussion summary by topic
6. Open questions and blockers
7. Follow-up email draft (when 3+ action items or explicitly requested)

## Supported Meeting Types

- Standups (compressed Yesterday / Today / Blockers format)
- Planning sessions
- Retrospectives
- Client calls
- Executive syncs
- All-hands / town halls

## Sample Prompts

### Standup Summary

```text
Here are today's standup notes — clean them up.
Separate by person: yesterday, today, blockers.
Flag anything that needs immediate attention.
```

### Planning Session

```text
Summarize the planning session notes below.
Extract all decisions, action items with owners and deadlines,
and any open questions we still need to answer.
```

### Retrospective

```text
Turn these retro notes into a structured summary.
Include what went well, what to improve, and
one action item per improvement area with a named owner.
```

### Client Call Follow-Up

```text
Summarize this client call and write the follow-up email.
Separate our commitments from what the client agreed to do.
Send within 24 hours.
```

### Executive Sync

```text
Turn these exec sync notes into an executive brief.
Scannable in under 2 minutes — lead with decisions, then action items.
Every action item needs a named owner and a hard deadline.
```

### Extract Action Items Only

```text
From the meeting notes below, extract only the action items.
For each one: what is the task, who owns it, and when is it due?
Mark anything without a clear owner as TBD.
```

### Generate Follow-Up Email

```text
Write the follow-up email for the meeting notes below.
Subject line format: [Meeting Type] — [Date] Summary & Action Items
Include the TL;DR, decisions made, and action items table.
```

## Files

| File                             | Purpose                                                                                 |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| `SKILL.md`                       | Full skill definition, process, decision rules, and output template                     |
| `QUICK_REFERENCE.md`             | Trigger phrases, meeting type table, priority and deadline defaults                     |
| `references/MEETING_TYPES.json`  | Output format, required sections, owner/deadline inference, email tone per meeting type |
| `assets/action-item-tracker.csv` | Downloadable CSV template for tracking action items across meetings                     |
