# Git & GitHub Cheat Sheet

## What is Git?

Git is a version control system.

Think of it as:

```text
Save points for your code.
```

It allows you to:

* Track changes
* Restore previous versions
* Work on multiple features
* Collaborate with others

---

# Check Status

## Syntax

```bash
git status
```

## What it does

Shows:

* Modified files
* Deleted files
* New files
* Current branch

## Use Daily

When confused, run:

```bash
git status
```

first.

---

# Add Files

## Add Everything

```bash
git add .
```

## Add One File

```bash
git add filename.py
```

## What it does

Moves changes into the staging area.

---

# Commit Changes

## Syntax

```bash
git commit -m "Added pandas cheat sheet"
```

## What it does

Creates a snapshot of your work.

## Good Commit Messages

```text
Added SQL Day 3 practice

Completed ETH analysis

Fixed datetime parsing issue
```

---

# Push to GitHub

## Syntax

```bash
git push origin python-track
```

## What it does

Uploads commits to GitHub.

---

# Pull Latest Changes

## Syntax

```bash
git pull origin python-track
```

## What it does

Downloads latest changes.

---

# View Commit History

## Syntax

```bash
git log --oneline
```

## What it does

Shows commit history.

Example:

```text
a1b2c3 Added SQL Day 3
d4e5f6 Added Pandas project
```

---

# Branches

## View Branches

```bash
git branch
```

Example:

```text
main
python-track
sql-track
```

Current branch has:

```text
*
```

---

## Create New Branch

```bash
git checkout -b feature-branch
```

## What it does

Creates and switches to new branch.

---

## Switch Branch

```bash
git checkout python-track
```

---

# Restore File

## Syntax

```bash
git restore filename.py
```

## What it does

Discards local changes.

Use carefully.

---

# Remove File From Git Tracking

## Syntax

```bash
git rm --cached filename.csv
```

## What it does

Stops tracking a file without deleting it locally.

---

# Reset Last Commit

## Keep Changes

```bash
git reset --soft HEAD~1
```

## Remove Changes

```bash
git reset --hard HEAD~1
```

⚠️ Hard reset deletes work.

---

# Force Push

## Syntax

```bash
git push origin python-track --force
```

## What it does

Replaces remote history.

Use only when necessary.

---

# GitHub Large File Error

## Error

```text
GH001: Large files detected
```

## Cause

File larger than 100 MB.

Example:

```text
survey_results_public.csv
```

## Fix

Remove file:

```bash
git rm --cached data/survey_results_public.csv
```

Commit:

```bash
git commit -m "Removed large dataset"
```

Push again.

---

# Common Workflow

## Every Day

```bash
git status

git add .

git commit -m "Meaningful message"

git push origin python-track
```

---

# Repository Structure

Current Structure

```text
ai-engineer-journey/
│
├── 00_python_fundamentals/
├── 01_pandas_data_analysis/
├── 02_sql_basics/
├── 03_projects/
├── 04_ai_engineering/
└── docs/
```

---

# Common Problems

## Push Rejected

Cause:

Remote history conflict.

Fix:

```bash
git pull
```

or

```bash
git push --force
```

only if appropriate.

---

## File Deleted By Mistake

Check history:

```bash
git log --oneline
```

Restore file:

```bash
git checkout commit_id filename
```

---

## Wrong Branch

Check:

```bash
git branch
```

Switch:

```bash
git checkout branch-name
```

---

# Interview Questions

## What is Git?

Version control system that tracks code changes.

---

## Difference Between Git and GitHub

Git:

* Local version control

GitHub:

* Remote repository hosting

---

## What is a Commit?

A saved snapshot of code.

---

## What is a Branch?

An isolated line of development.

---

## What is Merge?

Combining changes from one branch into another.

---

## Most Important Commands

```bash
git status
git add .
git commit -m ""
git push
git pull
git branch
git checkout
git log --oneline
git restore
```
