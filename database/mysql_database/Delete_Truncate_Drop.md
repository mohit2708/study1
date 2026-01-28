### **Ques. Difference between Delete, Truncate & Drop?**
| Delete                                                | Truncate                                                       | Drop                  |
| :---------------------------------------------------- | :------------------------------------------------------------- | :-------------------- |
| Delete is a DML command                               | Truncate is DDL command                                        |                       |
| We can use where clause in delete command             | We cannot use where clause with truncate                       |                       |
| Delete statement is used to delete a row from a table | Truncate statement is used to remove all the row from a table  | Remove table and data |
| You can rollback data after using delete statement    | It is not possible to rollback after using TRUNCATE statement. | Can’t rollback        |
| Delete is slower                                      | Truncate is faster                                             |                       |


### **Ques. Difference b/w DROP and TRUNCATE statements?**
* **Drop Table:-**
  * Table structure will be dropped
  * Relationship will be dropped
  * Integrity constraints will be dropped
  * Access privileges will also be dropped
* **TRUNCATE Table:-**
  * On the other hand when we TRUNCATE a table, the table structure remains the same, so you will not face any of the above problems.

