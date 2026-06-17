from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Employee API"
    }

from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Employee API"}

@app.get("/employees")
def get_employees():

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    conn.close()

    employees = []

    for row in rows:
        employees.append({
            "name": row[1],
            "city": row[2],
            "salary": row[3]
        })

    return {"employees": employees}
# employee count
@app.get("/employees/count")
def employee_count():

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")

    count = cursor.fetchone()[0]

    conn.close()

    return {"employee_count": count}
#highest salary
@app.get("/highest-salary")
def highest_salary():

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, city, salary
        FROM employees
        ORDER BY salary DESC
        LIMIT 1
        """
    )

    employee = cursor.fetchone()

    conn.close()

    return {
        "name": employee[0],
        "city": employee[1],
        "salary": employee[2]
    }
#Dynamic search
@app.get("/city/{city_name}")
def employees_by_city(city_name):

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, city, salary
        FROM employees
        WHERE city = ?
        """,
        (city_name,)
    )

    rows = cursor.fetchall()

    conn.close()

    employees = []

    for row in rows:
        employees.append({
            "name": row[0],
            "city": row[1],
            "salary": row[2]
        })

    return {"employees": employees}