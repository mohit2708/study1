|  No.  | [Mysql]()                                                                                                                                                 |
| :---: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       | [Check version of the sql?](#ques-check-version-of-the-sql)                                                                                               |
|       | [Current date?](#current-date)                                                                                                                            |
|       | [How to copy a table in another table?](#ques-how-to-copy-a-table-in-another-table)                                                                       |
|       | [How to copy structure of a table but not data?](#ques-how-to-copy-structure-of-a-table-but-not-data)                                                     |
|       | [Create a table through another table/Duplicate table through another table?](#create-a-table-through-another-tableduplicate-table-through-another-table) |
|       | [Duplicate table through another table, with structure and data?](#duplicate-table-through-another-table-with-structure-and-data)                         |


#### **Ques. Check version of the sql?**
```sql
select version()
```
#### **Current date?**
```sql
select GETDATE();
```

### **Ques. How to copy a table in another table?**
```sql
CREATE TABLE EMP1 AS (SELECT * FROM EMP); //constraint will not copied.
```

### **Ques. How to copy structure of a table but not data?**
```sql
CREATE TABLE STD AS (SELECT * FROM EMP WHERE EMPNO=-1);
```

### **create a table through another table/Duplicate table through another table.**
```sql
CREATE TABLE IF NOT EXISTS new_table_name LIKE exsting_table_name;
```

### **Duplicate table through another table, with structure and data?**
```sql
CREATE TABLE IF NOT EXISTS new_table_name AS SELECT * FROM exsting_table_name;
```