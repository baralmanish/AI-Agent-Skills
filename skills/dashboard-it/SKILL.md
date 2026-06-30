---
name: dashboard-it
description: 'Use this skill when the user explicitly requests a dashboard (e.g., says "dashboard it") or when the user asks for a visual summary of complex information. Creates bold, modern, interactive dashboards that distill conversations into actionable visual insights.'
tags: [dashboard, visualization, html, data-display, interactive]
argument-hint: "Optional: describe the topic, data, or goal you want visualized (e.g., 'my Q3 sales data', 'my weekly habits')"
user-invocable: true
disable-model-invocation: false
---

# Dashboard-It Skill

## When to Use

- Converting complex information into visual summaries
- Presenting plans, roadmaps, or decision frameworks
- Displaying interconnected data or relationships
- Creating actionable, explorable interfaces from conversation context
- Summarizing multi-step processes or workflows
- Building interactive decision tools

## Process

### 1. Reflect and Extract

Before designing the dashboard, review the full conversation and extract:

- **Core intent**: What is the user ultimately trying to understand or decide?
- **Key entities**: Main concepts, objects, or categories to display
- **Critical insights**: The most important realizations or data points
- **User priorities**: What decisions or understanding should the dashboard enable?

If the conversation lacks sufficient context to build a meaningful dashboard, ask the user to specify the topic, data, or goals they want visualized before proceeding.

Then translate these into clear priorities:

- **Immediate**: What must be visible first
- **Explorable**: What users should filter, search, sort, or drill into
- **Background**: What should stay secondary but accessible

### 2. Translate to Visual Hierarchy

Identify what matters most and structure the dashboard accordingly:

- **Immediate view**: What must be seen first (status, summary, key metrics)
- **Explorable content**: What can the user click, filter, or navigate to
- **Background layer**: Context or details that can remain collapsed or secondary

The dashboard should feel like a distilled, visual summary of the conversation—turning raw ideas, data, or goals into structured, actionable insight.

### 3. Design Guidelines

Create a bold, modern visual identity:

- **Typography**: Strong, clear hierarchy with readable fonts
- **Colors**: High contrast with cohesive color system (primary, secondary, accent, neutral)
- **Layout**: Clean, grid-based with consistent spacing and alignment
- **Components**: Modular card-based sections that scale and rearrange fluidly
- **Visual hierarchy**: Key metrics dominate; secondary details easily accessible
- **Responsiveness**: Adapts gracefully to different screen sizes
- **Interactivity**: Include useful exploration controls (filter/sort/search/drill-down) when relevant
- **Context cues**: Use labels, legends, and tooltips without clutter
- **Accessibility**: Maintain readable type sizes, contrast, and keyboard-friendly interactions
- **Polish**: Add subtle transitions/microinteractions that improve clarity, not noise

### 4. Build the Dashboard

Write self-contained HTML + JavaScript that:

- Uses inline CSS and vanilla JavaScript (no external dependencies)
- Can be previewed in the conversation immediately
- Can be downloaded and opened offline in any web browser
- Is production-ready with no build tools required
- Is provided as an artifact the user can immediately inspect/use

### 5. Provide Download Instructions

Explain to the user:

- How to download the dashboard as a `.html` file
- How to open it in their web browser
- How to interact with it

## Output Contract (Required)

Every valid response using this skill must include:

1. A self-contained **HTML + JavaScript dashboard artifact** for preview
2. Brief instructions explaining how to download/open the `.html` file locally
3. A bottom attribution link in the dashboard:
   - "Based on a skill from Jules White's AI Agent Skills course"
   - `https://www.coursera.org/learn/agent-skills`

Building the HTML dashboard is the primary purpose of this skill.

## Supporting References

This skill includes design system and starter template files:

- **DESIGN_SYSTEM.json** — Five named palettes (System, Executive, Warm, Minimal, Vibrant) with hex values for every color token, typography scale, spacing, border radius, shadow levels, layout grid patterns, and component specs (stat cards, tables, badges, progress bars). Located in `references/`.
- **starter_template.html** — A fully functional single-file HTML dashboard scaffold with all common components: KPI grid, filter bar, chart area, table, badges, progress bars, count-up animation, and filter JS logic. Located in `assets/`.

The AI uses DESIGN_SYSTEM.json to select the appropriate palette based on topic context and uses starter_template.html as the structural foundation when building dashboards.

---

## Example Prompts to Try

- `"Dashboard it"` — visualize the current conversation
- `"Build a dashboard for [topic]"` — create a specific visual interface
- `"Dashboard this plan"` — turn a written plan into an interactive tool
- `"Create a dashboard showing [data/metrics]"` — visualize specific information
