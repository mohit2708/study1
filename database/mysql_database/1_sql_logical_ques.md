|  No.  | My SQL Logical Questions                                                                                     |
| :---: | ------------------------------------------------------------------------------------------------------------ |
|       | [Salary:- Maximum salary](#find-maximum-salary)                                                              |
|       | [Salary:- Nth Highest salary](#find-3rd-highest-salary)                                                      |
|       | [Salary:- Top Nth salary](#find-top-n-salaries)                                                              |
|       | [salary + department:- Department-wise Total Salary](#department-wise-total-salary)                          |
|       | [salary + department:- Highest Salary ka Department kaun sa hai?](#highest-salary-ka-department-kaun-sa-hai) |
|       | [salary + department:-Department Having Total Salary > 100000](#department-having-total-salary--100000)      |
|       | [salary + department:- Department-wise average salary?](#department-wise-average-salary)                     |
|       | [value count:- Email]()                                                                                      |
|       | [Duplicate values in a Table?](#how-to-find-duplicate-values-in-a-table)                                     |
|       | [Duplicate values remove](#duplicate-value-remove)                                                           |
|       | [Replace a column value:- M to F & F to M](#replace-a-column-values-from-male-to-female-and-female-to-male)  |





<div style="page-break-before: always;"></div>

### 🎯**Find Maximum Salary**
```sql
+----------+---------+
| emp_name | salary  |
+----------+---------+
| AMIT     | 50000   |
| ROHIT    | 90000   |
| NEHA     | 90000   |
| PRIYA    | 65000   |
+----------+---------+
```

* Sirf salary chaiye
```sql
SELECT MAX(salary) AS highest_salary FROM employees;

+------------+
| max_salary |
+------------+
| 90000      |
+------------+
```

* Employee with Maximum Salary (Name + Salary chahiye)
```sql
SELECT emp_name, salary FROM employees
WHERE salary = (
    SELECT MAX(salary) FROM employees
);

+----------+---------+
| emp_name | salary  |
+----------+---------+
| ROHIT    | 90000   |
| NEHA     | 90000   |
+----------+---------+
```
<div style="page-break-before: always;"></div>

### 🎯**Find 3rd Highest Salary**
```sql
+----------+---------+
| emp_name | salary  |
+----------+---------+
| AMIT     | 50000   |
| ROHIT    | 90000   |
| NEHA     | 70000   |
| PRIYA    | 80000   |
| RAVI     | 60000   |
+----------+---------+
```

#### Using Limit
* The limit clause has two components, the **First component** is to skip a number of rows from the top and the **second component** is to display the number of rows we want.

```sql
-- Syntex:- Using Limit
Select DISTINCT Salary from table_name order by Salary DESC limit n-1,1;

-- 3rd highest salary
SELECT salary FROM employees ORDER BY salary DESC LIMIT 2,1;
SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 2,1;

-- (OR) Standard style
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;

-- For DISTINCT duplicate salary ko handle karega
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;

-- Example:- 4th Highest salary using limit
Select DISTINCT emp_name, salary from Employee order by salary DESC limit 3,1;
```

#### Using Subquery
```sql
SELECT MAX(salary) AS third_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
);

+----------------------+
| third_highest_salary |
+----------------------+
| 70000                |
+----------------------+
```
<div style="page-break-before: always;"></div>

#### Employee name ke sath 3rd Highest Salary
* Using Sub Query 
```sql
SELECT emp_name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
        WHERE salary < (
            SELECT MAX(salary)
            FROM employees
        )
    )
);

+----------+---------+
| emp_name | salary  |
+----------+---------+
| NEHA     | 70000   |
+----------+---------+
```

* Agar Duplicate hai to dono print honge
```sql
+----------+---------+
| emp_name | salary  |
+----------+---------+
| NEHA     | 70000   |
| RAVI     | 70000   |
+----------+---------+
```

#### Using DENSE_RANK() (Most Preferred for Experienced Interview)

#### Using COUNT() Subquery
<div style="page-break-before: always;"></div>

### 🎯**Find Top n Salaries**

#### Find Top 4 Salaries
* Using Limit
```sql
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 4;

-- with name isme distinct nahi aayega
SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 4;
```

* DISTINCT salaries ke saath employees ke names bhi chahiye to using Subquery
```sql
SELECT emp_name, salary
FROM employees
WHERE salary IN (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 4
)
ORDER BY salary DESC;
```


* Using Subquery
```sql
SELECT emp_name, salary
FROM (
    SELECT emp_name,
           salary,
           DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
    FROM employees
) AS temp
WHERE rnk <= 4;

-- In Oracle
SELECT SAL FROM(SELECT DISTINCT SAL FROM EMP WHERE SAL IS NOT NULL  ORDER BY SAL DESC)WHERE ROWNUM <6;
```
<div style="page-break-before: always;"></div>


### 🎯**Department salary Question**
```sql
+----------+------------+---------+
| emp_name | department | salary  |
+----------+------------+---------+
| AMIT     | IT         | 50000   |
| ROHIT    | HR         | 60000   |
| NEHA     | IT         | 70000   |
| PRIYA    | HR         | 80000   |
| RAVI     | SALES      | 40000   |
+----------+------------+---------+
```

#### Department-wise Total Salary

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees GROUP BY department;

+------------+--------------+
| department | total_salary |
+------------+--------------+
| HR         | 140000       |
| IT         | 120000       |
| SALES      | 40000        |
+------------+--------------+
```

#### Highest Salary ka Department kaun sa hai?
```sql
SELECT department, SUM(salary) AS total_salary FROM employees
GROUP BY department
ORDER BY total_salary DESC
LIMIT 1;

+------------+--------------+
| department | total_salary |
+------------+--------------+
| HR         | 140000       |
+------------+--------------+
```
<div style="page-break-before: always;"></div>

#### Department Having Total Salary > 100000
```sql
SELECT department, SUM(salary) AS total_salary
FROM employees GROUP BY department
HAVING SUM(salary) > 100000;

+------------+--------------+
| department | total_salary |
+------------+--------------+
| HR         | 140000       |
| IT         | 120000       |
+------------+--------------+
```

#### Department-wise average salary?
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees GROUP BY department;

+------------+-------------+
| department | avg_salary  |
+------------+-------------+
| HR         | 70000       |
| IT         | 60000       |
| SALES      | 45000       |
+------------+-------------+
```
<div style="page-break-before: always;"></div>

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

* Only duplicate emails
```sql
SELECT email, COUNT(email) AS total_email FROM Person
GROUP BY email HAVING COUNT(email) > 1;

+-----------------+-------------+
| email           | total_email |
+-----------------+-------------+
| mohit@gmail.com |           2 |
| rahul@gmail.com |           2 |
+-----------------+-------------+
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