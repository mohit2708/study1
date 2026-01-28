### Explain the difference between WHERE and HAVING clauses.
#### WHERE Clause
- Purpose: Filters rows from the database before any grouping or aggregation is done.
- Usage: Used when you want to filter records based on individual column values.
- When to use: When you need to filter rows based on conditions on the individual fields in a table (e.g., filtering employees by age, or customers by their location).
```sql
SELECT name, age
FROM employees
WHERE age > 30;
```
- In this case, the WHERE clause filters out employees who are 30 or younger before any aggregation happens.


#### HAVING Clause
- Purpose: Filters data after the GROUP BY operation and after any aggregation functions are applied (like COUNT(), SUM(), AVG()).
- Usage: Used when you want to filter groups or aggregated data.
- When to use: When you're working with GROUP BY and need to filter based on aggregate results.
```sql
SELECT department_id, COUNT(*) AS num_employees
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```
- In this case, the query groups the employees by department_id and counts how many employees are in each department. The HAVING clause filters out departments that have 5 or fewer employees.

####
```sql
| salesperson_id | amount | region |
| -------------- | ------ | ------ |
| 1              | 1000   | North  |
| 2              | 1500   | South  |
| 3              | 800    | North  |
| 4              | 1200   | North  |
| 5              | 2500   | East   |
| 6              | 2000   | South  |

-- Using WHERE to filter rows:
SELECT salesperson_id, amount, region
FROM sales
WHERE amount > 1000;

| salesperson_id | amount | region |
| -------------- | ------ | ------ |
| 2              | 1500   | South  |
| 4              | 1200   | North  |
| 5              | 2500   | East   |
| 6              | 2000   | South  |

--Example 2: Using HAVING to filter groups:
SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(amount) > 4000;

| region | total_sales |
| ------ | ----------- |
| North  | 3000        |
| South  | 3500        |
| East   | 2500        |
```

### Combining WHERE and HAVING:
- You can use both WHERE and HAVING in the same query. The WHERE clause filters rows before aggregation, while HAVING filters after aggregation.
```sql
SELECT region, COUNT(*) AS num_sales
FROM sales
WHERE amount > 1000  -- Filters rows before GROUP BY
GROUP BY region
HAVING COUNT(*) > 1  -- Filters groups after GROUP BY
```