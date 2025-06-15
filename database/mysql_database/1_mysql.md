

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
* When a SELECT statement is executed, the database(ORACLE/SQL SERVER/MYSQL) allocates a memory area to hold the result set, which is managed internally using a cursor.
* A cursor is a pointer to this context area. PL/SQL controls the context area through a Cursor.
* A Cursor can hold more than one row, but can process only one row at a time. The set of rows the cursor hold is called the active set.
* A cursor is a temporary work area created in the system memory when a SQL statement is executed. A cursor contains information on a select statement and the rows of data accessed by it.
* This temporary work area is used to store the data retrieved from the database and manipulate this data.

```sql
DELIMITER //

CREATE PROCEDURE process_customers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE cust_name VARCHAR(100);
    
    -- Declare the cursor
    DECLARE cur CURSOR FOR 
        SELECT name FROM customers;

    -- Declare continue handler for NOT FOUND condition
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO cust_name;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Do something with cust_name
        SELECT CONCAT('Processing customer: ', cust_name);

    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

DELIMITER ;

```

#### There are two type of cursor in PL/SQL:-

1. **Implicit cursor:-**
   * These are creating by default when DML statement like, INSERT, UPDATE, and DELETE statement are executed. They are also created when a SELECT statement that returns just one row is executed.
   * Implicit cursors are automatically created by oracle whenever an SQL statement is executed, when there is no explicit cursor for the statement. Programmers cannot control the implicit cursor and the information in it.



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




SQL Queries:-
-------?

Insert data in another table


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