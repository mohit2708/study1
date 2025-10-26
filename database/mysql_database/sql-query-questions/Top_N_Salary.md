### **Top N Salary?**
```sql
-- Using Limit
SELECT salary FROM employee ORDER BY salary DESC LIMIT 4
+----------+---------+
| emp_name | salary  |
+----------+---------+
| KAYLING  | 6000.00 |
| FRANK    | 3100.00 |
| SCARLET  | 3100.00 |
| JONAS    | 2957.00 |
| BLAZE    | 2750.00 |
+----------+---------+
-- using subquery
SELECT name, salary FROM employees
WHERE salary IN ( SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 5)
ORDER BY salary DESC;

-- In Oracle
SELECT SAL FROM(SELECT DISTINCT SAL FROM EMP WHERE SAL IS NOT NULL  ORDER BY SAL DESC)WHERE ROWNUM <6;
```