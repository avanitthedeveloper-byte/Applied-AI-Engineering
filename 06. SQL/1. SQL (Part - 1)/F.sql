-- 6. Our First Table

CREATE DATABASE college;

USE college;

CREATE TABLE student(
	roll_no int,
    name varchar(30),
    age int
);

INSERT INTO student VALUES
	(101, "Cipher", 28),
    (102, "Mind", 18),
    (103, "Cipher Mind", 26);
    
SELECT * FROM student;

DROP DATABASE college;