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