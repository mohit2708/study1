|  No.  | My SQL Questions                                                                               |
| :---: | ---------------------------------------------------------------------------------------------- |
|       | [What is MySQL](#what-is-mysql)                                                                |
|       | [What is MySQL?](#what-is-mysql)                                                               |
|       | [What is Sql?](#what-is-sql)                                                                   |
|       | [What is the difference between SQL and MySQL?](#what-is-the-difference-between-sql-and-mysql) |

|  No.  | [Database](#database)                                                      |
| :---: | -------------------------------------------------------------------------- |
||[What is a database?]|
|       | [Show Database](#show-database)                                            |
|       | [Create Databse](#create-databse)                                          |
|       | [Rename Database](#rename-database)                                        |
|       | [Drop/Delete Database](#drop-database)                                     |
|       | [Select Database](#select-database)                                        |
|       | [Difference between CHAR vs VARCHAR](#-difference-between-char-vs-varchar) |
|       | [SQL Comments?](#sql-comments)                                             |



<div style="page-break-before: always;"></div>

### 🎯**What is MySQL?**
- MySQL is an open-source relational **database management system** (RDBMS) that uses SQL to store, manage, and retrieve data.
- It's commonly used for managing data in web applications and is known for its performance and ease of use.

### 🎯**What is Sql?**
* SQL is stands for **structure query language**. 
* SQL (Structured Query Language) is a standard language used to **create**, **read**, **update**, and **delete** data in relational databases. It is also used to create and modify database structures such as tables.
* SQL language hai, database nahi.


### 🎯**What is the difference between SQL and MySQL?**
- SQL is a standard language used to communicate with relational databases, whereas MySQL is an RDBMS that uses SQL to store, manage, and retrieve data.
- SQL → Language
- MySQL → RDBMS / Database Management System
  
<div style="page-break-before: always;"></div>

### 🎯 **What is a database?**
- A database is an organized collection of data that allows efficient storage, retrieval, and management.

#### Show Database
```sql
SHOW DATABASES/SCHEMAS;
SHOW DATABASES [LIKE 'pattern' | WHERE expr];
SHOW DATABASES LIKE 'test%';
SELECT * FROM sys.databases;
EXEC sp_databases;
+---------------------+
| Database            |
+---------------------+
| employeesdb         |
| profile_fastapi     |
+---------------------+
```

#### Create Databse
```sql
CREATE DATABASE databasename;
```

#### Rename Database
```sql
RENAME DATABASE old_database_name TO new_database_name
(OR)
ALTER DATABASE old_datbase MODIFY NAME = new_database
```

#### Drop Database
```sql
DROP DATABASE/SCHEMA database_name;

-- DROP DATABASE IF EXISTS Statement
DROP DATABASE IF EXISTS DatabaseName;

-- Deleting Multiple Databases
DROP DATABASE testDB3, testDB4;
```

#### Select Database
```sql
USE YourDatabaseName;
```


<div style="page-break-before: always;"></div>

### 🎯 **Difference between CHAR vs VARCHAR**
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

### **SQL Comments?**
* There are typically two main types of SQL comments:

1. **Single-line Comments:** Started with two dashes (--)
```sql
-- This is a single-line comment
SELECT * FROM employees; -- Retrieve all employee records
```

2. **Multi-line Comments:** Started with /* and ended with */
```sql
/* This is a 
   multi-line comment 
   explaining the query */
SELECT id, name, email FROM employees;
```
