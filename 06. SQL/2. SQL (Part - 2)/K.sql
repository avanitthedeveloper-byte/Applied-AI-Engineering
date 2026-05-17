-- 11. Index in SQL

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
    
CREATE INDEX idx_name ON CustomerTable(name);

-- Now, just because of INDEX this retrieval will be fastest.
SELECT * FROM CustomerTable
WHERE name = "Charlie";

SHOW INDEX FROM CustomerTable;

SELECT * FROM CustomerTable;
SELECT * FROM OrderTable;

DROP DATABASE DataBox;