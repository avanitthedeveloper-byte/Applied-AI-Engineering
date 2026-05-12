-- 18. Order By Clause

CREATE DATABASE Employee_Data;

USE Employee_Data;

CREATE TABLE employee(
	emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(50),
    salary INT,
    city VARCHAR(50),
    joining_date DATE,
    experience INT,
    status VARCHAR(8)
);

INSERT INTO employee VALUES
(1, "Alice", 25, "IT", 50000, "Chennai", "2022-01-15", 2, "Active"),
(2, "Bob", 30, "HR", 60000, "Delhi", "2020-06-10", 5, "Active"),
(3, "Charlie", 35, "Finance", 70000, "Mumbai", "2018-03-20", 7, "Active"),
(4, "David", 28, "IT", 55000, "Banglore", "2021-09-01", 3, "Inctive"),
(5, "Eve", 40, "HR", 80000, "Chennai", "2015-11-25", 10, "Active"),
(6, "Frank", 23, "Marketing", 45000, "Kolkata", "2023-05-12", 1, "Active"),
(7, "Grace", 31, "Finance", 72000, "Delhi", "2019-07-18", 6, "Inctive"),
(8, "Henry", 29, "IT", 58000, "Mumbai", "2021-02-11", 4, "Active"),
(9, "Ivy", 27, "Marketing", 47000, "Chennai", "2022-08-30", 2, "Active"),
(10, "Jack", 45, "Management",90000, "Banglore", "2010-12-05", 15, "Active");

-- Basic Comparison(=, !=, >, >=, <, <=)
SELECT name, department FROM employee
WHERE department = "IT";

SELECT name, salary FROM employee
WHERE salary > 60000;

SELECT name, age FROM employee
WHERE age <= 30;

SELECT name, salary FROM employee
WHERE salary != 50000;

-- Logical Operators(AND, OR, NOT)
SELECT name, department, salary FROM employee
WHERE department = "IT" AND salary > 55000;

SELECT name, department FROM employee
WHERE department = "IT" OR department = "Marketing";

SELECT * FROM employee
WHERE department != "Finance";

-- Range(BETWEEN)
SELECT name, salary FROM employee
WHERE salary BETWEEN 50000 AND 70000;

SELECT name, age FROM employee
WHERE age BETWEEN 25 AND 35;

-- List (IN, NOT IN)
SELECT name, department FROM employee
WHERE department IN ("IT", "HR", "Finance");

SELECT * FROM employee
WHERE city Not IN ("Chennai", "Delhi");

-- Pattern Matching(LIKE)
SELECT * FROM employee
WHERE name LIKE "A%"; # Starts with 'A'

SELECT * FROM employee
WHERE name LIKE "%e"; # Ends with 'e'

SELECT * FROM employee
WHERE name LIKE "%a%"; # Contains 'a'

-- Data Filtering
SELECT * FROM employee
WHERE joining_date > "2020-01-01";

SELECT * FROM employee
WHERE joining_date < "2021-01-01";

-- Combined Combination
SELECT * FROM employee
WHERE city = "Chennai" AND salary > 45000 AND age < 35;

SELECT * FROM employee
WHERE (department = "IT" OR department = "HR") AND salary > 55000;

-- Advanced Practice
SELECT * FROM employee
WHERE experience >= 5 AND status = "Active";

SELECT * FROM employee
WHERE city Like "%a%" AND salary BETWEEN 40000 AND 80000;

SELECT name, department FROM employee
WHERE name NOT LIKE "A%" AND DEPARTMENT IN ("IT", "HR");

-- Limit Clause
SELECT emp_id, name, salary, city FROM employee
LIMIT 3;

-- Order By Clause
SELECT name, salary FROM employee
ORDER BY salary ASC;

SELECT name, salary FROM employee
ORDER BY salary DESC;

SELECT * FROM employee;

DROP DATABASE Employee_Data;