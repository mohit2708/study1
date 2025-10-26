### **Ques. Wildcard Characters?**
* Wildcard characters are used with the **LIKE operator**. The LIKE operator is **used** in a **WHERE** clause to search for a specified pattern in a column.

| Symbol | Description                        |
| :----- | :--------------------------------- |
| %      | Represents zero or more characters |
| _      | Represents a single character      |

##### Some Example
| LIKE Operator                   | Description                                                                   |
| :------------------------------ | :---------------------------------------------------------------------------- |
| WHERE CustomerName LIKE 'a%'    | Finds any values that starts with "a"                                         |
| WHERE CustomerName LIKE '%a'    | Finds any values that ends with "a"                                           |
| WHERE CustomerName LIKE '%or%'  | Finds any values that have "or" in any position                               |
| WHERE CustomerName LIKE '_r%'   | Finds any values that have "r" in the second position                         |
| WHERE CustomerName LIKE 'a_%_%' | Finds any values that starts with "a" and are at least 3 characters in length |
| WHERE ContactName LIKE 'a%o'    | Finds any values that starts with "a" and ends with "o"                       |

```sql
SELECT * FROM Customers WHERE City LIKE 'ber%';
```