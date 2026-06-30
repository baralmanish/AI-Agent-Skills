---
name: qbr-intelligence-engine
description: Transforms raw business data into executive-ready Quarterly Business Review (QBR) reports with trend analysis, predictive insights, strategic recommendations, and board-presentation-ready dashboards
tags:
  [
    business-intelligence,
    executive-reports,
    qbr,
    analytics,
    strategy,
    data-driven-decisions,
  ]
argument-hint: "Provide your quarterly business metrics: revenue, customers, churn, key initiatives, and company context"
user-invocable: true
disable-model-invocation: false
---

# QBR Intelligence Engine

## Purpose

Transform scattered business metrics into a cohesive, executive-ready Quarterly Business Review (QBR) that tells your company's story, identifies critical trends, predicts risks, and recommends strategic actions. This skill turns raw data into the insights C-suite needs to make confident quarterly decisions.

---

## Input Requirements

The AI should gather the following business data:

### Company Context

- Company name and industry
- Fiscal quarter (Q1-Q4, what year)
- Company stage (startup, growth, mature)
- Number of employees
- Geographic markets served
- Primary business model (SaaS, marketplace, DTC, B2B services, etc.)

### Financial Metrics

- Revenue (current quarter vs. last quarter vs. year-ago quarter)
- Gross profit / Gross margin %
- Operating expenses (broken down by category: R&D, Sales/Marketing, G&A, Other)
- Operating income / Operating margin %
- Cash position / Runway (in months)
- Headcount (current vs. target)
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- Burn rate (if pre-revenue or pre-profitability)

### Product/Customer Metrics

- Total customers / Monthly Active Users
- Net Revenue Retention (NRR)
- Churn rate %
- New customer acquisition
- Customer acquisition by channel (% breakdown)
- Product usage metrics (daily active, sessions, feature adoption)
- Customer satisfaction (NPS, CSAT, or similar)
- Support metrics (ticket volume, resolution time, satisfaction)

### Key Initiatives & Execution

- Top 3 initiatives launched this quarter
- Progress on quarterly OKRs (% completed)
- Key wins (major customer, partnership, milestone)
- Key challenges faced
- Any product/market misalignment signals
- Competitive landscape changes

### Looking Ahead

- Priorities for next quarter
- Hiring plans
- Budget allocation changes
- Market expansion plans
- Known risks/concerns

---

## Processing Steps

The AI should perform the following analysis:

### Step 1: Normalize & Validate Data

- Convert all metrics to consistent formats
- Identify data gaps and flag for stakeholder
- Calculate missing-but-essential metrics (e.g., if MRR given, calculate quarterly)
- Note data quality concerns

### Step 2: Calculate Performance Metrics

- Quarter-over-Quarter (QoQ) growth %
- Year-over-Year (YoY) growth %
- Trend direction (accelerating, maintaining, decelerating)
- Benchmark against industry standards (reference: KPI_BENCHMARKS.json)
- Calculate health scores (revenue health, customer health, team health)

### Step 3: Identify Trends & Patterns

- Revenue momentum (accelerating or decelerating?)
- Unit economics health (CAC, LTV, payback period)
- Retention trends (stable, improving, concerning?)
- Efficiency trends (burn rate, operating margin trajectory)
- Customer concentration risk (top customer % of revenue)
- Geographic/channel concentration risk

### Step 4: Predictive Analysis

- Revenue forecast (next 2 quarters using trend extrapolation from current metrics)
- Runway projection (if pre-profitability)
- Churn forecast (if applicable)
- Hiring impact on margins
- Identify 1-3 leading indicators that predict next quarter performance

### Step 5: Risk Assessment

- Score risks using reference: RISK_FRAMEWORK.json
- Identify 5-7 key risks (customer concentration, market, execution, financing, retention)
- Rate each: High/Medium/Low + impact if realized + mitigation strategy
- Highlight any "red flags" requiring immediate attention

### Step 6: Competitive Context

- How metrics position company vs. industry benchmarks
- Major competitive moves this quarter
- Market share implications
- Differentiation strengths/weaknesses

### Step 7: Strategic Recommendations

- 3-5 high-impact strategic actions for next quarter
- Prioritization framework (impact × effort)
- Resource allocation recommendations
- Quick wins vs. longer-term bets
- Key decisions needed from board/leadership

### Step 8: Generate Executive Outputs

- Board-ready presentation
- Executive summary (1 page)
- Deep-dive analytics dashboard
- 90-day action plan
- Risk register & mitigation playbook

---

## Expected Outputs

### 1. Executive Summary (1 page)

- Quarter headline ("Q2: Accelerating Growth, Margin Pressure" or similar)
- Key metrics snapshot (Revenue, Growth %, Customers, NRR, Burn)
- 3-5 "headlines" (wins, challenges, decisions needed)
- Forward outlook in 3 sentences

### 2. Board Presentation (8-12 slides)

- Slide 1: Quarter at a glance (headline metrics)
- Slide 2-3: Financial performance (revenue, margins, cash)
- Slide 4: Customer metrics (growth, retention, NRR)
- Slide 5: Key initiatives progress
- Slide 6: Market & competitive landscape
- Slide 7: Risk register & mitigation
- Slide 8: Strategic recommendations & decisions needed
- Optional: Deep dives on specific topics

### 3. Analytics Dashboard (Interactive HTML)

- Real-time KPI cards (Revenue, MRR, Churn, CAC, LTV)
- Trend charts (QoQ growth, retention curve, burn trajectory)
- Cohort analysis view
- Unit economics breakdown
- Waterfall chart (revenue bridges)
- Customer segmentation view
- Forecast projections (next 2 quarters)

### 4. 90-Day Action Plan

- Top 3 initiatives ranked by impact
- Detailed tasks with ownership & due dates
- Resource requirements
- Success metrics for each initiative
- Risk mitigations

### 5. Risk Register & Playbook

- 5-7 identified risks with severity rating
- Probability × impact matrix
- Mitigation strategy for each
- Early warning indicators
- Escalation triggers
- Contingency plans

### 6. Financial Forecast Model

- Detailed P&L projection (next 2 quarters)
- Sensitivity analysis (upside/base/downside scenarios)
- Key assumptions documented
- Variance analysis (vs. prior forecast)
- Funding runway calculation

### 7. Customer Health Dashboard

- Churn risk scoring by segment
- NRR trajectory by cohort
- Expansion revenue pipeline
- At-risk account alerts
- Customer satisfaction trends

### 8. Investor Deck (Optional)

- Polished 12-15 slide presentation
- Story arc (where we are, where we're going, why we'll win)
- Key metrics with narrative
- Market opportunity
- Competitive advantage
- Use of funds (if fundraising)

---

## Supporting Scripts

This skill includes Python scripts for data processing:

- **kpi_calculator.py**: Calculates growth %, trends, benchmarking
- **forecast_engine.py**: Generates revenue/churn forecasts using reference models
- **risk_scorer.py**: Scores risks using defined framework
- **cohort_analyzer.py**: Analyzes customer cohorts, retention, LTV trends
- **benchmark_analyzer.py**: Compares metrics vs. industry standards

Scripts are referenced in `/scripts` folder. AI uses these for precision calculations.

---

## Supporting References

This skill includes data-driven reference files:

- **KPI_BENCHMARKS.json**: Industry benchmarks by stage/industry
- **RISK_FRAMEWORK.json**: Risk scoring matrix & playbooks
- **STRATEGIC_FRAMEWORKS.json**: Decision frameworks (2×2, prioritization)

All in `/references` folder. AI cites these for authority & consistency.

---

## Supporting Assets

This skill includes presentation templates:

- **qbr_dashboard_template.html**: Polished HTML presentation framework
- **dashboard_theme.css**: Professional dashboard styling
- **email_templates.txt**: QBR communication templates

All in `/assets` folder. AI uses these to generate professional output.

---

## When to Use This Skill

- Executive says: "Generate my Q3 board presentation"
- Finance asks: "Can you create a detailed QBR report?"
- CEO needs: "Data-driven quarterly strategy session preparation"
- Investor requests: "Quarterly update with metrics and forecast"
- Company does: Regular board reporting and strategic planning

---

## Success Criteria

The skill has succeeded when:

- ✅ Executive summary captures quarter in compelling narrative
- ✅ Board presentation is visually professional & data-rich
- ✅ Metrics are accurate and benchmark-compared
- ✅ Trends are clearly identified (accelerating/decelerating)
- ✅ Risks are surfaced with severity & mitigation
- ✅ Recommendations are actionable & prioritized
- ✅ Forecasts are reasonable & scenario-tested
- ✅ Dashboard is interactive & mobile-responsive
- ✅ Entire QBR package is boardroom-ready

---

## AI Implementation Notes

- **Tone**: Professional, data-driven, slightly strategic (not just reporting facts)
- **Narrative**: Connect metrics to strategic implications
- **Benchmarking**: Always compare to industry standards (cite reference)
- **Forecast**: Show multiple scenarios (upside/base/downside)
- **Risk**: Identify not just "what could go wrong" but "what ARE the signals we're seeing now"
- **Recommendations**: Prioritize ruthlessly (not 10 ideas, top 3-5)
- **Visuals**: Use charts to show trends; tables for detailed data
- **Rigor**: All metrics calculated precisely using scripts; validate against reference frameworks
