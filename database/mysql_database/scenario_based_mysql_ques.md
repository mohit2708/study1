### **scenarioYou are faced with a slow query that uses a JOIN operation on a large table. How would you optimize it?**
* First, I use EXPLAIN to identify bottlenecks. Then I ensure proper indexes exist on JOIN and WHERE columns, avoid SELECT *, filter data as early as possible, and use composite indexes where appropriate. For very large datasets, I may consider partitioning, query rewriting, or summary tables.
```sql
1. Check Execution Plan

Use EXPLAIN to see how MySQL executes the query.

EXPLAIN
SELECT *
FROM orders o
JOIN customers c
ON o.customer_id = c.id;

Look for:

Full Table Scan (type = ALL)
Missing indexes
High row counts
2. Create Proper Indexes

Columns used in JOIN conditions should be indexed.

CREATE INDEX idx_customer_id
ON orders(customer_id);

Example:

SELECT *
FROM employees e
JOIN departments d
ON e.department_id = d.id;

Indexes:

CREATE INDEX idx_department_id
ON employees(department_id);

CREATE INDEX idx_id
ON departments(id);
3. Select Only Required Columns

Avoid:

SELECT *
FROM orders o
JOIN customers c
ON o.customer_id = c.id;

Better:

SELECT o.order_id,
       c.customer_name
FROM orders o
JOIN customers c
ON o.customer_id = c.id;

Less data = Faster query.

4. Filter Early

Apply WHERE conditions before joining large datasets.

SELECT o.order_id,
       c.customer_name
FROM orders o
JOIN customers c
ON o.customer_id = c.id
WHERE o.order_date >= '2026-01-01';
5. Avoid Functions on Indexed Columns

Bad:

SELECT *
FROM orders
WHERE YEAR(order_date) = 2026;

Index cannot be used efficiently.

Better:

SELECT *
FROM orders
WHERE order_date >= '2026-01-01'
  AND order_date < '2027-01-01';
6. Use Appropriate JOIN Type

If only matching records are needed:

INNER JOIN

instead of:

LEFT JOIN

when unnecessary.

7. Consider Composite Indexes

If query filters on multiple columns:

SELECT *
FROM orders
WHERE customer_id = 101
AND status = 'PAID';

Create:

CREATE INDEX idx_customer_status
ON orders(customer_id, status);
8. Partition Very Large Tables

For tables with millions of rows:

PARTITION BY RANGE(YEAR(order_date))

This reduces data scanning.

9. Check Join Order

Sometimes joining smaller filtered datasets first improves performance.

SELECT *
FROM (
    SELECT *
    FROM orders
    WHERE status = 'PAID'
) o
JOIN customers c
ON o.customer_id = c.id;
10. Consider Denormalization or Materialized Tables

For frequently executed reporting queries:

Summary tables
Aggregated tables
Materialized views (where supported)

can significantly improve performance.
```

### Given a table with 100+ million rows, how would you optimize its performance?
* For a table with 100+ million rows, I would first analyze slow queries using EXPLAIN, then create appropriate indexes on frequently searched, joined, and sorted columns. I would avoid SELECT *, use proper data types, implement partitioning and archiving for old data, optimize joins with indexed columns, use covering indexes where possible, and introduce caching or read replicas for high-traffic workloads. These techniques together significantly improve query performance and scalability.
```sql
1. Create Proper Indexes

Most important step.

CREATE INDEX idx_customer_id
ON orders(customer_id);

For queries using multiple columns:

CREATE INDEX idx_customer_status
ON orders(customer_id, status);

Benefits:

Faster search
Faster JOINs
Faster filtering
2. Analyze Queries Using EXPLAIN
EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 101;

Check for:

Full Table Scan (type=ALL)
Missing indexes
High rows scanned
3. Avoid SELECT *

Bad:

SELECT *
FROM orders;

Good:

SELECT order_id,
       amount
FROM orders;

Less data transferred = better performance.

4. Partition Large Tables

Example: Order table by year.

PARTITION BY RANGE (YEAR(order_date))

Benefits:

Reads only relevant partition
Faster scans

Example:

orders_2024
orders_2025
orders_2026

instead of scanning 100M rows.

5. Archive Old Data

Keep active data in main table.

Example:

orders_active
orders_archive

Move old records periodically.

6. Use Appropriate Data Types

Bad:

amount VARCHAR(100)

Good:

amount DECIMAL(10,2)

Bad:

id BIGINT

when values never exceed INT range.

Smaller data types = smaller indexes = faster queries.

7. Optimize JOINs

Ensure indexes on join columns.

SELECT *
FROM orders o
JOIN customers c
ON o.customer_id = c.id;

Indexes:

orders(customer_id)
customers(id)
8. Use Pagination

Bad:

SELECT *
FROM orders;

Good:

SELECT *
FROM orders
LIMIT 100;

For large offsets, keyset pagination is better:

SELECT *
FROM orders
WHERE id > 100000
LIMIT 100;
9. Use Covering Indexes

Instead of reading table + index.

Query:

SELECT customer_id, status
FROM orders
WHERE customer_id = 101;

Index:

CREATE INDEX idx_cover
ON orders(customer_id, status);

MySQL can satisfy the query directly from the index.

10. Table Maintenance

Regularly run:

ANALYZE TABLE orders;

and when needed:

OPTIMIZE TABLE orders;
11. Caching

Frequently accessed data can be cached using:

Redis
Memcached
Application cache

Reduces database load significantly.

12. Read Replicas

For heavy read traffic:

Primary DB
     |
     ├── Replica 1
     ├── Replica 2
     └── Replica 3
Writes → Primary
Reads → Replicas
```

### How would you structure a database to handle millions of daily transactions efficiently?
* For millions of daily transactions, I would design the database with normalized tables and proper primary/foreign keys, create indexes based on actual query patterns, and partition very large transaction tables by date or another suitable key. I would use short ACID transactions for critical operations, batch processing for bulk operations, caching for frequently accessed data, and read replicas to scale read traffic. I would also archive old data and continuously monitor slow queries, locks, deadlocks, and replication lag.

```sql
Interview Answer

I would design the database with proper normalization, indexing, partitioning, transactions, and scalability mechanisms.

1. Proper Database Design

Frequently accessed entities ko separate tables mein maintain karunga.

Example:

customers
---------
id (PK)
name
email

orders
------
id (PK)
customer_id (FK)
order_date
status
total_amount

order_items
-----------
id (PK)
order_id (FK)
product_id
quantity
price

Isse duplicate data kam hota hai aur data consistency maintain hoti hai.

2. Proper Indexing

Frequently searched aur JOIN columns par indexes:

CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_orders_date
ON orders(order_date);

CREATE INDEX idx_orders_status_date
ON orders(status, order_date);

Lekin har column par index nahi banaunga, kyunki excessive indexes writes ko slow kar sakte hain.

3. Partitioning

Agar transactions bahut large ho jayein, transaction table ko date ke basis par partition kar sakte hain.

transactions
    |
    ├── 2026_01
    ├── 2026_02
    ├── 2026_03
    └── ...

For example, monthly transaction queries mein database ko unnecessary historical data scan nahi karna padega.

4. Read/Write Separation

Heavy traffic mein:

                 Application
                     |
             ┌───────┴───────┐
             ↓               ↓
         Primary          Read Replicas
         (Writes)          (Reads)
Primary DB → INSERT/UPDATE/DELETE
Read replicas → SELECT

Isse read traffic distribute ho jata hai.

5. Caching

Frequently requested data ke liye Redis jaise cache ka use kar sakte hain.

Application
    |
    ↓
  Redis
    |
    ↓
 Database

Har request ko database tak jaane ki zarurat nahi padegi.

6. Use Transactions Carefully

Financial/order transactions mein ACID properties important hain.

START TRANSACTION;

UPDATE accounts
SET balance = balance - 1000
WHERE id = 1;

UPDATE accounts
SET balance = balance + 1000
WHERE id = 2;

COMMIT;

Failure hone par:

ROLLBACK;
7. Avoid Long-Running Transactions

Millions of transactions mein long-running transactions locks ko hold kar sakti hain.

Isliye transactions ko:

Short
Focused
Quickly committed

rakhunga.

8. Batch Processing

Agar millions of records insert/update karne hain, ek-ek record ke bajay batch operations use karunga.

INSERT INTO transactions
    (customer_id, amount, transaction_date)
VALUES
    (101, 500, NOW()),
    (102, 700, NOW()),
    (103, 900, NOW());
9. Archiving

Old transactions ko archive storage/table mein move kar sakte hain.

transactions_current
        |
        | older data
        ↓
transactions_archive

Isse operational database manageable rahega.

10. Monitoring

Production mein continuously monitor karunga:

Slow queries
CPU / RAM
Disk I/O
Connection count
Lock waits
Deadlocks
Replication lag
Index usage

MySQL mein slow queries identify karne ke liye:

EXPLAIN
SELECT ...
Simple Architecture
                  Application
                       |
                Load Balancer
                       |
              ┌────────┴────────┐
              ↓                 ↓
          App Server         App Server
              |
       ┌──────┴──────┐
       ↓             ↓
     Redis       Database Layer
                     |
             ┌───────┴────────┐
             ↓                ↓
          Primary         Read Replica
          (Write)            (Read)
             |
       Partitioned Tables
             |
          Archive
```