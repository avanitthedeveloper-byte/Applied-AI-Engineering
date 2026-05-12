-- 9. What are Constraints?

CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user(
	Id INT UNIQUE,
    Name VARCHAR(30) NOT NULL,
    Age INT,
    Email VARCHAR(30) UNIQUE,
    Followers INT DEFAULT 0,
    Following INT,
    
    CONSTRAINT age_check CHECK (Age >= 13)
);