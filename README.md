# AI Agent Skills

A collection of reusable, production-ready AI agent skills that can be dropped into any AI coding assistant or chat agent. Each skill is a self-contained instruction set that transforms a capable AI model into a specialized expert — generating dashboards, planning projects, writing emails, coaching you, and more.

---

## Skills Overview

| Skill                                                       | Folder                            | What it Does                                                                                        |
| ----------------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------- |
| [Dashboard-It](#dashboard-it)                               | `dashboard-it/`                   | Converts any conversation or data into a bold, interactive HTML dashboard                           |
| [Email Writing](#email-writing)                             | `email-writing/`                  | Writes perfectly-tailored emails across 10+ contexts with multiple draft options                    |
| [Expense Analyzer](#expense-analyzer)                       | `expense-analyzer/`               | Analyzes spending data and generates interactive budgeting dashboards                               |
| [Frontend Design](#frontend-design)                         | `frontend-design/`                | Creates distinctive, production-grade frontend interfaces and components with exceptional design    |
| [Humanizer](#humanizer)                                     | `humanizer/`                      | Strips AI tells from text and rewrites it as natural human prose                                    |
| [Meeting Notes](#meeting-notes)                             | `meeting-notes/`                  | Turns raw meeting notes or transcripts into structured summaries with action items                  |
| [MCP Builder](#mcp-builder)                                 | `mcp-builder/`                    | Generates and deploys production-ready Model Context Protocol servers with custom tools            |
| [Code Reviewer](#code-reviewer)                             | `code-reviewer/`                  | Reviews code for security (OWASP Top 10), bugs, performance, and style with severity-rated findings |
| [Organize Files](#organize-files)                           | `organize-files/`                 | Renames and restructures files into a logical, downloadable zip archive                             |
| [Personal Coach](#personal-coach)                           | `personal-coach/`                 | Surfaces hidden strengths from your work patterns and proposes one weekly experiment                |
| [Project Planning Dashboard](#project-planning-dashboard)   | `project-planning-dashboard/`     | Turns project ideas or notes into a Gantt-style dashboard + CSV plan                                |
| [QBR Intelligence Engine](#qbr-intelligence-engine)         | `qbr-intelligence-engine/`        | Transforms business metrics into board-ready QBR reports and dashboards                             |
| [Resume Builder](#resume-builder)                           | `resume-builder/`                 | Builds ATS-optimized, impact-driven resumes with keyword gap analysis and cover letters             |
| [Strategic Insights](#strategic-insights)                   | `strategic-insights/`             | Identifies one high-leverage career opportunity and creates a trackable experiment                  |
| [Weekly Meal Planner](#weekly-meal-planner-for-weight-loss) | `weekly-meal-planner-weightloss/` | Builds personalized weekly meal plans with shopping lists and a nutrition dashboard                 |

---

## Skill Details

### Dashboard-It

**Folder:** `dashboard-it/`  
**Trigger:** "Dashboard it" / "Build a dashboard for..." / "Visualize this"

Turns any conversation, plan, dataset, or workflow into a self-contained, modern HTML+JavaScript dashboard. No external dependencies — download and open in any browser.

**Key outputs:**

- Interactive HTML artifact with inline CSS + vanilla JS
- Filter, sort, drill-down controls where relevant
- Download instructions for offline use

---

### Email Writing

**Folder:** `email-writing/`  
**Trigger:** "Write an email to..." / "Help me email my manager about..."

Generates polished emails across 10+ contexts (executive updates, apologies, outreach, decline, announcements, etc.) with tone matching, recipient psychology analysis, and 2-3 draft variants.

**Key outputs:**

- Primary recommended draft
- Alternate formal and casual versions
- Subject line options

---

### Expense Analyzer

**Folder:** `expense-analyzer/`  
**Trigger:** "Analyze my spending" / "Here's my credit card statement..."

Accepts transaction data, CSVs, or pasted statements. Categorizes spending, finds recurring charges, flags high-spend areas, and builds a luxury interactive dashboard with what-if budgeting and savings projections.

**Key outputs:**

- Interactive budgeting dashboard (HTML)
- Spending category breakdown and trend charts
- Savings projection over 6 months, 1 year, 5 years
- Subscription and recurring-charge audit

---

### Frontend Design

**Folder:** `frontend-design/`  
**Trigger:** "Build a landing page" / "Design a component" / "Redesign this UI to be..."

Creates distinctive, production-grade web interfaces that avoid generic "AI aesthetics." Combines design thinking with implementation guidance across multiple frameworks (HTML, React, Vue). Every design choice is intentional and visually striking.

**Key outputs:**

- Production-grade HTML/React/Vue components
- Complete design system (typography, colors, motion, spacing)
- Responsive, accessible, high-performance code
- 10+ aesthetic directions to choose from (minimal, maximalist, luxury, brutalist, retro, etc.)

---

### Humanizer

**Folder:** `humanizer/`  
**Trigger:** "Humanize this" / "Make this sound less like AI"

Applies a strict humanization protocol: rewrites with sentence rhythm variety, removes banned AI words (`delve`, `tapestry`, `vibrant`, etc.), eliminates em-dashes, "not only...but also" patterns, and corporate boilerplate. Output is plain text ready to use — no filler or explanation.

**Key outputs:**

- Direct rewrite with no commentary
- Natural voice: decisive, specific, rhythmically varied

---

### Organize Files

**Folder:** `organize-files/`  
**Trigger:** "Organize these files" / "Clean up my folder" / "Rename these files consistently"

Designs a naming scheme and folder taxonomy first, then executes a full reorganization of uploaded or referenced files. Delivers everything in a single downloadable `.zip` archive.

**Key outputs:**

- Renamed files following consistent naming rules
- Logical folder hierarchy
- Downloadable zip archive
- Brief explanation of naming and structural decisions

---

### Personal Coach

**Folder:** `personal-coach/`  
**Trigger:** "Coach me" / "What should I work on this week?" / "Give me career insights"

Reads your conversation patterns to surface one non-obvious hidden strength or opportunity. Proposes a single, low-friction weekly experiment (<15 min/day) with a simple daily + weekly tracking method.

**Key outputs:**

- One strategic insight
- One weekly behavior change
- `What | Why | How` action table
- CSV tracker + link to downloadable template

---

### Project Planning Dashboard

**Folder:** `project-planning-dashboard/`  
**Trigger:** "Plan this project" / "Create a project dashboard" / "Build a Gantt chart for..."

Takes any project idea, meeting notes, or scope document and produces a structured plan with phases, tasks, dependencies, estimates, and risks — plus a polished HTML Gantt-style dashboard.

**Key outputs:**

- CSV project plan (Task ID, Phase, Dependencies, Estimates, Risks, Owner, Rationale)
- HTML dashboard with Gantt timeline, critical path, and risk view
- Stakeholder-presentation-ready output

---

### QBR Intelligence Engine

**Folder:** `qbr-intelligence-engine/`  
**Trigger:** "Generate my Q3 QBR" / "Build my board presentation" / "Create a quarterly business review"

Transforms raw business metrics into a complete QBR package: executive summary, board deck outline, interactive analytics dashboard, 90-day action plan, and risk register. References bundled `KPI_BENCHMARKS.json`, `RISK_FRAMEWORK.json`, and `STRATEGIC_FRAMEWORKS.json` for authoritative benchmarking.

**Key outputs:**

- 1-page executive summary
- 8-12 slide board presentation outline
- Interactive HTML analytics dashboard
- 90-day action plan with ownership and metrics
- Risk register with probability × impact matrix

---

### Strategic Insights

**Folder:** `strategic-insights/`  
**Trigger:** "Give me strategic insights" / "What's my career blind spot?" / "Help me think about my growth"

Similar to Personal Coach but focused on longer-horizon career and professional strategy. Surfaces one under-leveraged opportunity from your conversation patterns and pairs it with a trackable 7-day experiment.

**Key outputs:**

- One strategic insight (strengths-based, practical)
- One weekly change (7 days, low-friction)
- `What | Why | How` table
- CSV tracker with copy-paste block + downloadable template

---

### Weekly Meal Planner for Weight Loss

**Folder:** `weekly-meal-planner-weightloss/`  
**Trigger:** "Create a meal plan for me" / "Help me lose weight this week" / "Build my weekly meals"

Gathers personal health metrics, dietary preferences, budget, and cooking time to produce a science-backed 7-day meal plan. Outputs everything from a grocery list to a full interactive HTML dashboard with macro tracking.

**Key outputs:**

- 7-day meal plan with calories and macros per meal
- Optimized shopping list grouped by store section
- Nutrition summary report
- Meal prep guide (batch cooking timeline + storage)
- Restaurant/takeout alternatives
- Interactive HTML dashboard with macro circles, weight projection, and checklist

---

### Meeting Notes

**Folder:** `meeting-notes/`  
**Trigger:** "Summarize these meeting notes" / "Extract action items" / "Clean up my notes from today's call"

Transforms raw, messy meeting notes or transcripts (Zoom, Teams, handwritten) into a structured output the whole team can act on — with a decisions log, action items table with owners and deadlines, and an optional follow-up email draft.

**Key outputs:**

- TL;DR executive summary (2–3 sentences)
- Decisions made (table)
- Action items with owner, due date, and priority
- Discussion summary by topic
- Open questions and blockers
- Follow-up email draft (when 3+ action items or explicitly requested)

---

### MCP Builder

**Folder:** `mcp-builder/`  
**Trigger:** "Build an MCP server" / "Create a tool for..." / "Deploy an MCP server"

Generates production-ready Model Context Protocol servers with custom tools and resources. Supports Python (FastMCP) and Node.js/TypeScript with comprehensive implementation patterns, async operations, error handling, testing, and deployment guidance.

**Key outputs:**

- Fully functional MCP server with custom tools
- Support for databases, APIs, file operations, workflows
- Docker deployment ready
- Comprehensive reference guides for Python and Node.js SDKs
- 6 common tool design patterns with production code examples

---

### Code Reviewer

**Folder:** `code-reviewer/`  
**Trigger:** "Review this code" / "Is this secure?" / "Check for vulnerabilities" / "Performance review"

Performs a structured, multi-dimensional code review across security (OWASP Top 10), correctness, performance, maintainability, and idiomatic style. Every finding includes the exact problematic code and a specific corrected version — no vague advice.

**Key outputs:**

- Scorecard (count per severity: Critical / High / Medium / Low / Suggestion)
- Security findings mapped to OWASP Top 10 and language-specific CVEs
- Correctness, performance, and maintainability findings
- Each finding: location + description + current code + fixed code
- Top 3 priority actions

---

### Resume Builder

**Folder:** `resume-builder/`  
**Trigger:** "Improve my resume" / "Tailor this resume to the job" / "Write a cover letter" / "Build my resume from scratch"

Builds or optimizes a resume for ATS screening and human recruiter readability. Rewrites experience bullets using the CAR/XYZ impact framework (every bullet has a strong verb + metric), performs a keyword gap analysis against the job description, and generates a tailored cover letter.

**Key outputs:**

- ATS keyword gap table (Present / Partial / Missing per job description term)
- Before vs. After comparison for key bullets
- Rewritten professional summary (no filler phrases)
- Optimized skills section grouped by category
- Full formatted resume (copy-paste ready, single-column ATS-safe)
- Tailored cover letter (if job description provided)

---

## How to Use in Different AI Agents

### GitHub Copilot (VS Code)

1. Copy the skill folder (e.g., `dashboard-it/`) into your workspace or a shared location.
2. In VS Code settings, add the `SKILL.md` path to your Copilot instructions:
   - Open `.vscode/settings.json` or your workspace's `.github/copilot-instructions.md`
   - Reference the skill with: `@workspace /path/to/SKILL.md`
3. In Copilot Chat, invoke with the skill's trigger phrase (e.g., `"Dashboard it"`).
4. Alternatively, add the skill to your **User Instructions** under `GitHub Copilot > Instructions` in VS Code settings.

**Tip:** Place frequently used skills in `~/.github/copilot-instructions.md` to make them always available across workspaces.

---

### Cursor

1. Copy the desired `SKILL.md` into your project root as `.cursorrules` **or** add it to Cursor's rules via `Settings > Rules for AI`.
2. For project-scoped rules, create `.cursor/rules/` directory and place skill files there.
3. Invoke skills using their trigger phrases in Cursor Chat (`Cmd+L`).
4. For multi-skill setups, use the `@file` reference syntax: `@SKILL.md dashboard-it please dashboard the current plan`.

**Tip:** Cursor's `notepads` feature (Beta) lets you attach skill files as persistent context to any composer session.

---

### Claude Code

1. Place the `SKILL.md` in your project root or a `skills/` subfolder.
2. Reference it at the start of your session:
   ```
   Read the skill file at ./skills/dashboard-it/SKILL.md and apply it.
   ```
3. Or add skills to your `CLAUDE.md` project memory file so they load automatically on every session:

   ```markdown
   ## Active Skills

   - Dashboard-It: see ./skills/dashboard-it/SKILL.md
   - Humanizer: see ./skills/humanizer/SKILL.md
   ```

4. Invoke via trigger phrase in any message.

**Tip:** Claude Code respects `CLAUDE.md` at the project root as persistent instructions — ideal for always-on skills like Humanizer or Personal Coach.

---

### OpenAI Codex (and ChatGPT with custom instructions)

1. **Custom Instructions (ChatGPT):** Paste the contents of a `SKILL.md` into _Settings > Personalization > Custom Instructions_ (the "How should ChatGPT respond" field) to make a skill always active.
2. **API / Codex:** Include the `SKILL.md` content as a system prompt:

   ```python
   with open("skills/dashboard-it/SKILL.md") as f:
       skill_prompt = f.read()

   response = client.chat.completions.create(
       model="gpt-4o",
       messages=[
           {"role": "system", "content": skill_prompt},
           {"role": "user", "content": "Dashboard it — here's my project data..."}
       ]
   )
   ```

3. For multi-skill sessions, concatenate the relevant `SKILL.md` files with a separator into the system prompt.

**Tip:** Keep each `SKILL.md` under ~1,500 tokens for best results within context limits.

---

### Antigravity

1. Create a new agent or workflow in Antigravity.
2. In the **System Prompt** or **Instructions** field, paste the full contents of the desired `SKILL.md`.
3. Use the skill's `name` field value as the agent's name for easy identification.
4. Set the `argument-hint` as the agent's input description or placeholder so users know what to provide.
5. For complex skills with reference assets (like `qbr-intelligence-engine`), upload the JSON/asset files and reference them in the prompt.

**Tip:** Chain skills together in Antigravity workflows — for example, run `expense-analyzer` first, then pipe the output into `dashboard-it` for a two-stage financial visualization pipeline.

---

## Skill File Structure

Each skill follows this standard structure:

```
skill-name/
├── SKILL.md          # Main skill definition (YAML frontmatter + instructions)
├── README.md         # Human-readable overview and usage notes
├── assets/           # Optional supporting files (templates, CSS, data files)
└── references/       # Optional JSON reference files for data-driven skills
```

### SKILL.md Frontmatter Fields

```yaml
---
name: skill-name # Unique identifier, matches folder name
description: "..." # When the AI should invoke this skill
tags: [tag1, tag2] # Categorization tags
argument-hint: "..." # What input the user should provide
user-invocable: true # Whether users can trigger it directly
disable-model-invocation: false # Whether the AI can auto-invoke it
---
```

---

## Adding a New Skill

1. Create a new folder with a kebab-case name: `my-skill/`
2. Add `SKILL.md` with the standard frontmatter (use an existing skill as template)
3. Add `README.md` describing the skill's purpose
4. Add any reference files to `assets/` or `references/`
5. Add the skill to the table at the top of this README

---

## Credits

Some skills reference the [AI Agent Skills course](https://www.coursera.org/learn/agent-skills) by Jules White on Coursera. The `dashboard-it` skill includes a required attribution link in all generated outputs.
