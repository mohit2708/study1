### What are constraints in MySQL?
- Constraints in MySQL are rules applied to table columns to enforce data integrity and accuracy. They control what kind of data can be stored in a table.
- Constraints are like rules on a form
  - “This field is required” → NOT NULL
  - “Must be unique” → UNIQUE
  - “Must be at least 18 years old” → CHECK


### The following constraints are commonly used in SQL:
- **NOT NULL** - Ensures that a column cannot have a NULL value
- **UNIQUE** - Ensures that all values in a column are different
- **PRIMARY KEY** - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
- **FOREIGN KEY** - Prevents actions that would destroy links between tables
- **CHECK** - Ensures that the values in a column satisfies a specific condition
- **DEFAULT** - Sets a default value for a column if no value is specified
- **CREATE INDEX** - Used to create and retrieve data from the database very quickly
