# Day 34 - Pandas String Operations

## Topics Covered

* str.strip()
* str.lower()
* str.upper()
* str.title()
* str.contains()
* str.replace()
* fillna()

## Learning Objectives

Learn how to clean and transform text data using Pandas string methods. These operations are commonly used in data cleaning, preprocessing, and AI applications.

## Exercises Completed

### Exercise 1

Created a DataFrame with names and emails.

### Exercise 2

Removed extra spaces using:

```python
df["name"] = df["name"].str.strip()
```

### Exercise 3

Converted text to lowercase using:

```python
df["name"] = df["name"].str.lower()
```

### Exercise 4

Converted text to title case using:

```python
df["name"] = df["name"].str.title()
```

### Exercise 5

Converted email addresses to lowercase.

### Exercise 6

Checked if emails contain "gmail":

```python
df["email"].str.contains("gmail")
```

### Exercise 7

Replaced email domains:

```python
df["email"] = df["email"].str.replace(
    "gmail.com",
    "company.com"
)
```

## Challenge

### Input

```python
data = {
    "name": ["  ravi  ", " ANU ", "john", None]
}
```

### Tasks

1. Remove spaces
2. Convert names to title case
3. Replace missing values with "Unknown"

### Expected Output

```text
Ravi
Anu
John
Unknown
```

## Key Takeaways

* String operations are essential for cleaning messy data.
* Pandas provides powerful `.str` methods for text processing.
* Missing values should be handled before analysis.
* Text preprocessing is a common step in AI and machine learning workflows.


