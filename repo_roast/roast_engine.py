from repo_roast.roasts.lines import ROASTS


def roast_repo(facts: dict) -> dict:
    findings = []

    if not facts["has_readme"]:
        findings.append(make_finding("high", "docs", "no_readme"))
    else:
        readme = next(
            (f for f in facts["files"] if f["name"].lower() == "readme.md"),
            None,
        )
        if readme and readme["lines"] < 10:
            findings.append(make_finding("medium", "docs", "weak_readme"))

    if not facts["has_license"]:
        findings.append(make_finding("medium", "legal", "no_license"))

    if not facts["has_gitignore"]:
        findings.append(make_finding("medium", "git", "no_gitignore"))

    if not facts["has_tests"]:
        findings.append(make_finding("high", "tests", "no_tests"))

    if not facts["has_env_example"]:
        findings.append(make_finding("low", "setup", "no_env_example"))

    largest = facts.get("largest_file")
    if largest and largest["lines"] > 500:
        findings.append(
            make_finding(
                "high",
                "structure",
                "huge_file",
                path=largest["path"],
                lines=largest["lines"],
            )
        )

    root_file_count = sum(1 for f in facts["files"] if "/" not in f["path"])
    if root_file_count > 12:
        findings.append(
            make_finding(
                "medium",
                "structure",
                "too_many_root_files",
                count=root_file_count,
            )
        )

    score = max(0, 100 - sum(severity_penalty(f["severity"]) for f in findings))

    return {
        "score": score,
        "grade": grade(score),
        "findings": findings,
    }


def make_finding(severity: str, category: str, roast_key: str, **kwargs) -> dict:
    return {
        "severity": severity,
        "category": category,
        "roast": ROASTS[roast_key].format(**kwargs),
    }


def severity_penalty(severity: str) -> int:
    return {
        "low": 5,
        "medium": 10,
        "high": 20,
    }.get(severity, 5)


def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 40:
        return "D"
    return "F"
