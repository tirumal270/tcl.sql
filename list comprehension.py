START TRANSACTION;

UPDATE accounts
SET balance = balance + 2000
WHERE holder_name = 'Rahul';

SELECT * FROM accounts
WHERE holder_name = 'Rahul';

COMMIT;



START TRANSACTION;

UPDATE accounts
SET balance = balance - 1500
WHERE holder_name = 'Priya';

SELECT * FROM accounts
WHERE holder_name = 'Priya';

ROLLBACK;

SELECT * FROM accounts
WHERE holder_name = 'Priya';


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




START TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE holder_name = 'Rahul';

UPDATE accounts
SET balance = balance + 2000
WHERE holder_name = 'Priya';

COMMIT;

SELECT * FROM accounts;



START TRANSACTION;

UPDATE accounts
SET balance = balance - 3000
WHERE holder_name = 'Sneha';

-- Error occurs here

ROLLBACK;

SELECT holder_name, balance
FROM accounts
WHERE holder_name IN ('Sneha','Rohit');







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



