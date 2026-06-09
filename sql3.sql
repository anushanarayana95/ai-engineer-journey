-- DAY 3 SQL - GROUP BY PRACTICE

SELECT city, COUNT(*) AS total_employees
FROM employees
GROUP BY city;

SELECT city, AVG(salary) AS avg_salary
FROM employees
GROUP BY city;

SELECT city, SUM(salary) AS total_salary
FROM employees
GROUP BY city;

SELECT city, MAX(salary) AS max_salary
FROM employees
GROUP BY city;

SELECT city, MIN(salary) AS min_salary
FROM employees
GROUP BY city;

-- HAVING example
SELECT city, COUNT(*) AS total
FROM employees
GROUP BY city
HAVING COUNT(*) > 1;