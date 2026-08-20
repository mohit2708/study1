|  No.  | [Keys](#keys)                                                                                      |
| :---: | -------------------------------------------------------------------------------------------------- |
|       | [Primary Key?](#primary-key)                                                                       |
|       | [Add primary Key?](#add-primary-key)                                                               |
|       | [Delete primary Key?](#delete-primary-key)                                                         |
|       | [Unique Key?](#ques-what-is-unique-key)                                                            |
|       | [ALTER unique key?](#alter-unique-key)                                                             |
|       | [Drop unique key?](#drop-unique-key)                                                               |
|       | [Foreign Key?](#ques-what-is-foreign-key)                                                          |
|       | [Foreign Key Add/ALTER?](#adding-foreign-key-to-existing-table)                                    |
|       | [DROP Foreign Key?](#drop-a-foreign-key-from-the-table)                                            |
|       | [Composite Key?](#ques-what-is-composite-key)                                                      |
|       | [Difference between Primary Key & Unique Key?](#ques-difference-between-primary-key--unique-key)   |
|       | [Difference between Primary Key & Foreign Key?](#ques-difference-between-primary-key--foreign-key) |

<div style="page-break-before: always;"></div>

### Primary Key?
* A PRIMARY KEY is a column or combination of columns that **uniquely identifies each record** in a database table.
* A Primary Key column **cannot have Null values**.
* A table can have only **one primary key** per table.
* When **multiple fields** are used as a primary key, they are called a **composite key**.

```sql
-- Create Primary Key
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);
-- (OR)
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100),
    PRIMARY KEY (student_id) 
);

-- Create Primary Key with multiple column
CREATE TABLE Order_Items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)  -- Multiple columns as primary key
);
```

#### Add primary Key
```sql
-- if primary key doesn’t exists in the created table 
ALTER TABLE table_name ADD PRIMARY KEY (Id)

-- For multiple column 
ALTER table Employee ADD constraints PK_Employee PRIMARY KEY (column_name1, column_name2);
-- (OR)
ALTER TABLE table_name ADD PRIMARY KEY (column1, column2);

-- Adding Primary Key with Auto-Increment
ALTER TABLE table_name MODIFY column_name INT AUTO_INCREMENT PRIMARY KEY;
```

#### Delete primary Key
```sql
ALTER TABLE table_name DROP PRIMARY KEY;

-- For multiple column 
ALTER TABLE Employee DROP CONSTRAINT PK_Employee;
-- (OR)
ALTER TABLE table_name DROP PRIMARY KEY;
```
<div style="page-break-before: always;"></div>



#### Ques. What Is Unique Key?
* A Unique Key is a constraint that ensures all values in a column or a combination of columns are unique across all records in a table.
* The Unique and Primary Key constraints both provide a guarantee for a column or set of columns.
* A Primary Key consist automatically has a unique constraint define on it.
  * Defining unique key
```sql
-- Single Column Unique Key
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);

-- Multiple Column Unique Key
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    UNIQUE (first_name, last_name)
);
```

#### ALTER unique key
```sql
-- Single Column
ALTER table Employee ADD UNIQUE(column name);
-- (OR)
ALTER TABLE table_name ADD CONSTRAINT constraint_name UNIQUE (column_name);

-- Multiple Columns
ALTER TABLE table_name ADD CONSTRAINT constraint_name UNIQUE (column1, column2);
``` 

#### Drop unique key
```sql
ALTER TABLE Employee DROP CONSTRAINT Employee_ID;
-- (OR)
ALTER TABLE table_name DROP INDEX constraint_name;
```
<div style="page-break-before: always;"></div>


### **Ques. What Is Foreign Key?**
* A foreign key is a key used to link two tables together. This is something called a reference key.
* A column or set of columns in a table that references the PRIMARY KEY of another table.
* Foreign key is a column or a combination of columns whose values match a primary key in a different table.
* The relationship between two tables matches the primary key in one of the tables with a foreign key in the second table.

```sql
-- create Customers table
CREATE TABLE Customers (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100),
  age INTEGER
);

-- create Products table
CREATE TABLE Products (
    customer_id INTEGER ,
    name VARCHAR(100),
    FOREIGN KEY (customer_id)
    REFERENCES Customers(id)
);

-- Here, the customer_id column in the Products table references the id column in the Customers table.
```
```sql
-- One-to-One:- Each record in one table connects to single record in another
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    passport_number INT,
    FOREIGN KEY (passport_number) 
    REFERENCES Passport(passport_number)
);

-- One-to-Many:- One record in parent table can relate to multiple records in child table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) 
    REFERENCES Customers(customer_id)
);

-- Many-to-Many:- Multiple records in both tables can relate to each other
CREATE TABLE StudentCourses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```

#### Adding Foreign Key to Existing Table?
```sql
-- if primary key doesn’t exists in the created table
ALTER TABLE Employee ADD FOREIGN KEY (department_id) REFERENCES Department(department_id);
(OR)
ALTER TABLE `bookings` ADD CONSTRAINT `advance_bookings_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE

-- For multiple column
ALTER TABLE Employee ADD CONSTRAINT FK_dept_id FOREIGN KEY (department_id) REFERENCES Department(department_id);
```

#### DROP a Foreign Key from the table
```sql
-- For single column/multiple column
ALTER TABLE Employee DROP FOREIGN KEY FK_dept_id;
```
<div style="page-break-before: always;"></div>



#### Ques. What is Composite Key?
* Composite key is combination of two or more columns that can uniquely identify each row in the table.
* composite key is also a primary key, but the difference is that it is made by the combination of more than one column to identify the particular row in the table.
* A composite key cannot be null.
```sql
CREATE TABLE student
(rollNumber INT, 
name VARCHAR(30), 
class VARCHAR(30), 
section VARCHAR(1), 
mobile VARCHAR(10),
PRIMARY KEY (rollNumber, mobile));
```

#### Types of Composite Keys
1. Composite Primary Key
```sql
CREATE TABLE StudentCourses (
    student_id INT,
    course_id INT,
    semester VARCHAR(10),
    PRIMARY KEY (student_id, course_id, semester)
);
```
2. Composite Unique Key
```sql
CREATE TABLE Employees (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    UNIQUE (first_name, last_name, department)
);
```

#### Can any one field in a composite key be NULL?
* **Composite Primary Key:** No, because all columns that are part of a primary key are automatically NOT NULL.
* **Composite Unique Key:** Yes, in MySQL NULL values can be allowed depending on the constraint and database behaviour.



<div style="page-break-before: always;"></div>


#### Ques. Difference between Primary Key & Unique Key?
| Primary Key                                            | Unique Key                                                           |
| :----------------------------------------------------- | :------------------------------------------------------------------- |
| A table can have only one primary key                  | A table can have more than one unique key                            |
| It does not allow null values                          | Allows null values                                                   |
| Primary key Can be made foreign key into another table | In SQL server, unique key Can be made foreign key into another table |
| By default it adds a clustered index                   | By default it adds a unique non-clustered index                      |
| Primary key support auto increment value.              | Unique constraint does not support auto increment value.             |




#### Ques. Difference between Primary Key & Foreign Key?
| Primary Key                                            | Foreign Key                                                              |
| :----------------------------------------------------- | :----------------------------------------------------------------------- |
| A table can have only one primary key                  | A table can have more than one foreign key                               |
| Primary key uniquely identified  a record in the table | Foreign key is a field in the table that is primary key in another table |
| It does not allow null values                          | Allows null values                                                       |
| Duplicate not allowed                                  | Duplicate allowed                                                        |
| Primary key support auto increment value               | Foreign key do not automatically create an index.                        |