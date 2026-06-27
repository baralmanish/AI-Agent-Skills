# Dashboard-It — Quick Reference

## Trigger Phrases
```
"Dashboard it"
"Build a dashboard for [topic or data]"
"Visualize this conversation / plan / data"
"Create a dashboard showing [metrics/decisions/workflow]"
"Turn this into an interactive HTML dashboard"
```

## How It Works
1. Reads the conversation — extracts core intent, key entities, priorities
2. Picks the right palette + layout from DESIGN_SYSTEM.json
3. Builds a self-contained HTML + JS dashboard (no external dependencies)
4. Delivers as an artifact you can preview, download, and open offline

## Palette Guide
| Palette | Best For |
|---|---|
| System (dark) | Tech, analytics, metrics, product dashboards |
| Executive (light) | Board reports, QBR, business intelligence |
| Warm (orange) | Personal productivity, coaching, wellness, habits |
| Minimal (neutral) | Clean design, portfolio, professional |
| Vibrant (dark/neon) | Creative, marketing, learning, motivational |

## Common Dashboard Types
| Type | What to Say |
|---|---|
| Metrics / KPI | "Show revenue, users, conversion — trend over time" |
| Project status | "Track tasks, blockers, milestones, owners" |
| Decision support | "Options, tradeoffs, recommendation" |
| Roadmap | "Group by quarter and priority with dependencies" |
| Personal productivity | "Goals, habits, focus areas, weekly progress" |
| Financial | "Spending by category, trends, savings opportunities" |

## Output Rules
- Single `.html` file — inline CSS + vanilla JS, no external deps
- Works offline in any browser
- Mobile responsive
- Footer attribution to Jules White's AI Agent Skills course

## Reference Files
- `references/DESIGN_SYSTEM.json` — palettes, typography, layout patterns, component specs
- `assets/starter_template.html` — full working scaffold with all common UI components
