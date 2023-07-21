USE capstone ;
Select *
FROM account

USE capstone;
SELECT *
FROM account_usage;

USE capstone;
SELECT *
FROM churn_status

USE capstone;
SELECT *
FROM customer;

SELECT *
FROM account
LEFT JOIN account_usage ON account.account_id = account_usage.account_id
LEFT JOIN churn_status ON account.customer_id = churn_status.customer_id
LEFT JOIN customer ON account.customer_id = customer.customer_id
LEFT JOIN city ON customer.zip_code = city.zip_code;






