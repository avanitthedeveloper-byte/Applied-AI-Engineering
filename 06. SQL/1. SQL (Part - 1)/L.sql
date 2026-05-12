-- 12 Insert into Table

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

INSERT INTO user VALUES
	(1, "Adam", 26, "adom@yahoo.in", 123, 145),
    (2, "Bob",  16, "bob123@gmail.com", 200, 200),
    (3, "Casey", 19, "casey@email.com", 300, 306),
    (4, "Donald", 23, "donald@gmail.com", 300, 306),
    (5, "Cipher Mind", 34, "cm123@gmail.com", 200, 105);
    
INSERT INTO post
(id, content)
VALUES
(101, "Hello World"),
(102, "Bye Bye"),
(103, "Hello Cipher");


SELECT * FROM user;

SELECT * FROM post;

DROP DATABASE instagram;