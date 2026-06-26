# Contributing to Repo Roast 🔥

Thanks for checking out Repo Roast.

Repo Roast is a brutally honest Python CLI that scans repositories and gives useful, funny feedback about repo quality.

The goal is simple:

> Help developers improve their repos before other developers silently judge them.

Repo Roast should stay:

- Fast
- Local-first
- Funny
- Useful
- Beginner-friendly
- Dependency-light
- Easy to run

---

## What Repo Roast Does

Repo Roast scans a project and checks for common repo hygiene problems.

Current checks include:

- Missing `README.md`
- Weak README files
- Missing `LICENSE`
- Missing `.gitignore`
- Missing tests
- Missing `.env.example`
- Very large files
- Messy repo root
- Repo score
- Repo grade
- Funny terminal roast messages

Example:

```bash
repo-roast .
```

Example output:

```txt
🔥 Repo Roast
========================================
Score: 75/100
Grade: B

🔥 [HIGH] tests
   No tests found. Production is not a testing framework.

🔥 [LOW] setup
   No .env.example found. Your setup instructions are probably hidden in your DMs.
```

---

## Project Philosophy

Repo Roast is not trying to be a huge security scanner, AI reviewer, dashboard, or full linter.

It is a simple repo hygiene tool with personality.

Good contributions should be:

- Easy to understand
- Useful in under 10 seconds
- Funny enough to share
- Simple enough to maintain
- Safe to run locally
- Helpful for open-source maintainers

Bad contributions are:

- Too complex
- Cloud-dependent
- Slow
- Boring
- Full of unnecessary dependencies
- Hard for beginners to understand

---

## Local Setup

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/repo-roast.git
cd repo-roast
```

Install locally:

```bash
pip install -e .
```

Run Repo Roast:

```bash
repo-roast .
```

Or:

```bash
python -m repo_roast .
```

Run tests:

```bash
python -m pytest
```

Check Python syntax:

```bash
python -m py_compile repo_roast/*.py repo_roast/roasts/*.py
```

---

## Current Project Structure

```txt
repo-roast/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── repo_roast/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── scanner.py
│   ├── roast_engine.py
│   ├── report.py
│   └── roasts/
│       ├── __init__.py
│       └── lines.py
└── tests/
    ├── test_scanner.py
    └── test_roast_engine.py
```

---

## How The Code Works

### `repo_roast/cli.py`

Handles the command-line interface.

This is where arguments like this should be added:

```bash
repo-roast . --json
repo-roast . --strict
repo-roast . --version
```

Keep this file focused on CLI input and output.

---

### `repo_roast/scanner.py`

Scans the target repository and collects facts.

Example facts:

```python
{
    "has_readme": True,
    "has_license": False,
    "has_tests": False,
    "largest_file": {
        "path": "src/app.py",
        "lines": 900
    }
}
```

The scanner should not roast anything.  
It should only collect information.

---

### `repo_roast/roast_engine.py`

Turns scanned facts into findings.

Example finding:

```python
{
    "severity": "high",
    "category": "tests",
    "roast": "No tests found. Production is not a testing framework."
}
```

This is where scoring and grading happen.

---

### `repo_roast/report.py`

Prints the final result.

Future output formats like JSON and Markdown should be added here.

---

### `repo_roast/roasts/lines.py`

Stores roast messages.

This file gives Repo Roast its personality.

Good roast:

```txt
No tests found. Production is not a testing framework.
```

Bad roast:

```txt
Only an idiot would write this.
```

Roast the repo, not the person.

---

## Contribution Rules

Repo Roast should be funny, but not cruel.

Allowed:

- Jokes about code
- Jokes about repo structure
- Jokes about missing docs
- Jokes about technical decisions

Not allowed:

- Personal insults
- Slurs
- Harassment
- Attacks on identity
- NSFW content
- Roasts aimed at the developer instead of the repo

---

## Good First Issues

These are beginner-friendly contributions.

### Add More Roast Lines

File:

```txt
repo_roast/roasts/lines.py
```

Acceptance criteria:

- Add at least 5 new roast messages
- Keep them funny but safe
- Do not use slurs or personal attacks
- Tests should still pass

---

### Improve README Checks

Add better detection for README sections.

Checks to add:

- Installation section
- Usage section
- Example command
- License section
- Contributing section

Possible roast:

```txt
Your README has a title and confidence. Sadly, neither installs the project.
```

---

### Add `.env` Detection

Repo Roast should warn when a real `.env` file is committed.

Rules:

- `.env` should trigger a warning
- `.env.example` should be allowed
- Never print secret values

Possible roast:

```txt
You committed a .env file. Security teams call this job security.
```

---

### Add `--version`

Add:

```bash
repo-roast --version
```

Acceptance criteria:

- Shows the current version
- Does not scan a repo
- Tests still pass

---

### Add JSON Output

Add:

```bash
repo-roast . --json
```

Acceptance criteria:

- Output valid JSON
- Include score, grade, and findings
- Do not print normal roast text in JSON mode

Example:

```json
{
  "score": 75,
  "grade": "B",
  "findings": [
    {
      "severity": "high",
      "category": "tests",
      "roast": "No tests found. Production is not a testing framework."
    }
  ]
}
```

---

### Add Markdown Output

Add:

```bash
repo-roast . --markdown
```

Acceptance criteria:

- Output valid Markdown
- Include score, grade, and findings
- Can be redirected to a file

Example:

```bash
repo-roast . --markdown > ROAST_REPORT.md
```

---

## Roadmap

### v0.1.x — Stabilize Current CLI

- [ ] Add more tests
- [ ] Improve error handling
- [ ] Add more roast messages
- [ ] Improve README docs
- [ ] Add example output
- [ ] Make sure invalid paths do not crash badly

---

### v0.2.0 — Better CLI Options

Planned commands:

```bash
repo-roast .
repo-roast . --version
repo-roast . --quiet
repo-roast . --no-roast
repo-roast . --strict
repo-roast . --fail-under 70
```

Tasks:

- [ ] Add `--version`
- [ ] Add `--quiet`
- [ ] Add `--no-roast`
- [ ] Add `--strict`
- [ ] Add `--fail-under`
- [ ] Add cleaner terminal formatting

---

### v0.3.0 — Better README Analysis

Checks to add:

- [ ] Project title
- [ ] Description
- [ ] Installation
- [ ] Usage
- [ ] Example output
- [ ] Screenshots
- [ ] Contributing section
- [ ] License section
- [ ] Badges

Possible roast:

```txt
This README says what the project is, but not how to run it. That is a trailer, not documentation.
```

---

### v0.4.0 — Dependency Checks

Detect dependency files:

Python:

- [ ] `requirements.txt`
- [ ] `pyproject.toml`
- [ ] `Pipfile`
- [ ] `poetry.lock`
- [ ] `uv.lock`

JavaScript / TypeScript:

- [ ] `package.json`
- [ ] `package-lock.json`
- [ ] `pnpm-lock.yaml`
- [ ] `yarn.lock`
- [ ] `bun.lockb`

Checks:

- [ ] Missing lockfile
- [ ] Multiple lockfiles
- [ ] Multiple package managers
- [ ] Empty dependency file
- [ ] Too many dependencies
- [ ] Missing test script
- [ ] Missing lint script

Possible roast:

```txt
You have three lockfiles. Your package manager situation needs couples therapy.
```

---

### v0.5.0 — Secret and Unsafe File Detection

Files to flag:

- [ ] `.env`
- [ ] `.pem`
- [ ] `.key`
- [ ] `id_rsa`
- [ ] `credentials.json`
- [ ] `secrets.json`

Important:

Repo Roast should never print full secrets.

It should only show the file path and a safe warning.

---

### v0.6.0 — Language-Specific Rules

Python:

- [ ] Missing `pyproject.toml`
- [ ] Missing tests
- [ ] Giant scripts
- [ ] Missing formatter config
- [ ] Missing lint config

JavaScript / TypeScript:

- [ ] Missing `package.json`
- [ ] Missing test script
- [ ] Missing build script
- [ ] Missing TypeScript config
- [ ] Multiple package managers

iOS / Swift:

- [ ] Missing setup instructions
- [ ] Missing screenshots
- [ ] Missing test target
- [ ] Large Swift files
- [ ] Missing architecture explanation

Possible roast:

```txt
This Swift file is longer than the App Store review guidelines.
```

---

### v0.7.0 — JSON and Markdown Reports

Commands:

```bash
repo-roast . --json
repo-roast . --markdown
repo-roast . --markdown > ROAST_REPORT.md
```

Tasks:

- [ ] Add JSON output
- [ ] Add Markdown output
- [ ] Add tests for both output modes
- [ ] Make output useful for CI

---

### v0.8.0 — Config File Support

Supported config files:

- [ ] `.repo-roast.toml`
- [ ] `repo-roast.toml`
- [ ] `[tool.repo-roast]` inside `pyproject.toml`

Example:

```toml
[repo_roast]
max_file_lines = 500
strict = true
tone = "brutal"
ignore = [
  "vendor",
  "dist",
  "build",
  "docs/generated"
]
```

---

### v0.9.0 — GitHub Actions Support

Command:

```bash
repo-roast . --fail-under 70
```

Example workflow:

```yaml
name: Repo Roast

on:
  pull_request:
  push:

jobs:
  roast:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install Repo Roast
        run: pip install repo-roast

      - name: Roast repository
        run: repo-roast . --fail-under 70
```

---

### v1.0.0 — Stable Public Release

Before v1, Repo Roast should have:

- [ ] Stable CLI
- [ ] Good test coverage
- [ ] JSON output
- [ ] Markdown output
- [ ] Config support
- [ ] GitHub Actions support
- [ ] PyPI release
- [ ] Good README
- [ ] Good contributing guide
- [ ] Good issue templates

---

## Future Ideas

These should come after the core is stable.

### Plugin System

Allow users to add custom rules.

### Interactive Mode

```bash
repo-roast . --interactive
```

Possible features:

- Choose rules
- Show one roast at a time
- Suggest fixes
- Generate missing files

### Auto-Fix Suggestions

Possible commands:

```bash
repo-roast . --suggest-fixes
repo-roast . --write-gitignore
repo-roast . --write-env-example
```

Rule:

> Roast first. Auto-fix carefully.

### Tone Modes

Possible commands:

```bash
repo-roast . --tone brutal
repo-roast . --tone polite
repo-roast . --tone founder
repo-roast . --tone senior
```

Examples:

```txt
Brutal: Your repo structure looks like it was assembled during a fire drill.
Polite: Your repo structure could be easier to navigate.
Founder: This repo has MVP energy. Unfortunately, so does the documentation.
Senior: Please split this file before it becomes a department.
```

---

## Suggested Future Structure

As Repo Roast grows, the structure can become:

```txt
repo-roast/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
├── repo_roast/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── scanner.py
│   ├── roast_engine.py
│   ├── report.py
│   ├── config.py
│   ├── scoring.py
│   ├── models.py
│   ├── rules/
│   │   ├── __init__.py
│   │   ├── readme_rules.py
│   │   ├── structure_rules.py
│   │   ├── dependency_rules.py
│   │   ├── secret_rules.py
│   │   ├── python_rules.py
│   │   ├── javascript_rules.py
│   │   └── ios_rules.py
│   └── roasts/
│       ├── __init__.py
│       └── lines.py
└── tests/
    ├── test_scanner.py
    ├── test_roast_engine.py
    ├── test_report.py
    ├── test_config.py
    └── fixtures/
        ├── good_repo/
        ├── bad_repo/
        ├── python_repo/
        ├── node_repo/
        └── ios_repo/
```

Do not add this structure too early.

Add files only when the code actually needs them.

---

## Pull Request Checklist

Before opening a PR:

- [ ] Code is simple
- [ ] Tests pass
- [ ] New behavior has tests
- [ ] README updated if needed
- [ ] CONTRIBUTING updated if needed
- [ ] No unnecessary dependencies added
- [ ] Output is useful
- [ ] Roast messages are funny but safe

Run this before submitting:

```bash
python -m pytest
python -m py_compile repo_roast/*.py repo_roast/roasts/*.py
python -m repo_roast .
```

---

## Recommended GitHub Labels

| Label | Meaning |
|---|---|
| `good first issue` | Easy beginner task |
| `help wanted` | Open for contributors |
| `bug` | Something broken |
| `docs` | Documentation work |
| `feature` | New feature |
| `tests` | Test-related work |
| `roast-lines` | New funny messages |
| `cli` | Command-line interface |
| `rules` | Repo scanning rules |
| `security` | Secret or unsafe file checks |
| `python` | Python-specific support |
| `javascript` | JavaScript or TypeScript support |
| `ios` | iOS or Swift support |

---

## Maintainer Notes

Keep the project small.

Do not add these too early:

- Web dashboard
- User accounts
- Cloud scanning
- Required AI features
- Database
- Heavy dependencies
- Complex plugin system

Repo Roast should feel like this:

```bash
pip install repo-roast
repo-roast .
```

Then the user laughs, learns something, and fixes their repo.

---

## Final Vision

Repo Roast should become the command developers run before publishing a project:

```bash
repo-roast .
```

Like a linter for repo hygiene, but with personality.

The dream:

> Before someone stars your repo, Repo Roast makes sure it deserves the star.
