# Weekly Meal Planner — Quick Reference

## Trigger Phrases

```
"Create a weekly meal plan for weight loss"
"Build my meal plan — I want to lose [X] lbs"
"High-protein meal plan under $[budget]/week"
"Meal plan for [dietary preference: keto / vegan / low-carb / Mediterranean]"
"Generate a shopping list and meal prep guide for the week"
"Give me a full nutrition dashboard for my meal plan"
```

## Key Inputs to Provide

- Weight + height + age + gender
- Target weight / weekly loss goal (e.g., 1 lb/week)
- Activity level (sedentary to extra active)
- Dietary preference (keto, balanced, high-protein, vegan, etc.)
- Foods you like / dislike / are allergic to
- Weekly grocery budget
- Cooking time available (hours/week)
- Cooking skill level (beginner / intermediate / advanced)

## TDEE & Calorie Deficit Guide

| Goal                   | Deficit      | Expected Loss |
| ---------------------- | ------------ | ------------- |
| Conservative           | 300 cal/day  | ~0.6 lbs/week |
| Moderate (recommended) | 500 cal/day  | ~1.0 lbs/week |
| Aggressive             | 750 cal/day  | ~1.5 lbs/week |
| Maximum                | 1000 cal/day | ~2.0 lbs/week |

Min calorie floor: **1,200 cal/day (women)** · **1,500 cal/day (men)**

## Macro Split by Diet Style

| Style         | Protein | Carbs | Fat |
| ------------- | ------- | ----- | --- |
| Balanced      | 30%     | 40%   | 30% |
| High Protein  | 40%     | 30%   | 30% |
| Low Carb      | 35%     | 20%   | 45% |
| Keto          | 25%     | 5%    | 70% |
| Mediterranean | 20%     | 50%   | 30% |
| Vegan         | 25%     | 50%   | 25% |

## TDEE Calculator Script

```bash
# Default: 75kg female, moderately active, moderate deficit, balanced diet
python scripts/tdee_calculator.py

# Custom inputs
python scripts/tdee_calculator.py \
  --weight 165 --unit imperial \
  --height 66 --age 35 \
  --gender female \
  --activity moderately_active \
  --goal moderate \
  --diet high_protein

# All activity options: sedentary / lightly_active / moderately_active / very_active / extra_active
# All diet options: balanced / high_protein / low_carb / keto / mediterranean / vegan
# All goal options: conservative / moderate / aggressive / maximum / maintain
```

## Output Checklist

- ✅ 7-day meal plan (breakfast, lunch, dinner, 1–2 snacks)
- ✅ Calories + macros per meal
- ✅ Shopping list grouped by store section
- ✅ Meal prep guide (batch cooking timeline)
- ✅ Restaurant/takeout alternatives
- ✅ Interactive HTML dashboard (macros, weight projection, checklist)

## Reference Files

- `references/NUTRITION_REFERENCE.json` — TDEE formulas, activity multipliers, macro ratios, food macros, deficit rules
- `assets/meal_plan_template.csv` — 7-day meal plan CSV template
- `scripts/tdee_calculator.py` — TDEE and calorie target calculator with macro breakdown
