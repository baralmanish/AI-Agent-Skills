---
name: expense-analyzer
description: Use this skill when a user wants to analyze credit card bills or transaction data and generate a rich spending analysis with interactive budgeting tools, visualizations, savings projections, and polished financial dashboards
tags:
  [
    expense-tracking,
    budgeting,
    financial-analysis,
    data-visualization,
    personal-finance,
  ]
argument-hint: "Optional: paste your transaction data, CSV, or credit card statement directly into the conversation"
user-invocable: true
disable-model-invocation: false
---

# Expense Analyzer

## When to Use

- User pastes credit card statements, bank exports, or transaction CSVs
- User wants to understand where their money is going
- User asks "analyze my spending", "categorize my transactions", "what am I spending the most on"
- User wants interactive budgets, savings projections, or subscription audits

## Instructions

- Analyze the user’s credit card bills, statements, or transaction data. Categorize all transactions, detect recurring charges, identify spending patterns, highlight unusual expenses, and estimate where savings opportunities exist.
- Generate a set of luxury outputs based on the analysis:
  - A beautiful single-page interactive budgeting dashboard preloaded with the user’s most recent month of spending across categories
  - Visualizations showing category breakdowns, monthly trends, top merchants, and recurring subscriptions
  - What-if analysis tools that let the user adjust spending in categories like dining, shopping, or subscriptions and instantly see the effect
  - A savings projection view showing how small monthly spending changes could add up over 6 months, 1 year, or 5 years
  - A subscription and recurring-charge review that surfaces low-value or forgotten spending
  - A financial insights summary that explains not just where money is going, but what patterns matter most and what changes would have the biggest impact

Make the experience feel polished, modern, visual, and premium.

## Supporting References

This skill includes a category taxonomy reference:

- **SPENDING_CATEGORIES.json** — 15 standard spending categories (Housing, Food & Dining, Transportation, Health, Shopping, Entertainment, Travel, Subscriptions, etc.) each with merchant recognition signals, subcategories, typical budget percentages, 50/30/20 classification, and benchmark insights. Also includes budget framework definitions and savings projection rates. Located in `references/`.

The AI uses SPENDING_CATEGORIES.json to categorize transactions consistently, surface benchmark comparisons, and identify high-savings opportunities.

## Output

1. An interactive budgeting dashboard
2. Charts and visual spending breakdowns
3. Scenario tools for what-if budgeting decisions
4. Savings-growth projections
5. Recurring-expense analysis
6. A polished financial insights summary
