### 🎯**What is ACID property/SQL TRANSACTIONS?**
* A transaction in SQL is a **sequence** of one or more SQL operations that are executed as a single unit. 
* The goal of a transaction is to ensure that either all operations succeed or none of them do, maintaining the consistency of the database. Think of it like: "Do everything, or do nothing."
* (Transaction एक तरह का ब्लॉक है जिसमें कई SQL statements (जैसे INSERT, UPDATE, DELETE) एक साथ execute होते हैं। इसका मतलब है: या तो सारे काम पूरे होंगे, या कोई भी नहीं होगा।)

#### **ACID Properties**
- The ACID properties are four key principles that ensure database transactions are processed reliably and maintain data integrity.
1. **A – Atomicity**
  - A transaction is treated as a single unit of work. 
  - Either all operations are completed, or none of them are.
  - Example: During a bank transfer, if money is deducted from one account but cannot be added to the other, the entire transaction is rolled back.
    - Ya to transaction ka sara kaam hoga, ya kuch bhi nahi hoga.
    - All Operations Success OR All Operations Fail
2. **C – Consistency**
  - A transaction brings the database from one valid state to another.
  - It ensures that all database rules, constraints, and relationships remain valid.
  - Example: An account balance should never violate defined constraints after a transaction.
    - Database transaction ke baad bhi saare rules follow hone chahiye.
    - Database invalid state me nahi jana chahiye.
3. **I – Isolation**
  - Multiple transactions can occur at the same time without interfering with each other.
  - Each transaction behaves as if it is running alone until it is completed.
  - Example: Two users updating the same record simultaneously should not see inconsistent intermediate results.
    - Ek transaction dusre transaction ke beech me interfere nahi karega.
    - Database lock aur isolation levels use karta hai taaki dono transactions safely execute hon.
4. **D – Durability**
  - Once a transaction is successfully committed, its changes are permanent.
  - The data remains saved even if there is a power failure or system crash.
  - Example: After confirming an online payment, the transaction remains recorded even if the server restarts.
    - Ek baar transaction commit ho gaya. To data permanently save ho gaya. Chahe System Crash, Server Restart, Power Failure Kuch bhi ho jaye. Data lose nahi hoga.


```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT;

-- If any of those updates fail (e.g., account not found), you can use:
ROLLBACK;
```
<!-- https://chatgpt.com/share/68395891-c404-800b-8bd8-592e2b028b1a -->