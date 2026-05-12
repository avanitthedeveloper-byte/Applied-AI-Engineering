-- 8. Create Table (Table Queries)

CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user(
	Id INT,
    Name VARCHAR(30),
    Email VARCHAR(30),
    Followers INT,
    Following INT
);