---
name: resume-builder
description: "Use this skill when the user wants to create, improve, or tailor a resume or CV for a specific job. Optimizes for ATS (Applicant Tracking Systems), rewrites bullet points with impact metrics, aligns the resume to the job description, and optionally generates a tailored cover letter."
tags: [resume, cv, job-search, ats-optimization, career, cover-letter]
argument-hint: "Provide your current resume (or raw experience) and optionally the job description you're targeting"
user-invocable: true
disable-model-invocation: false
---

# Resume Builder

Build or optimize a resume that passes ATS screening, reads compellingly to human recruiters, and is precisely tailored to the target role. Every bullet point should prove impact, not just describe a duty.

## When to Use

- User shares their resume and asks to improve it
- User shares a job description and wants their resume tailored to it
- User describes their work experience and needs help building a resume from scratch
- User says "make my resume better", "tailor this to the job", "I'm not getting callbacks"
- User needs a cover letter to accompany the application

## Inputs

- **Required:** Current resume text, OR a description of work experience
- **Optional via `$ARGUMENTS`:**
  - Target job description (strongly recommended for tailoring)
  - Target role or company name
  - Career level (entry, mid, senior, executive)
  - Output format preference (one-page, two-page, academic CV)

## Process

### Step 1: Audit the Existing Resume

Analyze the provided resume for the following gaps:

**Content gaps:**

- Missing quantified impact (% improvement, revenue generated, users served, time saved)
- Duties written as responsibilities rather than achievements
- Missing skills required by the target job description
- Redundant or irrelevant experience for this role

**ATS gaps:**

- Missing keywords from the job description (job title, required skills, tools, certifications)
- Non-standard section headings that ATS parsers misread (use: Summary, Experience, Education, Skills, Certifications)
- Tables, columns, text boxes, headers/footers that ATS systems cannot parse
- Missing or inconsistent date formatting

**Readability gaps:**

- Bullet points longer than 2 lines
- Inconsistent tense (use past tense for all previous roles, present tense for current role)
- Weak opening verbs (avoid "Responsible for", "Helped with", "Worked on")
- Lack of a compelling professional summary

### Step 2: Keyword Alignment (if job description provided)

- Extract required skills, tools, and qualifications from the job description
- Map each against the resume — mark as Present, Partially Present, or Missing
- Flag the top 5 missing keywords that are critical to include
- Suggest where in the resume each missing keyword can be naturally integrated

### Step 3: Rewrite Bullet Points Using the CAR / XYZ Framework

Every bullet point must follow one of:

- **CAR:** Challenge → Action → Result
  - "Reduced API response time by 40% by introducing Redis caching, enabling the team to support 3× traffic without infrastructure changes"
- **XYZ (Google formula):** Accomplished [X] as measured by [Y], by doing [Z]
  - "Grew enterprise ARR from $2M to $5.1M (155% YoY) by redesigning outbound sales process and hiring 3 account executives"

Rules for rewriting:

- Lead with a strong action verb (Built, Led, Reduced, Increased, Launched, Negotiated, Designed, Automated)
- Include at least one metric per bullet (%, $, time saved, headcount, scale)
- If the user cannot provide exact metrics, use ranges or relative indicators ("~30% reduction", "across a team of 12")
- Cut bullets describing routine tasks with no differentiated impact
- Cap bullets at 2 lines

### Step 4: Write or Improve the Professional Summary

- 3–5 sentences maximum
- Lead with role title + years of experience + most distinctive credential
- Include 2–3 core strengths most relevant to the target role
- Close with what you bring to this specific type of company or challenge
- Never use generic filler ("results-driven professional", "team player", "passionate about...")

### Step 5: Optimize Skills Section

- Group by category: Technical Skills, Tools & Platforms, Methodologies, Languages, Certifications
- Include every tool and skill mentioned in the job description that the user genuinely has
- Remove skills that are universally expected and add no signal (Microsoft Word, Google Search)
- Order within categories by relevance to the target role (most relevant first)

### Step 6: Format for ATS + Human Readability

**Structure:**

1. Contact Info (Name, Email, Phone, LinkedIn, GitHub/Portfolio if relevant)
2. Professional Summary
3. Skills
4. Work Experience (reverse chronological)
5. Education
6. Certifications (if any)
7. Projects / Publications / Awards (if relevant)

**Formatting rules:**

- Single-column layout only (ATS-safe)
- No tables, no text boxes, no headers/footers
- Standard fonts: Calibri, Arial, Garamond (11–12pt body, 14–16pt name)
- Consistent date format: MMM YYYY (e.g., "Jan 2022 – Present")
- Section headings in ALL CAPS or Title Case — one style throughout
- Margins: 0.5–1 inch
- Length: 1 page for <10 years experience; 2 pages acceptable for 10+ years

### Step 7: Generate Cover Letter (if requested or ≥1 job description provided)

Structure:

- **Opening:** Why this company and this role specifically (not generic flattery)
- **Body (2 paragraphs):** Your 2 most relevant achievements directly mapped to the job's key requirements
- **Closing:** Clear call to action + availability for interview
- Tone: Confident, specific, human — matches the company's voice if discernible
- Length: 3–4 short paragraphs, fits one page

## Decision Rules

- If no job description is provided, optimize for the role title and industry inferred from experience
- If the user has gaps (career break, missing degree, overqualified): acknowledge them and provide a framing strategy, do not hide them
- If a bullet truly has no quantifiable impact, keep it but make the action and scope clear
- If the resume is for an academic or research role, switch to CV format: include publications, grants, conference presentations
- Always preserve the user's actual experience — never fabricate roles, companies, or metrics

## Quality Criteria (Completion Checks)

Every response must include:

- ✅ ATS keyword gap analysis (if job description was provided)
- ✅ Rewritten Professional Summary
- ✅ Rewritten Work Experience bullets (CAR/XYZ format, quantified)
- ✅ Optimized Skills section
- ✅ Full formatted resume (copy-paste ready)
- ✅ Cover letter (if job description provided or explicitly requested)
- ✅ "Before vs. After" comparison for at least 3 bullet points

## Output Template

---

### ATS Keyword Analysis

| Keyword from Job Description | Status                               | Where to Add         |
| ---------------------------- | ------------------------------------ | -------------------- |
| [keyword]                    | ✅ Present / ⚠️ Partial / ❌ Missing | [section suggestion] |

**Top 5 missing keywords to add:** [list]

---

### Before vs. After: Key Bullet Points

**Before:** Responsible for managing the customer support team  
**After:** Led 12-person customer support team to achieve 94% CSAT (↑11 pts YoY) by introducing tiered escalation workflows and weekly coaching sessions

---

### Optimized Resume

[Full formatted resume — copy-paste ready]

---

### Cover Letter

[Full cover letter — copy-paste ready]

---

## Supporting References

This skill includes reference files for keyword authority, writing quality, and output templates:

- **ACTION_VERBS.json** — Strong resume verbs grouped by function (leadership, building, optimizing, analyzing, etc.) with verbs to avoid, placement rules, and the full CAR/XYZ bullet framework. Located in `references/`.
- **ATS_KEYWORDS.json** — ATS keywords by role family (software engineering, product, marketing, sales, finance, design, operations, HR) and certification type. Includes rules on keyword density and placement priority. Located in `references/`.
- **cover_letter_template.txt** — Structured cover letter framework with opening/body/closing rules, example text, and a pre-send checklist. Located in `assets/`.
- **keyword_matcher.py** — CLI tool that compares a resume text file against a job description and outputs a keyword gap report with placement suggestions. Supports role family filtering. Located in `scripts/`.

The AI uses ACTION_VERBS.json to rewrite bullets and ATS_KEYWORDS.json to audit keyword coverage. The cover_letter_template.txt governs cover letter structure and quality rules.

---

## Example Invocations

- `"Here's my resume and the job description — tailor it for this role"`
- `"Improve my resume, I'm applying for senior engineering roles"`
- `"My resume isn't getting callbacks — what's wrong with it?"`
- `"Build me a resume from scratch — here's my work history"`
- `"Write a cover letter for this job posting"`
