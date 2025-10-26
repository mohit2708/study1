### **Ques. What is ACID property/SQL TRANSACTIONS?**
* A transaction in SQL is a **sequence** of one or more SQL operations that are executed as a single unit. 
* The goal of a transaction is to ensure that either all operations succeed or none of them do, maintaining the consistency of the database. Think of it like: "Do everything, or do nothing."
* (Transaction एक तरह का ब्लॉक है जिसमें कई SQL statements (जैसे INSERT, UPDATE, DELETE) एक साथ execute होते हैं। इसका मतलब है: या तो सारे काम पूरे होंगे, या कोई भी नहीं होगा।)

#### **ACID Properties**
1. **A - Atomicity:-** If all operations in a transaction succeed, the changes are saved to the database; if any operation fails, the entire transaction is rolled back.
2. **C - Consistency:-** Ensures that after a transaction, the data in the database is still correct and follows all rules.
3. **I - Isolation:-** Makes sure that when many transactions run at the same time, they don’t interfere with each other.(Ensures that concurrent transactions do not affect each other. The final result should be the same as if transactions were run sequentially.)
4. **D - Durability:-** Once a transaction is committed, it is permanently saved in the database—even in case of system failure or crashes.
```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT;

-- If any of those updates fail (e.g., account not found), you can use:
ROLLBACK;
```
<!-- https://chatgpt.com/share/68395891-c404-800b-8bd8-592e2b028b1a -->