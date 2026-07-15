# Pandas Cheat Sheet

## Import Pandas

### Syntax

```python
import pandas as pd
```

### What it does

Loads the Pandas library.

### Real Project Usage

Used in almost every data analysis and AI project.

---

## Read CSV

### Syntax

```python
df = pd.read_csv("employees.csv")
```

### What it does

Loads CSV data into a DataFrame.

### Think Of It As

Excel spreadsheet inside Python.

---

## View Data

### Head

```python
df.head()
```

Shows first 5 rows.

### Tail

```python
df.tail()
```

Shows last 5 rows.

### Info

```python
df.info()
```

Shows:

* Columns
* Data types
* Missing values

### Shape

```python
df.shape
```

Output:

```python
(rows, columns)
```

### Columns

```python
df.columns
```

Lists column names.

---

## Select Data

### Single Column

```python
df["salary"]
```

### Multiple Columns

```python
df[["name","salary"]]
```

---

## Filter Data

### Syntax

```python
df[df["salary"] > 50000]
```

### What it does

Returns rows matching a condition.

### SQL Equivalent

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

---

## Multiple Conditions

```python
df[
    (df["salary"] > 50000)
    &
    (df["city"] == "Hyderabad")
]
```

### Operators

```python
&
|
```

AND and OR

---

## Sorting

### Ascending

```python
df.sort_values("salary")
```

### Descending

```python
df.sort_values(
    "salary",
    ascending=False
)
```

---

## Create New Column

### Syntax

```python
df["bonus"] = df["salary"] * 0.10
```

### Use

Feature engineering.

---

## Update Column

```python
df["salary"] = df["salary"] + 5000
```

---

## Missing Values

### Check Missing Values

```python
df.isna().sum()
```

### Fill Missing Values

```python
df.fillna(0)
```

### Remove Missing Values

```python
df.dropna()
```

---

## String Operations

### Convert To Uppercase

```python
df["name"].str.upper()
```

### Lowercase

```python
df["name"].str.lower()
```

### Contains

```python
df["name"].str.contains("an")
```

### Replace

```python
df["name"].str.replace("Anu","Anusha")
```

---

## GroupBy

### Average Salary By City

```python
df.groupby(
    "city"
)["salary"].mean()
```

### Sum

```python
df.groupby(
    "city"
)["salary"].sum()
```

### Count

```python
df.groupby(
    "city"
)["salary"].count()
```

### Real Project Usage

Business reporting.

---

## Aggregations

### Max

```python
df["salary"].max()
```

### Min

```python
df["salary"].min()
```

### Mean

```python
df["salary"].mean()
```

### Sum

```python
df["salary"].sum()
```

### Describe

```python
df.describe()
```

### What it does

Generates summary statistics.

---

# Datetime

## Convert To Datetime

### Syntax

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

### Why

Required for time-series analysis.

---

## Extract Date Parts

### Year

```python
df["Date"].dt.year
```

### Month

```python
df["Date"].dt.month
```

### Day Name

```python
df["Date"].dt.day_name()
```

### Hour

```python
df["Date"].dt.hour
```

---

## Set Datetime Index

### Syntax

```python
df.set_index(
    "Date",
    inplace=True
)
```

### Why

Needed for resampling.

---

## Check Index Type

```python
type(df.index)
```

Expected:

```python
DatetimeIndex
```

---

# Resampling

## Daily Average

```python
df["Close"].resample(
    "D"
).mean()
```

## Weekly Average

```python
df["Close"].resample(
    "W"
).mean()
```

## Monthly Average

```python
df["Close"].resample(
    "M"
).mean()
```

### Common Codes

```python
D
W
M
Y
```

### Real Project Usage

Stock analysis.

Crypto analysis.

Sales analysis.

---

# Rolling Window

## 7-Day Moving Average

```python
df["MA7"] = (
    df["Close"]
    .rolling(7)
    .mean()
)
```

## 30-Day Moving Average

```python
df["MA30"] = (
    df["Close"]
    .rolling(30)
    .mean()
)
```

### Why

Shows trends.

Reduces noise.

---

# Merge

## Syntax

```python
pd.merge(
    employees,
    salaries,
    on="id"
)
```

### Use

Combine tables.

---

## Join Types

### Inner

Matching rows only.

### Left

All rows from left table.

### Right

All rows from right table.

### Outer

All rows from both tables.

---

# Concat

## Syntax

```python
pd.concat(
    [df1, df2]
)
```

### Use

Stack datasets.

---

# Visualization

## Line Chart

```python
import matplotlib.pyplot as plt

df["Close"].plot()

plt.show()
```

### Use

Trend analysis.

---

## Bar Chart

```python
df.groupby(
    "DayOfWeek"
)["Close"].mean().plot(
    kind="bar"
)
```

### Use

Compare categories.

---

# Debugging Notes

## KeyError: 'Date'

Cause:

Date already became index.

Fix:

```python
df.index
```

or

```python
df.reset_index()
```

---

## Only valid with DatetimeIndex

Cause:

RangeIndex used.

Fix:

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)

df.set_index(
    "Date",
    inplace=True
)
```

---

## Unknown datetime string format

Fix:

```python
pd.to_datetime(
    df["Date"],
    format="%Y-%m-%d %I-%p"
)
```

---

## NameError: df is not defined

Cause:

Notebook restarted.

Fix:

Reload CSV.

---

# Interview Questions

## Difference Between loc and iloc

```python
df.loc[]
```

Label-based.

```python
df.iloc[]
```

Position-based.

---

## Why Use GroupBy?

To summarize data by category.

---

## Why Convert To Datetime?

Required for time-series analysis.

---

## Why Use Resample?

To aggregate data by day, week, month, or year.
#
# Pandas Cheatsheet

## Import Pandas

```python
import pandas as pd
```

Loads the Pandas library.

---

## Read CSV

```python
df = pd.read_csv("employees.csv")
```

Loads CSV data into a DataFrame.

---

## View First Rows

```python
df.head()
```

Shows first 5 rows.

---

## View Last Rows

```python
df.tail()
```

Shows last 5 rows.

---

## Dataset Information

```python
df.info()
```

Shows:

* Column names
* Data types
* Missing values

---

## Dataset Shape

```python
df.shape
```

Returns:

```text
(rows, columns)
```

Example:

```text
(100, 5)
```

---

## Column Names

```python
df.columns
```

Returns all column names.

---

## Select One Column

```python
df["salary"]
```

Returns one column.

---

## Select Multiple Columns

```python
df[["name", "salary"]]
```

Returns selected columns.

---

## Summary Statistics

```python
df.describe()
```

Shows:

```text
count
mean
std
min
max
```

for numeric columns.

---

## Missing Values

```python
df.isnull().sum()
```

Counts missing values.

---

## Remove Missing Values

```python
df.dropna()
```

Removes rows with null values.

---

## Fill Missing Values

```python
df.fillna("Unknown")
```

Replaces missing values.

---

## Rename Columns

```python
df.rename(columns={"salary":"Salary"})
```

Changes column names.

---

## Sort Values

```python
df.sort_values("salary")
```

Ascending order.

```python
df.sort_values("salary", ascending=False)
```

Descending order.

---

## Filter Rows

```python
df[df["salary"] > 50000]
```

Returns matching rows.

---

## Group By

```python
df.groupby("city")["salary"].mean()
```

Average salary by city.

---

## Count Values

```python
df["city"].value_counts()
```

Counts frequency of each city.

---

## Unique Values

```python
df["city"].nunique()
```

Counts unique cities.

---

## Highest Salary

```python
df["salary"].max()
```

Returns highest salary.

---

## Lowest Salary

```python
df["salary"].min()
```

Returns lowest salary.

---

## Average Salary

```python
df["salary"].mean()
```

Returns average salary.

---

## Top 3 Records

```python
df.nlargest(3, "salary")
```

Returns top 3 salaries.

---

## Save CSV

```python
df.to_csv("output.csv", index=False)
```

Exports data.

---

# Analysis Workflow

```text
Load Data
    ↓
Inspect Data
    ↓
Clean Data
    ↓
Analyze Data
    ↓
Visualize Data
    ↓
Export Results
```
