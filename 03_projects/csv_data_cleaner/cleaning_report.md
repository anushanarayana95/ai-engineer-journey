# CSV Data Cleaning Report

## Dataset Summary

Original Dataset:

* Rows: 7
* Columns: 3

Cleaned Dataset:

* Rows: 6
* Columns: 3

---

## Issues Found

### 1. Duplicate Records

Duplicate Count:

1

Example:

```text
vishnu,mumbai,50000
vishnu,mumbai,50000
```

Action Taken:

Removed duplicate rows using:

```python
df.drop_duplicates()
```

---

### 2. Inconsistent Capitalization

Examples:

```text
ANU
john
```

Action Taken:

Standardized names using:

```python
str.title()
```

Result:

```text
Anu
John
```

---

### 3. Extra Whitespace

Example:

```text
 ravi
```

Action Taken:

Removed whitespace using:

```python
str.strip()
```

Result:

```text
Ravi
```

---

### 4. Missing Salary

Original Record:

```text
john,delhi,
```

Action Taken:

Filled missing salary using mean salary:

```python
fillna(
    df["salary"].mean()
)
```

Assigned Value:

```text
38000
```

---

## Final Validation

Missing Values:

```text
name      0
city      0
salary    0
```

Duplicate Records:

```text
0
```

---

## Skills Practiced

* read_csv()
* isna()
* fillna()
* duplicated()
* drop_duplicates()
* str.strip()
* str.title()
* to_csv()

---

## Key Learning

Raw datasets are rarely clean.

Before analysis, data must be:

* validated
* cleaned
* standardized
* checked for duplicates
* checked for missing values

Data cleaning is one of the most important tasks in Data Analytics, Data Science, and AI Engineering.
