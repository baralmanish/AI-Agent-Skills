"""
TDEE & Macro Target Calculator — Weekly Meal Planner Skill
Calculates Total Daily Energy Expenditure and sets calorie/macro targets for weight loss.

Usage:
    python tdee_calculator.py
    python tdee_calculator.py --weight 75 --height 170 --age 32 --gender female --activity moderately_active --goal moderate --diet balanced
    python tdee_calculator.py --weight 180 --unit imperial --height 69 --age 28 --gender male --activity lightly_active
"""

import argparse
import json
import sys
from pathlib import Path

REFERENCES_DIR = Path(__file__).parent.parent / "references"
NUTRITION_FILE = REFERENCES_DIR / "NUTRITION_REFERENCE.json"


def load_reference():
    if not NUTRITION_FILE.exists():
        print(f"[WARN] NUTRITION_REFERENCE.json not found — using built-in defaults")
        return None
    with open(NUTRITION_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def to_metric(weight, height, unit):
    """Convert imperial (lbs, inches) to metric (kg, cm)."""
    if unit == "imperial":
        return weight * 0.453592, height * 2.54
    return weight, height


def calc_bmr(weight_kg, height_cm, age, gender, formula="mifflin"):
    """Calculate Basal Metabolic Rate."""
    if formula == "mifflin":
        if gender == "male":
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    elif formula == "harris":
        if gender == "male":
            return 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
        return 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    raise ValueError(f"Unknown formula: {formula}")


ACTIVITY_MULTIPLIERS = {
    "sedentary":         1.2,
    "lightly_active":    1.375,
    "moderately_active": 1.55,
    "very_active":       1.725,
    "extra_active":      1.9,
}

DEFICIT_BY_GOAL = {
    "conservative": {"deficit": 300, "loss_lbs_week": 0.6},
    "moderate":     {"deficit": 500, "loss_lbs_week": 1.0},
    "aggressive":   {"deficit": 750, "loss_lbs_week": 1.5},
    "maximum":      {"deficit": 1000,"loss_lbs_week": 2.0},
    "maintain":     {"deficit": 0,   "loss_lbs_week": 0.0},
}

MACRO_RATIOS = {
    "balanced":     {"protein": 0.30, "carb": 0.40, "fat": 0.30},
    "high_protein": {"protein": 0.40, "carb": 0.30, "fat": 0.30},
    "low_carb":     {"protein": 0.35, "carb": 0.20, "fat": 0.45},
    "keto":         {"protein": 0.25, "carb": 0.05, "fat": 0.70},
    "mediterranean":{"protein": 0.20, "carb": 0.50, "fat": 0.30},
    "vegan":        {"protein": 0.25, "carb": 0.50, "fat": 0.25},
}

# Minimum calorie floors (safety)
CALORIE_FLOOR = {"male": 1500, "female": 1200}


def calc_macros(calories, diet_style):
    ratios = MACRO_RATIOS.get(diet_style, MACRO_RATIOS["balanced"])
    protein_cal = calories * ratios["protein"]
    carb_cal    = calories * ratios["carb"]
    fat_cal     = calories * ratios["fat"]
    return {
        "protein_g": round(protein_cal / 4),
        "carbs_g":   round(carb_cal   / 4),
        "fat_g":     round(fat_cal    / 9),
        "ratios":    ratios,
    }


def weight_loss_projection(deficit_per_day, weeks=(4, 8, 12)):
    return {f"{w}_weeks": round(deficit_per_day * 7 * w / 3500, 1) for w in weeks}


def print_report(args, weight_kg, height_cm, bmr, tdee, target_calories, goal_info, macros, projection):
    w_unit = f"{args.weight} lbs" if args.unit == "imperial" else f"{weight_kg:.1f} kg"
    h_unit = f"{args.height} in" if args.unit == "imperial" else f"{height_cm:.0f} cm"

    print("\n" + "=" * 60)
    print("  TDEE & MACRO TARGET CALCULATOR — Meal Planner Skill")
    print("=" * 60)
    print(f"\n  Input")
    print(f"  {'Weight':<25} {w_unit}")
    print(f"  {'Height':<25} {h_unit}")
    print(f"  {'Age':<25} {args.age} years")
    print(f"  {'Gender':<25} {args.gender.capitalize()}")
    print(f"  {'Activity Level':<25} {args.activity.replace('_', ' ').title()}")
    print(f"  {'Diet Style':<25} {args.diet.replace('_', ' ').title()}")
    print(f"  {'Weight Loss Goal':<25} {args.goal.capitalize()}")

    print(f"\n  Calorie Targets")
    print(f"  {'BMR (base metabolism)':<25} {bmr:.0f} cal/day")
    print(f"  {'TDEE (maintenance)':<25} {tdee:.0f} cal/day")
    print(f"  {'Daily deficit':<25} {goal_info['deficit']} cal/day")
    print(f"  {'Target calories':<25} {target_calories:.0f} cal/day")
    print(f"  {'Expected loss':<25} ~{goal_info['loss_lbs_week']} lbs/week")

    print(f"\n  Daily Macro Targets  (based on {args.diet.replace('_',' ').title()} split)")
    print(f"  {'Protein':<25} {macros['protein_g']}g  ({macros['ratios']['protein']*100:.0f}% of calories)")
    print(f"  {'Carbohydrates':<25} {macros['carbs_g']}g  ({macros['ratios']['carb']*100:.0f}% of calories)")
    print(f"  {'Fat':<25} {macros['fat_g']}g  ({macros['ratios']['fat']*100:.0f}% of calories)")
    print(f"  {'Fiber (minimum)':<25} 25g")

    print(f"\n  Weight Loss Projection (if plan is maintained)")
    for period, lbs in projection.items():
        weeks_label = period.replace("_weeks", " weeks").replace("_", " ")
        kgs = round(lbs * 0.453592, 1)
        print(f"  {'In ' + weeks_label:<25} ~{lbs} lbs  ({kgs} kg)")

    print(f"\n  Notes")
    floor = CALORIE_FLOOR[args.gender]
    if target_calories < floor:
        print(f"  ⚠️  Target ({target_calories:.0f} cal) is below the safety floor ({floor} cal).")
        print(f"     Adjusted to {floor} cal. Consider a less aggressive deficit.")
    print(f"  • Weight fluctuates ±2 lbs daily — judge progress over 2-week trends")
    print(f"  • After 4–6 weeks, take a 1-week break at TDEE to prevent metabolic adaptation")
    print(f"  • Add resistance training to minimize muscle loss during deficit")
    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Calculate TDEE and daily macro targets for a weight loss meal plan"
    )
    parser.add_argument("--weight",   type=float, default=75,   help="Body weight (kg or lbs)")
    parser.add_argument("--height",   type=float, default=170,  help="Height (cm or inches)")
    parser.add_argument("--age",      type=int,   default=30,   help="Age in years")
    parser.add_argument("--gender",   choices=["male","female"], default="female")
    parser.add_argument("--unit",     choices=["metric","imperial"], default="metric")
    parser.add_argument("--activity", choices=list(ACTIVITY_MULTIPLIERS), default="moderately_active")
    parser.add_argument("--goal",     choices=list(DEFICIT_BY_GOAL),      default="moderate")
    parser.add_argument("--diet",     choices=list(MACRO_RATIOS),         default="balanced")
    parser.add_argument("--formula",  choices=["mifflin","harris"],        default="mifflin")
    args = parser.parse_args()

    weight_kg, height_cm = to_metric(args.weight, args.height, args.unit)
    bmr  = calc_bmr(weight_kg, height_cm, args.age, args.gender, args.formula)
    tdee = bmr * ACTIVITY_MULTIPLIERS[args.activity]

    goal_info = DEFICIT_BY_GOAL[args.goal]
    target_calories = max(tdee - goal_info["deficit"], CALORIE_FLOOR[args.gender])

    macros     = calc_macros(target_calories, args.diet)
    projection = weight_loss_projection(goal_info["deficit"])

    print_report(args, weight_kg, height_cm, bmr, tdee, target_calories, goal_info, macros, projection)


if __name__ == "__main__":
    main()
