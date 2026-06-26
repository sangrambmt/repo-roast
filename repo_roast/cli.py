import argparse
from pathlib import Path

from repo_roast.scanner import scan_repo
from repo_roast.roast_engine import roast_repo
from repo_roast.report import print_report


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="repo-roast",
        description="Roast your repo like a brutally honest senior engineer.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repo you want roasted.",
    )

    args = parser.parse_args()
    repo_path = Path(args.path).resolve()

    facts = scan_repo(repo_path)
    result = roast_repo(facts)
    print_report(result)
