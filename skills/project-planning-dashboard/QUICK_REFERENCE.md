# Project Planning Dashboard — Quick Reference

## Trigger Phrases

```
"Plan this project"
"Create a project dashboard for [project name]"
"Turn these notes into a project plan"
"Build a Gantt chart for this"
"I need a project plan with tasks, dependencies, and risks"
```

## What Gets Generated (Always Both)

1. **CSV project plan** — task IDs, phases, dependencies, estimates, owners, risks, rationale
2. **HTML dashboard** — Gantt-style timeline, critical path, task cards, risk view, phase summaries

## Standard Phase Templates

| Project Type         | Phases                                                       |
| -------------------- | ------------------------------------------------------------ |
| Software / Product   | Discovery → Design → Development → QA → Launch → Post-Launch |
| Marketing Campaign   | Strategy → Creative → Approval → Launch → Measurement        |
| Data / Analytics     | Scoping → Data Prep → Analysis → Reporting → Handoff         |
| Research / Audit     | Scoping → Research → Analysis → Synthesis → Recommendations  |
| Operations / Process | Assessment → Design → Pilot → Rollout → Review               |
| Event                | Planning → Content → Promotions → Execution → Wrap-Up        |

## Task ID Convention

`[PHASE]-[NUMBER]` — e.g., `DIS-001`, `DEV-003`, `QA-001`

## Effort Size Guide

| Size | Hours | Description                          |
| ---- | ----- | ------------------------------------ |
| XS   | 1–4   | Quick task, single person, <half day |
| S    | 4–16  | 1–2 day task                         |
| M    | 16–40 | Multi-day, likely needs coordination |
| L    | 40–80 | Full week + effort                   |
| XL   | 80+   | Break into subtasks                  |

## Risk Ratings

- **High** — needs owner + mitigation plan now
- **Medium** — monitor with named watch owner
- **Low** — log and revisit if surfaces

## CSV Column Set

`task_id · task_name · phase · dependency_ids · effort · estimated_hours · owner_role · priority · risk_level · notes · rationale`

## Reference Files

- `references/PROJECT_PHASES.json` — standard phases by project type, typical tasks, common risks, deliverables per phase
- `assets/project_plan_template.csv` — ready-to-use CSV with 22 real tasks across all phases
