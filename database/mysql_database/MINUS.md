### 🎯**What is MINUS?**
* MINUS operator will return only those rows which are **unique(distinct)** in only first SELECT query and not those rows which are **common to both first and second** SELECT queries.
```sql
-- Employees                        -- Managers
| EmpID | EmpName | Department |  | EmpID | EmpName | Department |
| ----- | ------- | ---------- || ----- | ------- | ---------- |
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