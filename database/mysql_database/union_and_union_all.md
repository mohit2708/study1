### 🎯**Ques. What Is Union & Union All?**
* Both UNION and UNION ALL Operator combine rows from result sets into a single result set.
  
#### UNION
* The union operator **combines** the results of two or more select statements by **removing duplicate rows**.
* The columns and the data types must be the same in select statements.
```sql
+----+----------+       +----+----------+
| ID | NAME     |       | ID | NAME     |   
+----+----------+       +----+----------+ 
|  1 | Ramesh   |       |  3 | kaushik  | 
|  2 | Khilan   |       |  4 | Mohit    |     
|  3 | kaushik  |       |  5 | abhay    |     
+----+----------+       +----+----------+

Select Column1, Column2, Column3 from Table A
UNION
Select Column1, Column2, Column3 from Table B

+----+----------+    
| ID | NAME     |       
+----+----------+      
|  1 | Ramesh   |     
|  2 | Khilan   |       
|  3 | kaushik  |       
|  4 | Mohit    |       
|  5 | abhay    |
+----+----------+
```
<div style="page-break-before: always;"></div>

#### UNION ALL
* The UNION operator selects only distinct values by default. To **allow duplicate values**, use UNION ALL
```sql
Select Column1, Column2, Column3 from Table A
UNION ALL
Select Column1, Column2, Column3 from Table B

+----+----------+
| ID | NAME     |
+----+----------+
|  1 | Ramesh   |
|  2 | Khilan   |
|  3 | kaushik  |
|  3 | kaushik  |
|  4 | Mohit    |
|  5 | abhay    |
+----+----------+
```

### 🎯**Ques. Difference between Union & Union All?**
| Union                                                     | Union All                                     |
| :-------------------------------------------------------- | :-------------------------------------------- |
| Union removes duplicate rows.                             | Union All does not remove the duplicate rows. |
| Union uses a distinct sort                                | Union All does not use a distinct sort        |
| Union can’t work with a column that has a text data type. | Union All can work with all data type column. |
<div style="page-break-before: always;"></div>

### 🎯**What is MINUS?**
* MINUS operator will return only those rows which are **unique(distinct)** in only first SELECT query and not those rows which are **common to both first and second** SELECT queries.
```sql
-- Employees                        -- Managers
| EmpID | EmpName | Department |    | EmpID | EmpName | Department |
| ----- | ------- | ---------- |    | ----- | ------- | ---------- |
| 1     | Alice   | HR         |    | 2     | Bob     | IT         |
| 2     | Bob     | IT         |    | 4     | David   | IT         |
| 3     | Charlie | Finance    |    | 6     | Frank   | Sales      |
| 4     | David   | IT         |    | 7     | Grace   | Marketing  |
| 5     | Eve     | Marketing  |

-- output:-
SELECT EmpID, EmpName, Department FROM Employees
MINUS
SELECT EmpID, EmpName, Department FROM Managers;
| EmpID | EmpName | Department |
| ----- | ------- | ---------- |
| 1     | Alice   | HR         |
| 3     | Charlie | Finance    |
| 5     | Eve     | Marketing  |
```

#### Key characteristics of the MINUS operator:
* **Returns distinct rows:** Only unique rows from the first query that are not found in the second are returned.
* **Requires compatible SELECT statements:** Both SELECT statements involved in the MINUS operation must have the same number of columns, and the corresponding columns must have compatible data types and be in the same order. 

* **Note:-** While MINUS is a standard SQL operator supported by many database systems (like Oracle, PostgreSQL), **MySQL does not** directly **support** the MINUS operator.

#### Achieving the MINUS functionality in MySQL:
* We can achieve the same results as MINUS in MySQL using various techniques, most commonly by combining **LEFT JOIN** and **WHERE** clauses, or using **subqueries** with **NOT IN** or **NOT EXISTS**.

1. Using LEFT JOIN
```sql
SELECT a.*
FROM table_a AS a
LEFT JOIN table_b AS b ON a.id = b.id
WHERE b.id IS NULL;
```

2. Using NOT IN
```sql
SELECT *
FROM table_a
WHERE id NOT IN (SELECT id FROM table_b);
```

3. Using NOT EXISTS
```sql
SELECT *
FROM table_a AS a
WHERE NOT EXISTS (SELECT 1 FROM table_b AS b WHERE a.id = b.id);
```

```sql
table_a

id	value
1	Apple
2	Banana
3	Cherry
4	Date

----------------------
table_b

id	value
2	Banana
4	Date

------Output:----------
id	value
1	Apple
3	Cherry
```

### **What is EXCEPT?**
* same as minus nothing different.
* 