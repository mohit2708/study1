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
2. What are the features of MySQL?
3. What is the difference between SQL and MySQL?
4. What are databases and tables?
5. sql comments?
6. What are rows and columns?
7. What are MySQL data types?
8. What is NULL?
9. ⭐ [Difference between CHAR and VARCHAR?](/database/mysql_database/2_sql_questions.md#difference-between-char-vs-varchar)
10. Difference between INT and BIGINT?
11. What is AUTO_INCREMENT?
12. ⭐ Difference between WHERE and HAVING clauses?
13. [Wildcard Characters/Like Query?](/database/mysql_database/Wildcard_Characters_Like%20Query.md)

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
   1. SUM
   2. AVG
   3. MAX
   4. MIN
   5. COUNT
2. COUNT() vs COUNT(*) in MySQL?


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
4. [Left JOIN/LEFT OUTER JOIN]
5. [Right JOIN]
6. [Outer join](/database/mysql_database/Joins.md#outer-join)
7. [CROSS Join](/database/mysql_database/Joins.md#cross-join)
8. [Full Join/FULL OUTER JOIN]

### 🧠 [**Mysql Union & Union All Questions**](/database/mysql_database/union_and_union_all.md)
1. [What Is Union & Union All?](/database/mysql_database/union_and_union_all.md#what-is-union--union-all)
2. [Difference between Union & Union All?]
3. [What is MINUS?](/database/mysql_database/MINUS.md#what-is-minus)
4. What is EXCEPT?
5. [What is Intersect?](/database/mysql_database/Intersect.md#what-is-intersect)


### 🧠 [**Mysql View Questions**](/database/mysql_database/View.md)
1. What is View?
   1. Create view
   2. Show view
   3. Alter view
   4. Deleted view
2. Views used in real projects?

### 🧠 [**Mysql Index Questions**](/database/mysql_database/Index.md)
1. What is Index?
2. Types of Indexes
3. Unique Indexes
4. Show Index
5. Alter/Modify an Index
6. Drop Index
7. Unique Indexes
8. Cluster Index
9. Non cluster index
10. difference between cluster and non cluster index?

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
What is JOIN?
What is INNER JOIN?
What is LEFT JOIN?
What is RIGHT JOIN?
What is FULL OUTER JOIN?
What is SELF JOIN?
What is CROSS JOIN?
Difference between INNER JOIN and OUTER JOIN?
Difference between LEFT JOIN and RIGHT JOIN?
When do you use SELF JOIN?
📊 5. Aggregate Functions
What are Aggregate Functions?
COUNT() vs COUNT(*)?
SUM() function?
AVG() function?
MAX() and MIN() functions?
How does COUNT handle NULL values?
What is GROUP BY?
What is HAVING?
Can aggregate functions be used without GROUP BY?
Find department-wise employee count.
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
📑 7. Normalization
What is Normalization?
Why do we need Normalization?
What is 1NF?
What is 2NF?
What is 3NF?
What is BCNF?
What is 4NF?
What is 5NF?
What is Functional Dependency?
What is Transitive Dependency?
Difference between 3NF and BCNF?
Advantages and disadvantages of Normalization?
⚡ 8. Indexes
What is an Index?
Why are Indexes used?
Types of Indexes?
What is Clustered Index?
What is Non-Clustered Index?
What is Composite Index?
What is Unique Index?
How do indexes improve performance?
Can indexes slow down performance?
How to check indexes on a table?
🔄 9. Views
What is a View?
Why use Views?
Difference between View and Table?
Can data be inserted into a View?
What is a Materialized View?
How to create a View?
Advantages of Views?
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
What is UNION?
Difference between UNION and UNION ALL?
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

8+ years experience interviews usually focus heavily on Joins, Indexes, Transactions, Normalization, Query Writing, Performance Tuning, and Scenario-Based Questions.