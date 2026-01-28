### **Ques. Difference between **CHAR** and **VARCHAR** data types?**
* Both of these data types are used for characters.
* **CHAR data** type is used to store **fixed-length** character strings.
  * When **VARCHAR** data type is used to store **variable-length** character strings.
* char occupies all the space and if space is remaining, then it fill all the blank space with "space". But in case of varchar, It takes only the required length & release remaining.
```sql
Char -> 10      | R | A | M | space | space | sapce | space | space | space | space |
Varchar -> 10   | R | A | M |   |   |   |   |   |   |   |
| R | A | M |
```
* varchar is better than Char in term of space. 
* char perform is better than varchar.
* Char max 256 characters, varchar 65535 characters.