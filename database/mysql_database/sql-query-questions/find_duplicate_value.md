### 🎯**Count email number**
```sql
+----+----------+-----------------+
| id | emp_name | email           |
+----+----------+-----------------+
|  1 | Mohit    | mohit@gmail.com |
|  2 | Rahul    | rahul@gmail.com |
|  3 | Amit     | mohit@gmail.com |
|  4 | Sumit    | NULL            |
|  5 | Raj      | rahul@gmail.com |
+----+----------+-----------------+
```

* Total non-NULL emails
```sql
SELECT COUNT(email) AS total_email FROM Person;

+-------------+
| total_email |
+-------------+
|           4 |
+-------------+
```

* Count each email
```sql
SELECT email, COUNT(email) AS total_email FROM Person GROUP BY email;

+-----------------+-------------+
| email           | total_email |
+-----------------+-------------+
| NULL            |           0 |
| mohit@gmail.com |           2 |
| rahul@gmail.com |           2 |
+-----------------+-------------+
```
<div style="page-break-before: always;"></div>

### 🎯**How to Find Duplicate values in a Table?**
```sql
+----+----------+-------------------+
| id | emp_name | email             |
+----+----------+-------------------+
|  1 | Mohit    | mohit@gmail.com   |
|  2 | Rahul    | rahul@gmail.com   |
|  3 | Amit     | mohit@gmail.com   |
|  4 | Sumit    | sumit@gmail.com   |
|  5 | Raj      | rahul@gmail.com   |
+----+----------+-------------------+
```

```sql
-- COUNT(*) Null value ko bhi count karta hai
SELECT email, COUNT(*) AS count FROM employees GROUP BY email
HAVING COUNT(*) > 1;

-- COUNT(Email) NULL valu ko count nahi karta hai 
SELECT Email, COUNT(Email) AS total_email FROM employees GROUP BY Email
HAVING COUNT(Email) > 1;

+-------------------+-------------+
| Email             | total_email |
+-------------------+-------------+
| mohit@gmail.com   |           2 |
| rahul@gmail.com   |           2 |
+-------------------+-------------+

-- NULL values mtb
+-------------------+
| email             |
+-------------------+
| mohit@gmail.com   |
| rahul@gmail.com   |
| NULL              |
| sumit@gmail.com   |
| rahul@gmail.com   |
+-------------------+

-- If you want the complete records of duplicates
SELECT *
FROM employees
WHERE email IN (
    SELECT email
    FROM employees
    GROUP BY email
    HAVING COUNT(*) > 1
);
```

<div style="page-break-before: always;"></div>


### 🎯**Duplicate value remove**
* Using Join
```sql
DELETE t1
FROM my_table t1
INNER JOIN my_table t2
    ON t1.col1 = t2.col1
   AND t1.col2 = t2.col2 -- agar aap duplicate ko multiple columns ke combination ke basis par identify karna chahte ho, tab use karoge.
   AND t1.id > t2.id;
```

* Using Subquery
```sql
DELETE FROM Person
WHERE id IN (
    SELECT id
    FROM (
        SELECT t1.id
        FROM Person t1
        JOIN Person t2
            ON t1.email = t2.email
           AND t1.id > t2.id
    ) AS temp
);
```

### How do you find duplicate invoices?
* Invoice table mein jo invoice records duplicate hain, unhe find karna.
```sql
+-------------+----------+--------+
| invoice_no  | customer | amount |
+-------------+----------+--------+
| INV001      | AMIT     | 5000   |
| INV002      | ROHIT    | 7000   |
| INV001      | AMIT     | 5000   |
| INV003      | NEHA     | 9000   |
| INV002      | ROHIT    | 7000   |
+-------------+----------+--------+

--sql
SELECT invoice_no, COUNT(*) AS duplicate_count
FROM invoices
GROUP BY invoice_no
HAVING COUNT(*) > 1;

+-------------+----------------+
| invoice_no  | duplicate_count|
+-------------+----------------+
| INV001      |              2 |
| INV002      |              2 |
+-------------+----------------+
```

### Find customers having more than 5 invoices?
```sql
SELECT customer_id, COUNT(*) AS invoice_count
FROM invoices
GROUP BY customer_id
HAVING COUNT(*) > 5;

+-------------+----------------+
| customer_id | invoice_count  |
+-------------+----------------+
| 101         | 8              |
| 102         | 3              |
| 103         | 6              |
| 104         | 5              |
+-------------+----------------+

-- Result
+-------------+---------------+
| customer_id | invoice_count |
+-------------+---------------+
| 101         |             8 |
| 103         |             6 |
+-------------+---------------+
```

### Find the total invoice amount customer-wise?
* Har customer ne jitne invoices generate kiye hain, un sabka total amount find karo.
```sql
SELECT customer_id, SUM(invoice_amount) AS total_invoice_amount
FROM invoices
GROUP BY customer_id;

-- Customer 101:
    -- INV001 → 5000
    -- INV002 → 4000
    -- INV003 → 6000
    -- Total → 15000

-- Output:-
+-------------+---------------------+
| customer_id | total_invoice_amount|
+-------------+---------------------+
| 101         |              15000  |
| 102         |               9000  |
| 103         |              22000  |
+-------------+---------------------+

```