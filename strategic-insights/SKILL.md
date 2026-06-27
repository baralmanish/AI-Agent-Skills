---
name: strategic-insights
description: "Use this skill to help the user identify strategic insights related to work, professional growth, and career direction; propose one weekly change, one simple tracking method, a What/Why/How table, and a downloadable CSV tracker."
argument-hint: "Optional focus area (e.g., leadership, communication, career strategy, productivity)"
user-invocable: true
disable-model-invocation: false
---

# Strategic Insights Coach

Use this skill to surface one under-leveraged professional opportunity from conversation patterns, then run a 1-week experiment with simple tracking.

## When to Use

Use this skill when the user asks for:

- Strategic work or career insight
- A hidden pattern they may not be fully leveraging
- A simple weekly improvement experiment
- A lightweight way to track outcomes

## Inputs

- Primary input: available conversation history (or current conversation if prior history is unavailable)
- Optional argument (`$ARGUMENTS`): focus area (e.g., leadership, communication, career transitions)

## Supporting References

This skill includes strategic frameworks and insight identification models:

- **INSIGHT_FRAMEWORKS.json** — Signal lists for hidden strengths, underuse, and blind spots; five strategic frameworks (Ikigai, Strength Zone, Career Capital, Visibility vs. Impact Matrix, Contribution Ladder); weekly experiment design principles and categorized experiments by theme (communication, visibility, focus, relationships, decisions); output quality rules. Located in `references/`.
- **weekly-insight-tracker.csv** — Downloadable weekly experiment tracker. Located in `assets/`.

The AI uses INSIGHT_FRAMEWORKS.json to apply the most relevant framework to the user's situation and design a testable, specific weekly experiment.

## Process

1. **Reflect on prior conversation evidence**
   - Identify recurring patterns in how the user thinks, decides, communicates, and executes.
   - If historical context is limited, use current conversation evidence and explicitly state uncertainty.

2. **Reveal one hidden under-leveraged opportunity**
   - Tell the user one strategic insight about themselves that they likely have not fully leveraged in life/professional career.
   - Keep it practical, strengths-based, and specific.

3. **Propose one simple weekly change**
   - Exactly one change to try for 7 days.
   - Low-friction, realistic, and testable.

4. **Propose one simple tracking method**
   - One daily indicator and one weekly outcome indicator.
   - Tracking effort should be minimal.

5. **Output in required formats**
   - Provide a simple table with columns: `What`, `Why`, `How`.
   - Provide CSV content the user can copy.
   - Reference the downloadable CSV file: [`weekly-insight-tracker.csv`](./assets/weekly-insight-tracker.csv).

## Required Output Contract

Every response must include all of the following:

1. **Hidden strategic insight** (one concise insight)
2. **One weekly change** (single behavior)
3. **One simple tracking method** (daily + weekly metric)
4. **Action table** with `What | Why | How`
5. **CSV section** matching the downloadable tracker template

The purpose of this skill is to produce a practical behavior experiment with measurable tracking and a ready-to-use CSV capture format.

## Output Template

### Strategic Insight

- [1 concise insight the user likely has not fully leveraged]

### Weekly Change

- **Change:** [single behavior]
- **Duration:** 7 days
- **Daily effort:** [minutes/day]

### Action Table

| What         | Why                | How                      |
| ------------ | ------------------ | ------------------------ |
| [one change] | [strategic reason] | [simple daily execution] |

### Tracking

- **Daily metric:** [binary or count]
- **Weekly metric:** [outcome measure]

### CSV (copy/paste)

Use this CSV block or download the template at [`./assets/weekly-insight-tracker.csv`](./assets/weekly-insight-tracker.csv).

```csv
date,focus_area,strategic_insight,weekly_change,completed_0_1,daily_minutes,weekly_outcome_signal,notes
YYYY-MM-DD,[focus],[insight],[change],0,0,[signal],[notes]
```
