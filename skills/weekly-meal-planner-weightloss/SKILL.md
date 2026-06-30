---
name: weekly-meal-planner-weightloss
description: Creates comprehensive, personalized weekly meal plans for sustainable weight loss with nutritional optimization, shopping lists, prep guides, and interactive dashboards
tags: [meal-planning, nutrition, weight-loss, wellness, personalization]
argument-hint: "Optional: share your weight goal, dietary preferences, budget, or any allergies/restrictions"
user-invocable: true
disable-model-invocation: false
---

# Weekly Meal Planner for Weight Loss

## Supporting References

This skill includes nutrition science references and a TDEE calculator:

- **NUTRITION_REFERENCE.json** — Three TDEE formulas (Mifflin-St Jeor recommended, Harris-Benedict, Katch-McArdle), activity multipliers, calorie deficit rules with safety floors, macro ratio presets for 6 diet styles, calorie density per macronutrient, protein sources by budget, common food macros, hunger management strategies, and weight loss projection formula. Located in `references/`.
- **meal_plan_template.csv** — 7-day meal plan CSV template with breakfast/snack/lunch/snack/dinner slots and daily macro target rows. Located in `assets/`.
- **tdee_calculator.py** — CLI TDEE and calorie/macro target calculator supporting metric and imperial inputs, all diet styles, and all activity levels. Located in `scripts/`.

The AI uses NUTRITION_REFERENCE.json to calculate precise TDEE, set calorie targets, and design macro splits for the chosen diet style.

## Purpose

Transform vague weight loss intentions into a concrete, actionable weekly plan with luxury outputs that make healthy eating feel achievable, exciting, and well-organized. This skill turns nutrition science into practical daily eating patterns backed by detailed shopping lists, time-saving prep guides, and motivational tracking dashboards.

---

## Input Requirements

The AI should gather (through interview or form) the following information:

### Personal Health Metrics

- Current weight (lbs or kg)
- Height
- Age and gender
- Current activity level (sedentary, lightly active, moderately active, very active)
- Target weight and timeframe (e.g., "lose 15 lbs in 12 weeks")

### Dietary Preferences & Constraints

- Dietary style preference (keto, low-carb, balanced macro, high-protein, vegan, vegetarian, omnivore, etc.)
- Favorite cuisines/foods (e.g., Asian, Mediterranean, Mexican, American)
- Foods they strongly dislike or have allergies/intolerances to
- Eating patterns (breakfast person? skip breakfast? snacker? etc.)
- Cooking skill level (beginner, intermediate, advanced)
- Time available for meal prep (hours per week)

### Practical Constraints

- Budget per week for groceries
- Access to cooking equipment (basic kitchen? full kitchen? slow cooker? air fryer?)
- Preferred stores/delivery services (Whole Foods, Costco, Trader Joe's, etc.)
- Number of people to cook for (just me, family, meal prep for multiple days)
- Any special occasions or social eating plans this week

### Goals & Preferences

- Primary goal: rapid loss, steady loss, building muscle while losing fat
- Preferred weight loss rate (1-2 lbs/week is sustainable)
- Energy level goals (energetic, balanced, sustaining)
- Must-include meals or foods they want this week
- Days when they know they'll eat out (breakfast meetings, dinner dates, etc.)

---

## Processing Steps

The AI should perform the following analysis and planning:

### Step 1: Calculate Nutrition Targets

- Calculate TDEE (Total Daily Energy Expenditure) using Harris-Benedict or Katch-McArdle formula
- Determine calorie deficit needed for target weight loss (500 cal/day = ~1 lb/week loss)
- Set macronutrient targets based on:
  - Dietary preference (e.g., keto = 70% fat, 25% protein, 5% carbs)
  - Activity level (active = higher protein)
  - User preference for adherence (if they love carbs, don't force keto)
- Account for micronutrients: ensure sufficient fiber, vitamins, minerals for health

### Step 2: Design the Weekly Theme

- Create a cohesive weekly concept that makes meal prep logical:
  - Pick 3 protein bases (e.g., chicken, ground turkey, salmon)
  - Pick 3-4 vegetable combinations
  - Pick 2-3 healthy carb sources
  - Choose a cuisine angle for cohesion (Mediterranean week, Asian-inspired week, etc.)
  - Plan for variety but minimize shopping for 20 different ingredients

### Step 3: Build the 7-Day Meal Plan

- Create breakfast, lunch, dinner, and snack options for each day
- Ensure each day hits calorie and macro targets (±5%)
- Build in 2-3 flexible options per day for social eating or cravings
- Include prep-ahead meals for busy days
- Add 2 "treat meals" that stay within calorie/macro goals (pizza made healthy, dessert alternatives, etc.)
- Plan for 1 planned indulgence meal if user prefers (keeps adherence high)

### Step 4: Calculate Comprehensive Nutrition Data

- Calculate calories, protein, carbs, fat, fiber for every meal
- Calculate micronutrients (Vitamin D, Iron, Calcium, etc.)
- Identify any nutritional gaps and suggest additions
- Provide daily nutrition summary

### Step 5: Build Optimized Shopping List

- Consolidate all ingredients across the week's meals
- Group by store section (produce, proteins, dairy, pantry, frozen, etc.)
- Include quantities needed (account for using same ingredients multiple days)
- Cross-reference prices if possible
- Add budget tracker (item cost, total per category, total for week)
- Create a prioritized list (essentials first, nice-to-haves last) for budget flexibility
- Suggest bulk buys or deals (Costco rotisserie chicken, buy-in-bulk proteins, etc.)

### Step 6: Create Meal Prep Guide

- Batch cooking plan: what to cook on Sunday (or preferred prep day)
- Time-optimization: what can be done in parallel to save time
- Storage instructions: containers, fridge life, freezer options
- Simple step-by-step instructions for meal prep (non-chef friendly)
- 15-minute quick meals for unexpected busy days
- Restaurant/takeout emergency substitutes with calorie/macro equivalents

### Step 7: Generate Motivational & Contextual Content

- Weekly weight loss projection (if user maintains plan)
- Micro-wins to celebrate (e.g., "you're getting 25g fiber daily = great gut health")
- Hunger/energy management tips specific to their calorie deficit
- Strategies to handle common obstacles (social eating, cravings, energy dips)
- Research-backed explanation of why each meal choice supports their goal
- Accountability check-ins and progress tracking prompts

### Step 8: Build Comparison & Flexibility Guide

- Restaurant alternatives for each meal (McDonald's, Chipotle, Panera, Italian chains, etc.)
- Simple substitutions (swap this carb for that carb, still same macros)
- If-I'm-extra-hungry options (low-cal volume foods to add)
- If-I-need-energy options (strategic carb timing for workouts)
- Foods to always keep in pantry for emergencies

---

## Expected Outputs

The skill should generate **all of these outputs** to provide a complete, luxury meal planning experience:

### Standard Outputs

1. **Weekly Meal Plan (Text/Table Format)**
   - 7-day calendar with breakfast, lunch, dinner, snacks
   - Calorie and macro counts for each meal
   - Prep time and difficulty level for each recipe
   - Quick links to recipes (if available)
   - Notes on which meals are "meal-prep friendly"

2. **Optimized Shopping List (Formatted)**
   - Organized by grocery store section
   - Quantities with units clearly specified
   - Estimated price per item (optional)
   - Checkboxes for checking off items
   - Budget summary
   - Notes on substitutions or where to find items

3. **Nutrition Summary Report**
   - Daily calorie and macro breakdown for 7 days
   - Weekly averages vs. targets
   - Micronutrient analysis (hit or miss on key vitamins/minerals)
   - Fiber, sodium, and water intake suggestions
   - Any nutritional gaps identified and addressed

4. **Meal Prep Guide**
   - Step-by-step batch cooking instructions
   - Timeline for meal prep day (e.g., "8am start, done by 11am")
   - Container packing guide with storage life
   - Quick assembly instructions for busy days
   - Freezer-friendly meal options

5. **Restaurant & Takeout Alternatives**
   - 3-5 restaurant chains with specific healthy menu items
   - Calorie and macro counts for each option
   - Ordering tips (dressing on side, substitutions, etc.)
   - Approximate cost comparisons

### LUXURY Outputs

6. **Interactive HTML Dashboard**
   - **Weekly Calendar View**: Visual day-by-day meal layout with color-coded macros
   - **Nutrition Tracker**: Real-time macro circle graphs (protein%, carb%, fat% pie charts)
   - **Shopping List with Checkboxes**: Interactive checklist for grocery store
   - **Macro Counter**: Click each meal to see detailed nutrition
   - **Progress Projection Graph**: Weight loss timeline if plan is maintained
   - **Motivational Quotes**: Random tips and encouragement
   - **Quick Links**: One-click access to recipes or store locations
   - **Dark/Light Theme Toggle**: User preference
   - **Mobile Responsive**: Works on phone in grocery store
   - **Printable Version**: PDF-ready format for those who prefer paper

7. **Personalized Weekly Insight Report (PDF)**
   - Executive summary of the week ahead
   - "Your Body's Nutrition Blueprint" - personalized explanation of macro targets
   - Weight loss projection and sustainability assessment
   - Weekly theme explanation (why these meals = smart choices for you)
   - Psychological eating tips tailored to their stated preferences
   - Celebration of small wins (consistency, nutrition hits, budget awareness)
   - Custom motivational message based on their goals

8. **Recipe Cards (Formatted)**
   - 10-15 key recipes for the week
   - Each with: ingredients, steps, nutrition facts, prep time, difficulty
   - Portion-controlled sizing with macro counts
   - Substitution suggestions for variety
   - Freezer-friendly indicator
   - Pairing suggestions (what goes with what meal)

9. **JSON Nutrition Data File**
   - Machine-readable format for import into fitness apps
   - Daily meal data: calories, macros, micros, ingredients
   - Useful for apps like MyFitnessPal, Cronometer, Strong, etc.
   - Enables automated tracking if user chooses

10. **Sustainable Eating Playbook (Text)**
    - "This Week's Eating Strategy" - personalized mindset guide
    - Common pitfalls for their food preferences + how to avoid them
    - Energy management (when to eat carbs for workouts, etc.)
    - Hunger cues and fullness signals to watch for
    - Weekly reflection questions for habit tracking
    - Success metrics beyond the scale (energy, strength, sleep, etc.)

11. **Emergency Backup Meals Guide**
    - 5 "throw together in 10 minutes" meals using pantry staples
    - 3 frozen meal recommendations (brands/specific products)
    - 3 convenience store healthier options
    - All with calorie/macro counts so they don't derail the plan

12. **Cost Analysis & Budget Optimization Report**
    - Itemized cost breakdown by meal
    - Cost per serving for each meal
    - Weekly total vs. user's budget
    - Where to save money without sacrificing nutrition
    - Where splurging on quality matters (proteins, etc.)
    - Generic vs. brand-name comparisons

13. **Social Eating & Occasions Guide**
    - If user mentioned social meals: strategies for specific scenarios
    - "Eating out strategy" - how to handle restaurants while staying on track
    - Buffer calories to use if going to a party
    - How to navigate alcohol calories
    - Polite ways to stay committed without weird comments
    - Meal swaps for social situations

14. **Progress Tracking Template (CSV/Spreadsheet)**
    - Weekly tracking sheet with columns for:
      - Date, weight, energy level, hunger level, mood, exercise
      - Meals completed, cravings, notes
      - Win/challenge of the day
    - Can be downloaded and used with phone or spreadsheet app
    - Pre-filled with user's targets and meal plan
    - Charts auto-calculate trends

---

## Examples & Resources

### Example User Input

```
Name: Sarah
Age: 32, Female, 5'6"
Current Weight: 195 lbs, Goal Weight: 165 lbs (12 weeks)
Activity Level: Lightly active (desk job, 2 workouts/week)
Preferences: Loves Italian and Asian food, very busy during week, vegetarian,
   loves breakfast, batch-cooking enthusiast
Constraints: Budget $100/week, basic kitchen, family of 2
Goal: Steady, sustainable loss (1.5 lbs/week), maintain energy for workouts
```

### Example Output (Partial HTML Dashboard)

```
A beautiful, interactive HTML page showing:
- Sarah's Face (avatar placeholder)
- "Weekly Meal Plan: Mediterranean Italian Energy Week"
- Goal progress bar: "Target: 1.5 lbs/week | Plan: 1.4 lbs loss projected"
- 7-day calendar with click-able meals
- Macro circles: "Protein 30% | Carbs 40% | Fat 30%"
- Shopping list with Whole Foods store locations
- Budget tracker: "$98 total (under budget!)"
- Recipe quick-links
- Motivational message: "You're building momentum. This week, focus on
  enjoying the food and the ritual of meal prep—that's where habits stick."
```

### Reference Standards

- TDEE calculators: Harris-Benedict, Mifflin-St Jeor, Katch-McArdle formulas
- Macro split guidance: ISSN (International Society of Sports Nutrition)
- Micronutrient targets: NIH RDA (Recommended Dietary Allowances)
- Safe weight loss rate: 1-2 lbs/week (medical consensus)
- Caloric deficit for loss: 500-750 cal/day deficit = 1-1.5 lbs/week loss

---

## When to Use This Skill

- User says: "I want to lose weight but don't know where to start"
- User says: "Plan my meals for the week"
- User says: "Help me build a weight loss strategy with meal prep"
- User says: "I want a detailed nutrition plan that actually looks appealing"
- User is starting a diet and needs structure, not just willpower
- User wants to take guesswork out of healthy eating

---

## Quick Start Example: How to Run This Skill

### Step 1: User Initiates

**User says:**

> "I need help with a weight loss meal plan for next week. I'm 32, female, 5'6", currently 195 lbs, and want to get to 165 lbs. I have about 12 weeks and I'm lightly active with a desk job. I love Asian and Italian food, but I'm vegetarian. Budget is $100/week."

### Step 2: AI Interviews (if needed)

**AI asks clarifying questions:**

- Cooking skill level?
- Time available for meal prep?
- Any foods you dislike or allergies?
- Preferred weight loss pace (1-2 lbs/week)?
- Any special events or social meals this week?

### Step 3: AI Processes

AI runs through all 8 processing steps:

- Calculates TDEE and calorie targets
- Designs weekly vegetarian-Asian-Italian theme
- Builds 7-day meal plan hitting macros
- Calculates nutrition data
- Creates optimized shopping list
- Develops meal prep guide
- Generates motivational content
- Creates restaurant alternatives

### Step 4: AI Delivers All Outputs

User receives:

1. ✅ **Weekly meal plan** (text) with all 7 days
2. ✅ **Shopping list** (organized, with budget: $98)
3. ✅ **Nutrition summary** (daily/weekly breakdown)
4. ✅ **Meal prep guide** (Sunday 90-min prep timeline)
5. ✅ **Restaurant alternatives** (Panera, Asian chains, Chipotle)
6. ✅ **Interactive HTML dashboard** (color-coded macros, weight projection)
7. ✅ **Personalized insight report** (PDF with motivation + strategy)
8. ✅ **10-15 recipe cards** (with full nutrition data)
9. ✅ **JSON nutrition data** (for import to MyFitnessPal)
10. ✅ **Sustainable eating playbook** (personalized tips)
11. ✅ **Emergency backup meals** (10-minute options)
12. ✅ **Cost analysis report** (where to save/splurge)
13. ✅ **Social eating guide** (restaurant strategies)
14. ✅ **Progress tracking template** (downloadable CSV)

### Real Example Conversation

**User:** "Can you create a meal plan for weight loss? I'm trying to lose 20 pounds in 3 months."

**AI:** "I'd love to help! Let me gather some information to create a personalized plan. Quick questions:

1. What's your current weight, height, and age?
2. How active are you (sedentary, lightly active, moderate, very active)?
3. Any dietary preferences (vegan, keto, high-protein, balanced)?
4. Budget for groceries per week?
5. Cooking skill level and time for meal prep?"

**User:** "I'm 250 lbs, 5'10", 35 years old, guy, lightly active. I like chicken and high-protein stuff. Budget is $80/week. Intermediate cook, maybe 2 hours for meal prep Sunday."

**AI:** _Runs the skill_ "Perfect! I'm creating your personalized weight loss plan now...

Here's your Q2 2026 weight loss strategy:

**Your Targets:**

- Daily: 1,950 calories (500 cal deficit)
- Protein: 180g (high-protein for satiety)
- Carbs: 200g
- Fat: 65g
- Weight loss projection: 1.7 lbs/week = 20 lbs in 12 weeks ✅

**This Week's Theme:** High-Protein Bulk Cooking Week

[Then delivers all 14 outputs]"

---

## Success Criteria

The skill has succeeded when the user:

- ✅ Has a clear, actionable meal plan they're excited about (not dreading)
- ✅ Knows exactly what to buy and has a shopping list in hand
- ✅ Understands their nutrition targets and why they matter
- ✅ Feels supported with restaurant and emergency options
- ✅ Has a tracking mechanism ready to use
- ✅ Feels genuinely motivated, not restricted
- ✅ Can maintain this plan consistently for at least the week, ideally longer

The luxury experience happens when the user feels like they have a personal nutritionist, meal prep coach, and accountability partner all in one.

---

## Notes for AI Implementation

- **Tone**: Professional but warm. Act like a supportive, evidence-based nutrition coach, not a drill sergeant.
- **Personalization**: Reference the user's specific preferences throughout (not generic advice).
- **Science-backed**: Cite general principles but don't overwhelm with studies; focus on practical application.
- **Psychological safety**: Acknowledge that dieting is hard; validate struggles and celebrate small wins.
- **Flexibility over perfection**: Emphasize adherence > perfectionism. A plan they'll follow beats a perfect plan they'll quit.
- **Accessibility**: Recipes and suggestions should be realistically achievable for their stated skill level and time.
- **Multiple output formats**: Some people want dashboards, others want printable lists. Offer variety.
