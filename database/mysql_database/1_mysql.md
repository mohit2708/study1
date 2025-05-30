### Ques. Optimizing SQL Queries for Faster Performance
1. Minimize the use of wildcard characters
   * The use of wildcard characters, such as % and _, in SQL queries, can slow down query performance. When using wildcard characters, the database has to scan the entire table to find the relevant data. To optimize SQL queries, it is important to minimize the use of wildcard characters and to use them only when absolutely necessary.
```sql
SELECT * FROM customers WHERE last_name_city LIKE 'P%';
```
* This query will use the index on the last name column and will be faster than the previous query.
```sql
SELECT * FROM customers WHERE last_name_city >= 'P' AND last_name < 'Q';
```

2. Increase Query Performance with Indexes
3. Use appropriate data types
4. Avoid subqueries
5. Avoid using SELECT *
```sql
SELECT * FROM customers WHERE customer_id = 1;
```
```sql
SELECT name, email FROM customers WHERE customer_id = 1;
```
6. Use stored procedures
7. 




### What is MySQL?
### Explain the differences between **SQL** and **MySQL**?In which language has MySQL been written?How to create a database in MySQL?.What is the MySQL server’s default port?  ->3306

### **Ques. What are Constraints in SQL?**
Constraints are used to specify the rules concerning data in the table. It can be applied for single or multiple fields in an SQL table during the creation of the table or after creating using the ALTER TABLE command. The constraints are:<br>
* **NOT NULL** - Restricts NULL value from being inserted into a column.
* **CHECK** - Verifies that all values in a field satisfy a condition.
* **DEFAULT** - Automatically assigns a default value if no value has been specified for the field.
* **UNIQUE** - Ensures unique values to be inserted into the field.
* **INDEX** - Indexes a field providing faster retrieval of records.
* **PRIMARY KEY** - Uniquely identifies each record in a table.
* **FOREIGN KEY** - Ensures referential integrity for a record in another table.



**[⬆ Back to Top](#table-of-contents)**
### **What is Cursor?**
* WHEN WE USE SELECT STMT IN DATABASE(ORACLE/SQLSERVER/MYSQL) ,   it allocate memory for that known as cursor.
* A cursor is a pointer to this context area. PL/SQL controls the context area through a Cursor.
* A Cursor can hold more than one row, but can process only one row at a time. The set of rows the cursor hold is called the active set.
* A cursor is a temporary work area created in the system memory when a SQL statement is executed. A cursor contains information on a select statement and the rows of data accessed by it.
* This temporary work area is used to store the data retrieved from the database and manipulate this data.

#### There are two type of cursor in PL/SQL:-

1. **Implicit cursor:-**
   * These are creating by default when DML statement like, INSERT, UPDATE, and DELETE statement are executed. They are also created when a SELECT statement that returns just one row is executed.
   * Implicit cursors are automatically created by oracle whenever an SQL statement is executed, when there is no explicit cursor for the statement. Programmers cannot control the implicit cursor and the information in it.


### Difference between WHERE and HAVING in SQL?
| Having                                                           | Where                                                                      |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------- |
| Having ke sath GROUP BY use hota hai                             |                                                                            |
| Having post filter hai(data fatch hone ke baad filter lagta hai) | where pre filter hai(isme pahle filter lagta hai phir fatch data hota hai) |
| having can be used only with select command                      | can be used with select update delete                                      |
| HAVING is used for column operations.                            | WHERE is used for row operations                                           |
| having ke aggrigate function sath kar sakte hai                  | where ke sath aggrigate function use nahi kar sakte                        |
```sql
a   c1  40
a   c2  50
b   c3  30
c   c1  20

select std, sum(score) as total from record group by std having total>60;
```

### **List of Mysql storage Engines/Table Type?**
Mysql ne apni requirment ke according alag-alag table type diye hai.
1. MyIsam:-
* Myisam good for select command.
* it support full text searching.
* it support table level locking.
* it support Blob and text column can be indexed.
2. Innodb
* it support for referential integrity.
* it support foreign key constraint.
* it support Row level locking.
* it support for transaction. 
3. CSV
* The CSV storage engine stores data in text file using comma separated values format.
4. Archive
5. memory 
6. black hole
7. merge
8. federated


### **Ques. What is Stored procedure?**
* Stored procedure is a function which cantains a collection of sql quries, the procedure can take inputs, process them and send back output.
* Stored procedure is a database object which is used to perform some specific task.
* Stored procedure is called explicitly.
* Store procedures is set of structure Query language (SQL) statement that perform particular task.
* Store procedures is set of structure Query language (SQL) statement with an assigned name, which are stored in a relation database 
management system as a group, so it can be reused and shered by multipal program.
* Advantage: Stored Procedures are precompiled and stored in the database. This enables the Database to execute the queries much faster. Since many queries can be included in a stored procedure, round trip time to execute multiple queries from source code to
Database and back is avoided.
* A procedure is a group of SQL statement that you can call by name.
* Store procedures is a database object which is used to perform some specific task.

__Advantage__
* Store procedure is reducing the complexity of code in code behind.
* Store procedures have repeatedly having data. It helps to reuse the code.
* It store in precompiled format so execution of speed is much faster than SQL statement.

```
1. Store procedures explicitly call hote hai.
2. Tiger automatic call hote hai.
3. Function inside the sql call hote hai.
```

```sql
create procedure procedure_name as
begain
  select name, age from emp;
end

execute procedure_name
```

```sql
CREATE OR REPLACE PROCEDURE ABCD
IS 
BEGIN
DBMS_OUTPUT.PUT_LINE('JAI PL BABA');
END;
sql>EXECUTE ABCD (sql>set serveroutput on)
```
```sql
ALTER procedure [dbo].[inemp]
@eno int,@enm varchar(20),@sl int
as
begin
insert into emp(EMPNO,ENAME,SAL) values(@eno,@enm,@sl);
end
```



### **Ques. What is Json?**
* Json stands for Javascript Object Notation and Json is lightweight data interchange format.
* Json is syntax for storing and exchanging data.
* it is easy for machine to parse and recreates.
* Json is often used when data is sent from a server to a web page.

__JSON Advantage__
* JSON does not have namespace.
* JSON is not extensible.


### **Ques. is a blank space or zero the same as a null value in sql?**
No 


MySql Interview Questions



Ques. Difference between inner & self & cross ?
Ans. 
Inner:-
Self:-
Cross:-



SQL Queries:-
-------?

Delete table
Delete table_name; (only table data del)drop table persons;
drop table persons;



Insert data in another table

Add column
ALTER TABLE table_name
ADD column_name datatype(size), column_name datatype(size));
ALTER TABLE table_name
ADD column_name datatype



Data insert/update in a column
update emp set city='noida' where lastname='saxena'

Rename Datatype
ALTER TABLE LALU MODIFY (MOBILE NUMBER(15));









1.  What are set operators in SQL?



1.  What are types of locks?
2. Sheared lock: When a shared lock is applied on data item, other transactions can only read the
item, but can&#39;t write into it.
1. Exclusive lock: When an exclusive lock is applied on data item, other transactions can&#39;t read or
write into the data item.
1.  How to delete duplicate record from a table?
SQL&gt;DELETE FROM EMP WHERE ROWID NOT IN (SELECT MAX (ROWID) FROM EMP GROUP BY
ROLL)





#### When you would use it
1. **Merging data**: When you need to combine data from two tables into a single result set while preserving all records.
2. **Handling missing data**: In scenarios where data might be missing or incomplete in one or both tables.
3. **Comparing data**: For data analysis, auditing, or quality control to compare and identify differences between two data sources.
4. **Reporting exceptions**: To identify and report data discrepancies or anomalies across tables.