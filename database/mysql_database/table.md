|  No.  | [Tables](#tables)                                                             |
| :---: | ----------------------------------------------------------------------------- |
|       | [Types of SQL Commands/subsets of SQL?](#types-of-sql-commandssubsets-of-sql) |
|       | [-- Data Definition Language (DDL)](#types-of-sql-commandssubsets-of-sql)     |
|       | [-- Data Manipulation Language (DML)](#types-of-sql-commandssubsets-of-sql)   |
|       | [-- Data Control Language (DCL)](#types-of-sql-commandssubsets-of-sql)        |
|       | [-- Transaction Control Language (TCL)](#types-of-sql-commandssubsets-of-sql) |
|       | --------------------------------------------------------------                |
|       | [Create TABLE?](#create-table)                                                |
|       | [show Tables](#show-tables)                                                   |
|       | [See the table structure](#see-the-table-structure)                           |
|       | [Alter/Rename table name](#alterrename-table-name)                            |
|       | [Delete/Drop table](#deletedrop-table)                                        |
|       | [Truncate table](#truncate-table)                                             |
|       | [Column Modify](#column-modify)                                               |
|       | [-- Alter table column name](#add-a-column-in-the-table)                      |
|       | [-- Alter table column name after field](#add-column-after-particular-field)  |
|       | [-- Add column in first](#add-column-in-first)                                |
|       | [-- Add multiple columns in the table](#add-multiple-columns-in-the-table)    |
|       | [-- Change column name](#change-column-name)                                  |
|       | [-- Change Multipal column name](#change-multipal-column-name)                |
|       | [-- Change Datatype from alter cmd](#change-datatype-from-alter-cmd)          |
|       | [-- DROP column in table](#drop-column-in-table)                              |
|       | --------------------------------------------------------------                |


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
<div style="page-break-before: always;"></div>

# Table Commands
### **Create table**
```sql
-- CREATE TABLE IF NOT EXISTS table_name (  (it used for if table already exist)
CREATE TABLE table_name(
    id int NOT NULL AUTO_INCREMENT,  
    name varchar(45) NOT NULL,  
    PRIMARY KEY (id) 
);
```

### **Show tables**
```sql
SHOW TABLES;
+-----------------------+
| Tables_in_employee123 |
+-----------------------+
| employee_table        |
+-----------------------+
```

### **See the table structure**
```sql
DESCRIBE employee_table;
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int(11)     | NO   | PRI | NULL    | auto_increment |
| name       | varchar(45) | NO   |     | NULL    |                |
| occupation | varchar(35) | NO   |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
```

### **Alter/Rename table name**
```sql
RENAME old_table_name To new_table_name; -- (OR)
RENAME TABLE old_table_name TO new_table_name;
ALTER TABLE old_table_name RENAME TO new_table_name; -- using alter 
```

### **Delete/Drop table**
* **Deletes the entire table:** When we use DROP TABLE, the entire table structure, including its **schema**, **indexes**, **triggers**, and **constraints**, is deleted.
* **Permanently removes data:** All data stored in the table is lost forever.
* **Cannot be rolled back:** Once a table is dropped, it cannot be recovered unless you have a backup or use a third-party recovery tool.
* **Requires less permissions:** Typically, only the DROP privilege is required to drop a table.
```sql
DROP TABLE table_name;
```
<div style="page-break-before: always;"></div>

### **Truncate Table**

* **Deletes all rows:** When we use TRUNCATE TABLE, all rows in the table are deleted, but the table structure remains intact.
* **Resets auto-incrementing IDs:** If your table has an auto-incrementing primary key or other auto-incrementing columns, truncating the table will reset these IDs to their starting value (usually 1).
* **Faster than DELETE:** Truncation is generally faster than deleting all rows using DELETE because it doesn't involve individual row deletion and logging.
* **Cannot be rolled back:** Like DROP TABLE, once a table is truncated, the changes cannot be recovered unless you have a backup or use a third-party recovery tool.
* **Requires more permissions:** Typically, both the TRUNCATE privilege and the DELETE privilege are required to truncate a table.
* A truncate SQL statement is used to remove all rows (complete data) from a table.
* TRUNCATE is a DDL(Data Definition Language) command and is used to delete all the rows or tuples from a table. Unlike the DELETE command, the TRUNCATE command does not contain a WHERE clause.
```sql
TRUNCATE TABLE table_name;
```

### **Alter column name**
* ALTER TABLE lets you add columns to a table in a database.
```sql
-- syntex
ALTER TABLE table_name ADD column_name datatype;
(OR)
ALTER TABLE table_name ADD new_column_name datatype [ FIRST | AFTER column_name ]; 
```

# Column Modify
### **ADD a column in the table**
```sql
ALTER TABLE employee_table ADD cus_age varchar(40) NOT NULL;

DESCRIBE employee_table;
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int(11)     | NO   | PRI | NULL    | auto_increment |
| name       | varchar(45) | NO   |     | NULL    |                |
| occupation | varchar(35) | NO   |     | NULL    |                |
| age        | int(11)     | NO   |     | NULL    |                |
| cus_age    | varchar(40) | NO   |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
```

### **Add column after particular field**
```sql
ALTER TABLE employee_table ADD after_occupation varchar(40) NOT NULL AFTER occupation;

+------------------+-------------+------+-----+---------+----------------+
| Field            | Type        | Null | Key | Default | Extra          |
+------------------+-------------+------+-----+---------+----------------+
| id               | int(11)     | NO   | PRI | NULL    | auto_increment |
| name             | varchar(45) | NO   |     | NULL    |                |
| occupation       | varchar(35) | NO   |     | NULL    |                |
| after_occupation | varchar(40) | NO   |     | NULL    |                |
+------------------+-------------+------+-----+---------+----------------+
```

### **Add column in first**
```sql
ALTER TABLE employee_table ADD COLUMN unique_id INT(11) NOT NULL FIRST;

+------------------+-------------+------+-----+---------+----------------+
| Field            | Type        | Null | Key | Default | Extra          |
+------------------+-------------+------+-----+---------+----------------+
| unique_id        | int(11)     | NO   |     | NULL    |                |
| id               | int(11)     | NO   | PRI | NULL    | auto_increment |
| name             | varchar(45) | NO   |     | NULL    |                |
| occupation       | varchar(35) | NO   |     | NULL    |                |
| after_occupation | varchar(40) | NO   |     | NULL    |                |
| age              | int(11)     | NO   |     | NULL    |                |
| cus_age          | varchar(40) | NO   |     | NULL    |                |
+------------------+-------------+------+-----+---------+----------------+
```

### **Add multiple columns in the table**
```sql
ALTER TABLE employee_table 
    ADD COLUMN unique_id1 INT(11) NOT NULL FIRST,
    ADD COLUMN unique_id2 INT(11) NOT NULL FIRST;

+------------------+-------------+------+-----+---------+----------------+
| Field            | Type        | Null | Key | Default | Extra          |
+------------------+-------------+------+-----+---------+----------------+
| unique_id2       | int(11)     | NO   |     | NULL    |                |
| unique_id1       | int(11)     | NO   |     | NULL    |                |
| unique_id        | int(11)     | NO   |     | NULL    |                |
| id               | int(11)     | NO   | PRI | NULL    | auto_increment |
| name             | varchar(45) | NO   |     | NULL    |                |
| occupation       | varchar(35) | NO   |     | NULL    |                |
| after_occupation | varchar(40) | NO   |     | NULL    |                |
| age              | int(11)     | NO   |     | NULL    |                |
| cus_age          | varchar(40) | NO   |     | NULL    |                |
+------------------+-------------+------+-----+---------+----------------+

-- add enum column
ALTER TABLE table_name ADD field_name enum('0','1') NOT NULL DEFAULT '0' after password;
```

### Change column name
```sql
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
-- OR
ALTER TABLE table_name CHANGE old_column_name new_column_name data_type;
```

### Change multipal column name
```sql
ALTER TABLE table_name 
RENAME COLUMN old_column1 TO new_column1,
RENAME COLUMN old_column2 TO new_column2;
```

### **Change Datatype from alter cmd**
```sql
ALTER TABLE employee_table MODIFY unique_id4 VARCHAR(40) NULL;
OR
ALTER TABLE employee_table MODIFY COLUMN unique_id4 VARCHAR(40) NULL;
```

### **DROP column in table**
```sql
ALTER TABLE employee_table DROP COLUMN unique_id4;
```
<div style="page-break-before: always;"></div>


# Modify Table Data 
### **Insert table**
```sql
INSERT INTO table_name
(column1,column2,column3,...)
VALUES
('value1','value2','value3',...);
```

### **SELECT**
* SELECT statements are used to fetch data from a database. Every query will begin with SELECT.
```sql
SELECT * FROM table_name;   -- fetch Full data
SELECT column_name FROM table_name;     -- fetch particular column
```

### **UPDATE**
* UPDATE statements allow you to edit rows in a table.
```sql
UPDATE table_name
SET some_column = some_value
WHERE some_column = some_value;
--
Update customer set name="mohit" where id =1;
```

### **DELETE**
* DELETE is a DML(Data Manipulation Language) command and is used when we specify the row (tuple) that we want to remove or delete from the table or relation. The DELETE command can contain a WHERE clause.
```sql
DELETE FROM table_name
WHERE some_column = some_value;
```
* But if you do not specify the WHERE condition it will remove **all the rows** from the table.
```sql
DELETE FROM table_name;
```
