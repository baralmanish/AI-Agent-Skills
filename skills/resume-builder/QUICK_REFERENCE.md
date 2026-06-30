# Resume Builder — Quick Reference

## Trigger Phrases

```
"Improve my resume"
"Tailor this resume to the job description"
"My resume isn't getting callbacks"
"Build my resume from scratch"
"Write a cover letter for this role"
"ATS scan my resume"
```

## Process at a Glance

| Step                   | What Happens                                                   |
| ---------------------- | -------------------------------------------------------------- |
| 1. Audit               | Gaps in impact, ATS keywords, and formatting                   |
| 2. Keyword Analysis    | Job description mapped to resume — Present / Partial / Missing |
| 3. Bullet Rewrite      | Every bullet → strong verb + metric (CAR/XYZ framework)        |
| 4. Summary Rewrite     | 3–5 sentences, role-specific, zero filler phrases              |
| 5. Skills Optimization | Grouped by category, ordered by relevance                      |
| 6. Format Check        | Single-column ATS-safe layout, standard headings               |
| 7. Cover Letter        | 3–4 paragraphs, achievement-mapped to job requirements         |

## Bullet Point Rules

- **Lead verb**: Always first word — pick from ACTION_VERBS.json
- **Metric**: At least one number per bullet (%, $, time, scale)
- **Framework**: CAR (Challenge → Action → Result) or XYZ (Accomplished X as measured by Y by doing Z)
- **Length**: Max 2 lines — split if longer
- **Tense**: Past tense for previous roles; present for current role

## Verbs to AVOID

Responsible for · Helped with · Worked on · Assisted in · Participated in · Tasked with · Handled

## ATS Format Rules

- Single-column layout only (no tables, no text boxes)
- Standard section headings: Summary · Experience · Education · Skills · Certifications
- No headers/footers (ATS cannot parse them)
- Font: Calibri, Arial, or Garamond (11–12pt body)
- Length: 1 page for <10 years exp; 2 pages for 10+ years

## ATS Score Targets

| Score  | Meaning                            |
| ------ | ---------------------------------- |
| 80%+   | Strong match — safe to apply       |
| 60–79% | Moderate — improve before applying |
| <60%   | Weak — significant keyword gaps    |

## Keyword Matcher Script

```bash
# Compare resume to job description
python scripts/keyword_matcher.py --resume resume.txt --job job_description.txt

# With role family for richer keyword reference
python scripts/keyword_matcher.py --resume resume.txt --job job_description.txt --role software_engineering

# Show top 30 missing keywords
python scripts/keyword_matcher.py --resume resume.txt --job job_description.txt --top 30

# Exit codes: 0=strong (80%+), 1=moderate (60-79%), 2=weak (<60%)
```

## Supported Resume Formats

- Standard resume (1–2 page)
- Academic / research CV (publications, grants, conferences)
- Career-change resume (transferable skills emphasis)

## Reference Files

- `references/ACTION_VERBS.json` — Strong verbs grouped by function; includes verbs to avoid
- `references/ATS_KEYWORDS.json` — ATS keywords by role family and industry
- `assets/cover_letter_template.txt` — Cover letter framework with rules and checklist
- `scripts/keyword_matcher.py` — CLI ATS keyword gap analysis tool
