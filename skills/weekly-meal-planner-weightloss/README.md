# Weekly Meal Planner Weight Loss Skill

## Overview

**Weekly Meal Planner Weight Loss** creates personalized weekly meal plans for sustainable fat loss, along with nutrition targets, shopping lists, prep guidance, and dashboard-style summaries.

## What This Skill Does

Use this skill when you want a practical nutrition plan that balances calorie targets, macros, food preferences, schedule, and budget.

It can generate:

- weekly meal plans
- calorie and macro guidance
- shopping lists by category
- meal prep suggestions
- progress and motivation dashboards

## Sample Prompts For Testing

### General Weight Loss Plan

```text
Create a weekly meal plan for sustainable weight loss.
I want meals I can realistically follow, with calories, macros, a shopping list, and prep guidance.
```

### High-Protein Budget Plan

```text
Build a high-protein weekly meal plan for weight loss under my budget.
Include simple recipes, shopping list, and macro targets.
```

### Preference-Based Plan

```text
Create a weight-loss meal plan based on the food preferences and constraints below.
Make it practical for weekdays and easy to prep in advance.
```

### Structured Dashboard Output

```text
Design a weekly meal-planning dashboard for fat loss.
Show daily meals, calorie targets, macros, shopping list, and progress guidance in a polished layout.
```

## Typical Outputs

- weekly meal schedule
- calories and macro breakdowns
- categorized shopping list
- prep notes and adherence guidance
- dashboard-style summary

## Files

| File                                  | Purpose                                                                              |
| ------------------------------------- | ------------------------------------------------------------------------------------ |
| `SKILL.md`                            | Full skill definition, 8-step process, and output requirements                       |
| `QUICK_REFERENCE.md`                  | TDEE table, macro splits by diet, script usage                                       |
| `references/NUTRITION_REFERENCE.json` | TDEE formulas, activity multipliers, macro ratios, common food macros, deficit rules |
| `assets/meal_plan_template.csv`       | 7-day meal plan CSV template with daily macro targets                                |
| `scripts/tdee_calculator.py`          | CLI TDEE + calorie/macro target calculator                                           |
