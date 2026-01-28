|  No.  | [View](#index)                 |
| :---: | ------------------------------ |
|       | [What is View?](#what-is-view) |
|       | [Create view](#create-view)    |
|       | [Show view](#show-view)        |
|       | [Alter view](#alter-view)      |
|       | [Deleted view](#deleted-view)  |

### **What is View?**
* A view is a **virtual table** based on the result set of a SELECT query.
* It does not store data itself but provides a way to look at data from one or more tables in a structured and reusable manner.
* It **behaves** like a **table** but **doesn't store** the **data physically**.

### **Create view**
```sql
Create view view_name As
Select column1, column2
From  table_name  
Where [condition];
```

#### **Show view**
```sql
SELECT * FROM view_name;
```

#### **Alter view**
* CREATE OR REPLACE VIEW Syntax
```sql
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

#### **Deleted view**
* A view is **deleted** with the **DROP VIEW statement**.
```sql
DROP VIEW view_name
DROP VIEW IF EXISTS view_name;
```