### What is SELECT?
* SELECT is a **DQL (Data Query Language)** command used to retrieve/fetch data from a table.
* The SELECT statement is used to retrieve data from one or more tables in a database.
```sql
SELECT column_name
FROM table_name;
```

#### Fetch Specific Columns
```sql
SELECT emp_name, salary
FROM employees;
```

#### Fetch All Columns
```sql
SELECT *
FROM employees;
```

#### With Condition
```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

### Difference between SELECT * and SELECT column_name?
| SELECT *            | SELECT column_name            |
| ------------------- | ----------------------------- |
| Fetches all columns | Fetches only required columns |
| More data transfer  | Less data transfer            |
| Generally slower    | Generally faster              |
