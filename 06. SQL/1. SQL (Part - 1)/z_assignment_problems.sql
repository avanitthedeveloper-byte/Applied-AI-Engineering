-- Assignment Problem
CREATE DATABASE  IF NOT EXISTS EmployeeInfo;

USE EmployeeInfo;

CREATE TABLE EMPP (
	EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName Varchar(50),
    Department VARCHAR(50),
    Salary INT,
    HireDate DATE
);

INSERT INTO EMPP
(EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, "Alice", "Jonson", "IT", 6500, "2020-03-15"),
(102, "Mark", "Rivera", "HR", 4800, "2019-07-22"),
(103, "Sophia", "Lee", "Finance", 7200, "2021-01-10"),
(104, "Daniel", "Kim", "IT", 5800, "2018-11-05"),
(105, "Emma", "Brown", "Marketing", 5300, "2022-04-18"),
(106, "Liam", "Patel", "Finance", 6900, "2020-09-29"),
(107, "Olivia", "Garcia", "HR", 4600, "2017-06-30"),
(108, "Noah", "Thompson", "IT", 7500, "2023-02-12"),
(109, "Ava", "Martinez", "Marketing", 5100, "2019-12-02"),
(110, "Ethan", "Davis", "Finance", 8000, "2016-05-14");

SELECT * FROM EMPP;

SELECT FirstName, LastName, Salary FROM EMPP;

SELECT * FROM EMPP
WHERE Department = "IT";

SELECT * FROM EMPP
WHERE Salary > 6000;

SELECT * FROM EMPP
ORDER BY HireDate DESC;

SELECT department FROM EMPP
GROUP BY department;

SELECT * FROM EMPP
WHERE FirstName LIKE "A%";

SELECT * FROM EMPP
WHERE salary BETWEEN 4000 AND 7000;

SELECT AVG(salary) FROM EMPP;

SELECT department, COUNT(*) AS employee_count
FROM EMPP
GROUP BY department
HAVING COUNT(*) >= 3;
~