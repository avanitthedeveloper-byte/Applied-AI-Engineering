-- 9. Sub-Queries in SQL

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
    
SELECT * FROM OrderTable
WHERE amount > (
	SELECT avg(amount) FROM OrderTable
);

SELECT name, (
	SELECT COUNT(*)
    FROM OrderTable o
    WHERE o.customer_id = c.customer_id
) as order_count
FROM CustomerTable c;

SELECT summary.customer_id, summary.avg_amount
FROM (
	SELECT
		customer_id,
        AVG(amount) AS avg_amount
	FROM OrderTable
    GROUP BY customer_id
) AS summary;

SELECT * FROM CustomerTable;
SELECT * FROM OrderTable;

DROP DATABASE DataBox;