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
