### What is CTE (Common Table Expression) in MySQL?
* A CTE, or **Common Table Expression**, is a temporary named result set defined using the WITH clause. It is used to simplify complex queries, improve readability, and can be referenced by the main query. CTEs can also be recursive, which is useful for hierarchical data such as employee-manager relationships.
* CTE (Common Table Expression) ek **temporary named result set** hota hai jise hum complex SQL query ko readable aur reusable banane ke liye use karte hain.
* CTE **WITH keyword** se define hota hai.
```sql
-- syntax
WITH cte_name AS (
    SELECT ...
    FROM ...
    WHERE ...
)
SELECT *
FROM cte_name;
```

```sql
-- example
WITH it_employees AS (
    SELECT id, name, salary
    FROM employees
    WHERE department = 'IT'
)

-- calling
SELECT *
FROM it_employees;
```

#### CTE ka main advantage
* Complex query ko multiple logical steps mein divide kar sakte hain.
```sql
WITH dept_avg AS (
    SELECT
        department,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)

-- calling
SELECT *
FROM dept_avg
WHERE avg_salary > 70000;
```
* Step 1: CTE department-wise average salary calculate karta hai.
* Step 2: Outer query sirf woh departments filter karti hai jinki average salary 70000 se zyada hai.


### **With**
* WITH clause lets you store the result of a query in a temporary table using an alias. You can also define multiple temporary tables using a comma and with one instance of the WITH keyword.
* The WITH clause is also known as common table expression (CTE) and subquery factoring.
```sql
WITH temporary_name AS (
   SELECT *
   FROM table_name)
SELECT *
FROM temporary_name
WHERE column_name operator value;
```