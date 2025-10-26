### **How to Find Duplicate values in a Table?**
```sql
select col1, Email, count(Email) as total_email from Person group by col1, Email HAVING COUNT(Email) > 1;
+---------+-------------+
| Email   | total_email |
+ ------- + ----------- +
| a@b.com | 2           |
| c@d.com | 5           |
+---
```

### **Delete Duplicate Records?**
```sql
DELETE t1
FROM my_table t1
INNER JOIN my_table t2
  ON t1.col1 = t2.col1
 AND t1.col2 = t2.col2 -- optinal this line if check multipal column
 AND t1.id > t2.id;

-- using subquery
DELETE FROM my_table
WHERE id IN (
  SELECT t1.id
  FROM my_table t1
  JOIN my_table t2
    ON t1.col1 = t2.col1
   AND t1.col2 = t2.col2
   AND t1.id > t2.id
);
```