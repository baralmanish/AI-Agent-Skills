# Resume Builder Skill

Builds, improves, and tailors resumes for specific job applications. Optimizes for ATS keyword matching, rewrites experience bullets using the CAR/XYZ impact framework, and optionally generates a tailored cover letter.

## Triggers

- "Improve my resume"
- "Tailor my resume to this job description"
- "My resume isn't getting callbacks"
- "Build me a resume from scratch"
- "Write a cover letter for this role"

## Sample Prompts

### Tailor to a Job Description

```text
Here is my current resume and the job description I'm applying for.
Tailor my resume to this specific role.
Do an ATS keyword gap analysis and rewrite my bullets with metrics.
```

### Fix a Weak Resume

```text
My resume isn't getting callbacks. Review it and tell me what's wrong.
Rewrite the weakest bullets using the CAR framework.
Flag any ATS formatting issues.
```

### Build From Scratch

```text
Help me build a resume from scratch.
Here is my work history: [paste experience]
I'm targeting [role/industry]. Make it ATS-optimized and impact-driven.
```

### ATS Keyword Audit

```text
Run an ATS keyword analysis on my resume against this job description.
Show me which keywords are present, partial, or missing.
Tell me exactly where to add the missing ones.
```

### Bullet Rewrite Only

```text
Rewrite my experience bullets using the CAR or XYZ framework.
Every bullet needs a strong action verb and at least one metric.
Here are my current bullets: [paste]
```

### Write a Cover Letter

```text
Write a cover letter for this job posting.
Here is my resume and the job description.
Make it specific — no generic filler. Show two relevant achievements
mapped to the job's key requirements.
```

### Career Change Resume

```text
I'm changing from [current role] to [target role].
Help me reframe my resume to highlight transferable skills.
Adjust bullets and summary to speak to the new role.
```

## Files

| File                               | Purpose                                                                |
| ---------------------------------- | ---------------------------------------------------------------------- |
| `SKILL.md`                         | Full skill definition, CAR/XYZ framework, ATS rules, output template   |
| `QUICK_REFERENCE.md`               | Process table, bullet rules, ATS score targets, script usage           |
| `references/ACTION_VERBS.json`     | Strong verbs by function, verbs to avoid, bullet framework rules       |
| `references/ATS_KEYWORDS.json`     | ATS keywords for 9 role families and certification types               |
| `assets/cover_letter_template.txt` | Cover letter framework with per-paragraph rules and pre-send checklist |
| `scripts/keyword_matcher.py`       | CLI ATS keyword gap analysis — resume vs. job description              |

## What It Does

| Step                | Output                                                      |
| ------------------- | ----------------------------------------------------------- |
| ATS audit           | Keyword gap table — which job description terms are missing |
| Bullet rewriting    | CAR/XYZ format — every bullet has an action verb + metric   |
| Summary rewrite     | 3–5 sentences, role-specific, no filler phrases             |
| Skills optimization | Grouped by category, ordered by relevance to target role    |
| Formatting          | Single-column, ATS-safe, standard headings                  |
| Cover letter        | 3–4 paragraphs, achievement-mapped to job requirements      |

## Supported Formats

- Standard resume (1–2 page)
- Academic / research CV (publications, grants, conferences)
- Career-change resume (transferable skills emphasis)

## Files

| File       | Purpose                                                              |
| ---------- | -------------------------------------------------------------------- |
| `SKILL.md` | Full skill definition, CAR/XYZ framework, ATS rules, output template |
