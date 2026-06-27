# QBR Intelligence Engine - Complete Skill Package

## Overview

**QBR Intelligence Engine** is a comprehensive AI skill for transforming raw business data into executive-ready Quarterly Business Review (QBR) reports. This skill package includes scripts, references, and assets—everything needed for production-quality business intelligence.

---

## 📁 Folder Structure

```
qbr-intelligence-engine/
├── SKILL.md                          # Main skill definition
├── scripts/                          # Python calculation engines
│   ├── kpi_calculator.py            # KPI & benchmark calculations
│   ├── forecast_engine.py           # Revenue & churn forecasting
│   └── risk_scorer.py               # Risk identification & scoring
├── references/                       # Data-driven reference files
│   ├── KPI_BENCHMARKS.json          # Industry benchmarks by stage
│   ├── RISK_FRAMEWORK.json          # Risk scoring matrix & playbooks
│   └── STRATEGIC_FRAMEWORKS.json    # Decision-making frameworks
└── assets/                           # Presentation & dashboard components
    ├── dashboard_theme.css          # Professional styling
    ├── qbr_dashboard_template.html  # Dashboard HTML template
    ├── email_templates.txt          # Communication templates
    └── brand_elements.css           # Custom branding

README.md (this file)
```

---

## 🔧 Scripts - Calculation Engines

### `kpi_calculator.py`

**Purpose:** Precision financial calculations for KPIs

**Classes:**

- `KPICalculator`: Calculate growth rates, unit economics, margins, NRR trends
- `BenchmarkComparator`: Compare company metrics to industry standards

**Key Functions:**

```python
# Calculate QoQ or YoY growth
growth = KPICalculator.calculate_growth_rate(current=2500000, previous=2000000)

# Unit economics analysis
economics = KPICalculator.calculate_unit_economics(cac=500, ltv=3000)

# NRR trajectory
nrr_analysis = KPICalculator.calculate_nrr_trajectory(
    cohort_revenues=[1M, 1.1M, 1.15M],
    cohort_ages=[1, 2, 3]
)

# Compare to benchmarks
comparison = BenchmarkComparator.compare_metric('nrr', company_value=115, company_stage='SaaS_Growth')
```

---

### `forecast_engine.py`

**Purpose:** Generate financial forecasts and scenarios

**Classes:**

- `RevenueForecaster`: Project revenue using multiple models
- `ChurnForecaster`: Predict customer churn and retention
- `OperatingPlanForecaster`: Forecast operating expenses and margins

**Key Functions:**

```python
# Linear regression forecast
forecast = RevenueForecaster.linear_regression_forecast(
    historical_quarters=[1M, 1.2M, 1.5M, 1.8M],
    quarters_to_forecast=2
)

# Scenario planning (upside/base/downside)
scenarios = RevenueForecaster.scenario_forecast(
    current_revenue=1800000,
    upside_rate=0.15,
    base_rate=0.10,
    downside_rate=-0.05,
    quarters=2
)

# Churn rate forecast
churn_forecast = ChurnForecaster.churn_rate_forecast(
    current_churn=2.5,
    trend='improving',
    quarters=2
)

# Headcount impact on operating expenses
opex_impact = OperatingPlanForecaster.headcount_impact_forecast(
    current_headcount=50,
    hiring_plan=[10, 15, 10],
    cost_per_hire=150000
)
```

---

### `risk_scorer.py`

**Purpose:** Systematically identify and score business risks

**Classes:**

- `RiskScorer`: Score risks 1-10 based on indicators
- `RiskMitigationPlanner`: Generate mitigation strategies

**Key Functions:**

```python
# Score a specific risk
risk_score = RiskScorer.score_risk(
    'customer_concentration',
    top_customer_percent_revenue=35
)

# Create risk matrix (probability × impact)
matrix = RiskScorer.create_risk_matrix(risks_list)

# Get mitigation playbook for a risk
mitigation = RiskMitigationPlanner.get_mitigation_plan('customer_concentration')
```

**Risk Categories:**

- Customer concentration
- Retention & churn
- Financing & runway
- Execution & performance
- Market & competition
- Talent & organization
- Product-market fit

---

## 📚 References - Data-Driven Decision Making

### `KPI_BENCHMARKS.json`

Industry benchmarks organized by company stage and type.

**Stages:**

- SaaS Growth Stage (early-stage, strong growth)
- SaaS Mature Stage (established, profitability focus)
- Marketplace businesses
- DTC e-commerce
- Enterprise SaaS

**Metrics Include:**

- Magic Number (growth efficiency)
- Net Revenue Retention (NRR)
- CAC Payback Period
- Rule of 40 (growth + margin)
- Gross Margin
- Quick Ratio (cash health)

**Example:**

```json
{
  "SaaS_Growth_Stage": {
    "metrics": {
      "magic_number": {
        "excellent": 0.75,
        "good": 0.5,
        "acceptable": 0.3
      },
      "net_revenue_retention": {
        "excellent": 125,
        "good": 110,
        "acceptable": 100
      }
    }
  }
}
```

---

### `RISK_FRAMEWORK.json`

Standardized risk scoring framework with mitigation playbooks.

**Features:**

- 1-10 scoring scale with severity levels (critical, high, medium, low)
- 7 risk categories with scoring factors
- Red flags for each risk type
- Leading indicators to monitor
- Escalation criteria for board
- Mitigation timeline estimates

**Example Risk - Customer Concentration:**

```json
{
  "description": "Revenue dependency on too few customers",
  "scoring_factors": {
    "top_1_customer_percent": "if > 40%, score = 9"
  },
  "red_flags": ["Top customer > 30%", "Concentration increasing"],
  "leading_indicators": ["new_customer_bookings", "revenue_diversification"],
  "mitigation_timeline": "8-12 weeks"
}
```

---

### `STRATEGIC_FRAMEWORKS.json`

Decision-making and strategy frameworks for executives.

**Frameworks Included:**

1. **2×2 Matrix** (Impact × Effort) - Prioritize initiatives
2. **OKR Framework** - Objective & Key Result setting
3. **Value Creation Funnel** - Where is value being created?
4. **Three Horizon Strategy** - Balance today/tomorrow/future
5. **Porter's Five Forces** - Competitive analysis
6. **Ansoff Matrix** - Growth strategy options
7. **Decision-Making Frameworks** - Pros/cons, decision matrices, premortems

**Example - 2×2 Matrix:**

```json
{
  "quick_wins": {
    "position": "High Impact, Low Effort",
    "action": "Do immediately"
  },
  "strategic_bets": {
    "position": "High Impact, High Effort",
    "action": "Plan carefully, execute with full resources"
  }
}
```

---

## 🎨 Assets - Presentation Components

### `dashboard_theme.css`

Professional, modern CSS styling for QBR dashboards.

**Features:**

- Responsive grid layout
- KPI card styling with status indicators
- Chart containers
- Risk matrix cards (color-coded by severity)
- Recommendation styling
- Print and dark mode support
- Mobile responsive

**Key Classes:**

- `.kpi-card` - Metric display cards
- `.kpi-card.status-critical` - Red cards for warnings
- `.chart-container` - Chart area styling
- `.risk-card.critical|high|medium|low` - Risk severity colors
- `.recommendation-priority.p1|p2|p3` - Priority badges
- `.forecast-table` - Financial forecast table styling

---

### `qbr_dashboard_template.html`

Complete HTML template for QBR dashboard.

**Sections:**

1. **Header** - Company name, quarter, executive summary
2. **KPI Cards** - 6-8 key metrics (revenue, customers, margins, runway, etc.)
3. **Financial Charts** - Revenue trends, forecasts, unit economics
4. **Customer Metrics** - NRR, churn, acquisition trends
5. **Risk Assessment** - Cards showing top 3-5 risks with scores
6. **Strategic Recommendations** - Prioritized action items with impact/effort/timeline
7. **12-Month Forecast** - Revenue projections by scenario
8. **Executive Summary** - Key takeaways

**Usage:**

- AI fills in `[VALUE]`, `[COMPANY NAME]`, chart placeholders with actual data
- Integrates with dashboard_theme.css for styling
- Can be rendered to PDF for board presentations
- Mobile responsive for viewing on tablets/phones

---

## 🚀 How to Use This Skill

## 💬 Sample Prompts

### QBR From Raw Metrics

```text
Generate a QBR from the business metrics below.
Show revenue trends, retention, unit economics, major risks, and the top recommendations for leadership.
```

### Board-Ready Review

```text
Create a board-ready quarterly business review using the data below.
I want an executive summary, risk analysis, growth trends, and a polished dashboard.
```

### Financial Health and Forecast

```text
Analyze the quarterly metrics below and assess our financial health.
Include benchmarks, scenario forecasts, and the biggest strategic risks.
```

### Growth and Risk Dashboard

```text
Build a QBR dashboard from the operating data below.
Focus on growth momentum, retention, CAC/LTV, churn, and the actions we should prioritize next quarter.
```

## 🚀 How to Use This Skill

### Step 1: User Provides Data

User shares their business metrics:

```
Revenue: $2.5M ARR
Customers: 45
NRR: 115%
Monthly Burn: $750k
Runway: 18 months
Growth Rate: 12% QoQ
...
```

### Step 2: AI Processes Data

**Step 2a: Use Scripts for Calculations**

```python
# Import scripts
from scripts.kpi_calculator import KPICalculator, BenchmarkComparator
from scripts.forecast_engine import RevenueForecaster, ChurnForecaster
from scripts.risk_scorer import RiskScorer, RiskMitigationPlanner

# Calculate KPIs
growth = KPICalculator.calculate_growth_rate(2500000, 2200000)
unit_econ = KPICalculator.calculate_unit_economics(cac=500, ltv=3000)

# Compare to benchmarks
benchmark = BenchmarkComparator.compare_metric('magic_number', 0.65, 'SaaS_Growth')

# Forecast next quarter
forecast = RevenueForecaster.scenario_forecast(...)

# Score risks
risks = [
    RiskScorer.score_risk('customer_concentration', top_customer_percent_revenue=35),
    RiskScorer.score_risk('retention', churn_rate=2.5, nrr_trend='stable'),
    RiskScorer.score_risk('financing', runway_months=18, burn_rate_trend='stable')
]
```

**Step 2b: Consult References**

- Check `KPI_BENCHMARKS.json` to compare metrics
- Check `RISK_FRAMEWORK.json` to score risks
- Check `STRATEGIC_FRAMEWORKS.json` to generate recommendations

### Step 3: AI Generates Outputs

**Output 1: Executive Summary (1 page)**

```
Q2 2026 Review: Accelerating Growth, Strong Unit Economics

Key Metrics:
- Revenue: $2.5M ARR (+12% QoQ)
- Customers: 45 (+8% QoQ)
- NRR: 115% (stable, excellent)
- Runway: 18 months (healthy)
- Gross Margin: 68% (trending up)

Headline: Strong growth with improving margins. Key focus: customer concentration risk.
```

**Output 2: Board Presentation (8-12 slides)**

- Uses STRATEGIC_FRAMEWORKS.json for structure
- Includes KPIs, trends, risks, recommendations

**Output 3: Interactive Dashboard (HTML)**

- Uses qbr_dashboard_template.html as structure
- Uses dashboard_theme.css for styling
- Fills in actual data, charts, risk cards

**Output 4: Risk Register**

- Uses RISK_FRAMEWORK.json to format
- Shows 5-7 identified risks with scores, mitigation

**Output 5: 90-Day Action Plan**

- Uses decision frameworks to prioritize
- 3-5 strategic actions ranked by impact/effort

**Output 6: Financial Forecast**

- Uses forecast_engine.py outputs
- Shows upside/base/downside scenarios
- 12-month P&L projection

---

## 💡 Example: Full QBR Generation Flow

```
USER INPUT:
├─ Company: TechStartup Inc (SaaS, Growth stage)
├─ Q2 2026 metrics: Revenue $2.5M, Customers 45, NRR 115%
├─ Burn: $750k/month, Runway: 18 months
├─ Growth: 12% QoQ, Top customer: 22% of revenue
└─ OKR completion: 82%

AI PROCESSING:
├─ [kpi_calculator.py] Calculate growth, margins, unit economics
├─ [BenchmarkComparator] Compare NRR 115% vs. benchmark 110-125% = "Good"
├─ [forecast_engine.py] Project Q3 scenarios
├─ [risk_scorer.py] Score risks:
│   ├─ Customer concentration: 6/10 (High - 22% top customer)
│   ├─ Financing: 4/10 (Medium - 18 month runway)
│   └─ Execution: 2/10 (Low - 82% OKR completion)
├─ [RISK_FRAMEWORK.json] Get mitigation strategies
├─ [STRATEGIC_FRAMEWORKS.json] Generate recommendations (2×2 matrix)
└─ [qbr_dashboard_template.html] Create dashboard

OUTPUTS:
├─ Executive Summary PDF (1 page)
├─ Board Presentation (12 slides)
├─ Interactive Dashboard (HTML, mobile responsive)
├─ Risk Register (5 risks with mitigation)
├─ 90-Day Action Plan (3 initiatives prioritized)
└─ 12-Month Forecast (revenue scenarios)
```

---

## 💬 Quick Start: Example Prompts

### Example 1: Full QBR for Board Meeting

**User Prompt:**

```
Use the QBR Intelligence Engine to create our Q2 2026 board presentation.

Company: CloudTech SaaS (growth stage)
Revenue: $3.2M ARR (was $2.8M last quarter)
Customers: 52 (up from 48)
NRR: 118%
Monthly Burn: $850k
Runway: 16 months
Top customer: 18% of revenue
Gross Margin: 72%
OKR completion: 75%
```

**What the Skill Does:**

1. Calculates growth metrics (+14.3% QoQ, 57% annualized)
2. Benchmarks against SaaS_Growth_Stage standards → "Excellent growth, good margins"
3. Scores risks:
   - Customer concentration: 4/10 (Low-Medium)
   - Financing: 5/10 (Medium)
   - Execution: 2/10 (Low)
4. Forecasts Q3 scenarios (upside: $3.6M, base: $3.4M, downside: $3.1M)
5. Generates 6 deliverables

**Outputs You Get:**

- ✅ Executive Summary (1 page)
- ✅ 12-slide Board Presentation
- ✅ Interactive HTML Dashboard
- ✅ Risk Register (3-5 risks with mitigation)
- ✅ 90-Day Action Plan (top 3 initiatives)
- ✅ 12-Month Financial Forecast

---

### Example 2: Risk Assessment Only

**User Prompt:**

```
I need a risk assessment for our Q2 review. Use the QBR risk framework.

Current situation:
- Top 3 customers: 45% of revenue
- Churn rate: 3.2% monthly
- Runway: 10 months (concerning)
- Open headcount: 8 positions unfilled for 8+ weeks
- NRR declining slightly (119% → 116%)
```

**What the Skill Does:**

1. Scores each risk using RISK_FRAMEWORK.json:
   - Customer concentration: 8/10 (CRITICAL)
   - Retention: 6/10 (HIGH)
   - Financing: 7/10 (HIGH)
   - Talent: 6/10 (HIGH)
2. Maps to risk matrix (probability × impact)
3. Gets mitigation playbooks for each

**Outputs You Get:**

- ✅ Risk Register with all 4 risks scored
- ✅ Mitigation strategies & timelines
- ✅ Escalation triggers for board
- ✅ Leading indicators to monitor

---

### Example 3: Investor Deck with Financials

**User Prompt:**

```
Create an investor update for our Series A follow-on. Generate a professional deck with our Q2 metrics and forward outlook.

Context: SaaS platform for financial services
ARR: $1.8M (was $1.4M, +29%)
Customers: 34
CAC: $8,500
LTV: $42,000
Gross Margin: 78%
Operating Burn: $280k/month
Runway: 22 months
```

**What the Skill Does:**

1. Calculates unit economics:
   - LTV:CAC ratio: 4.9x (excellent)
   - CAC Payback: 14 months (good)
   - Magic Number: 0.68 (excellent)
2. Benchmarks against Enterprise_SaaS standards → "Exceptional metrics"
3. Forecasts 18-month P&L
4. Generates strategic narrative

**Outputs You Get:**

- ✅ Investor Deck (15 slides)
- ✅ Financial Dashboard (HTML)
- ✅ Detailed Financial Forecast
- ✅ Risk Disclosure & Mitigation
- ✅ Competitive Positioning

---

### Example 4: Strategic Planning & Prioritization

**User Prompt:**

```
We need to prioritize our initiatives for the next quarter using QBR frameworks.

Current initiatives:
1. Expand into SMB segment (High impact, High effort, 8 weeks)
2. Improve product retention (High impact, Low effort, 4 weeks)
3. Optimize pricing (Medium impact, Low effort, 2 weeks)
4. Enter European market (High impact, Very high effort, 16 weeks)
5. Hire customer success team (Medium impact, Medium effort, 12 weeks)

Current metrics show we need to address churn and diversify customer base.
```

**What the Skill Does:**

1. Uses 2×2 Matrix framework from STRATEGIC_FRAMEWORKS.json
2. Plots each initiative: Quick Wins | Strategic Bets | Nice-to-Haves | Time Sinks
3. Recommends prioritization based on current risks
4. Creates action plan with owners & timelines

**Outputs You Get:**

- ✅ 2×2 Prioritization Matrix (visual + explanation)
- ✅ 90-Day Action Plan (top 3 initiatives with owners)
- ✅ Success metrics & milestones
- ✅ Resource allocation plan

---

### Example 5: Rapid Metrics Review & Benchmarking

**User Prompt:**

```
Quick benchmark check - how are we doing against industry?

Our current metrics:
- NRR: 112%
- Magic Number: 0.52
- CAC Payback: 16 months
- Gross Margin: 68%
- Rule of 40: 38 (32% growth + 6% margin)

We're a B2B SaaS, growth stage company.
```

**What the Skill Does:**

1. Looks up each metric in KPI_BENCHMARKS.json
2. Compares to SaaS_Growth_Stage benchmarks
3. Classifies each as Excellent/Good/Acceptable
4. Flags any red flags

**Outputs You Get:**

- ✅ Benchmark Report (1 page)
- ✅ Visual comparison chart
- ✅ Recommendations on what to improve
- ✅ Peer context & industry trends

---

### Example 6: Executive Team Strategic Alignment

**User Prompt:**

```
Generate a comprehensive Q2 review for our exec team meeting. Include all key metrics,
strategic context, risks, and recommendations. Use professional formatting.

TechScale Inc - SaaS platform for operations management
Q2 Metrics:
  Revenue: $5.2M ARR (Q1: $4.6M = +13% QoQ, +48% YoY)
  Customers: 87
  NRR: 122% (strong expansion)
  Churn: 1.8% monthly (improving)
  Gross Margin: 71%
  Operating Burn: $1.2M/month (stable)
  Runway: 14 months
  Win Rate: 28% (up from 24%)
  Sales Cycle: 4 months average
```

**What the Skill Does:**

1. Comprehensive calculations:
   - Growth metrics, unit economics, margins
   - Benchmarking (all metrics check out as "Good" to "Excellent")
   - Risk scoring (identify top 4-5 risks)
   - Forecasting (12-month P&L, scenarios)
2. Generates complete QBR package

**Outputs You Get:**

- ✅ Executive Summary Report (2 pages)
- ✅ Metrics Dashboard (HTML, interactive)
- ✅ Risk Register & Mitigation
- ✅ 90-Day Strategic Priorities
- ✅ 12-Month Forecast (upside/base/downside)
- ✅ Board-ready presentation slides
- ✅ Action Plan with owners & deadlines

---

## 🎯 When to Use This Skill

- **Quarterly board meetings** → Generate board presentation
- **Executive team planning** → Generate forecast & recommendations
- **Risk management** → Generate risk register & mitigation plans
- **Investor updates** → Generate investor deck with metrics
- **Strategic planning** → Generate 3-year plan using frameworks
- **Budget planning** → Generate OpEx forecast & headcount impact
- **Performance reviews** → Compare metrics to benchmarks

---

## 📖 Documentation Files

- **SKILL.md**: Full skill definition, inputs, outputs, processing steps
- **scripts/**: Working Python calculation engines
- **references/**: JSON data files for benchmarks & frameworks
- **assets/**: HTML/CSS presentation components
- **README.md**: This guide

---

## 🔄 Integration Points

This skill can integrate with:

- **Spreadsheets**: Read CSV data of metrics, generate insights
- **BI Tools**: Pull metrics from Tableau, Looker, etc.
- **CRM Systems**: Pull customer/revenue data
- **HR Systems**: Pull headcount data
- **Accounting Systems**: Pull financial data

---

## ✅ Success Criteria

A successful QBR output should have:

- ✅ Accurate calculations using scripts
- ✅ Metrics benchmarked against industry standards
- ✅ 5-7 risks identified with severity scores
- ✅ Realistic 2-quarter revenue forecast with scenarios
- ✅ 3-5 strategic recommendations ranked by impact/effort
- ✅ Professional, board-ready presentation
- ✅ Clear narrative connecting data to strategy
- ✅ Actionable 90-day plan with owners and deadlines

---

## 📝 Example Reference Data Usage

```
When AI needs to evaluate if 115% NRR is good:
→ Check KPI_BENCHMARKS.json
→ Find "SaaS_Growth_Stage" → "net_revenue_retention"
→ See: excellent=125%, good=110%, acceptable=100%
→ Conclusion: "115% is GOOD (above 110% threshold)"

When AI needs to score customer concentration risk:
→ Check RISK_FRAMEWORK.json
→ Find "customer_concentration" → "scoring_factors"
→ See: "if top_1_customer > 40%, score=9; if > 25%, score=7; if > 15%, score=5"
→ User data: top customer = 22%
→ Conclusion: "Score = 5-6 range (Medium risk)"

When AI needs to prioritize initiatives:
→ Check STRATEGIC_FRAMEWORKS.json
→ Use "2x2_matrix" (Impact × Effort)
→ Plot each initiative in quadrant
→ Recommendation: Focus on "Quick Wins" first
```

---

## 🎁 What Makes This Unique

Unlike generic QBR tools, this skill includes:

✓ **Production-grade calculation scripts** - Not guesses, precise math
✓ **Industry benchmarks** - Know if your metrics are good
✓ **Systematic risk framework** - Don't miss critical risks
✓ **Strategic decision frameworks** - Not just data, actionable strategy
✓ **Professional presentation assets** - Board-ready aesthetics
✓ **Scenario planning** - Upside/base/downside forecasts
✓ **Mitigation playbooks** - Know what to do about risks
✓ **Multiple output formats** - Dashboards, decks, reports, plans

---

This is a **complete, production-ready skill** that transforms raw business data into executive intelligence. All components work together to deliver comprehensive quarterly business reviews in minutes instead of days.
