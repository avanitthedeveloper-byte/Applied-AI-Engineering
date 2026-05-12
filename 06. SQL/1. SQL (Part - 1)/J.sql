-- 10. Key Constraints

CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user(
	Id INT UNIQUE,
    Name VARCHAR(30) NOT NULL,
    Age INT,
    Email VARCHAR(30) UNIQUE,
    Followers INT DEFAULT 0,
    Following INT,
    
    CONSTRAINT age_check CHECK (Age >= 13),
    PRIMARY KEY (Id)
);

CREATE TABLE post(
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user (id)
);