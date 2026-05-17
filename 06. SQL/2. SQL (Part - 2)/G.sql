-- 7. Self Join

CREATE DATABASE DataBox;

USE DataBox;

CREATE TABLE CustomerTable(
	customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE OrderTable(
	order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO CustomerTable VALUES
	(1, "Alice", "Mumbai"),
	(2, "Bob", "Delhi"),
	(3, "Charlie", "Banglore"),
	(4, "David", "Mumbai");

INSERT INTO OrderTable VALUES
	(101, 1, 500),
    (102, 1, 900),
    (103, 2, 300),
    (104, 5, 700);
    
SELECT *
FROM CustomerTable as A
JOIN CustomerTable as B
ON A.customer_id = B.customer_id;


SELECT * FROM CustomerTable;
SELECT * FROM OrderTable;

DROP DATABASE DataBox;