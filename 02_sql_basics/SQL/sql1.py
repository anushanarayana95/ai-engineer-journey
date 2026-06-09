import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("Day_12/employees.csv")

# Create database
conn = sqlite3.connect("employees.db")

# Convert CSV into SQL table
df.to_sql("employees", conn, if_exists="replace", index=False)

# Run SQL query
result = pd.read_sql("""
SELECT *
FROM employees
WHERE salary > 30000
""", conn)

print(result)

conn.close()