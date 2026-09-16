|  No.  | Other Logical Questions                                                                                     |
| :---: | ----------------------------------------------------------------------------------------------------------- |
|       | [Replace a column value:- M to F & F to M](#replace-a-column-values-from-male-to-female-and-female-to-male) |


<div style="page-break-before: always;"></div>


### 🎯**Replace a Column Values from 'male' to 'female' and 'female' to 'male'**
```sql
UPDATE empdata
SET GENDER = CASE
    WHEN GENDER='male' THEN 'female'
    WHEN GENDER='female' THEN 'male'
    END;
(OR)
UPDATE EMPDATA 
SET gender = CASE 
    gender WHEN 'male' THEN 'female' 
            WHEN 'female' THEN 'male'
    ELSE gender
END;
```

### **find monthly transaction counts?**
* Har month mein kitne transactions hue, ye find karo.
```sql
SELECT 
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY YEAR(transaction_date), MONTH(transaction_date)
ORDER BY year, month;

-- Output:
+------+-------+------------------+
| year | month | transaction_count|
+------+-------+------------------+
| 2026 |     1 |               120|
| 2026 |     2 |               150|
| 2026 |     3 |               135|
+------+-------+------------------+

-- Sirf GROUP BY MONTH(transaction_date) karoge to different years ke same months combine ho jayenge.
```

### **Find NULL values?**
* Table mein jis column ki value NULL hai, un records ko find karo.
```sql
+----------+------------+--------+
| emp_name | department | salary |
+----------+------------+--------+
| AMIT     | IT         | 50000  |
| ROHIT    | NULL       | 60000  |
| NEHA     | IT         | 70000  |
+----------+------------+--------+

-- sql
SELECT * FROM employees
WHERE department IS NULL;

-- output
+----------+------------+--------+
| emp_name | department | salary |
+----------+------------+--------+
| ROHIT    | NULL       | 60000  |
+----------+------------+--------+
```

### **How do you replace NULL values?**
* “In MySQL, I can use COALESCE() to replace NULL values while retrieving data. For permanent replacement, I can use UPDATE with WHERE column IS NULL.”
```sql
+----------+------------+--------+
| emp_name | department | salary |
+----------+------------+--------+
| AMIT     | IT         | 50000  |
| ROHIT    | NULL       | 60000  |
| NEHA     | IT         | 70000  |
+----------+------------+--------+

-- Actual table mein NULL ko replace karna
UPDATE employees
SET department = 'Not Assigned'
WHERE department IS NULL;

-- sirf view mai show karna
SELECT 
    emp_name,
    COALESCE(department, 'Not Assigned') AS department
FROM employees;
```

### How do you update records based on another table?
* Ek table ki information use karke doosri table ke records ko update karna.
```sql
-- employees table                   -- department_updates
+----+----------+-------------+     +-------------+------------------+
| id | emp_name | department  |     | emp_id      | new_department   |
+----+----------+-------------+     +-------------+------------------+
| 1  | AMIT     | IT          |     | 1           | SALES            |
| 2  | ROHIT    | HR          |     | 3           | FINANCE          |
| 3  | NEHA     | IT          |     +-------------+------------------+
+----+----------+-------------+

-- Query
UPDATE employees e
JOIN department_updates d
    ON e.id = d.emp_id
SET e.department = d.new_department;
-- Yahan JOIN ka purpose hai dono tables ke matching records find karna, aur phir doosri table ki value se first table ko update karna.

-- result
+----+----------+------------+
| id | emp_name | department |
+----+----------+------------+
| 1  | AMIT     | SALES      |
| 2  | ROHIT    | HR         |
| 3  | NEHA     | FINANCE    |
+----+----------+------------+
```