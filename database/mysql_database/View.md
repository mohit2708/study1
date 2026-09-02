### view
|  No.  | View                                                                 |
| :---: | -------------------------------------------------------------------- |
|       | [What is View?](#what-is-view)                                       |
|       | [Create view](#create-view)                                          |
|       | [Show view](#show-view)                                              |
|       | [Alter view](#alter-view)                                            |
|       | [Deleted view](#deleted-view)                                        |
|       | [Views used in real projects?](#why-are-views-used-in-real-projects) |


### **What is View?**
* A view is a **virtual table** based on the result set of a SELECT query.
* It does not store data itself but provides a way to look at data from one or more tables in a structured and reusable manner.
* It **behaves** like a **table** but **doesn't store** the **data physically**.

#### Why use Views?
* Security provide karti hai (sab columns hide kar sakte hain).
* Complex queries ko simple banati hai.
* Reusable query hoti hai.
* Data abstraction provide karti hai.
* Multiple tables ko ek virtual table ki tarah dikhaya ja sakta hai.

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
<div style="page-break-before: always;"></div>

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

#### Can we insert data into a View?
* Haan, lekin sirf simple views me.

#### Can we create a View on another View?
* haa
```sql
CREATE VIEW view2 AS
SELECT * FROM view1;
```

#### Why are Views used in real projects?
* Users ko sirf required columns dikhaye ja sakte hain bina original table ka access diye.
* Security, code reusability, complex query simplification, aur data abstraction ke liye Views use ki jaati hain. 

