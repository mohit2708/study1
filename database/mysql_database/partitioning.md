### What is Partitioning?
* Partitioning is a technique to split a large table into smaller logical pieces called partitions.
* User ko table ek hi dikhti hai, lekin MySQL data ko internally multiple partitions me store karta hai.
```sql
employees
│
├── Partition 1
├── Partition 2
├── Partition 3
└── Partition 4
```

#### Why Partitioning?
* Suppose a table contains: 100 Crore Records

```sql

Agar aap query chalao:

SELECT *
FROM orders
WHERE order_year = 2026;

Without partitioning:

MySQL scans entire table

With partitioning:

MySQL scans only relevant partition

Result:

Faster Query
Less I/O
Better Performance
```

### Types of Partitioning
1. RANGE Partitioning
* Data ranges ke basis par divide hota hai.

```sql
-- Example:
CREATE TABLE sales (
    id INT,
    sale_year INT,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE (sale_year) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION pmax  VALUES LESS THAN MAXVALUE
);

Data:

2023 → p2023
2024 → p2024
2025 → p2025
```

2. LIST Partitioning
```sql

Specific values ke basis par partition.

CREATE TABLE employees (
    id INT,
    dept_id INT
)
PARTITION BY LIST (dept_id) (
    PARTITION p_it VALUES IN (1,2),
    PARTITION p_hr VALUES IN (3,4),
    PARTITION p_other VALUES IN (5,6)
);
dept_id 1,2 → p_it
dept_id 3,4 → p_hr
```

3. HASH Partitioning
```sql

MySQL hash calculate karke partition choose karta hai.

CREATE TABLE users (
    id INT,
    name VARCHAR(100)
)
PARTITION BY HASH(id)
PARTITIONS 4;
id=1 → Partition 1
id=2 → Partition 2
id=3 → Partition 3
id=4 → Partition 0

Data evenly distribute hota hai.

4. KEY Partitioning

HASH jaisa hi hota hai, lekin hash function MySQL khud manage karta hai.

CREATE TABLE users (
    id INT,
    name VARCHAR(100)
)
PARTITION BY KEY(id)
PARTITIONS 4;
Partition Pruning

Ye interview ka important concept hai.

Query:

SELECT *
FROM sales
WHERE sale_year = 2025;

MySQL:

Only Partition p2025 scanned

Baaki partitions ignore.

Is process ko Partition Pruning kehte hain.

Partitioning vs Sharding
Feature	Partitioning	Sharding
Location	Same Database	Multiple Databases/Servers
Managed By	MySQL	Application/Infrastructure
Complexity	Low	High
Scale	Moderate	Very Large
Partitioning
Server 1
 ├─ Partition 1
 ├─ Partition 2
 └─ Partition 3
Sharding
Server 1 → Shard A
Server 2 → Shard B
Server 3 → Shard C
Partitioning vs Indexing

Many interviewers ask this.

Indexing	Partitioning
Speeds up record lookup	Reduces data scanned
Creates index structure	Splits table
Useful for small & large tables	Mostly very large tables
Often used together	Often used with indexes
Advantages

✅ Faster queries on huge tables

✅ Easier maintenance

✅ Faster archival of old data

✅ Better partition-wise backups

✅ Reduced I/O

Disadvantages

❌ More complex design

❌ Not useful for small tables

❌ Wrong partition key can hurt performance

❌ Some partitioning restrictions exist in MySQL

Interview Answer (Short)

Partitioning is a database optimization technique that divides a large table into smaller logical partitions while appearing as a single table to users. It improves query performance by allowing MySQL to scan only relevant partitions through partition pruning. Common types are RANGE, LIST, HASH, and KEY partitioning. Partitioning is different from sharding because all partitions remain within the same database server.
```