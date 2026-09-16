### 🎯**What is Trigger?**
* A Trigger is a database object that **automatically executes (fires) when a specific event occurs on a table**.
* Interview Points
  * Triggers execute automatically.
  * They are associated with a table.
  * Trigger events are INSERT, UPDATE, DELETE.
  * Can execute BEFORE or AFTER an event.
  * Useful for auditing and data validation.
* Trigger  are set of structure Query language (SQL) statement that perform particular task. They invoke specific event (after Insert,u,d – before I,u,d)
* Database triggers are sets of commands that get executed when an event (Before Insert, After Insert, On Update, on delete of a row) occurs on a table.
* Triggers are special type of stored procedures that are defined to execute automatically in place or after data modification.
* Trigger allows you to execute a batch of SQL code an insert, update or delete command is execute against a specific table.
```sql
CREATE OR REPLACE TRIGGERRESTRICT_EMP
BEFORE INSERT ON EMP
BEGIN
RAISE_APPLICATION_ERROR(-20987,’INSERT MAT KAR NAHI HOGA’);
END;
```

### **Why Use Triggers?**
### Advantages of Triggers
* Maintain audit logs
* Track changes in data
* Enforce business rules
* Automatically update related tables
* **Automatic execution:-** Trigger automatically executes when an event like INSERT, UPDATE, or DELETE occurs.
* **Maintains data integrity:-** Helps enforce business rules and keep data consistent.
* **Automatic auditing:-** Can store old and new values in an audit/log table.
  * Example: Track who changed an employee's salary.
* **Reduces duplicate application code:-** Logic can be maintained at the database level instead of writing the same logic in multiple applications.
* **Automatic validation/actions:-** Can automatically perform actions when data changes.

### Disadvantages of Triggers
* **Hidden logic:-** Trigger runs automatically, so developers may not immediately know that additional operations are happening.
* **Difficult to debug:-** If something goes wrong, finding the trigger responsible can be difficult.
* **Performance impact:-** Triggers add extra database operations, which can slow down INSERT, UPDATE, or DELETE.
* Complex maintenance :- Multiple triggers can make database logic difficult to understand and maintain.
* Unexpected side effects:- One operation can automatically trigger another operation, which may produce unexpected results.

### Types of Triggers
1. BEFORE INSERT
2. AFTER INSERT
3. BEFORE UPDATE
4. AFTER UPDATE
5. BEFORE DELETE
6. AFTER DELETE
<div style="page-break-before: always;"></div>

#### Example of triger AFTER INSERT
* Suppose we want to log every new employee added.
```sql
-- create employee table
CREATE TABLE employees (
    id INT,
    name VARCHAR(50)
);

-- employee_log table
CREATE TABLE employee_log (
    log_message VARCHAR(100)
);
```

```sql
-- create Trigger after emp insert
CREATE TRIGGER trg_after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
INSERT INTO employee_log
VALUES (CONCAT('Employee Added: ', NEW.name));

-- insert data
INSERT INTO employees VALUES (1, 'Mohit');

-- MySQL automatically inserts:   into employee_log.
Employee Added: Mohit
```
<div style="page-break-before: always;"></div>

#### UPDATE Trigger Example (Employee Salary Update)
```sql
-- salary log table
CREATE TABLE salary_log (
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2)
);

-- create triger
CREATE TRIGGER trg_salary_update
AFTER UPDATE ON employees
FOR EACH ROW
INSERT INTO salary_log (
    emp_id,
    old_salary,
    new_salary
)
VALUES (
    OLD.id,
    OLD.salary,
    NEW.salary
);

-- now updte salary
UPDATE employees
SET salary = 60000
WHERE id = 1;

-- Trigger ke andar values
    -- Update se pehle:
    id = 1
    salary = 50000

    -- update ke baad
    id = 1
    salary = 60000


+--------+------------+------------+
| emp_id | old_salary | new_salary |
+--------+------------+------------+
|   1    |   50000    |   60000    |
+--------+------------+------------+
```

### 🎯**Difference between Trigger and Stored Procedure?**
* Trigger **automatically execute hota hai**, jabki Stored Procedure ko **explicitly call karna padta hai**.
* A Trigger is automatically executed when a specified event such as INSERT, UPDATE, or DELETE occurs on a table, whereas a Stored Procedure is a reusable set of SQL statements that must be explicitly called to execute.

| Trigger                                                | Stored Procedure                                       |
| ------------------------------------------------------ | ------------------------------------------------------ |
| Automatically execute hota hai                         | Manually call karna padta hai                          |
| `INSERT`, `UPDATE`, `DELETE` event se execute hota hai | `CALL` statement se execute hota hai                   |
| Specific table/event se associated hota hai            | Table se necessarily associated nahi hota              |
| Usually automatic actions/auditing ke liye             | Business logic/reusable operations ke liye             |
| Directly `CALL` nahi karte                             | `CALL procedure_name()` se call karte hain             |
| `OLD` aur `NEW` use kar sakta hai                      | `OLD` aur `NEW` trigger references available nahi hote |
