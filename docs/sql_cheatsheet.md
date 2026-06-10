# SQL Cheat Sheet

## What is SQL?

SQL (Structured Query Language) is used to store, retrieve, filter, and analyze data in databases.

Think of SQL as:

```text
Pandas → Python Data
SQL → Database Data
```

---

# Create Table

## Syntax

```sql
CREATE TABLE employees(
    id INTEGER,
    name TEXT,
    city TEXT,
    salary INTEGER
);
```

## What it does

Creates a new table.

## Real Project Usage

Store employee data, customer data, product data.

---

# Insert Data

## Syntax

```sql
INSERT INTO employees
VALUES
(1,'Anu','Hyderabad',50000);
```

## What it does

Adds a new record.

---

# View All Data

## Syntax

```sql
SELECT *
FROM employees;
```

## What it does

Shows all rows and columns.

---

# Select Specific Columns

## Syntax

```sql
SELECT name, salary
FROM employees;
```

## What it does

Shows only selected columns.

---

# WHERE

## Syntax

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

## What it does

Filters rows.

## Pandas Equivalent

```python
df[df["salary"] > 50000]
```

---

# AND

## Syntax

```sql
SELECT *
FROM employees
WHERE city='Hyderabad'
AND salary > 50000;
```

## What it does

Both conditions must be true.

---

# OR

## Syntax

```sql
SELECT *
FROM employees
WHERE city='Hyderabad'
OR city='Chennai';
```

## What it does

At least one condition must be true.

---

# ORDER BY

## Ascending

```sql
SELECT *
FROM employees
ORDER BY salary;
```

## Descending

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

## What it does

Sorts results.

---

# COUNT

## Syntax

```sql
SELECT COUNT(*)
FROM employees;
```

## What it does

Counts rows.

---

# SUM

## Syntax

```sql
SELECT SUM(salary)
FROM employees;
```

## What it does

Adds all salary values.

---

# AVG

## Syntax

```sql
SELECT AVG(salary)
FROM employees;
```

## What it does

Calculates average salary.

---

# MAX

## Syntax

```sql
SELECT MAX(salary)
FROM employees;
```

## What it does

Returns highest salary.

---

# MIN

## Syntax

```sql
SELECT MIN(salary)
FROM employees;
```

## What it does

Returns lowest salary.

---

# GROUP BY

## Syntax

```sql
SELECT city,
AVG(salary)
FROM employees
GROUP BY city;
```

## What it does

Creates summaries by category.

## Pandas Equivalent

```python
df.groupby("city")["salary"].mean()
```

---

# INNER JOIN

## Syntax

```sql
SELECT *
FROM employees e
INNER JOIN salaries s
ON e.id = s.id;
```

## What it does

Returns matching rows only.

---

# LEFT JOIN

## Syntax

```sql
SELECT *
FROM employees e
LEFT JOIN salaries s
ON e.id = s.id;
```

## What it does

Returns all rows from left table.

---

# RIGHT JOIN

## Syntax

```sql
SELECT *
FROM employees e
RIGHT JOIN salaries s
ON e.id = s.id;
```

## What it does

Returns all rows from right table.

---

# OUTER JOIN

## Syntax

```sql
SELECT *
FROM employees e
FULL OUTER JOIN salaries s
ON e.id = s.id;
```

## What it does

Returns everything from both tables.

---

# SQLite Commands

## Open Database

```bash
sqlite3 employees.db
```

---

## Show Tables

```sql
.tables
```

---

## Show Schema

```sql
.schema employees
```

---

## Exit SQLite

```sql
.quit
```

---

# Common Errors

## Table Already Exists

Error:

```text
table employees already exists
```

Fix:

```sql
DROP TABLE employees;
```

Then recreate.

---

## No Such Column

Cause:

Column name is wrong.

Check:

```sql
PRAGMA table_info(employees);
```

---

# Interview Questions

## Difference Between WHERE and GROUP BY

WHERE:

* Filters rows

GROUP BY:

* Creates summaries

---

## Difference Between COUNT(*) and COUNT(column)

COUNT(*)

* Counts all rows

COUNT(column)

* Counts non-null values

---

## Difference Between DELETE and DROP

DELETE:

* Removes rows

DROP:

* Removes entire table
