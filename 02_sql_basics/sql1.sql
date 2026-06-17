DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    city TEXT,
    salary REAL
);

INSERT INTO employees (name, city, salary)
VALUES 
('Ravi', 'Chennai', 30000),
('Anu', 'Mumbai', 25000),
('John', 'Delhi', 40000),
('Meena', 'Chennai', 45000);
SELECT * FROM employees;

UPDATE employees
SET salary = 45000
WHERE name = 'Ravi';