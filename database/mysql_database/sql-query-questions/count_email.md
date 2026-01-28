### **Count email number**
```sql
SELECT email, count(email) as total_email FROM `users` WHERE role_id = 4 group by email having count(email) > 1;
```

