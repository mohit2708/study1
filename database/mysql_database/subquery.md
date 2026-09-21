### **What is a Nested Query?**
### **What is a Subquery?**
* A Subquery (also called an Inner Query or Nested Query) is a query written inside another SQL query.
* The inner query executes first, and its result is used by the outer query.
* Subqueries can be used in SELECT, WHERE, FROM, HAVING, INSERT, UPDATE, and DELETE statements. They can be single-row, multi-row, or correlated subqueries.
```sql
SELECT column_name
FROM table_name
WHERE column_name OPERATOR (
    SELECT column_name
    FROM another_table
);
```


### Types of Subqueries?

#### 1. Single Row Subquery
* Jo subquery sirf 1 row return kare usse Single-Row Subquery kehte hain.
```sql
SELECT *
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);

-- inner query
SELECT AVG(salary)
FROM employees;
+-------------+
| AVG(salary) |
+-------------+
| 60000       |
+-------------+
-- Sirf 1 row return hui. Isliye ye Single-Row Subquery hai.
```

#### 2. Multiple Row Subquery
* Jo subquery multiple rows return kare usse Multi-Row Subquery kehte hain.
```sql
SELECT *
FROM employees
WHERE dept_id IN
(
    SELECT dept_id
    FROM departments
);
```

#### 3. Correlated Subquery
* A correlated subquery is a subquery that references columns from the outer query and is executed once for each row processed by the outer query.
* The inner query depends on the outer query and runs for each row.
```sql
SELECT e1.*
FROM employees e1
WHERE salary >
(
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e1.dept_id = e2.dept_id
);
```

### **What is a Scalar Subquery?**
* A Scalar Subquery is a subquery that **returns exactly one row and one column (a single value)**.
* Because it returns a single value, it can be used anywhere a normal value can be used.

```sql
-- Scalar Subquery in SELECT
SELECT
    name,
    salary,
    (
        SELECT AVG(salary)
        FROM employees
    ) AS avg_salary
FROM employees;

+-------+--------+------------+
| name  | salary | avg_salary |
+-------+--------+------------+
| Mohit | 50000  | 60000      |
| Amit  | 70000  | 60000      |
| Ravi  | 40000  | 60000      |
+-------+--------+------------+


-- Scalar Subquery in UPDATE
UPDATE employees
SET bonus = 5000
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);
```

* yha Confusion ye hai ki outer query multiple rows return kar rahi hai, lekin Scalar Subquery khud kitni rows return kar rahi hai, ye dekhna hota hai.

```sql
SELECT name, salary
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);

-- outer query
SELECT name, salary
FROM employees
WHERE salary > (...)

-- Scalar Subquery:- Bracket ke andar wala query:
-- Aur kyunki ye 1 row + 1 column return karta hai, isliye ye Scalar Subquery hai.
SELECT AVG(salary)
FROM employees
```