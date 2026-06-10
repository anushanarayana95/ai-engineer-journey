# Mistakes and Fixes

## Pandas

### KeyError: 'Date'

Cause:
Date column already became index.

Fix:

```python
df.index
```

or

```python
df.reset_index()
```

---

### Only valid with DatetimeIndex

Cause:
Using resample() on a RangeIndex.

Fix:

```python
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
```

---

### NameError: df is not defined

Cause:
Notebook restarted or cell not executed.

Fix:

Reload CSV and rerun previous cells.

---

### Unknown datetime string format

Cause:
Datetime format doesn't match data.

Fix:

```python
pd.to_datetime(
    df['Date'],
    format='%Y-%m-%d %I-%p'
)
```

---

## GitHub

### GH001 Large File Error

Cause:
File larger than 100 MB.

Fix:

```bash
git rm --cached filename
```

Then recommit and push.
