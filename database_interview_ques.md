# 🎯 Mysql Interview Questions

### 🧠 [**Database**](/database/mysql_database/Database.md)
1. What is a database?
   1. Database:- Show
   2. Database:- Create
   3. Database:- Rename
   4. Database:- Drop/Delete
   5. Database:- Select
2. What Is DBMS?
3. What Is RDBMS?
4. Difference between DBMS & RDBMS?


### 🧠 [**Mysql Basic Questions**](/database/mysql_database/2_sql_questions.md)
1. [What is MySQL?](/database/mysql_database/2_sql_questions.md#what-is-mysql)
2. [Check version of the sql?](/database/mysql_database/1_mysql.md#check-version-of-the-sql)
3. What are the features of MySQL?
4. What is the difference between SQL and MySQL?
5. What are databases and tables?
6. sql comments?
7. What are rows and columns?
8. What are MySQL data types?
9. What is NULL?
10. ⭐ [Difference between CHAR and VARCHAR?](/database/mysql_database/2_sql_questions.md#difference-between-char-vs-varchar)
11. Difference between INT and BIGINT?
12. What is AUTO_INCREMENT?
13. ⭐ Difference between WHERE and HAVING clauses?
14. [Wildcard Characters/Like Query?](/database/mysql_database/Wildcard_Characters_Like%20Query.md)

### 🧠 [**User Management**](/database/mysql_database/User_Management.md)
1. Create Databse user?
2. Show Databse user?
3. Show Current user?
4. User Password Change?
5. Drop User?
6. Grant Privileges to the MySQL New User?
7. Show Privileges?
8. REVOKE Privileges?

### 🧠 [**Aggregate function**](/database/mysql_database/Aggregate_function.md)
1. What is Aggregate function?
   1. SUM() function
   2. AVG
   3. MAX
   4. MIN
   5. COUNT
2. [COUNT() vs COUNT(*) in MySQL?](/database/mysql_database/Aggregate_function.md#-count-vs-count-in-mysql)
3. Can aggregate functions be used without GROUP BY?
4. How does COUNT handle NULL values?


What is GROUP BY?
What is HAVING?
Find department-wise employee count.


### 🧠 [**Mysql Keys Questions**](/database/mysql_database/keys.md)
1. [Primary Key?]
   1. [primary Key:- Add]
   2. [primary Key:- Delete]
2. [Unique Key?]
   1. [ALTER unique key?]
   2. [Drop unique key?]
3. ⭐ [Difference between Primary Key & Unique Key?]
4. [Foreign Key?]
   1. [Foreign Key Add/ALTER?]
   2. [DROP Foreign Key?]
5. [Composite Key?]
6. [Difference between Primary Key & Foreign Key?]

### 🧠 [**Mysql joins Questions**](/database/mysql_database/Joins.md)
1. [What Is Joins?]
2. [self join]
3. [INNER JOIN]
4. When do you use SELF JOIN?
5. [Left JOIN/LEFT OUTER JOIN]
6. [Right JOIN]
7. [Outer join](/database/mysql_database/Joins.md#outer-join)
8. [CROSS Join](/database/mysql_database/Joins.md#cross-join)
9. [Full Join/FULL OUTER JOIN]
10. Difference between INNER JOIN and OUTER JOIN?
11. Difference between LEFT JOIN and RIGHT JOIN?

### 🧠 [**Mysql Normalization Questions**](/database/mysql_database/normalization_denormalization.md)
1. What is Normalization?
2. Why do we need Normalization?
3. Advantages and disadvantages of Normalization?
4. What is 1NF?
5. What is 2NF?
6. What is 3NF?
7. What is BCNF?
8. What is 4NF?
9. What is 5NF?
10. What is Functional Dependency?
11. What is Transitive Dependency?
12. Difference between 3NF and BCNF?

### 🧠 [**Mysql Union & Union All Questions**](/database/mysql_database/union_and_union_all.md)
1. What is UNION?
2. [What Is Union & Union All?](/database/mysql_database/union_and_union_all.md#what-is-union--union-all)
3. [Difference between Union & Union All?]
4. [What is MINUS?](/database/mysql_database/MINUS.md#what-is-minus)
5. What is EXCEPT?
6. [What is Intersect?](/database/mysql_database/Intersect.md#what-is-intersect)


### 🧠 [**Mysql View Questions**](/database/mysql_database/View.md)
1. What is View?
   1. Create view
   2. Show view
   3. Alter view
   4. Deleted view
2. Why use Views?
3. Views used in real projects?


Difference between View and Table?
Can data be inserted into a View?
What is a Materialized View?
How to create a View?
Advantages of Views?

### 🧠 [**Mysql Index Questions**](/database/mysql_database/Index.md)
1. What is Index?
2. Why are Indexes used?
3. Types of Indexes
4. Unique Indexes
5. Show Index
6. Alter/Modify an Index
7. Drop Index
8. Unique Indexes
9. Cluster Index
10. Non cluster index
11. difference between cluster and non cluster index?
12. What is Composite Index?
13. How do indexes improve performance?
14. Can indexes slow down performance?
15. How to check indexes on a table?

### 🧠 **Mysql Logical Questions**
1. [Duplicate values in a Table?](/database/mysql_database/sql-query-questions/find_duplicate_value.md)
2. [Duplicate values remove]
3. [value count:- Email]
4. [Replace a column value:- M to F & F to M]
<div style="page-break-before: always;"></div>

#### 🧠 **Mysql Salary logical Questions**
1. [Salary:- Maximum salary](/database/mysql_database/1_sql_logical_ques.md#find-maximum-salary)
2. [Salary:- Nth Highest salary]
3. [Salary:- Top Nth salary]
4. [salary + department:- Department-wise Total Salary]
5. [salary + department:- Highest Salary ka Department kaun sa hai?]
6. [salary + department:-Department Having Total Salary > 100000]
8. [salary + department:- Department-wise average salary?]
⭐



📚 MySQL Interview Questions (Topic-Wise)
🧠 1. MySQL Basics
What is a Candidate Key?
What is a Super Key?
Can a table have multiple Primary Keys?
Can a Foreign Key contain NULL values?
What are constraints in MySQL?
🔍 3. SELECT Queries
What is SELECT?
Difference between WHERE and HAVING?
What is DISTINCT?
What is ORDER BY?
What is LIMIT?
Difference between GROUP BY and ORDER BY?
What is LIKE?
Difference between IN and EXISTS?
What is BETWEEN?
What is CASE statement?
🔗 4. Joins

📊 5. Aggregate Functions


🏆 6. SQL Query-Based Questions
Find the 2nd highest salary.
Find the 3rd highest salary.
Find duplicate records.
Delete duplicate records.
Find employees earning more than average salary.
Find the highest salary in each department.
Find departments having more than 5 employees.
Find nth highest salary.
Find records without duplicates.
Find top 5 highest salaries.

🔒 10. Transactions
What is a Transaction?
What are ACID properties?
What is COMMIT?
What is ROLLBACK?
What is SAVEPOINT?
What is Auto Commit?
What is Transaction Isolation Level?
Difference between COMMIT and ROLLBACK?
What causes deadlocks?
How do you handle deadlocks?
🛡️ 11. Locks
What is Locking?
What is Shared Lock?
What is Exclusive Lock?
Difference between Row-Level and Table-Level Lock?
What is Deadlock?
How does MySQL resolve deadlocks?
What is Optimistic Locking?
What is Pessimistic Locking?
🚀 12. Performance Optimization
How do you optimize SQL queries?
What is EXPLAIN?
How do you identify slow queries?
What is Query Cache?
What is Partitioning?
What are execution plans?
How do indexes affect performance?
What is Denormalization?
How do you optimize JOINs?
What is a covering index?
🏗️ 13. Stored Procedures & Functions
What is a Stored Procedure?
What is a Function?
Difference between Procedure and Function?
Advantages of Stored Procedures?
How do you create a Procedure?
Can a Function return multiple values?
What are IN, OUT, and INOUT parameters?
⚙️ 14. Triggers
What is a Trigger?
Types of Triggers?
BEFORE INSERT Trigger?
AFTER INSERT Trigger?
BEFORE UPDATE Trigger?
AFTER UPDATE Trigger?
Advantages and disadvantages of Triggers?
Difference between Trigger and Stored Procedure?
🔄 15. UNION & Subqueries

What is a Subquery?
What is a Correlated Subquery?
What is a Nested Query?
EXISTS vs IN?
Scalar Subquery?
Single-row vs Multi-row Subquery?
🏢 16. Database Design
What is ER Diagram?
What is Cardinality?
One-to-One Relationship?
One-to-Many Relationship?
Many-to-Many Relationship?
What is Referential Integrity?
How do you design a scalable database?
🔥 17. MySQL Advanced Questions
What is a Cursor?
What is Partitioning?
What is Replication?
Master-Slave Replication?
What is Sharding?
What is a Temporary Table?
What is CTE (Common Table Expression)?
Difference between DELETE, TRUNCATE, and DROP?
What is an Execution Plan?
What is MySQL Engine?
⭐ 18. MySQL Scenario-Based Questions
How would you find duplicate records in a table?
How would you improve a slow query?
A query is taking 10 seconds. How will you debug it?
How would you handle millions of records?
How would you design a banking transaction system?
How would you prevent duplicate entries?
How would you optimize a JOIN query?
How would you archive old data?
How would you handle deadlocks?
How would you design an e-commerce database?
🎯 Most Important Interview Topics (Must Prepare)

✅ Joins
✅ Keys & Constraints
✅ Normalization (1NF, 2NF, 3NF, BCNF)
✅ Indexes
✅ Transactions & ACID
✅ Aggregate Functions
✅ GROUP BY & HAVING
✅ Subqueries
✅ UNION vs UNION ALL
✅ DELETE vs TRUNCATE vs DROP
✅ 2nd/3rd Highest Salary Queries
✅ Views
✅ Stored Procedures & Triggers
✅ Performance Optimization (EXPLAIN, Indexing)
✅ Locks & Deadlocks
✅ Database Design & Relationships


### Table of Contents
<!-- ❌ 👉 👈 🧠 ✅ 📌 🔧 🧪 🔍 -->
||  No.  | [Database](#database)                                                            |
| :---: | -------------------------------------------------------------------------------- |
|       | [What is storage engine/Table Types in mysql?](#what-is-storage-engine-in-mysql) |

|  No.  | [Tables](#tables)                                                                                |
| :---: | ------------------------------------------------------------------------------------------------ |
|       | [Types of SQL Commands/subsets of SQL?](#types-of-sql-commandssubsets-of-sql)                    |
|       | [Data Definition Language (DDL)](#types-of-sql-commandssubsets-of-sql)                           |
|       | [Data Manipulation Language (DML)](#types-of-sql-commandssubsets-of-sql)                         |
|       | [Data Control Language (DCL)](#types-of-sql-commandssubsets-of-sql)                              |
|       | [Transaction Control Language (TCL)](#types-of-sql-commandssubsets-of-sql)                       |
|       | --------------------------------------------------------------                                   |
|       | [Alter](#alter)                                                                                  |
|       | [ADD a column in the table](#add-a-column-in-the-table)                                          |
|       | [Add column after particular field](#add-column-after-particular-field)                          |
|       | [Add column in first](#add-column-in-first)                                                      |
|       | [Add multiple columns in the table](#add-multiple-columns-in-the-table)                          |
|       | --------------------------------------------------------------                                   |
|       | [RENAME column in table?](#rename-column-in-table)                                               |
|       | [UPDATE](#update)                                                                                |
|       | [DELETE](#delete)                                                                                |
|       | [Change Datatype from alter cmd?](./4_Tables.md#change-datatype-from-alter-cmd)                  |
|       | [DROP column in table?](./4_Tables.md#drop-column-in-table)                                      |
|       | [TRUNCATE table?](#truncate)                                                                     |
|       | [RENAME table name?](#rename-table-name)                                                         |
|       | [Difference between Delete, Truncate & Drop?](#ques-difference-between-delete-truncate--drop)    |
|       | [Difference b/w DROP and TRUNCATE statements?](#ques-difference-bw-drop-and-truncate-statements) |


|  No.  | [SQL Comments?](#sql-comments)                                                                                  |
| :---: | --------------------------------------------------------------------------------------------------------------- |
|       | [Difference between In and Between Operator in SQL?](#ques-difference-between-in-and-between-operator-in-sql)   |
|       | [BETWEEN and NOT BETWEEN Operator?](#ques-between-and-not-between-operator)                                     |
|       | [Difference between WHERE and HAVING in SQL?](#difference-between-where-and-having-in-sql)                      |
|       | [Ques. Difference between Group By And Order By?](#ques-difference-between-group-by-and-order-by)               |
|       | [What is Aggregate function?(sum,avg,max,min,count)](#what-is-aggregate-function)                               |
|       | [SQL Operators and Clauses](#sql-operators-and-clauses)                                                         |
|       | [LIKE](#like)                                                                                                   |
|       | [INNER JOIN](#inner-join)                                                                                       |
|       | [OUTER JOIN](#outer-join)                                                                                       |
|       | [IF()](#if)                                                                                                     |
|       | [IFNULL](#ifnull)                                                                                               |
|       | [NULLIF](#nullif)                                                                                               |
|       | [IS NULL and IS NOT NULL](#is-null-and-is-not-null)                                                             |
|       | [Round()](#round)                                                                                               |
|       | [BETWEEN()](#between)                                                                                           |
|       | [Case](#case)                                                                                                   |
|       | [GROUP BY](#group-by)                                                                                           |
|       | [Having](#having)                                                                                               |
|       | [Limit](#limit)                                                                                                 |
|       | [ORDER BY](#order-by)                                                                                           |
|       | [SELECT DISTINCT](#select-distinct)                                                                             |
|       | [With()](#with)                                                                                                 |
|       | [WHERE](#where)                                                                                                 |
|       | [Wildcard Characters/Like Query](#wildcard-characterslike-query)                                                |
|       | [what is Aliases?](#aliases)                                                                                    |
|       | [What Is Union & Union All](#ques-what-is-union--union-all)                                                     |
|       | [What is Intersect?](#what-is-intersect)                                                                        |
|       | [What is MINUS?](#what-is-minus)                                                                                |
|       | [Optimizing SQL Queries for Faster Performance?](#ques-optimizing-sql-queries-for-faster-performance)           |
|       | ------------------------------                                                         |
|       | [What is ACID property/SQL TRANSACTIONS?](#ques-what-is-acid-propertysql-transactions) |

|  No.  | interview_Questions_answers                                       |
| :---: | ----------------------------------------------------------------- |
|       | [What are Constraints in SQL?](#ques-what-are-constraints-in-sql) |


|  No.  | [Sql Query questions](#sql-query-questions)                                                                                                |
| :---: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|       | [Demo data for execute the query](#demo-data-for-execute-the-query)                                                                        |
|       | [Current date?](#current-date)                                                                                                             |
|       | [How to copy a table in another table?](#ques-how-to-copy-a-table-in-another-table)                                                        |
|       | [How to copy structure of a table but not data?](#ques-how-to-copy-structure-of-a-table-but-not-data)                                      |
|       | [Duplicate table through another table, with structure and data?](#duplicate-table-through-another-table-with-structure-and-data)          |
|       | [How to find **Nth** highest salary from a table?](#nth-highest-salary)                                                                    |
|       | [Top Nth Salery?](#top-N-salery)                                                                                                           |
|       | [Find the Highest Salary of Each Department?](#find-the-highest-salary-of-each-department)                                                 |
|       | [How to Find Duplicate values in a Table?](#how-to-find-duplicate-values-in-a-table)                                                       |
|       | [Delete Duplicate Records?](#delete-duplicate-records)                                                                                     |
|       | [Check max_salary is not exceed the upper limit of 25000](#create-a-table-and-check-max_salary-is-not-exceed-the-upper-limit-of-25000)     |
|       | [Replace a Column Values from 'male' to 'female' and 'female' to 'male'?](#replace-a-column-values-from-male-to-female-and-female-to-male) |
|       | [Update remaing days startdate - enddate](#update-remaing-days-startdate---enddate)                                                        |
|       | [Count phone number](#count-phone-number)                                                                                                  |



<!-- ![asdf](./img/mohit_pic.jpg){width=600 height=500} -->

https://www.w3resource.com/sql-exercises/joins-hr/sql-joins-hr-exercise-11.php