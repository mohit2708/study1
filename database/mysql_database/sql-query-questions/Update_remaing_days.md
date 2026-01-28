### **Update remaing days startdate - enddate**
```sql
UPDATE advance_bookings
SET remaining_days = DATEDIFF('2025-01-31', CURDATE()), end_date = '2025-01-31'
WHERE id = 4529;

-- End date dynamic
UPDATE advance_bookings
SET remaining_days = DATEDIFF(end_date, CURDATE()), end_date = end_date
WHERE id = 4529;
```

```sql
SELECT user_id, start_date, end_date, DATEDIFF(end_date, CURDATE()) AS remaining_days from advance_bookings;
```


### Update remaining days according to end date
```sql
UPDATE advance_bookings 
SET remaining_days = IF(CURDATE() > end_date, 0, DATEDIFF(end_date, CURDATE()))
WHERE plan_name = 11;
```