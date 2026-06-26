# Repo Roast 🔥

A brutally honest Python CLI that roasts your repository like a senior engineer who has seen too much.

Repo Roast scans your project and points out common repository hygiene problems such as missing tests, weak documentation, missing license files, missing `.gitignore`, missing `.env.example`, huge files, and messy structure.

It is part code-quality tool and part comedy weapon.

---

## Why Repo Roast?

Most repositories do not need another dashboard.

They need someone to say:

> Your README explains the product but not how to run it. That is marketing, not documentation.

Repo Roast gives fast, blunt feedback before other developers silently judge your project and leave.

---

## Features ✨

- Checks if your repo has a README
- Detects weak README files
- Detects missing LICENSE files
- Detects missing `.gitignore`
- Detects missing tests
- Detects missing `.env.example`
- Finds very large files
- Detects cluttered repo roots
- Scores your repo out of 100
- Gives your repo a grade from A to F
- Prints funny but useful roast messages

---

## Installation 🚀

Clone the repository:

```bash
git clone https://github.com/sangrambmt/repo-roast.git
cd repo-roast
```

Install it locally:

```bash
pip install -e .
```

---

## Usage

Roast the current repository:

```bash
repo-roast .
```

Run it with Python:

```bash
python -m repo_roast .
```

Roast another repository:

```bash
repo-roast /path/to/your/project
```

Example:

```bash
repo-roast /Users/yourname/Documents/my-project
```

---

## Example Output 🔥

```txt
🔥 Repo Roast
========================================
Score: 75/100
Grade: B

🔥 [HIGH] tests
   No tests found. Production is not a testing framework.

🔥 [LOW] setup
   No .env.example found. Your setup instructions are probably hidden in your DMs.

🔥 [MEDIUM] docs
   Your README exists, but barely. A napkin has more onboarding value.
```

---

## What Repo Roast Checks

| Check | Why it matters |
|---|---|
| README | Developers need to understand what your project does and how to run it. |
| LICENSE | People need to know whether they can legally use your code. |
| `.gitignore` | Keeps cache files, virtual environments, and junk out of your repo. |
| Tests | Hope is not a testing strategy. |
| `.env.example` | Setup should not require guessing or private messages. |
| Huge files | Giant files are usually hard to maintain. |
| Root clutter | A messy root folder makes the project look abandoned. |

---

## Project Structure

```txt
repo-roast/
  README.md
  CONTRIBUTING.md
  LICENSE
  pyproject.toml
  repo_roast/
    __init__.py
    __main__.py
    cli.py
    scanner.py
    roast_engine.py
    report.py
    roasts/
      __init__.py
      lines.py
  tests/
    test_scanner.py
    test_roast_engine.py
```

---

## Development 🛠️

Run tests:

```bash
python -m pytest
```

Check Python syntax:

```bash
python -m py_compile repo_roast/*.py repo_roast/roasts/*.py
```

Run locally:

```bash
python -m repo_roast .
```

Install locally after changes:

```bash
pip install -e .
```

---

## Current Checks

Repo Roast currently checks for:

- Missing README
- Weak README
- Missing LICENSE
- Missing `.gitignore`
- Missing tests
- Missing `.env.example`
- Very large files
- Too many files in the repo root

This is the first version, so the rules are intentionally simple.

---

## Roadmap 🗺️

Planned improvements include:

- JSON output
- Markdown report output
- Better README analysis
- Dependency checks
- Secret detection
- Language-specific rules
- GitHub Actions support
- Config file support
- PyPI release
- Plugin system
- More roast lines
- Better scoring

---

## Contributing 🤝

Contributions are welcome.

Good contributions include:

- Adding funny roast lines
- Adding new repo checks
- Improving test coverage
- Improving CLI output
- Improving documentation
- Adding JSON or Markdown output
- Adding language-specific checks

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

---

## Good First Issue Ideas

Starter tasks:

- Add more roast messages
- Add `--version`
- Add JSON output
- Add Markdown output
- Improve README checks
- Add `.env` detection
- Add dependency file detection
- Add more tests
- Improve terminal formatting

---

## Philosophy

Repo Roast should stay:

- Fast
- Local-first
- Funny
- Useful
- Beginner-friendly
- Dependency-light
- Easy to run

Repo Roast should not become:

- A giant dashboard
- A cloud-only scanner
- A slow enterprise tool
- A dependency-heavy monster
- A boring linter clone

The best version of Repo Roast is simple:

```bash
repo-roast .
```

Then the user laughs, learns something, and fixes their repo.

---

## License

MIT License.

---

## Brutal Truth

This tool will not fix your repo.

It will just insult you until you do.
