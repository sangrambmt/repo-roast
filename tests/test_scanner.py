from repo_roast.scanner import scan_repo


def test_scanner_detects_readme(tmp_path):
    repo = tmp_path
    (repo / "README.md").write_text("# Test Repo")
    (repo / "LICENSE").write_text("MIT")

    result = scan_repo(repo)

    assert result["has_readme"] is True
    assert result["has_license"] is True
