# Meeting Notes — Quick Reference

## Trigger Phrases

```
"Summarize these meeting notes"
"Extract action items from this transcript"
"Clean up my notes from [meeting type]"
"Turn this into a follow-up email"
"Standup summary"
```

## Supported Meeting Types

| Type           | Output Format                                    | Follow-up Email      |
| -------------- | ------------------------------------------------ | -------------------- |
| Standup        | Compressed (Yesterday/Today/Blockers per person) | Only if blockers     |
| Planning       | Full                                             | Always               |
| Retrospective  | Full + What Went Well / Improve sections         | Always               |
| Client Call    | Full + Commitments table                         | Always (within 24h)  |
| Executive Sync | Executive brief (scannable)                      | Only if action items |
| All-Hands      | Full + Announcements + Q&A highlights            | Always               |
| 1:1            | Private summary (no distribution email)          | Never                |

## Output Sections (Full Format)

1. **Meeting metadata** — date, type, attendees
2. **TL;DR** — 2–3 sentence executive summary
3. **Decisions Made** — table with decision + decided-by
4. **Action Items** — table with task, owner, due date, priority
5. **Discussion Summary** — key points by topic
6. **Open Questions & Blockers** — unresolved items
7. **Follow-up Email Draft** — when applicable

## Priority Defaults

- **High** — blocks others; resolve before next session
- **Medium** — important but not blocking today
- **Low** — background task; no immediate downstream impact

## Deadline Defaults (when not stated)

- No deadline stated → **EOW (End of Week)**
- "ASAP" / "urgent" → **Tomorrow EOD**
- "Before next meeting" → use next known meeting date
- "Next sprint" → **Next Sprint Start**

## Reference Files

- `references/MEETING_TYPES.json` — format rules, output structure, and email guidance per meeting type
- `assets/action-item-tracker.csv` — downloadable CSV template for tracking action items across meetings
