### **What is Intersect?**
* The INTERSECT statement will return only those rows that are **identical/common** to both of the SELECT statements from two or more tables
```sql
-- Employees                          -- Managers
| EmpID | EmpName | Department |  | EmpID | EmpName | Department |
| ----- | ------- | ---------- || ----- | ------- | ---------- |
| 1     | Alice   | HR         |      | 2     | Bob     | IT         |
| 2     | Bob     | IT         |      | 4     | David   | IT         |
| 3     | Charlie | Finance    |      | 6     | Frank   | Sales      |
| 4     | David   | IT         |      | 7     | Grace   | Marketing  |
| 5     | Eve     | Marketing  |

-- Output
SELECT EmpID, EmpName, Department FROM Employees
INTERSECT
SELECT EmpID, EmpName, Department FROM Managers;
| EmpID | EmpName | Department |
| ----- | ------- | ---------- |
| 2     | Bob     | IT         |
| 4     | David   | IT         |

```