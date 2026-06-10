# Mistakes and Fixes

This document contains real problems I encountered while learning Python, Pandas, SQL, and Git.

Format:

Problem → Cause → Fix → Lesson Learned

---

# Pandas

## Problem

```text
KeyError: 'Date'
```

### Cause

Date column was already converted into the DataFrame index.

Trying to access:

```python
df["Date"]
```

when Date no longer exists as a column.

### Fix

Check columns:

```python
df.columns
```

Check index:

```python
df.index
```

Bring Date back:

```python
df.reset_index()
```

### Lesson Learned

Always check:

```python
df.columns
df.index
```

before debugging.

---

## Problem

```text
Only valid with DatetimeIndex,
TimedeltaIndex or PeriodIndex
```

### Cause

Tried using:

```python
resample()
```

on a RangeIndex.

### Fix

Convert date:

```python
df["Date"] = pd.to_datetime(df["Date"])
```

Set index:

```python
df.set_index("Date", inplace=True)
```

### Lesson Learned

Resample requires a DatetimeIndex.

---

## Problem

```text
NameError: df is not defined
```

### Cause

Notebook restarted or previous cells were not executed.

### Fix

Reload dataset.

```python
df = pd.read_csv("file.csv")
```

Run previous cells.

### Lesson Learned

Always execute cells in order.

---

## Problem

```text
Unknown datetime string format
```

### Cause

Pandas could not automatically understand the date format.

Example:

```text
2020-03-13 08-PM
```

### Fix

Specify format manually.

```python
pd.to_datetime(
    df["Date"],
    format="%Y-%m-%d %I-%p"
)
```

### Lesson Learned

Check raw date values before converting.

---

## Problem

```text
No output from matplotlib chart
```

### Cause

Missing:

```python
plt.show()
```

or chart cell not executed.

### Fix

```python
plt.show()
```

### Lesson Learned

Always verify plot execution.

---

## Problem

```text
Same output for all joins
```

### Cause

Both tables contained matching IDs.

Example:

```python
1
2
3
```

in both tables.

### Fix

Add unmatched IDs.

Example:

```python
employees:
1 2 3

salaries:
2 3 4
```

Then test:

```python
inner
left
right
outer
```

### Lesson Learned

Join differences appear only when data differs.

---

# SQL

## Problem

```text
table employees already exists
```

### Cause

Tried running CREATE TABLE again.

### Fix

Drop table first.

```sql
DROP TABLE employees;
```

or use

```sql
DROP TABLE IF EXISTS employees;
```

### Lesson Learned

Check existing tables before creating.

---

## Problem

```text
No such column
```

### Cause

Wrong column name.

### Fix

Check schema.

```sql
PRAGMA table_info(employees);
```

### Lesson Learned

Verify column names first.

---

# Git & GitHub

## Problem

```text
GH001: Large files detected
```

### Cause

GitHub does not allow files larger than 100 MB.

Example:

```text
survey_results_public.csv
```

### Fix

Remove file from Git tracking.

```bash
git rm --cached filename.csv
```

Commit again.

Push again.

### Lesson Learned

Never commit large datasets.

Store only sample datasets.

---

## Problem

```text
Push rejected
```

### Cause

Remote repository rejected commit.

Possible reasons:

* Large file
* History mismatch

### Fix

Read error carefully.

Check:

```bash
git status
```

```bash
git log --oneline
```

Fix issue then push again.

### Lesson Learned

Git errors usually tell you exactly what is wrong.

Read them carefully.

---

## Problem

```text
docs/docs not found
```

### Cause

Already inside docs folder.

Tried:

```bash
git add docs
```

again.

### Fix

Check current location.

```bash
pwd
```

Use:

```bash
git add .
```

when already inside folder.

### Lesson Learned

Always check current directory before running commands.

---

# Personal Debugging Checklist

Whenever something breaks:

## Step 1

Read the error carefully.

---

## Step 2

Check object type.

```python
type(df)
```

---

## Step 3

Inspect dataset.

```python
df.head()
```

```python
df.info()
```

```python
df.columns
```

---

## Step 4

Check index.

```python
df.index
```

---

## Step 5

Google or document solution.

Add it to this file.

---

# Rule

If I solve a problem once:

Add it here.

Future me should never waste time solving the same problem twice.
