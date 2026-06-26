from repo_roast.roast_engine import roast_repo


def test_repo_without_tests_gets_roasted():
    facts = {
        "has_readme": True,
        "has_license": True,
        "has_gitignore": True,
        "has_tests": False,
        "has_env_example": True,
        "files": [
            {"name": "README.md", "path": "README.md", "lines": 20},
        ],
        "largest_file": {"path": "app.py", "lines": 100},
    }

    result = roast_repo(facts)

    assert result["score"] < 100
    assert any(f["category"] == "tests" for f in result["findings"])
