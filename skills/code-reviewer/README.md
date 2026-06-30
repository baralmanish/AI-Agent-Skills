# Code Reviewer Skill

Performs a structured, multi-dimensional code review covering security (OWASP Top 10), correctness, performance, maintainability, and idiomatic style. Returns severity-rated findings with specific fixed code — not generic advice.

## Triggers

- "Review this code"
- "Is this secure?"
- "Check for SQL injection / XSS / security issues"
- "What's wrong with this function?"
- "Performance review"

## Review Dimensions

| Dimension       | What It Checks                                                 |
| --------------- | -------------------------------------------------------------- |
| Security        | OWASP Top 10, language-specific CVEs, hardcoded secrets        |
| Correctness     | Logic bugs, null references, unhandled errors, race conditions |
| Performance     | N+1 queries, O(n²) loops, blocking I/O, missing pagination     |
| Maintainability | Complexity, naming, magic numbers, dead code, duplication      |
| Style           | Language idioms, framework conventions, testability            |

## Severity Levels

| Badge         | Meaning                                                     |
| ------------- | ----------------------------------------------------------- |
| 🔴 Critical   | Security vulnerability or data-loss risk — fix before merge |
| 🟠 High       | Likely bug or serious performance issue — fix before merge  |
| 🟡 Medium     | Code quality issue — fix in near-term                       |
| 🟢 Low        | Style suggestion — fix when convenient                      |
| 💡 Suggestion | Non-blocking alternative approach                           |

## Outputs

1. Scorecard (count per severity)
2. Findings — each with: location, description, current code, fixed code
3. Top 3 priority actions

## Sample Prompts

### Security Review

```text
Review this code for security vulnerabilities.
Check against the OWASP Top 10 and flag any injection, auth,
or data exposure risks. Show me the exact lines and how to fix them.
```

### Full Code Review

```text
Full code review — this is a public REST API endpoint.
Check security, correctness, performance, and style.
Return a scorecard and prioritized findings with fixed code for each.
```

### SQL Injection Check

```text
Is this SQL query vulnerable to injection?
If so, show me exactly where and give me the parameterized version.
```

### Performance Review

```text
Review this code for performance issues.
Look for N+1 queries, unnecessary loops, blocking I/O,
and missing pagination. Show what to change.
```

### Python Security Scan

```text
Scan this Python code for dangerous patterns.
Check for eval(), exec(), pickle.loads(), shell=True,
and any hardcoded credentials.
```

### React Component Review

```text
Review this React component for best practices.
Check for XSS risks (innerHTML, dangerouslySetInnerHTML),
performance issues, and hooks rule violations.
```

### Pre-PR Security Check

```text
Do a security-focused review of this code before I open a PR.
Only flag Critical and High severity issues. Give me the fix for each.
```

## Files

| File                                | Purpose                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| `SKILL.md`                          | Full skill definition, OWASP checklist, review process, and output template    |
| `QUICK_REFERENCE.md`                | Severity table, OWASP checklist, scanner usage                                 |
| `references/OWASP_TOP10.json`       | Full OWASP Top 10 2021 — code signals, language patterns, CWE IDs, mitigations |
| `references/LANGUAGE_PATTERNS.json` | Dangerous patterns per language with severity and safe alternatives            |
| `references/SEVERITY_MATRIX.json`   | Scoring criteria, merge policies, examples per severity level                  |
| `scripts/pattern_scanner.py`        | CLI pre-check tool — scans files for dangerous patterns, CI/CD compatible      |
