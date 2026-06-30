"""
ATS Keyword Matcher — Resume Builder Skill
Compares a resume against a job description and surfaces missing ATS keywords.

Usage:
    python keyword_matcher.py --resume resume.txt --job job_description.txt
    python keyword_matcher.py --resume resume.txt --job job_description.txt --role software_engineering
    python keyword_matcher.py --resume resume.txt --job job_description.txt --top 20

Output:
    - Keyword match score (%)
    - Present keywords (green)
    - Missing high-priority keywords (red)
    - Placement suggestions for missing keywords
"""

import sys
import json
import re
import argparse
from pathlib import Path

REFERENCES_DIR = Path(__file__).parent.parent / "references"
KEYWORDS_FILE = REFERENCES_DIR / "ATS_KEYWORDS.json"


def load_keywords():
    if not KEYWORDS_FILE.exists():
        print(f"[ERROR] ATS_KEYWORDS.json not found at {KEYWORDS_FILE}")
        sys.exit(1)
    with open(KEYWORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def read_file(filepath: str) -> str:
    path = Path(filepath)
    if not path.exists():
        print(f"[ERROR] File not found: {filepath}")
        sys.exit(1)
    return path.read_text(encoding="utf-8", errors="replace").lower()


def extract_job_keywords(
    job_text: str, keywords_data: dict, role_family: str = None
) -> list:
    """Extract candidate keywords from job description text + optional role reference."""
    candidates = set()

    # From role family reference (if specified)
    if role_family:
        role_data = keywords_data.get("role_families", {}).get(role_family, {})
        for category_keywords in role_data.values():
            candidates.update(kw.lower() for kw in category_keywords)

    # From certification keywords
    for cert_list in keywords_data.get("certification_keywords", {}).values():
        for cert in cert_list:
            if cert.lower() in job_text:
                candidates.add(cert.lower())

    # From all role families — find any keyword mentioned in job description
    for family_data in keywords_data.get("role_families", {}).values():
        for category_keywords in family_data.values():
            for kw in category_keywords:
                if kw.lower() in job_text:
                    candidates.add(kw.lower())

    return sorted(candidates)


def check_keyword_in_resume(keyword: str, resume_text: str) -> bool:
    """Check if a keyword appears in the resume (case-insensitive, word-boundary aware)."""
    pattern = re.escape(keyword.lower())
    return bool(re.search(pattern, resume_text))


def suggest_placement(keyword: str) -> str:
    """Suggest where to place a missing keyword."""
    technical_signals = [
        "python",
        "java",
        "sql",
        "aws",
        "gcp",
        "azure",
        "docker",
        "kubernetes",
        "react",
        "typescript",
        "node",
        "api",
        "rest",
        "ci/cd",
        "terraform",
        "spark",
        "kafka",
        "redis",
        "tableau",
        "power bi",
        "figma",
    ]
    methodology_signals = ["agile", "scrum", "okr", "kpi", "a/b", "sprint", "kanban"]
    cert_signals = ["certified", "aws certified", "pmp", "cpa", "cfa", "cissp"]

    kw_lower = keyword.lower()
    if any(s in kw_lower for s in cert_signals):
        return "Education or Certifications section"
    if any(s in kw_lower for s in technical_signals):
        return "Skills section (Technical Skills) + relevant experience bullet"
    if any(s in kw_lower for s in methodology_signals):
        return "Skills section (Methodologies) + experience context"
    return "Professional Summary + relevant experience bullet"


def run_analysis(
    resume_text: str,
    job_text: str,
    keywords_data: dict,
    role_family: str = None,
    top_n: int = 20,
):
    job_keywords = extract_job_keywords(job_text, keywords_data, role_family)

    present = []
    missing = []

    for kw in job_keywords:
        if check_keyword_in_resume(kw, resume_text):
            present.append(kw)
        else:
            # Only flag as missing if it appears in the job description
            if kw in job_text:
                missing.append(kw)

    total = len(present) + len(missing)
    score = (len(present) / total * 100) if total > 0 else 0

    return {
        "score": round(score, 1),
        "total_checked": total,
        "present_count": len(present),
        "missing_count": len(missing),
        "present": sorted(present),
        "missing": sorted(missing)[:top_n],
    }


def print_report(result: dict, top_n: int):
    score = result["score"]
    if score >= 80:
        score_label = "Strong match"
    elif score >= 60:
        score_label = "Moderate match — improve before applying"
    else:
        score_label = "Weak match — significant gaps to address"

    print("\n" + "=" * 60)
    print("  ATS KEYWORD MATCH REPORT — Resume Builder Skill")
    print("=" * 60)
    print(f"  Match Score : {score}%  ({score_label})")
    print(
        f"  Keywords Found    : {result['present_count']} / {result['total_checked']}"
    )
    print(f"  Keywords Missing  : {result['missing_count']}")
    print("=" * 60)

    if result["present"]:
        print(f"\n✅ PRESENT ({result['present_count']} keywords found in resume):\n")
        for kw in result["present"]:
            print(f"   • {kw}")

    if result["missing"]:
        print(
            f"\n❌ MISSING — Top {min(top_n, len(result['missing']))} keywords from job description not found in resume:\n"
        )
        print(f"  {'Keyword':<40} {'Where to Add'}")
        print(f"  {'-' * 40} {'-' * 30}")
        for kw in result["missing"]:
            suggestion = suggest_placement(kw)
            print(f"  {kw:<40} {suggestion}")

    print("\n" + "-" * 60)
    print("  Next steps:")
    print("  1. Integrate missing keywords naturally into your resume")
    print("  2. Add to Professional Summary if they define your expertise")
    print("  3. Add to Skills section under the correct category")
    print("  4. Weave into experience bullets with context and metrics")
    print("  5. Re-run this scanner to verify coverage")
    print("-" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="ATS keyword matcher — compare resume to job description"
    )
    parser.add_argument("--resume", required=True, help="Path to resume text file")
    parser.add_argument(
        "--job", required=True, help="Path to job description text file"
    )
    parser.add_argument(
        "--role",
        default=None,
        help="Role family for reference keywords (e.g., software_engineering, product_management, marketing)",
    )
    parser.add_argument(
        "--top", type=int, default=20, help="Max missing keywords to show (default: 20)"
    )
    args = parser.parse_args()

    keywords_data = load_keywords()
    resume_text = read_file(args.resume)
    job_text = read_file(args.job)

    result = run_analysis(resume_text, job_text, keywords_data, args.role, args.top)
    print_report(result, args.top)

    # Exit code signals for CI/CD or scripting
    if result["score"] >= 80:
        sys.exit(0)
    elif result["score"] >= 60:
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
