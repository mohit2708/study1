|  No.  | [Database](#database)                      |
| :---: | ------------------------------------------ |
|       | [What is a database?](#what-is-a-database) |
|       | [Database:- Show](#show-database)          |
|       | [Database:- Create](#create-databse)       |
|       | [Database:- Rename](#rename-database)      |
|       | [Database:- Drop/Delete](#drop-database)   |
|       | [Database:- Select](#select-database)      |
<div style="page-break-before: always;"></div>

### 🎯**What is a database?**
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