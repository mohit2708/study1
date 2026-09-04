|  No.  | [Database](#database)                                               |
| :---: | ------------------------------------------------------------------- |
|       | [What is a database?](#what-is-a-database)                          |
|       | [Database:- Show](#show-database)                                   |
|       | [Database:- Create](#create-databse)                                |
|       | [Database:- Rename](#rename-database)                               |
|       | [Database:- Drop/Delete](#drop-database)                            |
|       | [Database:- Select](#select-database)                               |
|       | [What Is DBMS?](#what-is-dbms)                                      |
|       | [What Is RDBMS?](#what-is-rdbms)                                    |
|       | [Difference between DBMS & RDBMS?](#difference-between-dbms--rdbms) |
<div style="page-break-before: always;"></div>

### 🎯**What is a database?**
- A database is an organized collection of data that allows efficient storage, retrieval, and management.
* A database is an organized collection of data, stored and retrieved digitally from a remote or local computer system. Databases can be vast and complex, and such databases are developed using fixed design and modeling approaches.
* Database is nothing but an organized form of data for easy access, storing, retrieval and managing of data. 
* This is also known as structured form of data which can be accessed in many ways.

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

### **What Is DBMS?**
* A database management system is program that control creation, maintenance and use of a database.
* DBMS can be termed as File Manager that manages data in a database rather than saving it in ﬁle systems.

### **What is RDBMS?**
* RDBMS stands for Relational Database Management System. RDBMS store the data into the collection of tables, which is related by common fields between the columns of the table. It also provides relational operators to manipulate the data stored into the tables.

### **Difference between DBMS & RDBMS?**
| DBMS                                          | RDBMS                                           |
| :-------------------------------------------- | :---------------------------------------------- |
| DBMS applications store data as file          | RDBMS applications store data in a tabular form |
| Normalization is not present in DBMS          | Normalization is present in RDBMS               |
| DBMS does not support distributed data hnbase | RDBMS support distributed database              |