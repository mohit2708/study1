### Ques. What is ACID property/SQL TRANSACTIONS?
* Transactions group a set of tasks into a single execution unit. Each transaction begins with a specific job and ends when all the tasks in the group successfully completed. If any of the tasks fail, the transaction fails. Therefore, a transaction has only two results: success or failure.
* Example of a transaction to transfer $150 from account A to account B:
```php
1. read(A)
2. A:= A – 150
3. write(A)
4. read(B)
5. B:= B + 150
6. write(B)
```
* ACID property is used to ensure that the data transactions are processed reliably in a database system.
* A single logical operation of a data is called transaction.
* ACID is an acronym for Atomicity, Consistency, Isolation, and Durability. 

* **Atomicity: -** 
  * It requires that each transaction is all or nothing. It means if one part of the transaction fails, the entire transaction fails and the database state is left unchanged.
  * A transaction consists of many steps. When all the steps in a transaction get completed, it will get reflected in DB or if any step fails, all the transactions are rolled back.
__Consistency:__
* The consistency property ensures that the data must meet all validation rules. In simple words you can say that your transaction never leaves your database without completing its state.
* The database will move from one consistent state to another, if the transaction succeeds and remain in the original state, if the transaction fails.
Isolation:
 This property ensures that the concurrent property of execution should not be met. The
main goal of providing isolation is concurrency control.
 Every transaction should operate as if it is the only transaction in the system.
Durability:
 Durability simply means that once a transaction has been committed, it will remain so,
come what may even power loss, crashes or errors.
 Once a transaction has completed successfully, the updated rows/records must be
available for all other transactions on a permanent basis
