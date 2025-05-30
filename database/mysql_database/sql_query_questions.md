### Table of Contents

|  No.  | Questions                                                                                                                                  |
| :---: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|       | [How to copy a table in another table?](#ques-how-to-copy-a-table-in-another-table)                                                        |
|       | [How to copy structure of a table but not data?](#ques-how-to-copy-structure-of-a-table-but-not-data)                                      |
|       | [Delete Table?](#DELETE-TABLE)                                                                                                             |
|       | [Delete Duplicate Records?](#delete-duplicate-records)                                                                                     |
|       | [Add foreign key?](#add-foreign-key)                                                                                                       |
|       | [Highest Salary Department wise?](#highest-salary-department-wise)                                                                         |
|       | [Highest Salary Department wise with name?](#ques-find-the-highest-salary-of-each-department-with-name)                                    |
|       | [How to find Nth highest salary from a table?](#ques-how-to-find-nth-highest-salary-from-a-table)                                          |
|       | [Ques. Top 5 Salery?](#ques-top-5-salery)                                                                                                  |
|       | [Replace a Column Values from 'male' to 'female' and 'female' to 'male'?](#replace-a-column-values-from-male-to-female-and-female-to-male) |
|       | [Find Names of students whose age is greater than 21?](#find-names-of-students-whose-age-is-greater-than-21)                               |


|  No.  | [Aggregate function](#aggregate-function)      |
| :---: | ---------------------------------------------- |
|       | [SUM()](#aggregate-function)                   |
|       | [AVG()](#avg)                                  |
|       | [Max()](#max)                                  |
|       | [MIN()](#min)                                  |
|       | [COUNT()](#count)                              |
|       | [ROUND()](#round)                              |
|       | [BETWEEN()](#between)                          |
|       | [AND](#and)                                    |
|       | [OR](#or)                                      |
|       | [CASE](#case)                                  |
|       | [Aliases](#aliases)                            |
|       | [IS NULL / IS NOT NULL](#is-null--is-not-null) |
|       | [GROUP BY](#group-by)                          |
|       | [HAVING](#having)                              |
|       | [LIMIT](#limit)                                |
|       | [ORDER BY](#order-by)                          |
|       | [SELECT DISTINCT](#select-distinct)            |
|       | [With](#with)                                  |
|       | [WHERE](#where)                                |
|       | [UPDATE](#update)                              |

|  No.  | [Questions]()                                                                    |
| :---: | -------------------------------------------------------------------------------- |
|       | [Wildcard Characters/Like Characters?](#ques-wildcard-characterslike-characters) |

<div style="page-break-before: always;"></div>


### Demo data for execute the query
```sql
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    job_name VARCHAR(50),
    manager_id INT,
    hire_date DATE,
    salary DECIMAL(10, 2),
    commission DECIMAL(10, 2),
    dep_id INT
);

INSERT INTO employee (emp_id, emp_name, job_name, manager_id, hire_date, salary, commission, dep_id)
VALUES
    (68319, 'KAYLING', 'PRESIDENT', NULL, '1991-11-18', 6000.00, NULL, 1001),
    (66928, 'BLAZE', 'MANAGER', 68319, '1991-05-01', 2750.00, NULL, 3001),
    (67832, 'CLARE', 'MANAGER', 68319, '1991-06-09', 2550.00, NULL, 1001),
    (65646, 'JONAS', 'MANAGER', 68319, '1991-04-02', 2957.00, NULL, 2001),
    (67858, 'SCARLET', 'ANALYST', 65646, '1997-04-19', 3100.00, NULL, 2001),
    (69062, 'FRANK', 'ANALYST', 65646, '1991-12-03', 3100.00, NULL, 2001),
    (63679, 'SANDRINE', 'CLERK', 69062, '1990-12-18', 900.00, NULL, 2001),
    (64989, 'ADELYN', 'SALESMAN', 66928, '1991-02-20', 1700.00, 400.00, 3001),
    (65271, 'WADE', 'SALESMAN', 66928, '1991-02-22', 1350.00, 600.00, 3001),
    (66564, 'MADDEN', 'SALESMAN', 66928, '1991-09-28', 1350.00, 1500.00, 3001),
    (68454, 'TUCKER', 'SALESMAN', 66928, '1991-09-08', 1600.00, 0.00, 3001),
    (68736, 'ADNRES', 'CLERK', 67858, '1997-05-23', 1200.00, NULL, 2001),
    (69000, 'JULIUS', 'CLERK', 66928, '1991-12-03', 1050.00, NULL, 3001),
    (69324, 'MARKER', 'CLERK', 67832, '1992-01-23', 1400.00, NULL, 1001);


+--------+----------+-----------+------------+------------+---------+------------+--------+
| emp_id | emp_name | job_name  | manager_id | hire_date  | salary  | commission | dep_id |
+--------+----------+-----------+------------+------------+---------+------------+--------+
|  63679 | SANDRINE | CLERK     |      69062 | 1990-12-18 |  900.00 |       NULL |   2001 |
|  64989 | ADELYN   | SALESMAN  |      66928 | 1991-02-20 | 1700.00 |     400.00 |   3001 |
|  65271 | WADE     | SALESMAN  |      66928 | 1991-02-22 | 1350.00 |     600.00 |   3001 |
|  65646 | JONAS    | MANAGER   |      68319 | 1991-04-02 | 2957.00 |       NULL |   2001 |
|  66564 | MADDEN   | SALESMAN  |      66928 | 1991-09-28 | 1350.00 |    1500.00 |   3001 |
|  66928 | BLAZE    | MANAGER   |      68319 | 1991-05-01 | 2750.00 |       NULL |   3001 |
|  67832 | CLARE    | MANAGER   |      68319 | 1991-06-09 | 2550.00 |       NULL |   1001 |
|  67858 | SCARLET  | ANALYST   |      65646 | 1997-04-19 | 3100.00 |       NULL |   2001 |
|  68319 | KAYLING  | PRESIDENT |       NULL | 1991-11-18 | 6000.00 |       NULL |   1001 |
|  68454 | TUCKER   | SALESMAN  |      66928 | 1991-09-08 | 1600.00 |       0.00 |   3001 |
|  68736 | ADNRES   | CLERK     |      67858 | 1997-05-23 | 1200.00 |       NULL |   2001 |
|  69000 | JULIUS   | CLERK     |      66928 | 1991-12-03 | 1050.00 |       NULL |   3001 |
|  69062 | FRANK    | ANALYST   |      65646 | 1991-12-03 | 3100.00 |       NULL |   2001 |
|  69324 | MARKER   | CLERK     |      67832 | 1992-01-23 | 1400.00 |       NULL |   1001 |
+--------+----------+-----------+------------+------------+---------+------------+--------+
```

## Create Query

### Create table
```sql
CREATE TABLE table_name ( 
  id int(11) NOT NULL,

  column_name data_type(2),
  .......
);
```

### Create a table which is already exists?
```sql
CREATE TABLE IF NOT EXISTS table_name ( 
  column_name data_type(2),
  column_name data_type(2),
  .......
);
```

### Creaet a table through another table/Duplicate table through another table.
```sql
CREATE TABLE IF NOT EXISTS new_table_name LIKE exsting_table_name;
```

### Creaet a table through another table/Duplicate table through another table, with structure and data?
```sql
CREATE TABLE IF NOT EXISTS new_table_name AS SELECT * FROM exsting_table_name;
```

### Create a table and check max_salary is not exceed the upper limit of 25000
```sql
CREATE TABLE IF NOT EXISTS jobs(
    JOB_ID varchar(10) NOT NULL,
    JOB_TITLE varchar(35) NOT NULL,
    MIN_SALARY decimal(6,0),
    MAX_SALARY decimal(6,0),
    CHECK(MAX_SALARY<=25000)
);
```
<div style="page-break-before: always;"></div>




### UPDATE
* UPDATE statements allow you to edit rows in a table.
```sql
UPDATE table_name SET some_column = some_value
WHERE some_column = some_value;

Update customer set name="mohit" where id =1;
```


### DELETE TABLE?
* The DELETE statement is used to delete rows from a table. If you want to remove a **specific row** from a table you should use WHERE condition.
```sql
DELETE FROM table_name [WHERE condition];  
```
* But if you do not specify the WHERE condition it will remove **all the rows** from the table.
```sql
DELETE FROM table_name;
```

### Delete Duplicate Records?
```sql
CREATE TABLE employee (
    id INT,
    customer_name VARCHAR(255),
    email VARCHAR(255)
);
INSERT INTO employee (id, customer_name, email)
VALUES
    (1, 'John Doe', 'john.doe@example.com'),
    (2, 'Jane Doe', 'jane.doe@example.com'),
    (3, 'Muzamil Amin', 'Muzamilaminitoo@gmail.com'),
    (1, 'John Doe', 'john.doe@example.com'), 
    (4, 'Alice Johnson', 'alice.johnson@example.com'),
    (2, 'Jane Doe', 'jane.doe@example.com');

mysql> DELETE FROM employee WHERE id IN ( SELECT id FROM employee GROUP BY id HAVING COUNT(*) > 1 )
```


### Highest Salary Department wise
```sql
Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');
insert into Employee (id, name, salary, departmentId) values ('8', 'Mohit', '90000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');
```
```sql
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
| 8  | Mohit | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
```


* List of duplicate data
```sql
SELECT a.id, a.name, a.email
FROM sample_table a
INNER JOIN sample_table b ON a.name = b.name AND a.email = b.email
WHERE a.id != b.id;
```

```sql
select emp_name, salary from employee where salary = (select max(salary) from employee);
+----------+---------+
| emp_name | salary  |
+----------+---------+
| Mohit    | 6000.00 |
| KAYLING  | 6000.00 |
+----------+---------+
```

## How many employees under the manager
```sql
 emp_id | emp_name | job_name  | manager_id | hire_date  | salary  | commission | dep_id
--------+----------+-----------+------------+------------+---------+------------+--------
  68319 | KAYLING  | PRESIDENT |            | 1991-11-18 | 6000.00 |            |   1001
  66928 | BLAZE    | MANAGER   |      68319 | 1991-05-01 | 2750.00 |            |   3001
  67832 | CLARE    | MANAGER   |      68319 | 1991-06-09 | 2550.00 |            |   1001
  65646 | JONAS    | MANAGER   |      68319 | 1991-04-02 | 2957.00 |            |   2001
  67858 | SCARLET  | ANALYST   |      65646 | 1997-04-19 | 3100.00 |            |   2001
  69062 | FRANK    | ANALYST   |      65646 | 1991-12-03 | 3100.00 |            |   2001
  63679 | SANDRINE | CLERK     |      69062 | 1990-12-18 |  900.00 |            |   2001
  64989 | ADELYN   | SALESMAN  |      66928 | 1991-02-20 | 1700.00 |     400.00 |   3001
  65271 | WADE     | SALESMAN  |      66928 | 1991-02-22 | 1350.00 |     600.00 |   3001
  66564 | MADDEN   | SALESMAN  |      66928 | 1991-09-28 | 1350.00 |    1500.00 |   3001
  68454 | TUCKER   | SALESMAN  |      66928 | 1991-09-08 | 1600.00 |       0.00 |   3001
  68736 | ADNRES   | CLERK     |      67858 | 1997-05-23 | 1200.00 |            |   2001
  69000 | JULIUS   | CLERK     |      66928 | 1991-12-03 | 1050.00 |            |   3001
  69324 | MARKER   | CLERK     |      67832 | 1992-01-23 | 1400.00 |            |   1001
```

### How many employee under the manager
```sql
SELECT w.manager_id,
       count(*)
FROM employees w,
     employees m
WHERE w.manager_id = m.emp_id
GROUP BY w.manager_id
ORDER BY w.manager_id ASC;

Output:-
  manager_id | count
------------+-------
      65646 |     2
      66928 |     5
      67832 |     1
      67858 |     1
      68319 |     3
      69062 |     1

```

### and count higest emp under the manager.
```sql
SELECT m.emp_name,
       count(*)
FROM employees w,
     employees m
WHERE w.manager_id = m.emp_id
GROUP BY m.emp_name
HAVING count(*) =
  (SELECT MAX (mycount)
   FROM
     (SELECT COUNT(*) mycount
      FROM employees
      GROUP BY manager_id) a);

Output:-
 emp_name | count
----------+-------
 BLAZE    |     5
```
