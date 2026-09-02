|  No.  |                                                                               |
| :---: | ----------------------------------------------------------------------------- |
|       | [What Is Union & Union All?](#what-is-union--union-all)                       |
|       | [Difference between Union & Union All?](#difference-between-union--union-all) |

### 🎯**What Is Union & Union All?**
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

### 🎯**Difference between Union & Union All?**
| Union                                                     | Union All                                     |
| :-------------------------------------------------------- | :-------------------------------------------- |
| Union removes duplicate rows.                             | Union All does not remove the duplicate rows. |
| Union uses a distinct sort                                | Union All does not use a distinct sort        |
| Union can’t work with a column that has a text data type. | Union All can work with all data type column. |