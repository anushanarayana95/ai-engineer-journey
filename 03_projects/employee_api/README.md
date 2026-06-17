# Employee API

## Project Overview

Employee API is a FastAPI application connected to a SQLite database. It allows users to retrieve employee information through REST API endpoints.

This project demonstrates:

* FastAPI fundamentals
* SQLite database integration
* SQL queries
* Dynamic API routes
* JSON responses
* Backend development basics

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* SQLite
* SQL

---

## Project Structure

```text
employee_api/
│
├── main.py
├── employees.db
└── README.md
```

---

## Features

### Home Endpoint

```text
/
```

Returns a welcome message.

Example Response:

```json
{
  "message": "Employee API"
}
```

---

### Get All Employees

```text
/employees
```

Returns all employees stored in the database.

Example Response:

```json
{
  "employees": [
    {
      "name": "Ravi",
      "city": "Chennai",
      "salary": 55000
    },
    {
      "name": "Anu",
      "city": "Mumbai",
      "salary": 50000
    }
  ]
}
```

---

### Employee Count

```text
/employees/count
```

Returns total employee count.

Example Response:

```json
{
  "employee_count": 4
}
```

---

### Highest Salary

```text
/highest-salary
```

Returns the highest-paid employee.

Example Response:

```json
{
  "name": "Ravi",
  "city": "Chennai",
  "salary": 55000
}
```

---

### Search Employees By City

```text
/city/Chennai
```

Returns employees from a specific city.

Example Response:

```json
{
  "employees": [
    {
      "name": "Ravi",
      "city": "Chennai",
      "salary": 55000
    },
    {
      "name": "Meena",
      "city": "Chennai",
      "salary": 55000
    }
  ]
}
```

---

## SQL Queries Used

Get all employees:

```sql
SELECT * FROM employees;
```

Employee count:

```sql
SELECT COUNT(*) FROM employees;
```

Highest salary:

```sql
SELECT name, city, salary
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

Employees by city:

```sql
SELECT name, city, salary
FROM employees
WHERE city = ?;
```

---

## How to Run

Navigate to project folder:

```bash
cd 03_projects/employee_api
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8002
```

---

## Testing Endpoints

```bash
curl http://127.0.0.1:8002/
```

```bash
curl http://127.0.0.1:8002/employees
```

```bash
curl http://127.0.0.1:8002/employees/count
```

```bash
curl http://127.0.0.1:8002/highest-salary
```

```bash
curl http://127.0.0.1:8002/city/Chennai
```

---

## What I Learned

### FastAPI

* Creating API endpoints
* Dynamic path parameters
* Returning JSON responses

### SQLite

* Connecting to databases
* Executing SQL queries
* Fetching records

### SQL

* SELECT
* WHERE
* COUNT
* ORDER BY
* LIMIT

### Backend Development

* API → Database → Response workflow
* REST API fundamentals
* Querying databases through Python

---

## Future Improvements

* Add employee creation endpoint
* Add employee update endpoint
* Add employee delete endpoint
* Add salary filters
* Add pagination
* Deploy API online

---

## Author

Anusha Narayana
