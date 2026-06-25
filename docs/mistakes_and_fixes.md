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

# SQL---------------------------------

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
# SQLite Mistakes

## Mistake 1

no such column: summary

Cause:

Database schema not updated

Fix:

ALTER TABLE news
ADD COLUMN summary TEXT

---

## Mistake 2

Using non-existent fields

Error:

IndexError

Cause:

Field not present in database

Fix:

Check schema using:

PRAGMA table_info(news);


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


# gemini api

# Gemini Integration Mistakes

## Mistake 1

Hardcoded API Key

Bad:

client = genai.Client(api_key="AQ...")

Good:

client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)

---

## Mistake 2

Committed API Key to GitHub

Result:

* Push Protection blocked push

Fix:

* Remove secret
* Create new key
* Use .env

---

## Mistake 3

Empty .env File

Problem:

API KEY: None

Cause:

.env file had 0 bytes

Fix:

GEMINI_API_KEY=your_key

---

## Mistake 4

Quota Exceeded

Error:

429 RESOURCE_EXHAUSTED

Cause:

Free tier limits reached

---

## Mistake 5

Model Unavailable

Error:

503 UNAVAILABLE

Cause:

Google servers under high load


# ----------Analytics-----------

# Analytics Endpoint Mistakes

## Problem

Analytics returned:

(None, 20)

## Cause

Category column existed but all values were NULL.

## Learning

Analytics is only useful when data enrichment is completed.

Always inspect database contents before building reports.


# Search API Learnings

## Learning

Search should happen in the database, not in Python.

Bad:
Fetch all rows then filter.

Good:
Use SQL WHERE clause.

Benefits:

* Faster
* Scalable
* Less memory usage


# Streamlit API Connection Mistakes

1. FastAPI server must be running before Streamlit calls APIs.

Error:
ConnectionError

Fix:
Run uvicorn api:app --reload

2. Variable must be defined before use.

Error:
NameError: search_response not defined

Fix:
Create search_response before calling .json()

3. Check API endpoint in Swagger before connecting Streamlit.
