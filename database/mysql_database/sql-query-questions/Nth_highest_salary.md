### **Nth highest salary?**
* The limit clause has two components, the **First component** is to skip a number of rows from the top and the **second component** is to display the number of rows we want.
```sql
-- Syntex:- Using Limit
Select DISTINCT Salary from table_name order by Salary DESC limit n-1,1;
(OR) SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET N-1;
+----------+---------+
| emp_name | salary  |
+----------+---------+
| JONAS    | 2957.00 |
+----------+---------+
-- Example:- 4th Highest salary using limit
Select DISTINCT emp_name, salary from Employee order by salary DESC limit 3,1;

-- Using Subquery:- 3rd higest salery
SELECT MAX(salary) AS ThirdHighestSalary FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee));
+-------------+
| MAX(salary) |
+-------------+
|     2957.00 |
+-------------+
```