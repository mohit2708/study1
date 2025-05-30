## Tables

```sql
Commands
ALTER TABLE

ALTER TABLE table_name 
ADD column_name datatype;

ALTER TABLE lets you add columns to a table in a database.


CASE
SELECT column_name,
  CASE
    WHEN condition THEN 'Result_1'
    WHEN condition THEN 'Result_2'
    ELSE 'Result_3'
  END
FROM table_name;

CASE statements are used to create different outputs (usually in the SELECT statement). It is SQL’s way of handling if-then logic.


GROUP BY
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;

GROUP BY is a clause in SQL that is only used with aggregate functions. It is used in collaboration with the SELECT statement to arrange identical data into groups.

HAVING
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > value;

HAVING was added to SQL because the WHERE keyword could not be used with aggregate functions.

INNER JOIN
SELECT column_name(s)
FROM table_1
JOIN table_2
  ON table_1.column_name = table_2.column_name;

An inner join will combine rows from different tables if the join condition is true.


LIKE
SELECT column_name(s)
FROM table_name
WHERE column_name LIKE pattern;

LIKE is a special operator used with the WHERE clause to search for a specific pattern in a column.



ORDER BY
SELECT column_name
FROM table_name
ORDER BY column_name ASC | DESC;

ORDER BY is a clause that indicates you want to sort the result set by a particular column either alphabetically or numerically.

OUTER JOIN
SELECT column_name(s)
FROM table_1
LEFT JOIN table_2
  ON table_1.column_name = table_2.column_name;

An outer join will combine rows from different tables even if the join condition is not met. Every row in the left table is returned in the result set, and if the join condition is not met, then NULL values are used to fill in the columns from the right table.



SELECT DISTINCT
SELECT DISTINCT column_name
FROM table_name;

SELECT DISTINCT specifies that the statement is going to be a query that returns unique values in the specified column(s).


