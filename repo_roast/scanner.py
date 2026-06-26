from pathlib import Path


IGNORED_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
    "dist",
    "build",
}


def scan_repo(path: Path) -> dict:
    files = []

    for file_path in path.rglob("*"):
        if any(part in IGNORED_DIRS for part in file_path.parts):
            continue

        if file_path.is_file():
            try:
                text = file_path.read_text(errors="ignore")
                line_count = len(text.splitlines())
            except Exception:
                line_count = 0

            files.append(
                {
                    "path": str(file_path.relative_to(path)),
                    "name": file_path.name,
                    "suffix": file_path.suffix,
                    "lines": line_count,
                }
            )

    names = {file["name"] for file in files}
    paths = {file["path"] for file in files}

    return {
        "root": str(path),
        "files": files,
        "file_names": names,
        "file_paths": paths,
        "has_readme": "README.md" in names or "readme.md" in names,
        "has_license": "LICENSE" in names or "LICENSE.md" in names,
        "has_gitignore": ".gitignore" in names,
        "has_tests": any(
            p.startswith("tests/") or p.startswith("test/")
            for p in paths
        ),
        "has_env_example": ".env.example" in names,
        "largest_file": max(files, key=lambda f: f["lines"], default=None),
    }
