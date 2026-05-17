-- 3. Rollback & Savepoints
CREATE DATABASE Prime;

USE Prime;

CREATE TABLE account(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10, 2)
);

INSERT INTO account VALUES
(1, "Adom", 500.00),
(2, "Bob", 350.00),
(3, "Charlie", 800);

START TRANSACTION;
	UPDATE account SET balance = balance - 20 WHERE id = 1;
    COMMIT;
    UPDATE account SET balance = balance + 20 WHERE id = 2;
ROLLBACK;

START TRANSACTION;
	UPDATE account SET balance = balance + 2000 WHERE id = 1;
    SAVEPOINT after_wallet_topup;
    UPDATE account SET balance = balance + 20 WHERE id = 1;
	ROLLBACK TO after_wallet_topup;
COMMIT;

SELECT * FROM account;

DROP DATABASE Prime;