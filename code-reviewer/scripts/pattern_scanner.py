"""
Pattern Scanner — Code Reviewer Skill
Scans source code files for dangerous patterns defined in LANGUAGE_PATTERNS.json.
Use as a pre-check before AI review to surface obvious issues instantly.

Usage:
    python pattern_scanner.py <file_or_directory> [--lang python|javascript|sql|java|go]
    python pattern_scanner.py src/api/handler.py
    python pattern_scanner.py ./src --lang python
"""

import sys
import os
import json
import argparse
from pathlib import Path

REFERENCES_DIR = Path(__file__).parent.parent / "references"
PATTERNS_FILE = REFERENCES_DIR / "LANGUAGE_PATTERNS.json"

EXTENSION_TO_LANG = {
    ".py": "python",
    ".js": "javascript_typescript",
    ".ts": "javascript_typescript",
    ".jsx": "javascript_typescript",
    ".tsx": "javascript_typescript",
    ".java": "java",
    ".go": "go",
    ".sql": "sql",
}

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2}
SEVERITY_BADGES = {"critical": "🔴 CRITICAL", "high": "🟠 HIGH", "medium": "🟡 MEDIUM"}


def load_patterns():
    if not PATTERNS_FILE.exists():
        print(f"[ERROR] LANGUAGE_PATTERNS.json not found at {PATTERNS_FILE}")
        sys.exit(1)
    with open(PATTERNS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def detect_language(filepath: Path, override: str = None) -> str:
    if override:
        return override
    return EXTENSION_TO_LANG.get(filepath.suffix.lower(), None)


def scan_file(filepath: Path, patterns_data: dict, lang_override: str = None):
    lang = detect_language(filepath, lang_override)
    if lang is None:
        return []

    lang_patterns = patterns_data.get("languages", {}).get(lang, {})
    general_patterns = patterns_data.get("general_patterns", {})

    findings = []

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except OSError as e:
        print(f"[WARN] Cannot read {filepath}: {e}")
        return []

    # Scan language-specific patterns
    for severity in ("critical", "high", "medium"):
        for entry in lang_patterns.get(severity, []):
            pattern = entry.get("pattern", "")
            if not pattern:
                continue
            for line_num, line in enumerate(lines, start=1):
                if pattern in line:
                    findings.append(
                        {
                            "severity": severity,
                            "file": str(filepath),
                            "line": line_num,
                            "line_content": line.rstrip(),
                            "pattern": pattern,
                            "description": entry.get("description", ""),
                            "safe_alternative": entry.get("safe_alternative", ""),
                        }
                    )

    # Scan general patterns (hardcoded secrets, etc.)
    for key, entry in general_patterns.items():
        severity = entry.get("severity", "high").lower()
        for pattern in entry.get("patterns", []):
            for line_num, line in enumerate(lines, start=1):
                if (
                    pattern in line
                    and not line.strip().startswith("#")
                    and not line.strip().startswith("//")
                ):
                    findings.append(
                        {
                            "severity": severity,
                            "file": str(filepath),
                            "line": line_num,
                            "line_content": line.rstrip(),
                            "pattern": pattern,
                            "description": entry.get("description", ""),
                            "safe_alternative": entry.get("safe_alternative", ""),
                        }
                    )

    return findings


def collect_files(target: Path, lang_override: str = None) -> list:
    if target.is_file():
        return [target]
    files = []
    for ext in EXTENSION_TO_LANG:
        files.extend(target.rglob(f"*{ext}"))
    return sorted(files)


def print_report(all_findings: list, scanned_count: int):
    print("\n" + "=" * 60)
    print("  CODE PATTERN SCANNER — SECURITY PRE-CHECK")
    print("=" * 60)
    print(f"  Files scanned: {scanned_count}")
    print(f"  Total findings: {len(all_findings)}")

    counts = {
        s: sum(1 for f in all_findings if f["severity"] == s)
        for s in ("critical", "high", "medium")
    }
    print(
        f"  🔴 Critical: {counts['critical']}  🟠 High: {counts['high']}  🟡 Medium: {counts['medium']}"
    )
    print("=" * 60)

    if not all_findings:
        print("\n  ✅ No known dangerous patterns found.\n")
        print("  Note: This scanner checks for common patterns only.")
        print("  Use the full AI code-reviewer skill for a comprehensive review.\n")
        return

    # Sort by severity then file then line
    sorted_findings = sorted(
        all_findings,
        key=lambda x: (SEVERITY_ORDER.get(x["severity"], 9), x["file"], x["line"]),
    )

    for f in sorted_findings:
        badge = SEVERITY_BADGES.get(f["severity"], f["severity"].upper())
        print(f"\n{badge}")
        print(f"  File : {f['file']} — Line {f['line']}")
        print(f"  Match: {f['pattern']}")
        print(f"  Code : {f['line_content'].strip()}")
        print(f"  Issue: {f['description']}")
        if f["safe_alternative"]:
            print(f"  Fix  : {f['safe_alternative']}")

    print("\n" + "-" * 60)
    print("  Run the full AI code-reviewer skill for severity ratings,")
    print("  correctness, performance, and maintainability analysis.")
    print("-" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Scan source code for dangerous patterns (security pre-check)."
    )
    parser.add_argument("target", help="File or directory to scan")
    parser.add_argument(
        "--lang",
        help="Override language detection (python, javascript_typescript, java, go, sql)",
        default=None,
    )
    args = parser.parse_args()

    target = Path(args.target)
    if not target.exists():
        print(f"[ERROR] Target not found: {target}")
        sys.exit(1)

    patterns_data = load_patterns()
    files = collect_files(target, args.lang)

    all_findings = []
    for filepath in files:
        findings = scan_file(filepath, patterns_data, args.lang)
        all_findings.extend(findings)

    print_report(all_findings, scanned_count=len(files))

    # Exit with non-zero code if critical findings exist (useful in CI/CD)
    if any(f["severity"] == "critical" for f in all_findings):
        sys.exit(2)
    elif any(f["severity"] == "high" for f in all_findings):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
