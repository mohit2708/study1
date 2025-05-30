|  No.  | [Questions]()                                                                                                         |
| :---: | --------------------------------------------------------------------------------------------------------------------- |
|       | [Check the time slot between start time and end time?](#check-the-time-slot-between-start-time-and-end-time)          |
|       | [moved to first name to last name and first name is null ?](#moved-to-first-name-to-last-name-and-first-name-is-null) |

###
```sql
SELECT job_id, equipmentTitle, entery_by_qty,
    SUM(CASE WHEN entery_by = 'delivery' OR entery_by = 'cal_delivery' THEN entery_by_qty ELSE 0 END) AS total_delivery_qty,
    SUM(CASE WHEN entery_by = 'pickup' THEN entery_by_qty ELSE 0 END) AS total_pickup_qty
FROM job_equipment
WHERE job_id = 46 AND entery_by != 'admin'
GROUP BY equipmentTitle, sub_location_id
```

### Check the time slot between start time and end time
```sql
SELECT * FROM `bookings` WHERE ((`start_time` <='17:25:00' and `end_time` >='17:25:00') or (`start_time` <='18:05:00' and `end_time` >='18:05:00')) and (created_at like '2023-09-22%' )
```

### moved to first name to last name and first name is null 
```sql
# firstly to check how to record in the database.
SELECT users.*, user_details.is_import from users JOIN user_details on users.id = user_details.user_id WHERE user_details.is_import = '1';
OR
SELECT * from users
WHERE users.id IN (
    SELECT o.user_id
    FROM user_details o
    WHERE o.is_import = '1'
);

# second excute query 
UPDATE users set last_name = first_name
WHERE users.id IN (
    SELECT o.user_id
    FROM user_details o
    WHERE o.is_import = '1'
);
# for null
UPDATE users set first_name = NULL
WHERE users.id IN (
    SELECT o.user_id
    FROM user_details o
    WHERE o.is_import = '1'
);
```