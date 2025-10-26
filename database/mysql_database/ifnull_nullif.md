### **IFNULL()**
* If the first expression is not NULL, it will return the first expression, which is 'Hello' value.
```sql
SELECT IFNULL("Hello", "javaTpoint");   # Output:- Hello
```
```sql
SELECT IFNULL(NULL,5);  # Output:- 5
```
```sql
+-----------+-----------+-----------+
| emp_name  | cellphone | homephone |
+-----------+-----------+-----------+
| mohit     | 2531452   |  NULL     |
| Krishna   | NULL      | 345634634 |
| shivani   | 551113    | NULL      |
| akshra    | NULL      | 6574576   |
| abhinav   | NULL      | 674576457 |
+-----------+-----------+-----------+
SELECT emp_name, IFNULL(cellphone, homephone) phone  FROM  student_contact;
+-----------+-----------+
| emp_name  | phone     |
+-----------+-----------+
| mohit     | 2531452   |
| Krishna   | 345634634 |
| shivani   | 551113    |
| akshra    | 6574576   |
| abhinav   | 674576457 |
+-----------+-----------+
```
<div style="page-break-before: always;"></div>

### **NULLIF()**
* The NULLIF function accepts two expressions, and if the first expression is equal to the second expression, it returns the NULL. Otherwise, it returns the first expression.
```sql
SELECT NULLIF("javaTpoint", "javaTpoint");  # Output:- NULL
```
```sql
SELECT NULLIF("Hello", "404");  # Output:- Hello
```
```sql
+---------+----------------+-------------+--------+---------------+
| cust_id | cust_name      | occupation  | income | qualification |
+---------+----------------+-------------+--------+---------------+
|       1 | John Miller    | Developer   | 20000  | Btech         |
|       2 | Mark Robert    | Engineer    | 40000  | Btech         |
|       3 | Reyan Watson   | Scientist   | 60000  | MSc           |
|       4 | Shane Trump    | Businessman | 10000  | MBA           |
|       5 | Adam Obama     | Manager     | 80000  | MBA           |
|       6 | Rincky Ponting | Cricketer   | 200000 | Btech         |
+---------+----------------+-------------+--------+---------------+


SELECT cust_name, occupation, qualification, NULLIF (qualification,"Btech") result FROM customer;
Output:-
+----------------+-------------+---------------+--------+
| cust_name      | occupation  | qualification | result |
+----------------+-------------+---------------+--------+
| John Miller    | Developer   | Btech         | NULL   |
| Mark Robert    | Engineer    | Btech         | NULL   |
| Reyan Watson   | Scientist   | MSc           | MSc    |
| Shane Trump    | Businessman | MBA           | MBA    |
| Adam Obama     | Manager     | MBA           | MBA    |
| Rincky Ponting | Cricketer   | Btech         | NULL   |
+----------------+-------------+---------------+--------+
```