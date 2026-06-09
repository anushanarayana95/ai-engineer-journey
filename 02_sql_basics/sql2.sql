-- Day 2 SQL practice

UPDATE employees
SET salary = salary + 5000
WHERE city = 'Chennai';

UPDATE employees
SET salary = 45000
WHERE name = 'Ravi';
UPDATE employees SET salary = 50000;
UPDATE employees SET salary = salary + 5000 WHERE city = 'Chennai';

SELECT * FROM employees ORDER BY salary DESC;

SELECT * FROM employees LIMIT 3;