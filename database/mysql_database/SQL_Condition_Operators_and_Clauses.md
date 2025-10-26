|  No.  | [SQL Comments?](#sql-comments)                            |
| :---: | --------------------------------------------------------- |
|       | [Equal to(=)](#equal-to)                                  |
|       | [Greater than(>)](#greater-than)                          |
|       | [Less than(<)](#less-than)                                |
|       | [Greater than or equal to(>=)](#greater-than-or-equal-to) |
|       | [Less than or equal to(<=)](#less-than-or-equal-to)       |
|       | [Not equal to(<> or !=)](#not-equal-to-or-)               |
|       | [WHERE](#where)                                           |
|       | [Truncate](#truncate)                                     |
|       | [IS NULL and IS NOT NULL](#is-null-and-is-not-null)       |
|       | [AND](#and)                                               |
|       | [OR](#or)                                                 |
|       | [NOT](#not)                                               |
|       | [IN Operator](#in-operator)                               |
|       | [NOT IN Operator](#not-in-operator)                       |
|       | [IF()](#if)                                               |
|       | [BETWEEN](#between)                                       |
|       | [NOT BETWEEN](#not-between)                               |


## SQL Condition Operators and Clauses
### Comparison operators

#### Equal to(=)
```sql
WHERE salary = 50000
```

#### Greater than(>)
```sql
WHERE age > 30
```

#### Less than(<)
```sql
WHERE age < 30
```

#### Greater than or equal to(>=)
```sql
WHERE price >= 20.00
```

#### Less than or equal to(<=)
```sql
WHERE rating <= 4.5
```

#### Not equal to(<> or !=)
```sql
WHERE country <> 'USA'
```

### Logical operators

#### **AND**
* Displays a record if all conditions are TRUE
* AND is an operator that **combines two conditions**. **Both conditions must be true** for the row to be included in the result set.
* The MySQL AND Condition (also called the AND Operator) is used to test two or more conditions in a SELECT, INSERT, UPDATE, or DELETE statement.
```sql
-- syntex
SELECT column_name(s)
FROM table_name
WHERE column_1 = value_1 AND column_2 = value_2;
-- example
SELECT * FROM contacts
WHERE state = 'California' AND contact_id > 3000;
```

#### **OR**
* Displays a record if any of the conditions are TRUE
* OR is an operator that filters the result set to only include rows where either condition is true.
```sql
SELECT column_name
FROM table_name WHERE column_name = value_1 OR column_name = value_2;
```

#### **NOT**
* Reverses the logical outcome of an operator
```sql
WHERE NOT country = 'UK'
```

### Special operators
#### **WHERE**
* WHERE is a clause that indicates you want to filter the result set to include only rows where the following condition is true.
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator value;
```

#### **Truncate**
* A truncate SQL statement is used to **remove all rows** (complete data) from a table.
* TRUNCATE is a **DDL**(Data Definition Language) command and is used to delete all the rows or tuples from a table. Unlike the DELETE command, the TRUNCATE command does not contain a WHERE clause.
```sql
TRUNCATE TABLE table_name;
```

#### **ROUND()**
* The ROUND() function is used to round a numeric value to a specified number of decimal places.*
* syntex:- syntex:- ROUND(number, decimal_places)
```sql
SELECT ROUND(123.4567, 2);  -- Returns 123.46
SELECT ROUND(123.4567, 0);  -- Returns 123
SELECT ROUND(123.4567, -1); -- Returns 120 (rounds to the nearest 10)

-- example:-
SELECT ROUND(salary, 2) AS rounded_salary FROM employees;
```

#### **Case**
* CASE statements are used to create different outputs (usually in the SELECT statement). It is SQL’s way of handling if-then logic.
```sql
SELECT column_name,
  CASE
    WHEN condition THEN 'Result_1'
    WHEN condition THEN 'Result_2'
    ELSE 'Result_3'
  END
FROM table_name;
```

#### **GROUP BY**
* GROUP BY is a clause in SQL that is only used with aggregate functions. It is used in collaboration with the SELECT statement to arrange identical data into groups.
```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;
```

#### **HAVING**
* HAVING was added to SQL because the WHERE keyword could not be used with aggregate functions.
```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > value;
```

#### **LIMIT**
* LIMIT is a clause that lets you specify the maximum number of rows the result set will have.
```sql
SELECT column_name(s)
FROM table_name
LIMIT number;
```

#### **ORDER BY**
* ORDER BY is a clause that indicates you want to sort the result set by a particular column either alphabetically or numerically.
```sql
SELECT column_name
FROM table_name
ORDER BY column_name ASC | DESC;
```

#### **SELECT DISTINCT**
* SELECT DISTINCT specifies that the statement is going to be a query that returns unique values in the specified column(s).
```sql
SELECT DISTINCT column_name
FROM table_name;
```

#### **With**
* WITH clause lets you store the result of a query in a temporary table using an alias. You can also define multiple temporary tables using a comma and with one instance of the WITH keyword.
* The WITH clause is also known as common table expression (CTE) and subquery factoring.
```sql
WITH temporary_name AS (
   SELECT *
   FROM table_name)
SELECT *
FROM temporary_name
WHERE column_name operator value;
```

### **IS NULL and IS NOT NULL**
* IS NULL and IS NOT NULL are operators used with the WHERE clause to test for empty values.
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IS NULL;
```

### **IN Operator**
* The IN operator is a shorthand for multiple OR conditions, It reduces the use of multiple OR conditions in SELECT, INSERT, UPDATE, and DELETE queries.
* The IN operator is used to retrieves results when the specified value matches any value in a set of values or is returned by a subquery. 
* This operator allows us to specify multiple values along with the WHERE clause. 
```sql
select * from customers
+----+----------+-----+-----------+-----------+
| cust_id | cust_name | city      | occupation|
+---------+-----------+-----------+-----------+
|  1      | Peter     | Londen    | Business  |
|  2      | Joseph    | Texas     | Doctor    |
|  3      | Mark      | New Delhi | Engineer  |        
|  4      | Michael   | New York  | Scientist |
|  5      | Alexander | Maxico    | Student   |
+---------+-----------+-----------+-----------+
mysql> SELECT * FROM customer WHERE occupation IN ('Doctor', 'Scientist', 'Engineer');

+----+----------+-----+-----------+-----------+
| cust_id | cust_name | city      | occupation|
+---------+-----------+-----------+-----------+
|  2      | Joseph    | Texas     | Doctor    |
|  3      | Mark      | New Delhi | Engineer  |        
|  4      | Michael   | New York  | Scientist |
+---------+-----------+-----------+-----------+
```

### **NOT IN Operator**
* selects all customers that are located in "Texas", or "New York":
```sql
SELECT * FROM Customers WHERE city NOT IN ('Texas', 'New York');

Output:-
+----+----------+-----+-----------+-----------+
| cust_id | cust_name | city      | occupation|
+---------+-----------+-----------+-----------+
|  1      | Peter     | Londen    | Business  |
|  3      | Mark      | New Delhi | Engineer  |        
|  5      | Alexander | Maxico    | Student   |
+---------+-----------+-----------+-----------+
```

### **IF()**
```sql
SELECT IF(200>350,'YES','NO'); -- Output:- NO
SELECT IF(251 = 251,' Correct','Wrong');  -- Output:- Correct

--
SELECT salary, IF(salary>3000,"Mature","Immature") As Result FROM employee;
+---------+----------+
| salary  | Result   |
+---------+----------+
| 2957.00 | Immature |
| 3100.00 | Mature   |
+---------+----------+
```
```sql
SELECT IF(STRCMP('Rinky Ponting','Yuvraj Singh')=0, 'Correct', 'Wrong');
```

#### **BETWEEN**
* The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.
* The BETWEEN operator is inclusive: begin and end values are included.
```sql
SELECT column_name(s) FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

#### **NOT BETWEEN**
* To display the products outside the range of the previous example, use NOT BETWEEN:
```sql
SELECT column_name(s) FROM table_name
WHERE column_name NOT BETWEEN value1 AND value2;
```

### **Ques. Difference between Group By And Order By?**
```sql
| id  | product  | category  | quantity | price |
| --- | -------- | --------- | -------- | ----- |
| 1   | Apple    | Fruit     | 10       | 1.00  |
| 2   | Banana   | Fruit     | 5        | 0.50  |
| 3   | Carrot   | Vegetable | 7        | 0.30  |
| 4   | Apple    | Fruit     | 3        | 1.00  |
| 5   | Broccoli | Vegetable | 4        | 0.80  |
```
#### **Order By**
* ORDER BY clause is used to **sort the data** returned by a query in **ascending** or **descending** order.
```sql
SELECT product, category, quantity, price FROM sales ORDER BY price DESC;
| product  | category  | quantity | price |
| -------- | --------- | -------- | ----- |
| Apple    | Fruit     | 10       | 1.00  |
| Apple    | Fruit     | 3        | 1.00  |
| Broccoli | Vegetable | 4        | 0.80  |
| Banana   | Fruit     | 5        | 0.50  |
| Carrot   | Vegetable | 7        | 0.30  |
```

#### **Group By**
* Group by statement is used to group the rows that have the same value. 
* It is used with aggregate functions for example AVG(), COUNT(), SUM()etc. 
```sql
SELECT category, SUM(quantity) AS total_quantity
FROM sales GROUP BY category;
| category  | total\_quantity |              |
| --------- | --------------- | ------------ |
| Fruit     | 18              | (10 + 5 + 3) |
| Vegetable | 11              | (7 + 4)      |
```

#### **We can use together GROUP BY and ORDER BY**
```sql
-- You Can Use Both Together
SELECT category, SUM(quantity) AS total_quantity
FROM sales
GROUP BY category
ORDER BY total_quantity DESC;

| category  | total\_quantity |
| --------- | --------------- |
| Fruit     | 18              |
| Vegetable | 11              |
```


### **Difference between WHERE and HAVING in SQL?**
#### **Where**
* WHERE Clause is used to **filter** the records from the table or used while joining more than one table.
* Cannot be used with aggregate functions (like SUM(), COUNT(), AVG(), etc.).
```sql
SELECT * FROM emp WHERE salary > 50000;
```

#### **HAVING**
* HAVING Clause is used to filter the records from the groups based on the given condition in the HAVING Clause.
* It is applied after the grouping and aggregation of data.
```sql
SELECT department, COUNT(*) AS num_empl FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

| Having                                                           | Where                                                                      |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------- |
| Having ke sath GROUP BY use hota hai                             |                                                                            |
| Having post filter hai(data fatch hone ke baad filter lagta hai) | where pre filter hai(isme pahle filter lagta hai phir fatch data hota hai) |
| having can be used only with select command                      | can be used with select update delete                                      |
| HAVING is used for column operations.                            | WHERE is used for row operations                                           |
| having ke aggrigate function sath kar sakte hai                  | where ke sath aggrigate function use nahi kar sakte                        |

### **Ques. Difference between In and Between Operator in SQL?**
* BETWEEN operator is used to **select a range of data between two values** while The IN operator allows you to **specify multiple values**.
* The BETWEEN operator selects a range of data between two values. The values can be numbers, text,etc.
```sql
+----+----------+--------+
| ID | NAME     | mark   |
+----+----------+--------+
|  1 | Ramesh   |   89   |
|  2 | Khilan   |   81   |
|  3 | kaushik  |   73   |
|  3 | kaushik  |   67   |
|  4 | Chaitali |   52   |
+----+----------+--------+

-- between
SELECT * FROM emp WHERE marks BETWEEN 50 AND 80
+----+----------+--------+
| ID | NAME     | mark   |
+----+----------+--------+
|  3 | kaushik  |   73   |
|  3 | kaushik  |   67   |
|  4 | Chaitali |   52   |
+----+----------+--------+

-- In
SELECT * FROM emp WHERE marks IN (89,73)
+----+----------+--------+
| ID | NAME     | mark   |
+----+----------+--------+
|  1 | Ramesh   |   89   |
|  3 | kaushik  |   73   |
+----+----------+--------+
```

