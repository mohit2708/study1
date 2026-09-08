|  No.  | Salary Logical Questions                                |
| :---: | ------------------------------------------------------- |
|       | [Salary:- Maximum salary](#find-maximum-salary)         |
|       | [Salary:- Nth Highest salary](#find-3rd-highest-salary) |
|       | [Salary:- Top Nth salary](#find-top-n-salaries)         |

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