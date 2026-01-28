### **Ques. What is Stored procedure?**
- Stored procedures are precompiled collections of SQL statements that can be executed on demand. They help improve performance by reducing the amount of SQL sent to the server.
* A Stored Procedure is a precompiled SQL program stored inside the MySQL database that you can run again and again.
* It is used to:
  * Reduce repeated SQL code
  * Improve performance
  * Add security
  * Apply business logic at the database level
* Advantages of Stored Procedures
  * Faster execution (precompiled)
  * Code reusability
  * Better security (direct table access can be restricted)
  * Reduced network traffic
  * Easy maintenance


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

