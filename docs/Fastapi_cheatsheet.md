# FastAPI Cheatsheet

## Import FastAPI

```python
from fastapi import FastAPI
```

### Explanation

Imports the FastAPI framework so we can build APIs.

---

## Create FastAPI App

```python
app = FastAPI()
```

### Explanation

Creates the application object.

All API routes are attached to this app.

---

## Home Route

```python
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

### Explanation

`/` is the root route.

When a user visits:

```text
http://127.0.0.1:8000/
```

FastAPI runs the `home()` function.

Output:

```json
{
    "message": "Hello FastAPI"
}
```

---

## Create a Route

```python
@app.get("/about")
def about():
    return {
        "project": "FastAPI Project"
    }
```

### Explanation

Creates a new endpoint.

Visit:

```text
http://127.0.0.1:8000/about
```

---

## Return JSON

```python
return {
    "city": "Nellore",
    "temperature": 38
}
```

### Explanation

FastAPI automatically converts Python dictionaries into JSON.

---

## Run Server

```bash
uvicorn main:app --reload
```

### Explanation

`main`

```text
main.py file
```

`app`

```text
app = FastAPI()
```

`--reload`

```text
Automatically reloads when code changes.
```

---

## Path Parameters

```python
@app.get("/city/{city_name}")
def city(city_name):
    return {"city": city_name}
```

### Explanation

Value comes from URL.

Example:

```text
/ city/Chennai
```

Output:

```json
{
    "city": "Chennai"
}
```

---

## Query Parameters

```python
@app.get("/employee")
def employee(name: str):
    return {"name": name}
```

URL:

```text
/employee?name=Ravi
```

Output:

```json
{
    "name": "Ravi"
}
```

---

## API Response Example

```python
@app.get("/weather")
def weather():
    return {
        "city": "Nellore",
        "temperature": 37
    }
```

### Explanation

Creates a weather endpoint.

Visit:

```text
http://127.0.0.1:8000/weather
```

---

# SQLite + FastAPI

## Connect Database

```python
import sqlite3

conn = sqlite3.connect("employees.db")
```

### Explanation

Connects Python to SQLite database.

---

## Create Cursor

```python
cursor = conn.cursor()
```

### Explanation

Cursor executes SQL queries.

Think of it as a messenger between Python and SQLite.

---

## Execute Query

```python
cursor.execute("SELECT * FROM employees")
```

### Explanation

Runs SQL query.

---

## Fetch All Rows

```python
rows = cursor.fetchall()
```

### Explanation

Returns all records.

Example:

```python
[
 ("Ravi","Chennai",55000),
 ("Anu","Mumbai",50000)
]
```

---

## Fetch One Row

```python
row = cursor.fetchone()
```

### Explanation

Returns only the first matching record.

---

## Close Connection

```python
conn.close()
```

### Explanation

Always close database connections after use.

---

# FastAPI Docs

Automatic documentation:

```text
http://127.0.0.1:8000/docs
```

### Explanation

Swagger UI generated automatically by FastAPI.

You can:

```text
Test APIs
See routes
Send requests
View responses
```

---

# Employee API Examples

## Get All Employees

```python
@app.get("/employees")
```

Returns employee list.

---

## Employee Count

```python
@app.get("/employees/count")
```

Returns total employee count.

---

## Highest Salary

```python
@app.get("/highest-salary")
```

Returns employee with highest salary.

---

## Employees by City

```python
@app.get("/city/{city_name}")
```

Returns employees belonging to a city.

---

# FastAPI Workflow

```text
Client
  ↓
Request
  ↓
FastAPI Route
  ↓
Python Function
  ↓
SQLite/API
  ↓
JSON Response
  ↓
Client
```

Example:

```text
Browser
 ↓
/employees
 ↓
FastAPI
 ↓
SQLite Query
 ↓
Employee Data
 ↓
JSON
 ↓
Browser
```
