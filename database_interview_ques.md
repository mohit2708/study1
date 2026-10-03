# 🎯 Mysql Interview Questions

### 🧠 [**Database**](/database/mysql_database/Database.md)
1. [What is a database?](/database/mysql_database/Database.md#what-is-a-database)
   1. [Database:- Show](/database/mysql_database/Database.md#show-database)
   2. Database:- Create :- **CREATE DATABASE databasename;**
   3. [Database:- Rename](/database/mysql_database/Database.md#rename-database)
   4. [Database:- Drop/Delete](/database/mysql_database/Database.md#drop-database)
   5. Database:- Select :- **USE YourDatabaseName;**
2. [What Is DBMS?](/database/mysql_database/Database.md#what-is-dbms)
3. [What Is RDBMS?](/database/mysql_database/Database.md#what-is-rdbms)
4. [Difference between DBMS & RDBMS?](/database/mysql_database/Database.md#difference-between-dbms--rdbms)


### 🧠 [**Mysql Basic Questions**](/database/mysql_database/2_sql_questions.md)
1. [What is MySQL?](/database/mysql_database/1_mysql.md#what-is-mysql)
2. [What is Sql?](/database/mysql_database/1_mysql.md#what-is-sql)
3. [Check version of the sql?](/database/mysql_database/1_mysql.md#check-version-of-the-sql)
4. [What are the features of MySQL?](/database/mysql_database/1_mysql.md#what-are-the-advantages-of-mysql)
5. [What is the difference between SQL and MySQL?](/database/mysql_database/1_mysql.md#what-is-the-difference-between-sql-and-mysql)
6. [Types of SQL Commands](/database/mysql_database/1_mysql.md#types-of-sql-commands)
   1. [DDL (Data Definition Language)](/database/mysql_database/1_mysql.md#ddl-data-definition-language)
   2. [DML (Data Manipulation Language)](/database/mysql_database/1_mysql.md#dml-data-manipulation-language)
   3. [DQL (Data Query Language)](/database/mysql_database/1_mysql.md#dql-data-query-language)
   4. [DCL (Data Control Language)](/database/mysql_database/1_mysql.md#dcl-data-control-language)
   5. [TCL (Transaction Control Language)](/database/mysql_database/1_mysql.md#tcl-transaction-control-language)
7. [What is MySQL Engine?](/database/mysql_database/1_mysql.md#what-is-storage-engine-in-mysql)
8. What are databases and tables?
9. What are rows and columns?
10. What is NULL?
11. [What are the different data types in MySQL?](/database/mysql_database/data_types.md#what-are-the-different-data-types-in-mysql)
12. ⭐ [Difference between CHAR and VARCHAR?](/database/mysql_database/data_types.md#difference-between-char-vs-varchar)
13. [Difference between CharField and TextField?](/database/mysql_database/data_types.md#difference-between-charfield-and-textfield)
14. Difference between INT and BIGINT?
15. What is AUTO_INCREMENT?
16. ⭐ [Difference between WHERE and HAVING clauses?](/database/mysql_database/Condition_Operators_and_Clauses.md#difference-between-where-and-having-clauses)
17. [Wildcard Characters/Like Query?](/database/mysql_database/Wildcard_Characters_Like%20Query.md)
18. [What is LIKE?](/database/mysql_database/Wildcard_Characters_Like%20Query.md)
19. [What is SELECT?](/database/mysql_database/2_sql_questions.md#what-is-select)
20. [What is DISTINCT?](/database/mysql_database/Condition_Operators_and_Clauses.md#what-is-distinct)
21. ⭐ [Difference between DELETE, TRUNCATE, and DROP?](/database/mysql_database/2_sql_questions.md#difference-between-delete-truncate--drop)
22. [What are Constraints in SQL?](/database/mysql_database/2_sql_questions.md#what-are-constraints-in-mysql)
23. [What are execution plans?](/database/mysql_database/2_sql_questions.md#what-are-execution-plans)

### 🧠 Comments
1. [sql comments?](/database/mysql_database/Comments.md#sql-comments)

### 🧠 Condition Operators and Clauses
1. [What is EXPLAIN?](/database/mysql_database/Condition_Operators_and_Clauses.md#explain)
2. [What is ORDER BY?](/database/mysql_database/Condition_Operators_and_Clauses.md#what-is-order-by)
3. [What is BETWEEN?](/database/mysql_database/Condition_Operators_and_Clauses.md#between)
4. [What is NOT BETWEEN?](/database/mysql_database/Condition_Operators_and_Clauses.md#not-between)
5. [IN Operator](/database/mysql_database/Condition_Operators_and_Clauses.md#in-operator)
6. [NOT IN Operator](/database/mysql_database/Condition_Operators_and_Clauses.md#not-in-operator)
7. [Difference between IN and BETWEEN](/database/mysql_database/Condition_Operators_and_Clauses.md#difference-between-in-and-between)
8. [What is CASE statement?](/database/mysql_database/Condition_Operators_and_Clauses.md#case)
9. [GROUP BY](/database/mysql_database/Condition_Operators_and_Clauses.md#group-by)
10. [Having](/database/mysql_database/Condition_Operators_and_Clauses.md#having)
11. [What is LIMIT?](/database/mysql_database/Condition_Operators_and_Clauses.md#limit)
12. [Limit with offset?](/database/mysql_database/Condition_Operators_and_Clauses.md#limit-with-offset)
13. [Difference between GROUP BY and ORDER BY?](/database/mysql_database/Condition_Operators_and_Clauses.md#difference-between-group-by-and-order-by)
14. ⭐ [Difference between GROUP BY and HAVING?](/database/mysql_database/Condition_Operators_and_Clauses.md#difference-between-group-by-and-having)
15. [IF()](/database/mysql_database/Condition_Operators_and_Clauses.md#if)
16. NO=====
17. [IFNULL](#ifnull)                                                                                             |
18. [NULLIF](#nullif)                                                                                             |
19. [IS NULL and IS NOT NULL](#is-null-and-is-not-null)                                                           |
20. [Round()](#round)
21. [WHERE](#where)                                                                                               |
22. [what is Aliases?](#aliases)                                                                                  |
23. [Optimizing SQL Queries for Faster Performance?](#ques-optimizing-sql-queries-for-faster-performance)         |

### 🔒Transactions
1. [What is a Transaction?](/database/mysql_database/ACID_property_SQL_TRANSACTIONS.md#sql-transactions)
2. [What are ACID properties?](/database/mysql_database/ACID_property_SQL_TRANSACTIONS.md#what-is-acid-property)
3. What is COMMIT?
4. What is ROLLBACK?
5. What is SAVEPOINT?
6. What is Auto Commit?
7. What is Transaction Isolation Level?
8. Difference between COMMIT and ROLLBACK?
9. What causes deadlocks?
10. How do you handle deadlocks?

### 🧠 [Locks](/database/mysql_database/Locking.md)
1. [What is Locking?](/database/mysql_database/Locking.md#what-is-locking)
2. [What is Shared Lock?](/database/mysql_database/Locking.md#1-shared-lock-read-lock)
3. [What is Exclusive Lock?](/database/mysql_database/Locking.md#2-exclusive-lock-write-lock)
4. [Difference between Row-Level and Table-Level Lock?](/database/mysql_database/Locking.md#row-level-vs-table-level-locking)
5. [What is Deadlock?](/database/mysql_database/Locking.md#what-is-dead-lock)
6. [How does MySQL resolve deadlocks?](/database/mysql_database/Locking.md#how-to-preventresolve-deadlocks)
7. [What is Optimistic Locking?](/database/mysql_database/Locking.md#why-use-optimistic-locking)
8. [What is Pessimistic Locking?](/database/mysql_database/Locking.md#what-is-pessimistic-locking)


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
1. [What is Aggregate function?](/database/mysql_database/Aggregate_function.md#-what-is-aggregate-function)
   1. SUM()
   2. AVG
   3. MAX
   4. MIN
   5. COUNT
2. [COUNT() vs COUNT(*) in MySQL?](/database/mysql_database/Aggregate_function.md#-count-vs-count-in-mysql)
3. Can aggregate functions be used without GROUP BY?
4. How does COUNT handle NULL values?


### 🧠 [**Mysql Keys Questions**](/database/mysql_database/keys.md)
1. [Primary Key?](/database/mysql_database/keys.md#primary-key)
   1. [primary Key:- Add](/database/mysql_database/keys.md#add-primary-key)
   2. [primary Key:- Delete](/database/mysql_database/keys.md#delete-primary-key)
2. [Unique Key?](/database/mysql_database/keys.md#what-is-unique-key)
   1. [ALTER unique key?]
   2. [Drop unique key?]
3. ⭐ [Difference between Primary Key & Unique Key?]
4. [Foreign Key?](/database/mysql_database/keys.md#what-is-foreign-key)
   1. [Foreign Key Add/ALTER?]
   2. [DROP Foreign Key?]
   3. Can a Foreign Key contain NULL values?
5. [Composite Key?](/database/mysql_database/keys.md#what-is-composite-key)
6. [What is a Candidate Key?](/database/mysql_database/keys.md#what-is-a-candidate-key)
7. [Difference between Primary Key & Unique Key?](/database/mysql_database/keys.md#ques-difference-between-primary-key--unique-key)
8. [Difference between Primary Key & Foreign Key?](/database/mysql_database/keys.md#ques-difference-between-primary-key--unique-key)

### 🧠 [**Mysql joins Questions**](/database/mysql_database/Joins.md)
1. [What Is Joins?]
2. [self join]
3. [INNER JOIN]
4. When do you use SELF JOIN?
5. [Left JOIN/LEFT OUTER JOIN]
6. [Right JOIN]
7. [Outer join](/database/mysql_database/Joins.md#outer-join)
8. [What is a cross join and when would you use it?](/database/mysql_database/Joins.md#cross-join)
9. [Full Join/FULL OUTER JOIN]
10. Difference between INNER JOIN and OUTER JOIN?
11. Difference between LEFT JOIN and RIGHT JOIN?
12. Difference between INNER JOIN and LEFT JOIN?

### 🧠 [**Mysql Normalization Questions**](/database/mysql_database/normalization_denormalization.md)
1. [What is Normalization?](/database/mysql_database/normalization_denormalization.md#what-is-normalization)
2. [Why do we need Normalization?](/database/mysql_database/normalization_denormalization.md#why-do-we-need-normalization)
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
1. [What is View?](/database/mysql_database/View.md#what-is-view)
   1. [Create view](/database/mysql_database/View.md#create-view)
   2. [Show view](/database/mysql_database/View.md#show-view)
   3. [Alter view](/database/mysql_database/View.md#alter-view)
   4. [Deleted view](/database/mysql_database/View.md#deleted-view)
2. [Why use Views?](/database/mysql_database/View.md#why-use-views)
3. [Can we insert data into a View?](/database/mysql_database/View.md#can-we-insert-data-into-a-view)
4. [Can we create a View on another View?](/database/mysql_database/View.md#can-we-create-a-view-on-another-view)
5. [Views used in real projects?](/database/mysql_database/View.md#why-are-views-used-in-real-projects)


Difference between View and Table?
Can data be inserted into a View?
What is a Materialized View?
Advantages of Views?

### 🧠 [**Mysql Index Questions**](/database/mysql_database/Index.md)
1. [What is Index?](/database/mysql_database/Index.md#what-is-index)
2. Why are Indexes used?
3. [Types of Indexes](/database/mysql_database/Index.md#types-of-indexes)
4. Unique Indexes
5. Show Index
6. Alter/Modify an Index
7. [Drop Index](/database/mysql_database/Index.md#drop-index)
8. Unique Indexes
9. Cluster Index
10. Non cluster index
11. difference between cluster and non cluster index?
12. What is Composite Index?
13. How do indexes improve performance?
14. Can indexes slow down performance?
15. How to check indexes on a table?
16. Difference between a clustered index and a non-clustered index?

1. [What is CTE (Common Table Expression)?](/database/mysql_database/cte.md#what-is-cte-common-table-expression-in-mysql)
2. [what is With()?](/database/mysql_database/cte.md#with)

### 🧠 **Mysql Logical Questions**
1. [value count:- Email](/database/mysql_database/sql-query-questions/find_duplicate_value.md#count-email-number)
2. [Duplicate values in a Table?](/database/mysql_database/sql-query-questions/find_duplicate_value.md#how-to-find-duplicate-values-in-a-table)
3. [Find records without duplicates?](/database/mysql_database/sql-query-questions/find_duplicate_value.md#find-records-without-duplicates)
4. [remove Duplicate values](/database/mysql_database/sql-query-questions/find_duplicate_value.md#duplicate-value-remove)
5. [Replace a column value:- M to F & F to M]
6. [Find records present in one table but not another?](/database/mysql_database/sql-query-questions/table_query.md#find-records-present-in-one-table-but-not-another)
7. [How do you find duplicate invoices?](/database/mysql_database/sql-query-questions/find_duplicate_value.md#how-do-you-find-duplicate-invoices)
8. [Find customers having more than 5 invoices?](/database/mysql_database/sql-query-questions/find_duplicate_value.md#find-customers-having-more-than-5-invoices)
9. [find the total invoice amount customer-wise?](/database/mysql_database/sql-query-questions/find_duplicate_value.md#find-the-total-invoice-amount-customer-wise)
10. [Find the Current date?](/database/mysql_database/sql-query-questions/date_time_sql_ques.md#current-date)
11. [find monthly transaction counts?](/database/mysql_database/sql-query-questions/other_logic_ques.md#find-monthly-transaction-counts)
12. [find records created in the last 30 days?](/database/mysql_database/sql-query-questions/date_time_sql_ques.md#find-records-created-in-the-last-30-days)
13. [find records between two dates?](/database/mysql_database/sql-query-questions/date_time_sql_ques.md#find-records-between-two-dates)
14. Find NULL values?
15. How do you replace NULL values?
16. How do you update records based on another table?
<div style="page-break-before: always;"></div>

#### 🧠 **Mysql Salary logical Questions**
1. [Salary:- Maximum salary](/database/mysql_database/1_sql_logical_ques.md#find-maximum-salary)
2. [Salary:- Nth Highest salary](/database/mysql_database/sql-query-questions/Salary.md#find-3rd-highest-salary)
3. [Salary:- Top Nth salary](/database/mysql_database/sql-query-questions/Salary.md#find-top-n-salaries)
4. Salary + department
   1. [Department-wise Total Salary]
   2. [Highest Salary ka Department kaun sa hai?]
   3. [department Having Total Salary > 100000]
   4. [Department-wise average salary?]
   5. [find the highest salary department-wise?](/database/mysql_database/sql-query-questions/salary_department_and_manager.md#find-the-highest-salary-department-wise)
   6. [Find employees who don't have a department?](/database/mysql_database/sql-query-questions/salary_department_and_manager.md#find-employees-who-dont-have-a-department)
5. 
⭐

Find employees earning more than average salary.
Find the highest salary in each department.
Find departments having more than 5 employees.
Find department-wise employee count.

### 
What is a Super Key?


### Difference between IN and EXISTS?
* IN checks whether a value exists in a list returned by a subquery, whereas EXISTS checks whether the subquery returns at least one matching row. For large datasets and correlated subqueries, EXISTS is often preferred because it can stop searching after finding the first match.




### 🧠 [Cursor](/database/mysql_database/Cursor.md)
1. [What is a Cursor?](/database/mysql_database/Cursor.md#what-is-cursor)
2. Types of Curser?

### 🧠 [Triggers](/database/mysql_database/trigger.md)
1. [What is a Trigger?](/database/mysql_database/trigger.md#what-is-trigger)
2. [Types of Triggers?](/database/mysql_database/trigger.md#types-of-triggers)
   1. BEFORE INSERT Trigger?
   2. AFTER INSERT Trigger?
   3. BEFORE UPDATE Trigger?
   4. AFTER UPDATE Trigger?
3. [Advantages of Triggers?](/database/mysql_database/trigger.md#advantages-of-triggers)
4. [Disadvantages of Triggers?](/database/mysql_database/trigger.md#disadvantages-of-triggers)
5. [Diff between Trigger and Stored Procedure?](/database/mysql_database/trigger.md#difference-between-trigger-and-stored-procedure)

### 🧠 [Stored Procedures](/database/mysql_database/stored_procedure.md)
1. [What is a Stored Procedure?](/database/mysql_database/stored_procedure.md#ques-what-is-stored-procedure)
2. Advantages of Stored Procedure?
3. How do you create a Procedure?


### 🧠 [Subquery ques](/database/mysql_database/subquery.md)
1. [What is a Subquery?](/database/mysql_database/subquery.md#what-is-a-subquery)
2. [What is a Nested Query?](/database/mysql_database/subquery.md#what-is-a-subquery)
3. [Types of Subquery?](/database/mysql_database/subquery.md#types-of-subqueries)
   1. [Single-row?](/database/mysql_database/subquery.md#1-single-row-subquery)
   2. [Multi-row Subquery?](/database/mysql_database/subquery.md#2-multiple-row-subquery)
   3. [What is a Correlated Subquery?](/database/mysql_database/subquery.md#3-correlated-subquery)
4. [Scalar Subquery?](/database/mysql_database/subquery.md#what-is-a-scalar-subquery)


1. [What is Partitioning?](/database/mysql_database/partitioning.md)
2. [What is Replication?](/database/mysql_database/replication.md#what-is-replication-in-mysql)



🚀 12. Performance Optimization
How do you optimize SQL queries?
How do you identify slow queries?
What is Query Cache?
What is Partitioning?

How do indexes affect performance?
How do you optimize JOINs?
What is a covering index?

🏗️ 13. Stored Procedures & Functions
What is a Function?
Difference between Procedure and Function?
Can a Function return multiple values?
What are IN, OUT, and INOUT parameters?


🏢 16. Database Design
What is ER Diagram?
What is Cardinality?
One-to-One Relationship?
One-to-Many Relationship?
Many-to-Many Relationship?
What is Referential Integrity?
How do you design a scalable database?

🔥 17. MySQL Advanced Questions
Master-Slave Replication?
What is Sharding?
What is a Temporary Table?

⭐ 18. MySQL Scenario-Based Questions
How would you improve a slow query?
A query is taking 10 seconds. How will you debug it?
How would you handle millions of records?
How would you design a banking transaction system?
How would you prevent duplicate entries?
How would you optimize a JOIN query?
How would you archive old data?

How would you design an e-commerce database?
🎯 Most Important Interview Topics (Must Prepare)

✅ Transactions
✅ Subqueries
✅ Performance Optimization (EXPLAIN, Indexing)
✅ Database Design & Relationships


### Table of Contents
<!-- ❌ 👉 👈 🧠 ✅ 📌 🔧 🧪 🔍 -->
|       | No.                                                                              | [Database](#database) |
| :---: | -------------------------------------------------------------------------------- |
|       | [What is storage engine/Table Types in mysql?](#what-is-storage-engine-in-mysql) |

|  No.  | [Tables](#tables)                                                                                |
| :---: | ------------------------------------------------------------------------------------------------ |
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
|       | [RENAME table name?](#rename-table-name)                                                         |


|  No.  | [SQL Comments?](#sql-comments)                                                                                |
| :---: | ------------------------------------------------------------------------------------------------------------- |

|       | ------------------------------                                                                                |


|  No.  | [Sql Query questions](#sql-query-questions)                                                                                                |
| :---: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|       | [Demo data for execute the query](#demo-data-for-execute-the-query)                                                                        |
|       | [How to copy a table in another table?](#ques-how-to-copy-a-table-in-another-table)                                                        |
|       | [How to copy structure of a table but not data?](#ques-how-to-copy-structure-of-a-table-but-not-data)                                      |
|       | [Duplicate table through another table, with structure and data?](#duplicate-table-through-another-table-with-structure-and-data)          |
|       | [Find the Highest Salary of Each Department?](#find-the-highest-salary-of-each-department)                                                 |
|       | [Check max_salary is not exceed the upper limit of 25000](#create-a-table-and-check-max_salary-is-not-exceed-the-upper-limit-of-25000)     |
|       | [Update remaing days startdate - enddate](#update-remaing-days-startdate---enddate)                                                        |



<!-- ![asdf](./img/mohit_pic.jpg){width=600 height=500} -->

https://www.w3resource.com/sql-exercises/joins-hr/sql-joins-hr-exercise-11.php




  ==================
Discuss their roles in ensuring data integrity.
What is a NULL value in MySQL?
Explain how MySQL handles NULL and its use cases.
Explain types of subqueries like scalar, correlated, and non-correlated.
Describe their use and advantages.
Explain how views work and their use cases.
What are temporary tables in MySQL?
Discuss when to use temporary tables and their lifetime.

Intermediate MySQL Interview Questions:
What is a composite index?
How would you optimize a slow-performing query in MySQL?
Discuss query optimization techniques like indexing, query rewriting, and EXPLAIN.
What is a full-text index?
Discuss how it is used for full-text searches in MySQL.
What is an auto-increment column?
Explain how auto-incrementing primary keys work.
Discuss how transactions work and how you can commit or roll back a transaction.
What is the difference between a clustered index and a non-clustered index?
How can you handle errors in MySQL?
Discuss using TRY...CATCH (in MySQL 5.7 or above) or error handling techniques.



What are the different types of locks in MySQL?
Explain table-level locks, row-level locks, and the difference between them.

Advanced MySQL Interview Questions:

How does MySQL handle replication?

Discuss master-slave replication, master-master replication, and semi-synchronous replication.

Explain the concept of partitioning in MySQL.

Discuss how tables are partitioned and the benefits of partitioning.

How can you improve performance with MySQL queries and indexing?

What is MySQL clustering?

Explain the architecture of MySQL Cluster and its advantages.

What is the purpose of the ANALYZE TABLE statement?

Discuss how it helps optimize tables.

What are event schedulers in MySQL?

Explain how event schedulers work and how to automate tasks in MySQL.

How does MySQL handle concurrency and isolation levels?

Discuss isolation levels like READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE.



Explain the InnoDB and MyISAM storage engines.

Discuss their differences, advantages, and when to use each.

What are the differences between MySQL 5.x and MySQL 8.x?

Explain the concept of “Sharding” in MySQL and how it is implemented.

What are the advantages of using Prepared Statements in MySQL?

How would you perform a backup and restore of a MySQL database?

What is a Foreign Key constraint and how does it help in maintaining data integrity in MySQL?

Scenario-Based or Problem-Solving Questions:

How would you recover a MySQL database that has crashed?

How do you handle large BLOBs (Binary Large Objects) in MySQL?



### [Scenario Based MySql Ques](/database/mysql_database/scenario_based_mysql_ques.md)
1. [How do you optimize a SQL query?](/database/mysql_database/scenario_based_mysql_ques.md#how-do-you-optimize-a-sql-query)
2. How do you know a query is slow?
3. You are faced with a slow query that uses a JOIN operation on a large table. How would you optimize it?
4. Given a table with 100+ million rows, how would you optimize its performance?
5. How would you structure a database to handle millions of daily transactions efficiently?
