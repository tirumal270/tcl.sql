-- =========================
-- CREATE TABLE
-- =========================

CREATE TABLE accounts (
    acc_no INT PRIMARY KEY,
    holder_name VARCHAR(30),
    account_type VARCHAR(20),
    balance DECIMAL(10,2),
    branch VARCHAR(30)
);

-- =========================
-- INSERT DATA
-- =========================

INSERT INTO accounts VALUES
(101,'Rahul','Savings',5000,'Hyderabad'),
(102,'Priya','Current',8000,'Warangal'),
(103,'Amit','Savings',12000,'Karimnagar'),
(104,'Sneha','Current',7000,'Nizamabad'),
(105,'Rohit','Savings',15000,'Hyderabad');

SELECT * FROM accounts;

-- =========================
-- TASK 1 - COMMIT
-- Rahul deposits ₹2000
-- =========================

START TRANSACTION;

UPDATE accounts
SET balance = balance + 2000
WHERE holder_name = 'Rahul';

SELECT * FROM accounts
WHERE holder_name = 'Rahul';

COMMIT;

-- Verify
SELECT * FROM accounts
WHERE holder_name = 'Rahul';

-- =========================
-- TASK 2 - ROLLBACK
-- Priya withdraws ₹1500
-- =========================

START TRANSACTION;

UPDATE accounts
SET balance = balance - 1500
WHERE holder_name = 'Priya';

-- Check updated balance
SELECT * FROM accounts
WHERE holder_name = 'Priya';

-- Undo transaction
ROLLBACK;

-- Verify original balance restored
SELECT * FROM accounts
WHERE holder_name = 'Priya';

-- =========================
-- TASK 3 - SAVEPOINT
-- Amit transactions
-- =========================

START TRANSACTION;

UPDATE accounts
SET balance = balance + 3000
WHERE holder_name = 'Amit';

SAVEPOINT sp1;

UPDATE accounts
SET balance = balance - 1000
WHERE holder_name = 'Amit';

UPDATE accounts
SET balance = balance - 500
WHERE holder_name = 'Amit';

ROLLBACK TO sp1;

COMMIT;

SELECT * FROM accounts
WHERE holder_name = 'Amit';

-- =========================
-- TASK 4 - MONEY TRANSFER
-- Rahul transfers ₹2000 to Priya
-- =========================

START TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE holder_name = 'Rahul';

UPDATE accounts
SET balance = balance + 2000
WHERE holder_name = 'Priya';

COMMIT;

SELECT * FROM accounts;

-- =========================
-- TASK 5 - FAILED TRANSFER
-- Sneha transfers ₹3000 to Rohit
-- Error occurs
-- =========================

START TRANSACTION;

UPDATE accounts
SET balance = balance - 3000
WHERE holder_name = 'Sneha';

-- Error occurs before crediting Rohit

ROLLBACK;

SELECT holder_name, balance
FROM accounts
WHERE holder_name IN ('Sneha','Rohit');

-- =========================
-- TASK 6 - MULTIPLE SAVEPOINTS
-- Rohit transactions
-- =========================

START TRANSACTION;

UPDATE accounts
SET balance = balance + 2000
WHERE holder_name = 'Rohit';

SAVEPOINT sp1;

UPDATE accounts
SET balance = balance - 500
WHERE holder_name = 'Rohit';

SAVEPOINT sp2;

UPDATE accounts
SET balance = balance - 1000
WHERE holder_name = 'Rohit';

ROLLBACK TO sp2;

COMMIT;

SELECT * FROM accounts
WHERE holder_name = 'Rohit';
