---
name: code-reviewer
description: "Use this skill when the user pastes code and wants a structured review covering correctness, security (OWASP Top 10), performance, maintainability, and best practices. Returns severity-rated findings with specific fixes and a scorecard."
tags:
  [code-review, security, performance, best-practices, owasp, software-quality]
argument-hint: "Paste the code to review and optionally specify language, context, or focus area (e.g., 'focus on security', 'this is a REST API handler')"
user-invocable: true
disable-model-invocation: false
---

# Code Reviewer

Perform a thorough, structured code review covering correctness, security, performance, maintainability, and idiomatic style. Returns prioritized, actionable findings with specific fixes — not generic advice.

## When to Use

- User pastes code and asks "review this", "what's wrong with this code", "is this secure"
- Pre-pull-request review before merging
- Security audit of a specific function, module, or API endpoint
- Learning mode: user wants to understand _why_ certain patterns are problematic
- Performance profiling: user wants to know what's slow or wasteful

## Inputs

- **Required:** The code to review (any language)
- **Optional via `$ARGUMENTS`:**
  - Language or framework context (e.g., "Python FastAPI", "React 18")
  - Review focus (e.g., "security only", "performance", "full review")
  - Deployment context (e.g., "public API", "internal script", "production database query")
  - Coding standards to apply (e.g., "PEP 8", "Airbnb ESLint", "Google Java Style")

## Process

### Step 1: Identify Language, Framework, and Context

- Detect the programming language and framework from the code
- Identify the apparent purpose (API handler, utility function, database query, UI component, etc.)
- Note any deployment signals (environment variables, auth headers, SQL queries, file I/O, network calls)
- If context is ambiguous and it significantly affects the review, ask one clarifying question

### Step 2: Security Review (OWASP Top 10 + Language-Specific CVEs)

Check for all applicable OWASP Top 10 vulnerabilities:

1. **Injection** — SQL injection, command injection, LDAP injection, template injection
2. **Broken Authentication** — Hardcoded credentials, weak tokens, missing auth checks
3. **Sensitive Data Exposure** — Secrets in code, unencrypted data at rest/in transit, PII leakage
4. **XML External Entities (XXE)** — Unsafe XML parsing
5. **Broken Access Control** — Missing authorization checks, insecure direct object references
6. **Security Misconfiguration** — Debug modes, default credentials, permissive CORS, verbose errors
7. **Cross-Site Scripting (XSS)** — Unsanitized user input in HTML/JS context
8. **Insecure Deserialization** — Untrusted data passed to deserialization functions
9. **Using Components with Known Vulnerabilities** — Outdated or flagged library usage
10. **Insufficient Logging & Monitoring** — Missing audit trails for sensitive operations

Also check language-specific risks:

- Python: `eval()`, `exec()`, `pickle`, shell=True in subprocess
- JavaScript/TypeScript: `innerHTML`, `dangerouslySetInnerHTML`, prototype pollution, `eval()`
- SQL: raw query construction, missing parameterization
- Go: unsafe pointer use, goroutine leaks
- Java: deserialization, XXE, path traversal

### Step 3: Correctness Review

- Logic errors, off-by-one bugs, incorrect conditionals
- Null/nil/undefined reference risks
- Error handling: are all error paths handled? Are errors swallowed silently?
- Edge cases: empty inputs, zero values, very large inputs, concurrent access
- Return value misuse (ignored errors, unchecked results)
- Race conditions and thread safety issues

### Step 4: Performance Review

- Unnecessary loops, nested iterations with better alternatives (O(n²) → O(n log n))
- N+1 query problems in database access patterns
- Missing indexes implied by query patterns
- Unnecessary memory allocations or copies in hot paths
- Blocking I/O in async contexts
- Missing pagination on potentially large result sets
- Unnecessary re-computation (missing memoization or caching)

### Step 5: Maintainability & Code Quality Review

- Function/method length (>40 lines is a signal to decompose)
- Cyclomatic complexity (deeply nested conditionals)
- Magic numbers and hardcoded strings that should be constants
- Variable and function naming clarity
- Dead code, commented-out code, unused imports
- Duplication that should be extracted into a shared utility
- Missing or misleading comments on complex logic

### Step 6: Idiomatic Style & Best Practices

- Language-specific idioms (list comprehensions in Python, optional chaining in JS, etc.)
- Framework conventions (REST verb semantics, React hooks rules, Django ORM patterns, etc.)
- Dependency injection vs. tight coupling
- Separation of concerns (mixing I/O with business logic, etc.)
- Test coverage signals (is this code testable as-written?)

### Step 7: Generate Scorecard and Prioritized Findings

Rate each finding by severity:

- 🔴 **Critical** — Security vulnerability or data-loss risk; must fix before merge
- 🟠 **High** — Likely bug or serious performance issue; fix before merge
- 🟡 **Medium** — Code quality or maintainability issue; fix in near-term
- 🟢 **Low** — Style suggestion or minor improvement; fix when convenient
- 💡 **Suggestion** — Non-blocking improvement or alternative approach

## Decision Rules

- Always show the exact line or block being flagged, not just a description
- Always provide a specific corrected version, not just "fix the injection vulnerability"
- If no issues are found in a category, state "No issues found" — do not invent findings
- If the code is a snippet without full context, note assumptions made
- Cap findings at 15 total — prioritize Critical and High; group similar Low/Suggestion items
- Do not rewrite the entire codebase — only change what has a finding

## Quality Criteria (Completion Checks)

Every response must include:

- ✅ Scorecard with counts per severity level
- ✅ Security section (or explicit "No security issues found")
- ✅ Each finding: severity badge, location, description, corrected code block
- ✅ Summary of overall code quality in 2–3 sentences
- ✅ Top 3 priority actions if Critical/High findings exist

## Output Template

---

### Code Review Scorecard

| Severity      | Count |
| ------------- | ----- |
| 🔴 Critical   | 0     |
| 🟠 High       | 0     |
| 🟡 Medium     | 0     |
| 🟢 Low        | 0     |
| 💡 Suggestion | 0     |

**Overall assessment:** [1–2 sentence summary of code quality]

---

### Findings

#### 🔴 [Finding Title] — Line [N]

**Category:** Security / Correctness / Performance / Maintainability / Style

**Problem:**  
[Clear description of what is wrong and why it matters]

**Current code:**

```[language]
[problematic snippet]
```

**Fixed code:**

```[language]
[corrected snippet]
```

---

### Top Priority Actions

1. [Most critical fix with one-line rationale]
2. [Second priority]
3. [Third priority]

---

## Supporting References

This skill includes data-driven reference files for authority and consistency:

- **OWASP_TOP10.json** — Full OWASP Top 10 2021 with code signals, language-specific patterns, CWE mappings, and mitigations per vulnerability. Located in `references/`.
- **LANGUAGE_PATTERNS.json** — Dangerous code patterns per language (Python, JavaScript/TypeScript, SQL, Go, Java) with severity level and safe alternative for each. Located in `references/`.
- **SEVERITY_MATRIX.json** — Scoring criteria, merge policies, and real-world examples for each severity level (Critical → Suggestion). Located in `references/`.
- **pattern_scanner.py** — CLI pre-check tool that scans source files for known dangerous patterns. Returns exit code 2 for critical findings (useful in CI/CD). Located in `scripts/`.

The AI cites OWASP_TOP10.json and LANGUAGE_PATTERNS.json when identifying security issues and uses SEVERITY_MATRIX.json to rate every finding consistently.

---

## Example Invocations

- `"Review this Python function for security issues"`
- `"Is this SQL query safe from injection?"`
- `"Full code review — this is a public REST API endpoint"`
- `"Check this for performance problems, it's running slow"`
- `"Review my React component for best practices"`
