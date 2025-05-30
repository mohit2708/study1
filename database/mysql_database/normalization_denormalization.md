### **What is Normalization?**
* Normalization is the process of **organizing the data** in the database.
* The Normalization form is used to reduce redundancy from the database table, and improve data integrity.
* Normalization divides the larger table into smaller and links them using relationships using foreign keys.
* It is also used to eliminate undesirable characteristics like Insertion, Update, and Deletion Anomalies.

#### **Types of Normalization**
1. **First Normal Form (1NF)**
* Each column can have only one value, that is, there cannot be more than one value in the same cell.
* All values in a column must be of the same data type, such as all names or all numbers
* Each record (row) must be unique.
```sql
-- Unnormalized Table (UNF)
| OrderID | CustomerName | ProductName   |
| ------- | ------------ | ------------- |
| 1       | Alice        | Apple, Banana |
| 2       | Bob          | Banana        |

-- Normalized to 1NF
| OrderID | CustomerName | ProductName |
| ------- | ------------ | ----------- |
| 1       | Alice        | Apple       |
| 1       | Alice        | Banana      |
| 2       | Bob          | Banana      |
```

2. **Second Normal Form (2NF)**
* The table should already be in 1NF.
* Every non-prime attribute (which is not part of the primary key) in the table must depend on the entire primary key,
```sql
-- Unnormalized Table (UNF)
| std_id | course_id | std_name | course_name |
| ------ | --------- | -------- |-------------|
| 1      | 101       | Ram      | Math        |
| 2      | 101       | Sita     | Math        |
| 1      | 102       | Ram      | Hindi       |

-- Normalized to 2NF
| std_id | std_name |
| ------ | -------- |
| 1      | Ram      |
| 2      | Sita     |

| course_id | course_name |
| --------- |-------------|
| 101       | Math        |
| 102       | Hindi       |
```


#### Data modification anomalies can be categorized into three types:
* **Insertion Anomaly:** Insertion Anomaly refers to when one cannot insert a new tuple into a relationship due to lack of data.
* **Deletion Anomaly:** The delete anomaly refers to the situation where the deletion of data results in the unintended loss of some other important data.
* **Updatation Anomaly:** The update anomaly is when an update of a single data value requires multiple rows of data to be updated.

Notes:- Anomaly means 


### **Ques. What are types of normalization?**
1. **First Normal Form (1NF):-** A relation is said to be in ﬁrst normal form if and only if all underlying domains contain atomic values only. After 1NF, we can still have redundant data.
2. **Second Normal Form (2NF):-** A relation is said to be in 2NF if and only if it is in 1NF and every non key attribute is fully dependent on the primary key. After 2NF, we can still have redundant data.
3. **Third Normal Form (3NF):-** A relation is said to be in 3NF, if and only if it is in 2NF and every non key attribute is non-transitively dependent on the primary key.

```
**Types of normalization:**
A. First normal form (1NF): This should remove all the duplicate columns from the table.
Creation of tables for the related data and identification of unique columns.
B. Second normal form (2NF): Meeting all requirements of the first normal form. Placing the
subsets of data in separate tables and Creation of relationships between the tables using
primary keys
C. Third normal form (3NF): This should meet all requirements of 2NF. Removing the columns
0which are not dependent on primary key constraints.
D. Fourth normal form (4NF): Meeting all the requirements of third normal form and it should
not have multi- valued dependencies.
```

### **Ques. What is Denormalization?**
DeNormalization is a technique used to access the data from higher to lower normal
forms of database. It is also process of introducing redundancy into a table by
incorporating data from the related tables.
