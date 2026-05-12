-- Practice Set 2

CREATE DATABASE college;

USE college;

CREATE TABLE Teacher(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50),
    salary INT
);

INSERT INTO Teacher VALUES
	(23, "Ajay", "Math", 55000),
    (47, "Bharat", "English", 60000),
    (18, "Chetan", "Chemistry", 45000),
    (9, "Divya", "Physics", 75000);
    
    
SELECT * FROM Teacher
WHERE salary > 50000;

ALTER TABLE Teacher
CHANGE COLUMN salary ctc INT;

UPDATE Teacher
SET ctc = ctc+ctc*0.25;

ALTER TABLE Teacher
ADD COLUMN city varchar(50) default("Gurgaon");

ALTER TABLE Teacher
DROP COLUMN ctc;

SELECT * FROM Teacher;

CREATE TABLE Student(
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    marks INT
);

INSERT INTO Student VALUES
(110, "Adam", "Delhi", 76),
(108, "Bob", "Mumbai", 65),
(124, "Casey", "Pune", 94),
(112, "Duke", "Pune", 80);

SELECT * FROM Student
WHERE marks > 75;

SELECT city FROM Student;

SELECT city, max(marks) FROM Student
GROUP BY city;

SELECT avg(marks) FROM Student;

ALTER TABLE Student
ADD COLUMN grade char(1);

UPDATE Student
SET grade = 'O'
WHERE marks > 80;

UPDATE Student
SET grade = 'A'
WHERE marks BETWEEN 70 AND 80;

UPDATE Student
SET grade = 'B'
WHERE marks BETWEEN 60 AND 70;

SELECT * FROM Student;