|  No.  | [Joins](#joins)                                                                                 |
| :---: | ----------------------------------------------------------------------------------------------- |
|       | [What Is Joins?](#ques-what-is-joins)                                                           |
|       | [self join](#self-join)                                                                         |
|       | [INNER JOIN](#inner-join)                                                                       |
|       | [Left JOIN/LEFT OUTER JOIN](#left-joinleft-outer-join)                                          |
|       | [Right JOIN](#right-join)                                                                       |
|       | [Outer join](#outer-join)                                                                       |
|       | [CROSS Join](#cross-join)                                                                       |
|       | [Full Join/FULL OUTER JOIN](#full-joinfull-outer-join)                                          |
|       | [Difference between Delete, Truncate & Drop?](#ques-Difference-between-Delete,-Truncate-&-Drop) |

#### Ques. What Is Joins?
* A JOIN is a method used to combine rows from two or more tables based on a related column between them.
* MySQL JOINS are used with SELECT statement.

#### Many types of MySQL joins:
1. Self Join
2. Inner Join
3. Left JOIN
4. Right JOIN
5. Full Join
6. Outer Join
7. Cross Join 


#### Self Join
* A self join connects a table to itself. Used when you want to compare rows within the same table.
```sql
Customers table:                                      
+----+----------+-----+-----------+----------+        
| ID | NAME     | AGE | ADDRESS   | SALARY   |        
+----+----------+-----+-----------+----------+        
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |        
|  2 | Khilan   |  25 | Delhi     |  1500.00 |        
|  3 | kaushik  |  23 | Kota      |  2000.00 |        
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |        
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |   
|  6 | Komal    |  22 | MP        |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+

-- Example
SELECT c1.NAME AS Customer1, c2.NAME AS Customer2, c1.SALARY FROM Customers c1
JOIN Customers c2 ON c1.SALARY = c2.SALARY AND c1.ID < c2.ID;
-- Output:
+------------+------------+----------+
| Customer1  | Customer2  | SALARY   |
+------------+------------+----------+
| Ramesh     | kaushik    | 2000.00  |
+------------+------------+----------+
```
<div style="page-break-before: always;"></div>


#### INNER JOIN
* The MySQL Inner Join is used to returns only those results from the tables that **match** the specified condition and hides other rows and columns.
* Inner join: Inner join return rows when there is at least one match of rows between the tables.
```sql
Customers table:                                      
+----+----------+-----+-----------+----------+        
| ID | NAME     | AGE | ADDRESS   | SALARY   |        
+----+----------+-----+-----------+----------+        
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |        
|  2 | Khilan   |  25 | Delhi     |  1500.00 |        
|  3 | kaushik  |  23 | Kota      |  2000.00 |        
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |        
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |   
|  6 | Komal    |  22 | MP        |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+
Order table:
+-----+---------------------+-------------+--------+
|OID  | DATE                | CUSTOMER_ID | AMOUNT |
+-----+---------------------+-------------+--------+
| 101 | 2009-11-20 00:00:00 |           2 |   1560 |
| 103 | 2008-05-20 00:00:00 |           4 |   2060 |
+-----+---------------------+-------------+--------+

SELECT customers.name, customers.age, customers.salary, order.date 
FROM customers INNER JOIN order 
ON customers.id = order.CUSTOMER_ID;
+----------+-----+---------+---------------------+
| NAME     | AGE | SALARY  |   DATE              | 
+----------+-----+---------+---------------------+
| Khilan   |  25 | 1500.00 | 2009-11-20 00:00:00 |        
| Chaitali |  25 | 6500.00 | 2008-05-20 00:00:00 |     
+----------+-----+---------+---------------------+

-- Example 2
Order table:
+-----+---------------------+-------------+--------+
|OID  | DATE                | CUSTOMER_ID | AMOUNT |
+-----+---------------------+-------------+--------+
| 102 | 2009-10-08 00:00:00 |           3 |   3000 |
| 100 | 2009-10-08 00:00:00 |           3 |   1500 |
| 101 | 2009-11-20 00:00:00 |           2 |   1560 |
| 103 | 2008-05-20 00:00:00 |           4 |   2060 |
+-----+---------------------+-------------+--------+

-- Output:-
SQL> SELECT ID, NAME, AMOUNT, DATE   FROM CUSTOMERS
INNER JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

+----+----------+-----+--------+
| ID | NAME     | AGE | AMOUNT |
+----+----------+-----+--------+
|  3 | kaushik  |  23 |   3000 |
|  3 | kaushik  |  23 |   1500 |
|  2 | Khilan   |  25 |   1560 |
|  4 | Chaitali |  25 |   2060 |
+----+----------+-----+--------+
```
<div style="page-break-before: always;"></div>

#### Left JOIN/LEFT OUTER JOIN
* The LEFT JOIN keyword returns all records from the left table (the table listed first), and the matching records (if any) from the right table (table2).
```sql
CUSTOMERS Table
+----+----------+-----+-----------+----------+ 
| ID | NAME     | AGE | ADDRESS   | SALARY   |
+----+----------+-----+-----------+----------+
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
|  2 | Khilan   |  25 | Delhi     |  1500.00 |
|  3 | kaushik  |  23 | Kota      |  2000.00 |
|  4 | Chaitali |  25 | Mumbai    |  6500.00 |
|  5 | Hardik   |  27 | Bhopal    |  8500.00 |
|  6 | Komal    |  22 | MP        |  4500.00 |
|  7 | Muffy    |  24 | Indore    | 10000.00 |
+----+----------+-----+-----------+----------+

Orders Table
+-----+---------------------+-------------+--------+
| OID | DATE                | CUSTOMER_ID | AMOUNT |
+-----+---------------------+-------------+--------+
| 102 | 2009-10-08 00:00:00 |           3 |   3000 |
| 100 | 2009-10-08 00:00:00 |           3 |   1500 |
| 101 | 2009-11-20 00:00:00 |           2 |   1560 |
| 103 | 2008-05-20 00:00:00 |           4 |   2060 |
+-----+---------------------+-------------+--------+

SQL> SELECT  ID, NAME, AMOUNT, DATE FROM CUSTOMERS LEFT JOIN ORDERS
   ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

Result:-
+----+----------+--------+---------------------+
| ID | NAME     | AMOUNT | DATE                |
+----+----------+--------+---------------------+
|  1 | Ramesh   |   NULL | NULL                |
|  2 | Khilan   |   1560 | 2009-11-20 00:00:00 |
|  3 | kaushik  |   3000 | 2009-10-08 00:00:00 |
|  3 | kaushik  |   1500 | 2009-10-08 00:00:00 |
|  4 | Chaitali |   2060 | 2008-05-20 00:00:00 |
|  5 | Hardik   |   NULL | NULL                |
|  6 | Komal    |   NULL | NULL                |
|  7 | Muffy    |   NULL | NULL                |
+----+----------+--------+---------------------+
```
<div style="page-break-before: always;"></div>

#### Right JOIN
* The RIGHT JOIN keyword returns **all records** from the **right table** (table2), and the **matching records** (if any) from the **left table** (table1).
```sql
-- Customers Table
+----+----------+
| ID | NAME     |
+----+----------+
|  1 | Ramesh   |
|  2 | Khilan   |
|  3 | Kaushik  |

-- Orders Table
+----------+------------+
| OrderID  | CustomerID |
+----------+------------+
|   101    |     2      |
|   102    |     3      |
|   103    |     4      |
+----------+------------+

-- RIGHT JOIN Result
SELECT Customers.NAME, Orders.OrderID FROM Customers RIGHT JOIN Orders 
ON Customers.ID = Orders.CustomerID;
+----------+------------+
| NAME     | OrderID    |
+----------+------------+
| Khilan   |   101      |
| Kaushik  |   102      |
| NULL     |   103      |
+----------+------------+
```
<div style="page-break-before: always;"></div>

#### Outer join
* Returns all rows from both tables, Matching and non-matching rows.
* NULL values where no match exists
```sql
SELECT column_list
FROM table1
FULL OUTER JOIN table2 ON table1.column = table2.column;
```

```sql
-- Example query
employees:

| employee_id | employee_name | department_id |
| ----------- | ------------- | ------------- |
| 1           | John Smith    | 101           |
| 2           | Mary Johnson  | 102           |
| 3           | Sam Brown     | 103           |

departments:

| department_id | department_name |
| ------------- | --------------- |
| 101           | HR              |
| 102           | Finance         |
| 104           | Marketing       |

SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
FULL OUTER JOIN departments ON employees.department_id = departments.department_id;

| employee_id | employee_name | department_name |
| ----------- | ------------- | --------------- |
| 1           | John Smith    | HR              |
| 2           | Mary Johnson  | Finance         |
| 3           | Sam Brown     | NULL            |
| NULL        | NULL          | Marketing       |
```
<div style="page-break-before: always;"></div>


#### CROSS Join
* The CROSS JOIN keyword returns all records from both tables (table1 and table2).
* If you have a Products table with 3 products and a Colors table with 2 colors, a CROSS JOIN would return a result set with 6 combinations (3 * 2):
```sql
-- Products table
| ProductID | ProductName |
| --------- | ----------- |
| 1         | T-Shirt     |
| 2         | Jeans       |

-- Colors table
| ColorID | Color |
| ------- | ----- |
| 1       | Red   |
| 2       | Blue  |

-- Output:-
SELECT Products.ProductName, Colors.Color
FROM Products
CROSS JOIN Colors;

| ProductName | Color |
| ----------- | ----- |
| T-Shirt     | Red   |
| T-Shirt     | Blue  |
| Jeans       | Red   |
| Jeans       | Blue  |

```
<div style="page-break-before: always;"></div>

#### Full Join/FULL OUTER JOIN
* A FULL JOIN (also called a FULL OUTER JOIN) returns all rows when there is a match in either left (table1) or right (table2) table. It returns all records from both tables, and the result set will have NULL values for columns where there is no match.
#### Key Points:
* Rows from both tables are included even if there is no match.
* If there is no match, the columns from the table that doesn’t have a match will contain NULL.
* This join is useful when you want to retrieve all records, whether or not there's a match in both tables.

```sql
-- Employees Table:
| EmployeeID | EmployeeName | DepartmentID |
| ---------- | ------------ | ------------ |
| 1          | John         | 10           |
| 2          | Jane         | 20           |
| 3          | Mike         | 30           |
| 4          | Sara         | NULL         |

-- Departments Table:
| DepartmentID | DepartmentName |
| ------------ | -------------- |
| 10           | HR             |
| 20           | IT             |
| 30           | Sales          |
| 40           | Marketing      |

-- Output:-
SELECT Employees.EmployeeID, Employees.EmployeeName, Employees.DepartmentID, Departments.DepartmentName
FROM Employees
FULL JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
| EmployeeID | EmployeeName | DepartmentID | DepartmentName |
| ---------- | ------------ | ------------ | -------------- |
| 1          | John         | 10           | HR             |
| 2          | Jane         | 20           | IT             |
| 3          | Mike         | 30           | Sales          |
| 4          | Sara         | NULL         | NULL           |
| NULL       | NULL         | 40           | Marketing      |
```