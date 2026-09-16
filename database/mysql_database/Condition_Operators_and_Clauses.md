|  No.  | [SQL Comments?](#sql-comments)                            |
| :---: | --------------------------------------------------------- |
|       | [Equal to(=)](#equal-to)                                  |
|       | [Greater than(>)](#greater-than)                          |
|       | [Less than(<)](#less-than)                                |
|       | [Greater than or equal to(>=)](#greater-than-or-equal-to) |
|       | [Less than or equal to(<=)](#less-than-or-equal-to)       |
|       | [Not equal to(<> or !=)](#not-equal-to-or-)               |
|       | [WHERE](#where)                                           |
|       | [Truncate](#truncate)                                     |
|       | [IS NULL and IS NOT NULL](#is-null-and-is-not-null)       |
|       | [AND](#and)                                               |
|       | [OR](#or)                                                 |
|       | [NOT](#not)                                               |
|       | [IN Operator](#in-operator)                               |
|       | [NOT IN Operator](#not-in-operator)                       |
|       | [IF()](#if)                                               |
|       | [BETWEEN](#between)                                       |
|       | [NOT BETWEEN](#not-between)                               |
|       | [What is ORDER BY](#what-is-order-by)                     |


### 🎯**What is DISTINCT?**
* DISTINCT is used to **remove duplicate values** from the result set and **return only unique values**.
* DISTINCT is used to **eliminate duplicate rows from the result** set and return only unique values.
```sql
+--------+------------+
| emp_id | department |
+--------+------------+
| 1      | IT         |
| 2      | HR         |
| 3      | IT         |
| 4      | Sales      |
| 5      | HR         |
+--------+------------+

-- query
SELECT DISTINCT department FROM employees;

-- Output
+------------+
| department |
+------------+
| IT         |
| HR         |
| Sales      |
+------------+
```

* DISTINCT on Multiple Columns
```sql
SELECT DISTINCT department, salary
FROM employees;
```

* COUNT with DISTINCT
```sql
SELECT COUNT(DISTINCT department)
FROM employees;
```



### 🎯**EXPLAIN**
* EXPLAIN is used to view the query execution plan and understand how MySQL will execute a query, helping identify performance issues and optimize queries.
* EXPLAIN is used to analyze how MySQL executes a query. It shows the execution plan, such as which tables are accessed, which indexes are used, the join order, and the estimated number of rows scanned.
* Interview Points:-
  * **EXPLAIN does not execute the query; it shows the execution plan.**
  * Helps understand query performance.
  * Commonly used for query tuning and troubleshooting.
```sql
EXPLAIN SELECT * FROM employees
WHERE department_id = 10;

-- output
+----+-------------+-----------+------+---------------+----------------+---------+-------+------+-------+
| id | select_type | table     | type | possible_keys | key            | key_len | ref   | rows | Extra |
+----+-------------+-----------+------+---------------+----------------+---------+-------+------+-------+
| 1  | SIMPLE      | employees | ref  | idx_dept      | idx_dept       | 4       | const | 100  |       |
+----+-------------+-----------+------+---------------+----------------+---------+-------+------+-------+
```
| Column          | Meaning                                                    |
| --------------- | ---------------------------------------------------------- |
| `table`         | Table being accessed                                       |
| `type`          | Access method (ALL, index, range, ref, eq_ref, const)      |
| `possible_keys` | Indexes that could be used                                 |
| `key`           | Index actually used                                        |
| `rows`          | Estimated rows MySQL will scan                             |
| `Extra`         | Additional information (Using where, Using filesort, etc.) |


#### EXPLAIN ke output ka type column?
* const → Very fast (single row lookup)
  * Matlab: ek specific row ko directly find karna.
  ```sql
  SELECT * FROM employees WHERE id = 10;
  ```
* range → Uses index for a range search
* ALL → Full table scan (usually least efficient)
```sql
EXPLAIN output
      ↓
┌────┬─────────────┬───────┬──────┬───────────────┬─────┬─────────┬─────┬──────┬───────┐
│ id │ select_type │ table │ type │ possible_keys │ key │ key_len │ ref │ rows │ Extra │
└────┴─────────────┴───────┴──────┴───────────────┴─────┴─────────┴─────┴──────┴───────┘
                           ↑
                    ye ek column hai
                           ↓
                    const / range / ALL
```

### 🎯**What is ORDER BY?**
* ORDER BY clause is used to **sort the result** set based on one or more columns in ascending (ASC) or descending (DESC) order.
* The ORDER BY clause is used to arrange the records returned by a query in a specific order, either **ascending (ASC)** or **descending (DESC)**.
```sql
-- syntax
SELECT column_name FROM table_name ORDER BY column_name ASC/DESC;

-- Multiple Columns
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- with limit
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

-- use together GROUP BY and ORDER BY
SELECT category, SUM(quantity) AS total_quantity FROM sales
GROUP BY category ORDER BY total_quantity DESC;
```
* ASC (Ascending) is the default order.
* DESC is used for descending order.
* Can sort by one or multiple columns.
* Usually written at the end of the SELECT query.
* Commonly used with LIMIT to get top records.

### 🎯**BETWEEN**
* BETWEEN operator is used to filter records within a specified range. The range values are inclusive, meaning both the start and end values are included.
* The BETWEEN operator is used to retrieve records where a column value falls within a specified range, including both boundary values.
* BETWEEN works with numbers, dates, and strings.
* It is inclusive of both start and end values.
* It can make range conditions more readable than using >= and <=.

```sql
-- Example 1: Numbers
SELECT * FROM employees WHERE salary BETWEEN 30000 AND 50000;

-- Example 2: Dates
SELECT * FROM orders WHERE order_date BETWEEN '2026-01-01' AND '2026-01-31';

-- Equivalent Query
SELECT * FROM employees WHERE salary >= 30000 AND salary <= 50000;
```

### 🎯**NOT BETWEEN**
* NOT BETWEEN is used to retrieve records whose values do not fall within a specified range.
* The NOT BETWEEN operator is used to filter records where the column value is outside the specified range.
* NOT BETWEEN excludes the specified range.
* Works with numbers, dates, and strings.
* Equivalent to using < and > with OR.
* Since BETWEEN is inclusive, NOT BETWEEN excludes the boundary values as well.
```sql
-- syntax
SELECT column_name(s) FROM table_name WHERE column_name NOT BETWEEN value1 AND value2;

-- for number
SELECT * FROM employees WHERE salary NOT BETWEEN 30000 AND 50000;

-- Date Example
SELECT * FROM orders WHERE order_date NOT BETWEEN '2026-01-01' AND '2026-01-31';

-- Equivalent Query
SELECT * FROM employees WHERE salary < 30000 OR salary > 50000;
```

### 🎯**IN Operator**
* The IN operator is a shorthand for multiple OR conditions, It reduces the use of multiple OR conditions in SELECT, INSERT, UPDATE, and DELETE queries.
* The IN operator is used to retrieves results when the specified value matches any value in a set of values or is returned by a subquery. 
* This operator allows us to specify multiple values along with the WHERE clause. 
```sql
select * from customers
+----+----------+-----+-----------+-----------+
| cust_id | cust_name | city      | occupation|
+---------+-----------+-----------+-----------+
|  1      | Peter     | Londen    | Business  |
|  2      | Joseph    | Texas     | Doctor    |
|  3      | Mark      | New Delhi | Engineer  |        
|  4      | Michael   | New York  | Scientist |
|  5      | Alexander | Maxico    | Student   |
+---------+-----------+-----------+-----------+
mysql> SELECT * FROM customer WHERE occupation IN ('Doctor', 'Scientist', 'Engineer');

+----+----------+-----+-----------+-----------+
| cust_id | cust_name | city      | occupation|
+---------+-----------+-----------+-----------+
|  2      | Joseph    | Texas     | Doctor    |
|  3      | Mark      | New Delhi | Engineer  |        
|  4      | Michael   | New York  | Scientist |
+---------+-----------+-----------+-----------+
```

### 🎯**NOT IN Operator**
* selects all customers that are located in "Texas", or "New York":
```sql
SELECT * FROM Customers WHERE city NOT IN ('Texas', 'New York');

Output:-
+----+----------+-----+-----------+-----------+
| cust_id | cust_name | city      | occupation|
+---------+-----------+-----------+-----------+
|  1      | Peter     | Londen    | Business  |
|  3      | Mark      | New Delhi | Engineer  |        
|  5      | Alexander | Maxico    | Student   |
+---------+-----------+-----------+-----------+
```

### 🎯**Difference between IN and BETWEEN**
* IN → multiple specific values check karta hai
* BETWEEN → ek range ke andar values check karta hai
| `IN`                                | `BETWEEN`                                      |
| ----------------------------------- | ---------------------------------------------- |
| Multiple specific values ke liye    | Value ki range ke liye                         |
| Exact values match karta hai        | Lower aur upper limit ke beech check karta hai |
| `IN (10, 20, 30)`                   | `BETWEEN 10 AND 30`                            |
| Discrete values                     | Continuous range                               |
| `IN` multiple values ke liye useful | Numbers, dates, etc. ke range ke liye useful   |

### 🎯**GROUP BY**
* GROUP BY is used to **group rows that have the same value** in one or more columns.
* It is commonly used with aggregate functions like COUNT(), SUM(), AVG(), MIN(), and MAX().
* GROUP BY is used to group rows with the same values and perform aggregate calculations on each group.

#### Example of group by
```sql
+----+--------+------------+--------+
| id | name   | department | salary |
+----+--------+------------+--------+
| 1  | Mohit  | IT         | 50000  |
| 2  | Rahul  | IT         | 60000  |
| 3  | Amit   | HR         | 40000  |
| 4  | Raj    | HR         | 45000  |
+----+--------+------------+--------+

-- Query
SELECT department, COUNT(*) AS total_employees FROM employees
GROUP BY department;

-- output
+------------+-----------------+
| department | total_employees |
+------------+-----------------+
| HR         | 2               |
| IT         | 2               |
+------------+-----------------+

-- * GROUP BY department ne same department ke employees ko groups mein divide kar diya:
-- IT → Mohit, Rahul
-- HR → Amit, Raj

-- Example2 :- GROUP BY with SUM()
SELECT department, SUM(salary) AS total_salary FROM employees
GROUP BY department;

-- Output:-
+------------+-------------+
| department | total_salary|
+------------+-------------+
| HR         | 85000       |
| IT         | 110000      |
+------------+-------------+

-- GROUP BY + HAVING
SELECT department, COUNT(*) AS total FROM employees
GROUP BY department HAVING COUNT(*) > 2;
```

### 🎯**HAVING**
* HAVING is **used to filter grouped** results based on aggregate conditions.
* HAVING is **used to filter groups after GROUP BY**.
```sql
SELECT department, COUNT(*) AS total_employees FROM employees
GROUP BY department HAVING COUNT(*) > 1;
```

### 🎯**Difference between WHERE and HAVING clauses**
| WHERE                                                            | HAVING                                |
| ---------------------------------------------------------------- | ------------------------------------- |
| Filters rows                                                     | Filters groups                        |
| Used before `GROUP BY`                                           | Used after `GROUP BY`                 |
| Cannot normally use aggregate conditions like `COUNT()`, `AVG()` | Used with aggregate functions         |
| Example: `WHERE salary > 50000`                                  | Example: `HAVING AVG(salary) > 50000` |

### 🎯**Difference between DISTINCT and GROUP BY?**
| DISTINCT                                     | GROUP BY                                  |
| -------------------------------------------- | ----------------------------------------- |
| Removes duplicate rows                       | Groups rows for aggregation               |
| Used for unique values                       | Often used with COUNT, SUM, AVG, MAX, MIN |
| Simpler and usually preferred for uniqueness | Used when calculations are needed         |

### 🎯**Difference between GROUP BY and ORDER BY?**
| GROUP BY                                         | ORDER BY                          |
| ------------------------------------------------ | --------------------------------- |
| Rows ko groups mein combine karta hai            | Rows/result ko sort karta hai     |
| Mostly aggregate functions ke saath use hota hai | Sorting ke liye use hota hai      |
| `COUNT()`, `SUM()`, `AVG()` etc. ke saath common | `ASC` / `DESC` ke saath common    |
| Result mein groups banata hai                    | Result ka order change karta hai  |
| Example: department-wise count                   | Example: salary highest to lowest |

### 🎯**Difference between GROUP BY and HAVING?**
* **GROUP BY** → rows ko groups mein divide karta hai
* **HAVING** → un groups ko filter karta hai

| GROUP BY                                          | HAVING                                                      |
| ------------------------------------------------- | ----------------------------------------------------------- |
| Rows ko groups mein divide karta hai              | Groups ko filter karta hai                                  |
| Group create karta hai                            | Group par condition lagata hai                              |
| Usually aggregate functions ke saath use hota hai | Aggregate results par condition lagane ke liye use hota hai |
| `GROUP BY department`                             | `HAVING COUNT(*) > 5`                                       |

```sql
SELECT department, COUNT(*) FROM employees
WHERE salary > 50000
GROUP BY department
HAVING COUNT(*) > 5;
```


### 🎯**LIMIT**
* LIMIT is used to **restrict the number of rows** returned by a query.
* Agar table mein 100 records hain aur humein sirf 10 records chahiye, to LIMIT use karte hain.
```sql
-- syntax
SELECT column_name(s) FROM table_name LIMIT number;

-- Query
SELECT * FROM employees LIMIT 10;
```

### 🎯**LIMIT with OFFSET**
* First 20 rows → Skip
* Next 10 rows → Return
```sql
SELECT * FROM employees LIMIT 10 OFFSET 20;
```

## SQL Condition Operators and Clauses
### Comparison operators

#### Equal to(=)
```sql
WHERE salary = 50000
```

#### Greater than(>)
```sql
WHERE age > 30
```

#### Less than(<)
```sql
WHERE age < 30
```

#### Greater than or equal to(>=)
```sql
WHERE price >= 20.00
```

#### Less than or equal to(<=)
```sql
WHERE rating <= 4.5
```

#### Not equal to(<> or !=)
```sql
WHERE country <> 'USA'
```

### Logical operators

#### **AND**
* Displays a record if all conditions are TRUE
* AND is an operator that **combines two conditions**. **Both conditions must be true** for the row to be included in the result set.
* The MySQL AND Condition (also called the AND Operator) is used to test two or more conditions in a SELECT, INSERT, UPDATE, or DELETE statement.
```sql
-- syntex
SELECT column_name(s)
FROM table_name
WHERE column_1 = value_1 AND column_2 = value_2;
-- example
SELECT * FROM contacts
WHERE state = 'California' AND contact_id > 3000;
```

#### **OR**
* Displays a record if any of the conditions are TRUE
* OR is an operator that filters the result set to only include rows where either condition is true.
```sql
SELECT column_name
FROM table_name WHERE column_name = value_1 OR column_name = value_2;
```

#### **NOT**
* Reverses the logical outcome of an operator
```sql
WHERE NOT country = 'UK'
```

### Special operators
#### **WHERE**
* WHERE is a clause that indicates you want to filter the result set to include only rows where the following condition is true.
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator value;
```

#### **Truncate**
* A truncate SQL statement is used to **remove all rows** (complete data) from a table.
* TRUNCATE is a **DDL**(Data Definition Language) command and is used to delete all the rows or tuples from a table. Unlike the DELETE command, the TRUNCATE command does not contain a WHERE clause.
```sql
TRUNCATE TABLE table_name;
```

#### **ROUND()**
* The ROUND() function is used to round a numeric value to a specified number of decimal places.*
* syntex:- syntex:- ROUND(number, decimal_places)
```sql
SELECT ROUND(123.4567, 2);  -- Returns 123.46
SELECT ROUND(123.4567, 0);  -- Returns 123
SELECT ROUND(123.4567, -1); -- Returns 120 (rounds to the nearest 10)

-- example:-
SELECT ROUND(salary, 2) AS rounded_salary FROM employees;
```

#### **Case**
* CASE statements are used to create different outputs (usually in the SELECT statement). It is SQL’s way of handling if-then logic.
```sql
SELECT column_name,
  CASE
    WHEN condition THEN 'Result_1'
    WHEN condition THEN 'Result_2'
    ELSE 'Result_3'
  END
FROM table_name;
```


#### **With**
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

### **IS NULL and IS NOT NULL**
* IS NULL and IS NOT NULL are operators used with the WHERE clause to test for empty values.
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IS NULL;
```



### **IF()**
```sql
SELECT IF(200>350,'YES','NO'); -- Output:- NO
SELECT IF(251 = 251,' Correct','Wrong');  -- Output:- Correct

--
SELECT salary, IF(salary>3000,"Mature","Immature") As Result FROM employee;
+---------+----------+
| salary  | Result   |
+---------+----------+
| 2957.00 | Immature |
| 3100.00 | Mature   |
+---------+----------+
```
```sql
SELECT IF(STRCMP('Rinky Ponting','Yuvraj Singh')=0, 'Correct', 'Wrong');
```




#### **Group By**
* Group by statement is used to group the rows that have the same value. 
* It is used with aggregate functions for example AVG(), COUNT(), SUM()etc. 
```sql
SELECT category, SUM(quantity) AS total_quantity
FROM sales GROUP BY category;
| category  | total\_quantity |              |
| --------- | --------------- | ------------ |
| Fruit     | 18              | (10 + 5 + 3) |
| Vegetable | 11              | (7 + 4)      |
```




### **Difference between WHERE and HAVING in SQL?**
#### **Where**
* WHERE Clause is used to **filter** the records from the table or used while joining more than one table.
* Cannot be used with aggregate functions (like SUM(), COUNT(), AVG(), etc.).
```sql
SELECT * FROM emp WHERE salary > 50000;
```

#### **HAVING**
* HAVING Clause is used to filter the records from the groups based on the given condition in the HAVING Clause.
* It is applied after the grouping and aggregation of data.
```sql
SELECT department, COUNT(*) AS num_empl FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

| Having                                                           | Where                                                                      |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------- |
| Having ke sath GROUP BY use hota hai                             |                                                                            |
| Having post filter hai(data fatch hone ke baad filter lagta hai) | where pre filter hai(isme pahle filter lagta hai phir fatch data hota hai) |
| having can be used only with select command                      | can be used with select update delete                                      |
| HAVING is used for column operations.                            | WHERE is used for row operations                                           |
| having ke aggrigate function sath kar sakte hai                  | where ke sath aggrigate function use nahi kar sakte                        |
