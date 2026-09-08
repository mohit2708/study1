|  No.  | Salary related Logical Questions                                                                             |
| :---: | ------------------------------------------------------------------------------------------------------------ |
|       | [salary + department:- Department-wise Total Salary](#department-wise-total-salary)                          |
|       | [salary + department:- Highest Salary ka Department kaun sa hai?](#highest-salary-ka-department-kaun-sa-hai) |
|       | [salary + department:-Department Having Total Salary > 100000](#department-having-total-salary--100000)      |
|       | [salary + department:- Department-wise average salary?](#department-wise-average-salary)                     |

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
#### Find the Highest Salary of Each Department?
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