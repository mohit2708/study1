### What are the different data types in MySQL?
* MySQL data types are mainly categorized into Numeric, String, Date and Time, JSON, Spatial, and special types such as ENUM and SET. Numeric types include INT, BIGINT, DECIMAL, FLOAT, and DOUBLE; string types include CHAR, VARCHAR, TEXT, and BLOB; date/time types include DATE, TIME, DATETIME, TIMESTAMP, and YEAR.
* MySQL data types are mainly divided into these categories:

1. Numeric Data Types:- Used for numbers.
| Data Type   | Description                          | Example      |
| ----------- | ------------------------------------ | ------------ |
| `INT`       | Integer numbers                      | `100`, `-50` |
| `TINYINT`   | Very small integer                   | `1`, `0`     |
| `SMALLINT`  | Small integer                        | `10000`      |
| `MEDIUMINT` | Medium-sized integer                 | `500000`     |
| `BIGINT`    | Very large integer                   | `9999999999` |
| `DECIMAL`   | Exact decimal values                 | `9999.99`    |
| `FLOAT`     | Approximate decimal                  | `10.5`       |
| `DOUBLE`    | Higher precision approximate decimal | `10.56789`   |
| `BIT`       | Bit values                           | `b'1010'`    |


2. String / Character Data Types
* Used for text.
| Data Type    | Description                 | Example           |
| ------------ | --------------------------- | ----------------- |
| `CHAR(n)`    | Fixed-length string         | `'INDIA'`         |
| `VARCHAR(n)` | Variable-length string      | `'Mohit Saxena'`  |
| `TINYTEXT`   | Small text                  | Short description |
| `TEXT`       | Text data                   | Article/content   |
| `MEDIUMTEXT` | Medium-sized text           | Large content     |
| `LONGTEXT`   | Very large text             | Huge documents    |
| `BINARY`     | Fixed-length binary data    | Binary bytes      |
| `VARBINARY`  | Variable-length binary data | Binary bytes      |
| `BLOB`       | Binary large object         | Images/files      |
| `MEDIUMBLOB` | Medium binary data          | Large files       |
| `LONGBLOB`   | Very large binary data      | Very large files  |

3. Date and Time Data Types
* Used for dates and times.
| Data Type   | Example               |
| ----------- | --------------------- |
| `DATE`      | `2026-09-20`          |
| `TIME`      | `14:30:00`            |
| `DATETIME`  | `2026-09-20 14:30:00` |
| `TIMESTAMP` | `2026-09-20 14:30:00` |
| `YEAR`      | `2026`                |

4. JSON Data Type
* MySQL supports a native JSON data type.
* user_data JSON
```sql
{
  "name": "Mohit",
  "age": 30,
  "city": "Delhi"
}
```

5. Spatial Data Types
* Used to store geographical/spatial information.
* Examples:
  * GEOMETRY
  * POINT
  * LINESTRING
  * POLYGON
  * MULTIPOINT
  * MULTILINESTRING
  * MULTIPOLYGON
  * GEOMETRYCOLLECTION

6. Other / Special Types
* MySQL also has:
  * ENUM → one value from a predefined list
  * SET → zero or more values from a predefined list
```sql
gender ENUM('Male', 'Female', 'Other')
```

### DATETIME vs TIMESTAMP
* The main difference between DATETIME and TIMESTAMP is **timezone handling and range**. DATETIME stores the date and time value without timezone conversion and has a much larger range. TIMESTAMP represents a point in time and MySQL converts it according to the session time zone. TIMESTAMP also traditionally has a smaller range.

| Feature                       | `DATETIME`                   | `TIMESTAMP`                   |
| ----------------------------- | ---------------------------- | ----------------------------- |
| Stores                        | Date + Time                  | Date + Time                   |
| Example                       | `2026-09-20 21:30:00`        | `2026-09-20 21:30:00`         |
| Time zone conversion          | ❌ No                         | ✅ Yes                         |
| Range                         | `1000-01-01` to `9999-12-31` | `1970-01-01` to `2038-01-19`* |
| Storage                       | 8 bytes                      | 4 bytes                       |
| Time-zone sensitive           | ❌                            | ✅                             |
| Automatic `CURRENT_TIMESTAMP` | Can be used                  | Commonly used                 |
| Best for                      | Actual date/time values      | Event timestamps              |

### 🎯**Difference between CHAR vs VARCHAR**
* Both of these data types are used for characters.
* CHAR is a **fixed-length data type**, whereas VARCHAR is a **variable-length data type**. 
* CHAR is suitable for **fixed-size values**, while VARCHAR is suitable for **values whose length can vary**.
* char occupies all the space and if space is remaining, then it fill all the blank space with "space". But in case of varchar, It takes only the required length & release remaining.
```sql
Char -> 10      | R | A | M | space | space | sapce | space | space | space | space |
Varchar -> 10   | R | A | M |   |   |   |   |   |   |   |
| R | A | M |
```
* varchar is better than Char in term of space. 
* char perform is better than varchar.
* Char max 256 characters, varchar 65535 characters.

```sql
-- CHAR Example
CREATE TABLE users (
    country_code CHAR(2)
);

INSERT INTO users (country_code)
VALUES ('IN'), ('US'), ('UK');

-- Yahan CHAR(2) suitable hai kyunki har country code ki length fixed 2 characters hai.

--
-- varchar example
-- jaise name 
CREATE TABLE users (
    name VARCHAR(50)
);
```

### **Difference between CharField and TextField?**
* **CharField** is used for storing small strings and requires max_length, such as names, titles, and emails.
* **TextField** is used for storing large amounts of text like descriptions, comments, and blog content, and it does not require max_length.