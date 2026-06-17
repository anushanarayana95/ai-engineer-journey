# Project Checklist

Use this checklist before starting, during development, and before publishing any project.

---

# 1. Project Setup

## Before Starting

* [ ] Create project folder
* [ ] Create README.md
* [ ] Create main Python file
* [ ] Create data folder if needed
* [ ] Create output folder if needed
* [ ] Create requirements.txt (later when using external libraries)

Example:

```text
project_name/
│
├── README.md
├── main.py
├── data/
├── output/
└── notebooks/
```

---

# 2. Planning

Before coding answer:

### What problem am I solving?

Example:

```text
Analyze Ethereum price data.
```

### What skills am I practicing?

Example:

```text
Pandas
Visualization
Datetime
Data Cleaning
```

### What should the final output be?

Example:

```text
Charts
Insights
Summary Report
```

---

# 3. Development

During coding:

* [ ] Use meaningful variable names
* [ ] Use functions where possible
* [ ] Add comments for complex logic
* [ ] Test code frequently
* [ ] Save work regularly

Bad:

```python
a = 10
b = 20
```

Good:

```python
current_price = 10
average_price = 20
```

---

# 4. Data Validation

Before analysis:

* [ ] Check dataset shape
* [ ] Check column names
* [ ] Check data types
* [ ] Check missing values

Commands:

```python
df.head()
df.info()
df.shape
df.columns
df.isna().sum()
```

---

# 5. Debugging

If something breaks:

* [ ] Read error carefully
* [ ] Check dataframe columns
* [ ] Check dataframe index
* [ ] Verify data types
* [ ] Search notes in mistakes_and_fixes.md

Useful commands:

```python
df.head()
df.info()
df.columns
df.index
type(df)
```

---

# 6. Project Completion

Before finishing:

* [ ] Code runs without errors
* [ ] Output verified
* [ ] Charts display correctly
* [ ] Files organized
* [ ] Unused code removed

---

# 7. Documentation

README should contain:

## Project Name

Example:

```text
ETH Price Analysis
```

## Objective

What problem is being solved?

## Tools Used

Example:

```text
Python
Pandas
Matplotlib
```

## Key Learnings

Example:

```text
Datetime handling
Resampling
Rolling averages
```

## How To Run

Example:

```bash
python main.py
```

---

# 8. Git Checklist

Before commit:

* [ ] git status
* [ ] Remove unwanted files
* [ ] Check large datasets
* [ ] Verify project structure

Commands:

```bash
git status
git add .
git commit -m "Meaningful message"
git push origin python-track
```

---

# 9. Portfolio Checklist

Before publishing:

* [ ] README complete
* [ ] Project description added
* [ ] Insights written
* [ ] Screenshots included
* [ ] Code organized
* [ ] GitHub repo clean

---

# 10. Lessons Learned

After every project answer:

### What did I learn?

### What was difficult?

### What errors did I face?

### What would I improve next time?

Add important mistakes to:

```text
docs/mistakes_and_fixes.md
```

---

# Rule

A completed project is not just working code.

A completed project has:

* Working code
* Clean structure
* Documentation
* Git history
* Learnings recorded
