### Back To TOP

|  No.  | My SQL Questions                                                                               |
| :---: | ---------------------------------------------------------------------------------------------- |
|       | [What is MySQL](#what-is-mysql)                                                                |
|       | [What is Sql?](#what-is-sql)                                                                   |
|       | [What is the difference between SQL and MySQL?](#what-is-the-difference-between-sql-and-mysql) |
|       | [Difference between SQL and NoSQL?](#mysql-vs-nosql)                                           |


|  No.  | Other Questions                                                                              |
| :---: | -------------------------------------------------------------------------------------------- |
|       | [What is ACID property/SQL TRANSACTIONS](#what-is-acid-propertysql-transactions)             |
|       | [Difference between CHAR vs VARCHAR](#difference-between-char-vs-varchar)                    |
|       | [Difference between Delete, Truncate & Drop?](#difference-between-delete-truncate--drop)     |
|       | [Difference between WHERE and HAVING clauses?](#difference-between-where-and-having-clauses) |
|       | [SQL Comments?](#sql-comments)                                                               |
|       | [constraints](#what-are-constraints-in-mysql)                                                |
|       | [Aliases?](#aliases)                                                                         |

<div style="page-break-before: always;"></div>

|  No.  |                                                                               |
| :---: | ----------------------------------------------------------------------------- |
|       | [What is MINUS?](#what-is-minus)                                              |
|       | [What is EXCEPT?](#what-is-except)                                            |
|       | [What is Intersect?](#what-is-intersect)                                      |



<div style="page-break-before: always;"></div>

### 🎯**What is MySQL?**
- MySQL is an open-source relational **database management system** (RDBMS) that uses SQL to store, manage, and retrieve data.
- It's commonly used for managing data in web applications and is known for its performance and ease of use.

[🔝 Back to Top](#back-to-top)

### 🎯**What is Sql?**
* SQL is stands for **structure query language**. 
* SQL (Structured Query Language) is a standard language used to **create**, **read**, **update**, and **delete** data in relational databases. It is also used to create and modify database structures such as tables.
* SQL language hai, database nahi.


### 🎯**What is the difference between SQL and MySQL?**
- SQL is a standard language used to communicate with relational databases, whereas MySQL is an RDBMS that uses SQL to store, manage, and retrieve data.
- SQL → Language
- MySQL → RDBMS / Database Management System
  
<div style="page-break-before: always;"></div>

### 🎯**MySQL vs NoSQL?**
* **MySQL** is a **relational database** that stores data in tables with **predefined schemas** and uses SQL for querying.
* **NoSQL** is a **non-relational database** that stores data in **flexible formats such as documents, key-value pairs, graphs, or columns**, making it suitable for large-scale and rapidly changing applications.

#### When to Use MySQL?
* Banking Systems
* E-commerce Orders
* ERP/CRM Applications
* Applications requiring complex JOINs and transactions

#### When to Use NoSQL?
* Social Media Apps
* Real-time Analytics
* Chat Applications
* Large-scale Distributed Systems

| MySQL                              | NoSQL                                                           |
| ---------------------------------- | --------------------------------------------------------------- |
| Relational Database                | Non-Relational Database                                         |
| Data tables mein store hota hai    | Data documents, key-value, graph ya columns mein store hota hai |
| Fixed Schema                       | Flexible Schema                                                 |
| SQL language use karta hai         | Different query methods use karta hai                           |
| JOIN support karta hai             | JOIN support limited ya nahi hota                               |
| ACID transactions strong hote hain | Mostly scalability par focus                                    |
| Vertical Scaling (RAM/CPU badhao)  | Horizontal Scaling (servers badhao)                             |
| Complex relationships ke liye best | Large-scale data ke liye best                                   |
| Data consistency high              | High availability aur performance                               |
| Example: MySQL, PostgreSQL         | MongoDB, Redis, Cassandra                                       |

<div style="page-break-before: always;"></div>

### **Difference between SQL and NoSQL?**
- The main difference between SQL (Structured Query Language) and NoSQL (Not Only SQL) databases lies in how they store, manage, and retrieve data.
- Here's a breakdown of the key differences:
1. Data Structure:
   - SQL:
     - Relational databases use tables to store data in rows and columns.
     - Data is organized into predefined schemas with relationships (foreign keys) between tables.
     - Examples: MySQL, PostgreSQL, Oracle, MS SQL Server.
   - NoSQL:
     - Non-relational databases can store data in various formats such as key-value pairs, document-based, column-family, or graph-based.
     - More flexible schema (often schema-less or dynamic schemas), allowing changes in data structure without affecting the database.
     - Examples: MongoDB (document), Redis (key-value), Cassandra (column-family), Neo4j (graph).
2. Schema:
   - SQL:
     - Strict schema: data must adhere to a predefined structure (tables, columns, data types).
     - Changes to schema (adding/removing columns) can be complex.
   - NoSQL:
     - Flexible schema: no strict schema, data can be stored with varying structures.
     - Allows quick changes to the data model, making it ideal for rapidly evolving applications.
3. Scalability:
   - SQL:
     - Vertical scaling (scaling up by upgrading hardware resources like CPU, RAM).
     - More challenging to scale horizontally (across multiple machines).
   - NoSQL:
     - Horizontal scaling (scaling out by adding more servers or nodes).
     - Designed to handle large volumes of data and high-traffic loads more efficiently.
4. Transactions & Consistency:
   - SQL:
     - ACID (Atomicity, Consistency, Isolation, Durability) properties are strictly followed to ensure data integrity and reliability.
     - Best suited for applications where data consistency is critical (e.g., banking, financial systems).
   - NoSQL:
     - Most NoSQL databases follow the BASE (Basically Available, Soft state, Eventually consistent) model.
     - Designed to provide high availability and partition tolerance, but may allow some degree of eventual consistency.

5. Query Language:
- SQL:
  - Uses structured query language (SQL) for querying the database (e.g., SELECT, INSERT, UPDATE, DELETE).
  - Well-defined and standardized.
- NoSQL:
  - Query languages vary based on the type of NoSQL database (e.g., MongoDB uses its own query language).
  - Queries can be less standardized across NoSQL systems.
  - 
6. Use Cases:
- SQL:
  - Best suited for applications with complex querying needs, transactional systems, and when data consistency is paramount (e.g., banking, CRM systems).
- NoSQL:
  - Ideal for applications with large amounts of unstructured or semi-structured data, or when scalability and flexibility are more important than strict consistency (e.g., big data, real-time web apps, IoT).

7. Examples of Databases:
   - SQL: 
     - MySQL, PostgreSQL, SQLite, MS SQL Server, Oracle DB.
   - NoSQL: 
     - MongoDB, Cassandra, Couchbase, Redis, Neo4j.
<div style="page-break-before: always;"></div>


### 🎯**Difference between CHAR vs VARCHAR**
* Both of these data types are used for characters.
* CHAR is a **fixed-length data type**, whereas VARCHAR is a **variable-length data type**. 
* CHAR is suitable for **fixed-size values**, while VARCHAR is suitable for **values whose length can vary**.
* char occupies all the space and if space is remaining, then it fill all the blank space with "space". But in case of varchar, It takes only the required length & release remaining.
```sql
Char -> 10      | R | A | M | space | space | sapce | space | space | space | space |
Varchar -> 10   | R | A | M |   |   |   |   |   |   |   |
| R | A | M |
```
* varchar is better than Char in term of space. 
* char perform is better than varchar.
* Char max 256 characters, varchar 65535 characters.

```sql
-- CHAR Example
CREATE TABLE users (
    country_code CHAR(2)
);

INSERT INTO users (country_code)
VALUES ('IN'), ('US'), ('UK');

-- Yahan CHAR(2) suitable hai kyunki har country code ki length fixed 2 characters hai.

--
-- varchar example
-- jaise name 
CREATE TABLE users (
    name VARCHAR(50)
);
```
<div style="page-break-before: always;"></div>

### **Difference between Delete, Truncate & Drop?**
* DELETE removes selected rows and supports WHERE clause. TRUNCATE removes all rows from a table, keeps the structure, and is faster than DELETE. DROP removes the entire table including its structure, indexes, and data from the database. DELETE is DML, whereas TRUNCATE and DROP are DDL commands.

* **DELETE**
  * Used to remove specific rows from a table.
  * Supports WHERE clause.
  * Row-by-row deletion happens.
  * Triggers are fired.
  * Can be rolled back (inside a transaction).
  * Does not reset AUTO_INCREMENT.
```sql
DELETE FROM employees WHERE id = 10;
```

* TRUNCATE
  * Removes all records from a table.
  * Does not support WHERE.
  * Faster than DELETE because it doesn't scan rows one by one.
  * Resets AUTO_INCREMENT.
  * Table structure remains intact.
  * Usually does not fire DELETE triggers.
```sql
TRUNCATE TABLE employees;
```

* DROP
  * Deletes the entire table permanently.
  * Removes data, structure, indexes, constraints, and permissions.
  * Table no longer exists after execution.
  * Fastest operation.
  * To use the table again, it must be recreated.
```sql
DROP TABLE employees;
```
<div style="page-break-before: always;"></div>

### 🎯**Difference between WHERE and HAVING clauses?**
* WHERE **filters individual records before grouping**, whereas HAVING **filters groups after GROUP BY**. HAVING is mainly **used to apply conditions on aggregate functions** such as COUNT, SUM, and AVG.
```sql
-- WHERE → row filtering
SELECT * FROM employees
WHERE salary > 50000;

-- HAVING → group filtering
SELECT department, COUNT(*) FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
```

1. WHERE **filters rows**, while HAVING **filters groups**.
2. WHERE is applied **before** GROUP BY.
3. HAVING is applied **after** GROUP BY.
4. WHERE is generally used for **row-level conditions**.
5. HAVING is mainly used with aggregate functions like:
   1. COUNT()
   2. SUM()
   3. AVG()
   4. MAX()
   5. MIN()
6. WHERE cannot normally be used to filter an aggregate result directly.
7. HAVING can filter aggregate results.
8. WHERE can be used without GROUP BY.
9. HAVING is commonly used with GROUP BY.
10. Easy way to remember:
    1.  WHERE → Row filter
    2.  HAVING → Group filter

#### Example
1. WHERE
* Find employees whose salary is greater than 50,000:
```sql
id | name  | department | salary
---+-------+------------+-------
1  | Amit  | IT         | 50000
2  | Rahul | IT         | 60000
3  | Neha  | HR         | 40000
4  | Priya | HR         | 45000
5  | Raj   | IT         | 70000
```

```sql
SELECT * FROM employees WHERE salary > 50000;
```

1. HAVING
* Find departments where the average salary is greater than 50,000:
```sql
SELECT department, AVG(salary) AS avg_salary FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

#### Where VS Having
| WHERE                                                            | HAVING                                |
| ---------------------------------------------------------------- | ------------------------------------- |
| Filters rows                                                     | Filters groups                        |
| Used before `GROUP BY`                                           | Used after `GROUP BY`                 |
| Cannot normally use aggregate conditions like `COUNT()`, `AVG()` | Used with aggregate functions         |
| Example: `WHERE salary > 50000`                                  | Example: `HAVING AVG(salary) > 50000` |


#### Combining WHERE and HAVING:
```sql
SELECT department, COUNT(*) AS total FROM employees
WHERE salary > 40000 -- Filters rows before GROUP BY
GROUP BY department
HAVING COUNT(*) > 2;    -- Filters groups after GROUP BY
```
<div style="page-break-before: always;"></div>

### What are constraints in MySQL?
- Constraints are **rules applied to table columns** to ensure the accuracy, consistency, and integrity of data in a database.
- Constraints are like rules on a form
  - “This field is required” → NOT NULL
  - “Must be unique” → UNIQUE
  - “Must be at least 18 years old” → CHECK

#### Common MySQL Constraints
| Constraint       | Purpose                                                         |
| ---------------- | --------------------------------------------------------------- |
| `NOT NULL`       | Column cannot contain NULL values                               |
| `UNIQUE`         | All values in the column must be unique                         |
| `PRIMARY KEY`    | Uniquely identifies each row (`NOT NULL + UNIQUE`)              |
| `FOREIGN KEY`    | Maintains relationship between tables                           |
| `CHECK`          | Ensures values meet a condition                                 |
| `DEFAULT`        | Assigns a default value if none is provided                     |
| `AUTO_INCREMENT` | Automatically generates sequential numbers                      |
| CREATE INDEX     | Used to create and retrieve data from the database very quickly |
<div style="page-break-before: always;"></div>

[🔝 Back to Top](#back-to-top)
### **Aliases**
* AS is a keyword in SQL that allows you to rename a column or table using an alias.
* Aliases are used to give a table, or a column in a table, a temporary name.
* An alias is created with the **AS** keyword.

#### Alias Column Syntax:-
```sql
SELECT column_name AS alias_name FROM table_name;

-- Basic Column Alias
SELECT first_name AS name, last_name AS surname FROM employees;

-- Using quotes for aliases with spaces
SELECT 
    first_name AS 'Employee First Name',
    last_name AS 'Employee Last Name',
    salary AS 'Monthly Compensation'
FROM 
    employees;
    
-- Without AS keyword
SELECT first_name name, last_name surname FROM employees;

-- Simple Table Alias
SELECT e.first_name, e.last_name, d.department_name
FROM employees e JOIN departments d 
ON e.department_id = d.department_id;

-- Calculation with Alias
SELECT 
    product_name, 
    price * quantity AS total_value,
    (price * quantity) * 1.1 AS total_with_tax
FROM products;

-- Concatenation Alias
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    email AS contact_email
FROM customers;

-- Subquery with Alias
SELECT 
    (SELECT AVG(salary) FROM employees) AS avg_salary,
    (SELECT MAX(salary) FROM employees) AS max_salary;


-- Aggregate Function Aliases
SELECT 
    department_id,
    AVG(salary) AS average_salary,
    COUNT(*) AS employee_count,
    MAX(salary) AS highest_salary
FROM employees
GROUP BY department_id;

-- Conditional Aliases
SELECT 
    first_name,
    last_name,
    CASE 
        WHEN salary < 50000 THEN 'Junior'
        WHEN salary BETWEEN 50000 AND 100000 THEN 'Mid-Level'
        ELSE 'Senior'
    END AS salary_category
FROM employees;
```
<div style="page-break-before: always;"></div>



<div style="page-break-before: always;"></div>


<div style="page-break-before: always;"></div>

### 🎯**What is MINUS?**
* MINUS operator will return only those rows which are **unique(distinct)** in only first SELECT query and not those rows which are **common to both first and second** SELECT queries.
```sql
-- Employees                        -- Managers
| EmpID | EmpName | Department |  | EmpID | EmpName | Department |
| ----- | ------- | ---------- || ----- | ------- | ---------- |
| 1     | Alice   | HR         |    | 2     | Bob     | IT         |
| 2     | Bob     | IT         |    | 4     | David   | IT         |
| 3     | Charlie | Finance    |    | 6     | Frank   | Sales      |
| 4     | David   | IT         |    | 7     | Grace   | Marketing  |
| 5     | Eve     | Marketing  |

-- output:-
SELECT EmpID, EmpName, Department FROM Employees
MINUS
SELECT EmpID, EmpName, Department FROM Managers;
| EmpID | EmpName | Department |
| ----- | ------- | ---------- |
| 1     | Alice   | HR         |
| 3     | Charlie | Finance    |
| 5     | Eve     | Marketing  |
```

#### Key characteristics of the MINUS operator:
* **Returns distinct rows:** Only unique rows from the first query that are not found in the second are returned.
* **Requires compatible SELECT statements:** Both SELECT statements involved in the MINUS operation must have the same number of columns, and the corresponding columns must have compatible data types and be in the same order. 

* **Note:-** While MINUS is a standard SQL operator supported by many database systems (like Oracle, PostgreSQL), **MySQL does not** directly **support** the MINUS operator.

#### Achieving the MINUS functionality in MySQL:
* We can achieve the same results as MINUS in MySQL using various techniques, most commonly by combining **LEFT JOIN** and **WHERE** clauses, or using **subqueries** with **NOT IN** or **NOT EXISTS**.

1. Using LEFT JOIN
```sql
SELECT a.*
FROM table_a AS a
LEFT JOIN table_b AS b ON a.id = b.id
WHERE b.id IS NULL;
```

2. Using NOT IN
```sql
SELECT *
FROM table_a
WHERE id NOT IN (SELECT id FROM table_b);
```

3. Using NOT EXISTS
```sql
SELECT *
FROM table_a AS a
WHERE NOT EXISTS (SELECT 1 FROM table_b AS b WHERE a.id = b.id);
```

```sql
table_a

id	value
1	Apple
2	Banana
3	Cherry
4	Date

----------------------
table_b

id	value
2	Banana
4	Date

------Output:----------
id	value
1	Apple
3	Cherry
```

### 🎯**What is EXCEPT?**
* same as minus nothing different.
