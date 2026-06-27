# Project Planning Dashboard Skill

## Overview

**Project Planning Dashboard** turns project ideas, scope notes, or meeting notes into a structured project plan with dependencies, risks, estimates, and a polished HTML dashboard.

## What This Skill Does

The skill always aims to generate two deliverables:

1. a detailed CSV project plan
2. a polished HTML dashboard with a Gantt-style view

It breaks work into phases, tasks, dependencies, owners, priorities, risks, and rationale so the result is useful for both planning and stakeholder review.

## Sample Prompts For Testing

### Turn Notes Into a Plan

```text
Turn the project notes below into a complete project plan.
Break the work into phases, tasks, dependencies, time estimates, and risks.
Generate both a CSV plan and a polished HTML dashboard.
```

### Build a Gantt Dashboard

```text
Create a project planning dashboard from the scope below.
Show tasks, milestones, dependencies, critical path, and a Gantt-style timeline.
Also provide the supporting CSV dataset.
```

### Meeting Notes to Execution Plan

```text
Use the meeting notes below to build an execution plan.
Identify tasks, owners, risks, open questions, and sequencing.
Return both the CSV project plan and an HTML dashboard.
```

### Roadmap Breakdown

```text
Break the roadmap below into phases and concrete tasks.
Assign dependencies, priorities, and rationale, then generate a project dashboard I can share with stakeholders.
```

## Typical Outputs

- CSV project plan with IDs, phases, dependencies, owners, estimates, and risks
- HTML dashboard with project overview, tasks, risks, and Gantt-style visualization
- aggregated project insights and bottleneck visibility

## Files

| File                               | Purpose                                                                       |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| `SKILL.md`                         | Full skill definition and output requirements                                 |
| `QUICK_REFERENCE.md`               | Phase templates, task ID convention, effort sizing guide                      |
| `references/PROJECT_PHASES.json`   | Standard phases by project type with tasks, risks, and deliverables per phase |
| `assets/project_plan_template.csv` | 22-task ready-to-use CSV template covering all standard phases                |
