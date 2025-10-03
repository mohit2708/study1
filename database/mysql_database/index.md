|  No.  | [Index](#index)                                                                                                         |
| :---: | ----------------------------------------------------------------------------------------------------------------------- |
|       | [What is Index?](#what-is-index)                                                                                        |
|       | [Types of Indexes](#types-of-indexes)                                                                                   |
|       | [Unique Indexes](#unique-indexes)                                                                                       |
|       | [Show Index](#show-index)                                                                                               |
|       | [Alter/Modify an Index](#altermodify-an-index)                                                                          |
|       | [Drop Index](#drop-index)                                                                                               |
|       | [Unique Indexes](#unique-indexes)                                                                                       |
|       | [Cluster Index](#cluster-index)                                                                                         |
|       | [Non cluster index](#non-cluster-index)                                                                                 |
|       | [difference between cluster and non cluster index?](#ques-what-is-the-difference-between-cluster-and-non-cluster-index) |

#### What is Index?
* An index is used to enhance the performance of SQL Queries. It allows the database to find data quickly and efficiently by using Row ID, avoiding full table scans.
* Indexes can be created on one or more columns of a table.
* Index allows the database application to find data fast, without reading the whole table.
* An index can be created in a table to find data more quickly and efficiently.
* **How It Works:-** Behind the scenes, an index is usually implemented as a B-tree or similar structure.

#### Types of Indexes?
1. **Single-column index:-** on one column
```sql
CREATE INDEX idx_product_id ON Sales (product_id);
```
2. **Composite/Multi-column indexes:** on multiple columns
```sql
CREATE INDEX idx_dept_salary ON employees(department, salary);
```
3. Unique Index:- 
```sql
CREATE UNIQUE INDEX idx_email_unique ON employees(email);
```
4. Full-Text Index :- Designed for efficient text search in large text fields (e.g., for searching keywords in articles, product descriptions, etc.)
```sql
CREATE FULLTEXT INDEX idx_description ON products(description);
```

#### Show Index
```sql
show index from table_name
```

#### Unique Indexes
* A Unique Index is a database index that ensures the uniqueness of values in one or more columns of a database table.
* This index ensures that no two rows in the Employees table have the same employee_id(Colum_name), which maintains data integrity and prevents duplicate entries.
* The SQL Unique Index ensures that no two rows in the indexed columns of a table have the same values (no duplicate values allowed).
```sql
* Behind the scenes, when a new record is inserted, the database would:
  * Check the Index: It looks up the email in the index (which could be a B-tree or hash table) to find if that email already exists.
    * The database will search the index, and it will quickly identify whether the email you're trying to insert is already in the table.
  * Check for Duplicates:
    * For example, if we try to insert a new row:
    * INSERT INTO users (Name, Email) VALUES ('David', 'alice@example.com');
    * The database will search the unique index for the email alice@example.com. Since this email already exists in the index, the insert will fail with an error like:
    "Duplicate entry 'alice@example.com' for key 'idx_unique_email'".
```
```sql
-- Single column unique index
CREATE UNIQUE INDEX idx_email ON users(email);

-- Composite unique index
CREATE UNIQUE INDEX idx_name_age ON employees(last_name, first_name);
```

#### Alter/Modify an Index
```sql
-- Rename Index name
ALTER TABLE table_name 
RENAME INDEX old_index_name TO new_index_name;

-- Modify Index name
ALTER TABLE table_name DROP INDEX existing_index,
ADD INDEX new_index (column1, column2);

-- Rebuild Index
ALTER INDEX index_name 
ON table_name REBUILD;

-- Reorganize Index
ALTER INDEX index_name 
ON table_name REORGANIZE;

-- Disable Index
ALTER INDEX index_name 
ON table_name DISABLE;

-- Change Index Properties
ALTER INDEX index_name 
ON table_name 
SET (
    STATISTICS_NORECOMPUTE = OFF,
    ALLOW_ROW_LOCKS = ON,
    ALLOW_PAGE_LOCKS = ON
);
```

#### Drop Index 
```sql
Drop index index_name on table_name
(OR) DROP INDEX table_name.index_name;

-- DROP INDEX with IF EXISTS
DROP INDEX IF EXISTS index_name
ON table_name;


ALTER TABLE table_name DROP CONSTRAINT constraint_name;
```

#### Cluster Index
* A clustered index is an index where the data in the table is physically stored in the order of the indexed column. In other words, the rows of the table are sorted on disk based on the values in the indexed column. A table can have only one clustered index because the data can only be sorted in one way.
* **Example:** If you create a clustered index on the EmployeeID column, the table rows will be stored on disk in ascending order of EmployeeID. The clustered index itself dictates the physical arrangement of the data.
* jab kisi table par hum primary key lagate hai to wo cluster index ban jata hai.

##### Non cluster index
* A non-clustered index is an index where the data in the table is stored independently of the index. It creates a separate structure that contains the indexed column(s) and pointers to the actual rows in the table. A table can have multiple non-clustered indexes, allowing for efficient lookups on different columns without changing the physical order of the data.
* **Example:** If you create a non-clustered index on the Department column, the index will store the department values along with pointers to the corresponding rows in the table, but the table data itself remains in its original order.
* table mai jis column par select command sabse jyda chalte hai to us column par hum non cluster index bna lete hai.

#### Ques. What is the difference between cluster and non cluster index?

| Cluster index                                   | Non cluster index                                        |
| :---------------------------------------------- | :------------------------------------------------------- |
| Data rows are stored in the order of the index. | Data rows are not sorted in any particular order.        |
| Only one clustered index per table.             | Multiple non-clustered indexes can exist per table.      |
| Created by default for the primary key.         | Must be explicitly created (e.g., for specific queries). |