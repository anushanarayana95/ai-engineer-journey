# API & JSON Cheatsheet

## What is an API?

API = Application Programming Interface

Think of it like a waiter in a restaurant:

```text
You (Client)
    ↓ Request
API
    ↓
Server / Database
    ↓ Response
You
```

You ask for data, the API returns data.

---

## Making a GET Request

```python
import requests

response = requests.get(url)
```

### Explanation

`requests.get()` sends a request to an API and asks for data.

---

## Status Code

```python
print(response.status_code)
```

### Explanation

Checks if the request succeeded.

Common codes:

```text
200 = Success
404 = Not Found
500 = Server Error
```

---

## Convert Response to JSON

```python
data = response.json()
```

### Explanation

Converts API data into Python objects.

Usually becomes:

```python
dict
```

or

```python
list
```

---

## Dictionary Access

```python
person = {
    "name": "Anusha",
    "city": "Nellore"
}

print(person["name"])
```

### Explanation

Gets the value stored under a key.

Output:

```text
Anusha
```

---

## List Access

```python
names = ["Ravi", "Anu", "John"]

print(names[0])
```

### Explanation

Lists use indexes.

```text
0 = first item
1 = second item
2 = third item
```

Output:

```text
Ravi
```

---

## Nested Dictionary

```python
employee = {
    "name": "Ravi",
    "address": {
        "city": "Chennai"
    }
}

print(employee["address"]["city"])
```

### Explanation

Read it like a path:

```text
employee
 ↓
address
 ↓
city
```

Output:

```text
Chennai
```

---

## List of Dictionaries

```python
employees = [
    {"name": "Ravi"},
    {"name": "Anu"}
]

print(employees[0]["name"])
```

### Explanation

Get:

```text
first employee
      ↓
name
```

Output:

```text
Ravi
```

---

## Loop Through JSON

```python
for emp in employees:
    print(emp["name"])
```

### Explanation

Reads each employee one by one.

Output:

```text
Ravi
Anu
```

---

## Create DataFrame

```python
import pandas as pd

df = pd.DataFrame(employees)
```

### Explanation

Converts JSON data into a Pandas table.

---

## View Data

```python
df.head()
```

### Explanation

Shows first 5 rows.

---

## Dataset Shape

```python
df.shape
```

### Explanation

Returns:

```text
(rows, columns)
```

Example:

```text
(10, 4)
```

means:

```text
10 rows
4 columns
```

---

## Count Unique Values

```python
df["city"].nunique()
```

### Explanation

Counts distinct values.

Example:

```text
10
```

means 10 unique cities.

---

## Count Frequency

```python
df["city"].value_counts()
```

### Explanation

Counts how many times each city appears.

---

## Export CSV

```python
df.to_csv("output.csv", index=False)
```

### Explanation

Saves DataFrame as a CSV file.

`index=False` removes row numbers from the file.
