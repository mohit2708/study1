### **How to Find Duplicate values in a Table?**
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


### **Delete Duplicate Records?**
```sql
-- using join
DELETE t1
FROM my_table t1
INNER JOIN my_table t2
  ON t1.col1 = t2.col1
 AND t1.col2 = t2.col2 -- optinal this line if check multipal column
 AND t1.id > t2.id;

-- using subquery
DELETE FROM my_table
WHERE id IN (
  SELECT t1.id
  FROM my_table t1
  JOIN my_table t2
    ON t1.col1 = t2.col1
   AND t1.col2 = t2.col2
   AND t1.id > t2.id
);
```