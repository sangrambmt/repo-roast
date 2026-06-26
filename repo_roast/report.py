def print_report(result: dict) -> None:
    print()
    print("🔥 Repo Roast")
    print("=" * 40)
    print(f"Score: {result['score']}/100")
    print(f"Grade: {result['grade']}")
    print()

    findings = result["findings"]

    if not findings:
        print("✅ Clean repo. Annoyingly competent. I found very little to complain about.")
        return

    for finding in findings:
        severity = finding["severity"].upper()
        category = finding["category"]
        roast = finding["roast"]

        print(f"🔥 [{severity}] {category}")
        print(f"   {roast}")
        print()
