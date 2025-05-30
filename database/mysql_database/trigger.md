### **What is Trigger?**
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