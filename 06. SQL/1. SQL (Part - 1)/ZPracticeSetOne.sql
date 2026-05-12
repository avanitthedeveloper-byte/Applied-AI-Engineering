-- Practice Set 1
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
    
    
SELECT * FROM teacher
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