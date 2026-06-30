# Code Reviewer — Quick Reference

## Trigger Phrases

```
"Review this code"
"Is this secure? / Check for vulnerabilities"
"Security audit of this function"
"What's wrong with this code?"
"Performance review"
"Full code review — this is a public API"
```

## Review Dimensions

| Dimension       | Focus                                                                |
| --------------- | -------------------------------------------------------------------- |
| Security        | OWASP Top 10, language CVEs, hardcoded secrets, injection, auth      |
| Correctness     | Logic bugs, null refs, unhandled errors, edge cases, race conditions |
| Performance     | N+1 queries, O(n²) loops, blocking I/O, missing pagination           |
| Maintainability | Complexity, naming, magic numbers, dead code, duplication            |
| Style           | Idioms, framework conventions, testability                           |

## Severity Levels

| Badge         | Merge Policy  | Fix When                 |
| ------------- | ------------- | ------------------------ |
| 🔴 Critical   | Block merge   | Immediately              |
| 🟠 High       | Block merge   | Current sprint           |
| 🟡 Medium     | Prefer to fix | Within 2 sprints         |
| 🟢 Low        | Merge fine    | When touching code again |
| 💡 Suggestion | Always merge  | At author's discretion   |

## OWASP Top 10 (2021) Checklist

| ID  | Name                      | Common Signals                                               |
| --- | ------------------------- | ------------------------------------------------------------ |
| A01 | Broken Access Control     | Missing auth middleware, IDOR, no ownership check            |
| A02 | Cryptographic Failures    | MD5 passwords, verify=False, hardcoded secrets               |
| A03 | Injection                 | SQL concat, eval(), shell=True, os.system()                  |
| A04 | Insecure Design           | No rate limiting on auth, no confirmation on destructive ops |
| A05 | Security Misconfiguration | DEBUG=True, CORS wildcard, stack traces to user              |
| A06 | Outdated Components       | Unpinned deps, known-CVE libraries                           |
| A07 | Auth Failures             | No lockout, JWT alg=none, session not invalidated on logout  |
| A08 | Integrity Failures        | pickle.loads(), yaml.load(), no SRI on CDN assets            |
| A09 | Logging Failures          | Silent except/catch, passwords in logs                       |
| A10 | SSRF                      | User-controlled URL passed to fetch/requests                 |

## Pattern Scanner (CI/CD)

```bash
# Scan a single file
python scripts/pattern_scanner.py src/api/handler.py

# Scan a directory
python scripts/pattern_scanner.py ./src --lang python

# Exit codes: 0=clean, 1=high findings, 2=critical findings
```

## Reference Files

- `references/OWASP_TOP10.json` — Full OWASP Top 10 with code signals, language examples, and mitigations
- `references/LANGUAGE_PATTERNS.json` — Dangerous patterns per language with safe alternatives
- `references/SEVERITY_MATRIX.json` — Scoring criteria and merge policies per severity level
- `scripts/pattern_scanner.py` — CLI tool for automated pre-check scanning
