### 🎯**Find records present in one table but not another?**
* Table A mein jo records hain, lekin Table B mein nahi hain, unhe find karo.
```sql
-- employee             -- employee_bkp
+----+--------+         +----+--------+
| id | name   |         | id | name   |
+----+--------+         +----+--------+
| 1  | AMIT   |         | 1  | AMIT   |
| 2  | ROHIT  |         | 2  | ROHIT  |
| 3  | NEHA   |         | 4  | PRIYA  |
| 4  | PRIYA  |         +----+--------+
+----+--------+

-- Method 1 — NOT EXISTS
SELECT e.*
FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employees_backup b
    WHERE b.id = e.id
);

-- Method 2 — LEFT JOIN
SELECT e.*
FROM employees e
LEFT JOIN employees_backup b
    ON e.id = b.id
WHERE b.id IS NULL;

-- Output
+----+-------+
| id | name  |
+----+-------+
| 3  | NEHA  |
+----+-------+
```