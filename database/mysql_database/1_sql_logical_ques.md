|  No.  | My SQL Logical Questions                                                                                     |
| :---: | ------------------------------------------------------------------------------------------------------------ |
|       | [Salary:- Maximum salary](#find-maximum-salary)                                                              |
|       | [Salary:- Nth Highest salary](#find-3rd-highest-salary)                                                      |
|       | [Salary:- Top Nth salary](#find-top-n-salaries)                                                              |
|       | [salary + department:- Department-wise Total Salary](#department-wise-total-salary)                          |
|       | [salary + department:- Highest Salary ka Department kaun sa hai?](#highest-salary-ka-department-kaun-sa-hai) |
|       | [salary + department:-Department Having Total Salary > 100000](#department-having-total-salary--100000)      |
|       | [salary + department:- Department-wise average salary?](#department-wise-average-salary)                     |
|       | [Duplicate values in a Table?](#how-to-find-duplicate-values-in-a-table)                                     |




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
```sql
SELECT salary FROM employees ORDER BY salary DESC LIMIT 2,1;
SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 2,1;

-- (OR) Standard style
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;

-- For DISTINCT duplicate salary ko handle karega
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;
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