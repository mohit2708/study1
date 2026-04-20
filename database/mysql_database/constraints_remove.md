### how to remove unique from email in mysql
```sql
-- First, see the indexes on your table:
SHOW INDEX FROM users;

ALTER TABLE table_name DROP INDEX index_name;
```