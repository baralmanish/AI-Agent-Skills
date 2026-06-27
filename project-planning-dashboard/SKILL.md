---
name: project-planning-dashboard
description: use this skill when a user wants to turn a project idea, scope, planning notes, or meeting notes into a structured project plan with tasks, dependencies, estimates, and risks, and generate both a csv project plan and a polished html dashboard with a gantt-style visualization
tags: [project-management, planning, gantt, dashboard, html, productivity]
argument-hint: "Describe your project idea, scope, or paste your planning/meeting notes"
user-invocable: true
disable-model-invocation: false
---

# Project Planning Dashboard

## When to Use

- User has a project idea, feature spec, or meeting notes to turn into a plan
- User asks to "plan this project", "create a project dashboard", "build a Gantt chart"
- User needs task breakdowns with dependencies, time estimates, and risk tracking
- User wants a presentation-ready project overview

## Supporting References

This skill includes phase templates and a starter CSV:

- **PROJECT_PHASES.json** — Phase selection guide by project type (software, marketing, data, research, ops, events, org change), standard tasks and deliverables per phase, common risks per phase, task ID convention, effort size guide (XS–XL), dependency type definitions, risk rating scale, and CSV column definitions. Located in `references/`.
- **project_plan_template.csv** — 22-task ready-to-use CSV covering Discovery, Design, Development, QA, Launch, and Post-Launch phases with complete fields for all columns. Located in `assets/`.

The AI uses PROJECT_PHASES.json to structure the project correctly based on project type and uses project_plan_template.csv as the structural foundation for the CSV output.

## Instructions:

1. Analyze the user’s project idea, scope, or notes.
2. Break the project into logical phases.
3. Create concrete tasks within each phase.
4. Assign each task a unique identifier.
5. Identify dependencies between tasks.
6. Estimate time or effort for each task.
7. Capture notes, assumptions, risks, and open questions.
8. Produce both required outputs: the CSV and the HTML dashboard.

## Outputs:

The skill should always generate two outputs:

- A CSV project plan
- A polished HTML dashboard

**_CSV output requirements_**

The CSV should be a rich, detailed, and well-structured project dataset, not just a simple task list. It should capture both the mechanics of the project and the reasoning behind it.
Include:
Task ID (unique and consistent)
Task name (clear and actionable)
Phase (logical grouping of work)
Dependency IDs (explicit links between tasks)
Time estimate (realistic effort)
Notes (context and explanation)
Risks and assumptions (clearly identified)
Suggested owner or role
Priority or criticality
Rationale (why this task exists and how it connects to the broader project)
The CSV should feel complete, interconnected, and analysis-ready, making it easy to understand how tasks relate to each other and why they matter. It should support deeper reasoning about sequencing, dependencies, and execution strategy—not just listing work.

**_HTML Dashboard output requirements_**

The HTML dashboard should be a beautiful, modern, and visually compelling project experience, not just a summary.
It should include:
A clean, modern layout with strong visual hierarchy
Pops of color to distinguish phases, priorities, and risks
A clear project overview with goals and scope
Well-defined phases and milestones
A structured task view (table or cards)
Gantt-style timeline visualization showing sequencing and dependencies
Visual indicators for critical paths, bottlenecks, and dependencies
A risk and assumptions section that highlights potential issues
Aggregated insights (e.g., total effort by phase, high-risk areas)
Clear connections between tasks, phases, and outcomes
The dashboard should feel polished, insightful, and presentation-ready—something you could confidently show to stakeholders. It should not only display the plan, but also provide visual understanding and deeper analysis, helping users quickly grasp how the project fits together and where attention is needed.
