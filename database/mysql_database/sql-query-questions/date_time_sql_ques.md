### **Current date?**
```sql
select GETDATE();
```

### **Find records created in the last 30 days?**
* Aaj se pichhle 30 din ke andar jo records create hue hain, unko find karo.
```sql
SELECT * FROM employees
WHERE created_at >= NOW() - INTERVAL 30 DAY;

-- OR
SELECT * FROM employees
WHERE created_at >= CURDATE() - INTERVAL 30 DAY;
```

### **Find records between two dates?**
```sql
SELECT * FROM employees
WHERE created_at BETWEEN '2026-09-01' AND '2026-09-15';

-- OR
SELECT * FROM employees
WHERE created_at >= '2026-09-01'
  AND created_at < '2026-09-16';
```