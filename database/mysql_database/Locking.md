### **What is Locking?**
* Locking is a technique used by the database to prevent multiple transactions from modifying the same data simultaneously, ensuring data integrity and consistency.

#### Why is Locking Needed?
* Suppose Employee A and Employee B both try to update the salary of the same employee at the same time.
* Without locking:
  * A reads salary = 50,000
  * B reads salary = 50,000
  * A updates to 55,000
  * B updates to 60,000
* A's update is lost (Lost Update Problem).
* Locking prevents this issue.

### Types of Locks
#### 1. Shared Lock (Read Lock)
* Multiple transactions can read the same data.
* No transaction can modify the data while a shared lock exists.
```sql
SELECT * FROM employees;
```
* Many users can read simultaneously.

#### 2. Exclusive Lock (Write Lock)
* Used when data is being modified.
* No other transaction can read or write the locked data (depending on DBMS/isolation level).
```sql
UPDATE employees
SET salary = 60000
WHERE id = 1;
```
* The row gets an exclusive lock.

### Difference between Shared Lock and Exclusive Lock?
| Shared Lock             | Exclusive Lock                      |
| ----------------------- | ----------------------------------- |
| Read operation          | Write operation                     |
| Multiple users allowed  | Only one transaction allowed        |
| No modification allowed | Blocks other reads/writes as needed |


### Row-Level vs Table-Level Locking
| Lock Type  | Description              |
| ---------- | ------------------------ |
| Row Lock   | Locks only specific rows |
| Table Lock | Locks the entire table   |
* **Row locking** provides better concurrency and is commonly used in MySQL InnoDB.

### Example of Locking
```sql
-- Transaction 1:
START TRANSACTION;

UPDATE employees
SET salary = 70000
WHERE id = 1;

-- Transaction 2:
UPDATE employees
SET salary = 80000
WHERE id = 1;

Transaction 2 must wait until Transaction 1 performs:

COMMIT;
```

### what is dead lock?
* A deadlock is a situation where two or more transactions are permanently blocked because each transaction is waiting for a resource locked by another transaction.

#### Example
```sql
-- Transaction 1
START TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;  -- Locks row 1

-- Transaction 2
START TRANSACTION;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;  -- Locks row 2
```

* Now
```sql
-- Transaction 1 tries:
UPDATE accounts
SET balance = balance + 100
WHERE id = 2;  -- Waiting for Transaction 2

-- Transaction 2 tries:
UPDATE accounts
SET balance = balance - 100
WHERE id = 1;  -- Waiting for Transaction 1
```

* Result
```sql
Transaction 1 → Waiting for Transaction 2
Transaction 2 → Waiting for Transaction 1
```

### How Does DBMS Handle Deadlocks?
* Most databases (MySQL, SQL Server, PostgreSQL, Oracle) **automatically detect deadlocks**.
* When detected:
  * One transaction is chosen as the victim
  * That transaction is **rolled back**
  * The other transaction continues

### **How to Prevent/Resolve Deadlocks?**
1. Access tables/rows in the same order.
2. Keep transactions short.
3. Commit/Rollback quickly.
4. Avoid unnecessary locks.
5. Use proper indexes to reduce lock duration.

* MySQL Deadlock detect करेगा और किसी एक Transaction को rollback कर देगा।
* Same Order में Rows Access करो
```sql
❌ Wrong:
-- Transaction 1
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Transaction 2
UPDATE accounts SET balance = balance - 100 WHERE id = 2;
UPDATE accounts SET balance = balance + 100 WHERE id = 1;

-- यह Deadlock पैदा कर सकता है।


✅ Correct:
-- Transaction 1
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Transaction 2
UPDATE accounts SET balance = balance - 200 WHERE id = 1;
UPDATE accounts SET balance = balance + 200 WHERE id = 2;

-- दोनों Transactions पहले id=1 और फिर id=2 को access कर रहे हैं।
-- इसलिए Deadlock नहीं होगा, T2 बस T1 के lock release होने का wait करेगा।
```

### Lock vs Deadlock
| Lock                     | Deadlock                                  |
| ------------------------ | ----------------------------------------- |
| One transaction waits    | Multiple transactions wait for each other |
| Temporary                | Can continue forever unless resolved      |
| Normal behavior          | Problematic situation                     |
| Example: T2 waits for T1 | T1 waits for T2 and T2 waits for T1       |


### What is Optimistic Locking?
* Optimistic Locking is a **concurrency control technique** where the database does not lock the data while it is being read. Before updating the data, it checks whether another transaction has modified it.
* Optimistic Locking assumes that conflicts are rare. It allows multiple users to read and modify data simultaneously and checks for conflicts only when updating the data.
* Optimistic Locking एक **concurrency control technique है **जिसमें data को read करते समय lock नहीं लगाया जाता। Update के समय version number या timestamp check करके conflict detect किया जाता है।
* Optimistic Locking में database यह मानकर चलता है कि conflicts बहुत कम होंगे। इसलिए data को पढ़ते समय (READ) कोई lock नहीं लगाया जाता।
* जब data update किया जाता है, तब check किया जाता है कि किसी और user/transaction ने उस data को बीच में modify तो नहीं कर दिया।

#### Why Use Optimistic Locking?
* Better performance
* No long-running locks
* Suitable when conflicts are rare
* Common in web applications

#### How It Works?
* Usually a **version number** or **timestamp column** is maintained.
* Example
```sql
+----+--------+--------+
| id | name   | version|
+----+--------+--------+
| 1  | Mohit  | 1      |
+----+--------+--------+

-- User A Reads Record
SELECT id, name, version FROM employees WHERE id = 1;

-- Result:
id = 1
name = Mohit
version = 1

-- B User
-- User B Also Reads Same Record
version = 1


-- User A Updates First
UPDATE employees
SET name = 'Mohit Kumar',
    version = version + 1
WHERE id = 1
  AND version = 1;

-- Now
version = 2

-- User B Tries to Update
UPDATE employees
SET name = 'Mohit Saxena',
    version = version + 1
WHERE id = 1
  AND version = 1;

-- No row gets updated because version is now 2, not 1.
-- DB/Application knows that another user has already modified the record.
```

#### Real-Life Example of Optimistic Locking
* Google Docs जैसा सोचो:
  * 2 लोग document खोलते हैं।
  * दोनों edit करते हैं।
  * Save करते समय system check करता है कि document बीच में किसी और ने change तो नहीं किया।
* यह Optimistic Locking का concept है।

### My Question
* **Ques:-** jab user b update karega to 2 ka 3 ho jana chaiye usne kis base par check kiya ki upde ha ya nahi
* **Ans:-** User B जब update करता है, तो वह current database version नहीं, बल्कि जो version उसने read किया था उसी version के आधार पर update करता है।
* अगर User B सीधे यह query चलाता: लेकिन फिर User A का change overwrite हो सकता है (Lost Update Problem)।

### What is Pessimistic Locking?
* Pessimistic Locking में database यह मानकर चलता है कि data पर conflict होने की संभावना है। इसलिए जब कोई transaction data को access करता है, तो वह पहले ही lock लगा देता है, ताकि दूसरा transaction उसी data को modify न कर सके।

### Optimistic vs Pessimistic?
| Optimistic Locking              | Pessimistic Locking                              |
| ------------------------------- | ------------------------------------------------ |
| पहले lock नहीं लगाता            | पहले ही lock लगाता है                            |
| Conflict होने पर detect करता है | Conflict को पहले ही prevent करता है              |
| Version/Timestamp use करता है   | Database locks use करता है                       |
| दूसरे users पढ़/काम कर सकते हैं | Locked data पर दूसरा transaction wait कर सकता है |
| Conflicts rare हों तो useful    | Conflicts frequent हों तो useful                 |

* Pessimistic Locking कहता है: "पहले lock लगाओ, बाकी wait करें।"
* Optimistic Locking कहता है: "सब काम करो, लेकिन update के समय check करो कि data बीच में बदला तो नहीं।"