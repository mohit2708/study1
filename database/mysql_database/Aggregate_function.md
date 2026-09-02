### 🎯 **What is Aggregate function?**
```sql
-- Sum() :- The SUM() function returns the total sum of a numeric column. 
SELECT SUM(column_name) FROM table_name;

-- AVG():- The AVG() function returns the average value of a numeric column. 
SELECT AVG(column_name) FROM table_name;

-- MAX() :- The MAX() function returns the largest value of the selected column.
SELECT MAX(column_name) FROM table_name;

-- Min():- The MIN() function returns the smallest value of the selected column.
SELECT MIN(column_name) FROM table_name;

-- count():- The COUNT() function returns the number of rows that matches a specified criterion.
SELECT COUNT(column_name) FROM table_name;
```

### 🎯 **COUNT() vs COUNT(*) in MySQL?**
* **COUNT(*)** table ki total rows count karta hai, chahe column value NULL ho ya na ho.
* **COUNT(column_name)** sirf us column ki non-NULL values count karta hai. NULL values ko ignore karta hai.

#### Example
```sql
| id | name  | salary |
| -- | ----- | ------ |
| 1  | Mohit | 50000  |
| 2  | Amit  | NULL   |
| 3  | Rahul | 60000  |
| 4  | Neha  | NULL   |

SELECT COUNT(*) FROM employee;  -- Output:- 4
SELECT COUNT(salary) FROM employee; -- Output:- 2
```