|  No.  | [Mysql]()                                                                                                                                                 |
| :---: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       | [What is MySQL?](#what-is-mysql)                                                                                                                          |
|       | [What is Sql?](#what-is-sql)                                                                                                                              |
|       | [What is the difference between SQL and MySQL?](#what-is-the-difference-between-sql-and-mysql)                                                            |
|       | [What are the advantages of MySQL?](#what-are-the-advantages-of-mysql)                                                                                    |
|       | [Check version of the sql?](#ques-check-version-of-the-sql)                                                                                               |
|       | [Types of SQL Commands/subsets of SQL?](#types-of-sql-commandssubsets-of-sql)                                                                             |
|       | [-- Data Definition Language (DDL)](#types-of-sql-commandssubsets-of-sql)                                                                                 |
|       | [-- Data Manipulation Language (DML)](#types-of-sql-commandssubsets-of-sql)                                                                               |
|       | [-- Data Control Language (DCL)](#types-of-sql-commandssubsets-of-sql)                                                                                    |
|       | [-- Transaction Control Language (TCL)](#types-of-sql-commandssubsets-of-sql)                                                                             |
|       | [How to copy a table in another table?](#ques-how-to-copy-a-table-in-another-table)                                                                       |
|       | [How to copy structure of a table but not data?](#ques-how-to-copy-structure-of-a-table-but-not-data)                                                     |
|       | [Create a table through another table/Duplicate table through another table?](#create-a-table-through-another-tableduplicate-table-through-another-table) |
|       | [Duplicate table through another table, with structure and data?](#duplicate-table-through-another-table-with-structure-and-data)                         |


### **What is MySQL?**
- MySQL is an open-source relational **database management system** (RDBMS) based on SQL (Structured Query Language).
- It's commonly used for managing data in web applications and is known for its performance and ease of use.

### **What is Sql?**
* SQL is stands for **structure query language**. 
* It is a database language **used** for database **creation**, **deletion**, **fetching** rows and modifying rows etc.
* It is a kind of ANSI standard language, used with all database. 

### **What is the difference between SQL and MySQL?**
- SQL (Structured Query Language) is a language used to communicate with databases, while MySQL is a specific RDBMS that uses SQL to interact with data.

### **What are the advantages of MySQL?**
- Open-source and free
- High performance
- Supports large databases
- Secure (user authentication & privileges)
- Cross-platform
- ACID-compliant (InnoDB)

### **Ques. Check version of the sql?**
```sql
select version()
```

### **Types of SQL Commands/subsets of SQL?**
* DDL (Data Definition Language):
  * **[CREATE:](#create-table)** Creates a new table or database.
  * **[ALTER](#alter):** Modifies an existing database object.
  * **[DROP](#drop-column-in-table):** Deletes an entire table, database, or other objects.
  * **[TRUNCATE](#truncate):** Removes all records from a table, deleting the space allocated for the records.

* DML (Data Manipulation Language):
  * **[SELECT:](#select)** Retrieves data from the database.
  * **[INSERT:](#insert-table)** Adds new data to a table.
  * **[UPDATE](#update):** Modifies existing data within a table.
  * **[DELETE:](#delete)** Removes data from a table.
* DCL (Data Control Language):
  * **GRANT:** Gives users access privileges to the database.
  * **REVOKE:** Removes access privileges given with the GRANT command.
* TCL (Transaction Control Language):
  * **COMMIT:** Saves all changes made in the current transaction.
  * **ROLLBACK:** Restores the database to the last committed state.
  * **SAVEPOINT:** Sets a savepoint within a transaction.
  * **SET TRANSACTION:** Places a name on a transaction.

# Storage Engine/Table Type
### **What is storage engine in mysql?**
* In MySQL, a storage engine (also called a table type) is the component that handles how data is stored, retrieved, and managed in the database.
* Key points about MySQL storage engines:
  * Each storage engine has its own way of storing data and managing indexes.
  * We can choose a storage engine for each table depending on your needs. 

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100)
) ENGINE=InnoDB;

-- If you don’t specify an engine, MySQL uses the default storage engine (usually InnoDB).
```

#### **Types of mysql engine**
📌 **InnoDB (Default)**
* **Transaction-safe (ACID compliant):** InnoDB supports transactions, ensuring data integrity with Atomicity, Consistency, Isolation, and Durability properties.
* **Supports foreign keys:** This ensures that related data in different tables is properly linked.
* **Row-level locking:** Instead of locking the entire table, InnoDB locks only the rows that are changing, allowing multiple users to work more efficiently and improving system performance.(पूरी टेबल को लॉक करने की बजाय, InnoDB सिर्फ उन पंक्तियों (rows) को लॉक करता है जिनमें बदलाव हो रहा होता है, जिससे एक साथ कई यूजर बेहतर तरीके से काम कर सकते हैं और सिस्टम की परफॉर्मेंस बढ़ती है।)
* **Crash Recovery:** InnoDB uses a "write-ahead log" so that data is preserved and not lost or corrupted after a crash.(InnoDB एक “write-ahead log” का इस्तेमाल करता है ताकि किसी भी क्रैश के बाद डेटा सुरक्षित रहे और कोई नुकसान या खराबी न हो।)

2. **MyISAM**
* **No transaction support:** ❌ MyISAM does not support transactions, so it can’t guarantee ACID properties like InnoDB.
* **Table-level locking:** When a query modifies data, the entire table is locked, which can reduce performance in multi-user environments.
* **No support for foreign keys:** MyISAM does not enforce referential integrity or foreign key constraints between tables.
* Crash Recovery: ❌ Limited
* Use Case: Fast read-heavy operations (e.g., reporting, static content)
<div style="page-break-before: always;"></div>

3. **MEMORY**
* **Stores data in RAM:** MEMORY engine keeps all data in the server’s memory (RAM), making data access extremely fast.
* **Data is temporary:** Since data is stored in memory, it is lost when the MySQL server restarts or crashes.
* Best for temporary or cache tables: Ideal for temporary data storage, like caching or quick lookups during a session.
* Supports only hash indexes: By default, MEMORY tables use hash indexes for very fast lookups, but you can also use B-tree indexes.
* No support for transactions or foreign keys: MEMORY engine does not support transactions or foreign key constraints.
* Limited table size: The size of MEMORY tables is limited by the amount of available RAM.

4. **CSV**
* Stores data in CSV files: Tables are stored as plain text files with comma-separated values, making them easy to read and edit outside MySQL.
* No indexing support: CSV tables do not support indexes, so searches can be slow on large datasets.
* No transaction support: It does not support transactions or ACID properties.
* Good for data exchange: Useful for importing/exporting data between MySQL and other applications that use CSV format.
* No support for foreign keys: Does not enforce foreign key constraints or referential integrity.
* Data is stored as plain text: Easy to open and manipulate with text editors or spreadsheet software.

5. **ARCHIVE**
* Designed for storing large volumes of historical data: ARCHIVE is optimized for storing data that is rarely updated or deleted.
* Supports only INSERT and SELECT operations: You can insert and read data, but you cannot update or delete rows.
* High compression: Data is stored in a compressed format to save disk space.
* No indexes (except AUTO_INCREMENT): ARCHIVE tables do not support indexes, so searching can be slower (only AUTO_INCREMENT on primary key is allowed).
* No transaction or foreign key support: It does not support transactions, rollbacks, or foreign keys.
* Ideal for logging and auditing: Great for storing logs, archived records, or audit trails where data integrity and compact storage are more important than speed of access.

6. **BLACKHOLE**
* Accepts data but doesn’t store it: All INSERT operations are accepted, but the data is discarded—nothing is saved.
* Returns empty results on SELECT: Since no data is stored, any SELECT query will return an empty result.
* Useful for replication: Often used on master servers in replication setups to send data to slaves without storing it locally.
* No indexes or data storage: BLACKHOLE tables do not support indexing or actual data storage.
* Supports triggers: Triggers (like AFTER INSERT) still work, which can be useful for logging or monitoring actions.
* No transaction or foreign key support: Transactions and referential integrity are not supported.

7. **MERGE** 
* Combines multiple MyISAM tables into one virtual table: A MERGE table acts as a single table that maps to multiple underlying MyISAM tables with the same structure.
* Used for managing large datasets: Useful when you want to split large tables into smaller parts (like by date) but still query them together.
* Improves performance in some cases: Allows you to search across multiple tables as if they were one, which can be optimized for specific queries.
* Supports only MyISAM tables: All underlying tables must be MyISAM and have exactly the same structure.
* Inherits MyISAM limitations: No support for transactions or foreign keys, and uses table-level locking.
* Supports SELECT, DELETE, and INSERT (no UPDATE): You can read, delete, and insert data, but cannot use UPDATE queries directly on a MERGE table.
  
8. **FEDERATED**
* Accesses remote MySQL tables: FEDERATED allows you to create a table in your local MySQL server that connects to a table on a remote MySQL server.
* No data stored locally: Data is not stored on the local server—the table acts as a pointer to the remote table.
* Useful for distributed systems: Ideal when you need to work with data across different MySQL servers without replicating it.
* Supports only SELECT, INSERT, UPDATE, DELETE: You can perform basic queries, but not advanced operations like indexing locally.
* No transaction or foreign key support: Transactions and foreign keys are not supported with FEDERATED tables.
* Needs manual setup: You must provide connection info (host, user, password, etc.) when creating a FEDERATED table.


### What is a NULL value?
- A NULL value represents missing, unknown, or not applicable data in a database.
- Null means no value.


### What is the purpose of the mysql command-line tool?
- The MySQL command-line tool is an interactive interface that allows users to interact with a MySQL database server directly from the command line (or terminal). 
- It is one of the most commonly used ways to manage and interact with MySQL databases.
- Here's a breakdown of its purpose and key features:
  - Create, drop, and modify databases.
  - Execute SQL queries

#### Connecting to the MySQL Server:
```mysql
mysql -u root -p
```

#### Exit the MySQL Command-Line Tool:
```mysql
EXIT;
```


### What is the difference between SELECT and SHOW statements?
- The SELECT and SHOW statements in MySQL both retrieve data, but they serve different purposes and operate in different contexts. 
- Here's a breakdown of the key differences:
1. Purpose
- SELECT Statement:
  - The SELECT statement is used to query data from one or more tables in a database. It allows you to retrieve specific columns and rows, apply filters, sort the data, and perform various operations like joins, aggregations, and calculations.
  - Primary use case: Extracting data based on a query.
  - Example:
  ```sql
  SELECT * FROM employees WHERE department = 'Sales';
  ```
- SHOW Statement:
  - The SHOW statement is used to display metadata about the database structure, such as database tables, columns, indexes, and other schema-related information. It can also show the status of the server or the configuration of the MySQL system.
  - Primary use case: Inspecting the structure and configuration of the database system.
  - Example:
  ```sql
  SHOW TABLES;
  ```

  ==================
What is MySQL?

Define MySQL and explain its purpose.

What are the different data types in MySQL?

Discuss common data types like INT, VARCHAR, TEXT, DATE, and others.

What is the difference between CHAR and VARCHAR data types in MySQL?

What is normalization? What are the different normal forms in a database?

Discuss 1NF, 2NF, 3NF, and BCNF.

What are the different types of joins in MySQL?

Explain INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

What is the difference between DELETE, TRUNCATE, and DROP commands in MySQL?

How do you add, update, or delete records in MySQL?

Using INSERT, UPDATE, and DELETE statements.

What are primary keys and foreign keys?

Discuss their roles in ensuring data integrity.

What is a NULL value in MySQL?

Explain how MySQL handles NULL and its use cases.

Explain the concept of ACID properties in databases.

Discuss Atomicity, Consistency, Isolation, and Durability.

What is a subquery?

Explain types of subqueries like scalar, correlated, and non-correlated.

What are stored procedures and triggers in MySQL?

Describe their use and advantages.

What is a view in MySQL?

Explain how views work and their use cases.

What are temporary tables in MySQL?

Discuss when to use temporary tables and their lifetime.

Intermediate MySQL Interview Questions:

Explain the difference between INNER JOIN and LEFT JOIN.

What is a composite index?

Explain indexing on multiple columns.

How would you find duplicate records in a table?

What is a GROUP BY clause in MySQL?

Explain how it works and give an example use case.

What is the difference between WHERE and HAVING clauses in SQL?

How would you optimize a slow-performing query in MySQL?

Discuss query optimization techniques like indexing, query rewriting, and EXPLAIN.

What is a full-text index?

Discuss how it is used for full-text searches in MySQL.

What is the difference between UNION and UNION ALL?

What is an auto-increment column?

Explain how auto-incrementing primary keys work.

What is a transaction in MySQL?

Discuss how transactions work and how you can commit or roll back a transaction.

What is the difference between a clustered index and a non-clustered index?

How can you handle errors in MySQL?

Discuss using TRY...CATCH (in MySQL 5.7 or above) or error handling techniques.

What is a cross join and when would you use it?

Explain the use of EXPLAIN keyword in MySQL.

Discuss how it helps analyze query execution plans.

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

What is a deadlock in MySQL, and how do you resolve it?

Explain the InnoDB and MyISAM storage engines.

Discuss their differences, advantages, and when to use each.

What is the difference between a unique index and a primary key in MySQL?

What are the differences between MySQL 5.x and MySQL 8.x?

Explain the concept of “Sharding” in MySQL and how it is implemented.

What are the advantages of using Prepared Statements in MySQL?

How would you perform a backup and restore of a MySQL database?

What is a Foreign Key constraint and how does it help in maintaining data integrity in MySQL?

Scenario-Based or Problem-Solving Questions:

Given a table with 100+ million rows, how would you optimize its performance?

How would you structure a database to handle millions of daily transactions efficiently?

How would you recover a MySQL database that has crashed?

You are faced with a slow query that uses a JOIN operation on a large table. How would you optimize it?

How do you handle large BLOBs (Binary Large Objects) in MySQL?


