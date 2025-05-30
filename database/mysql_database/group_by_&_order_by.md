### **Ques. Difference between Group By And Order By?**
* **Order By:-**  ORDER BY clause is used to sort the data returned by a query in ascending or descending order. I

__Group By:-__ It is used to group our result sets of tables in a database and is often used with Count, Sum, avg etc. 
```sql
Ex:- Select COUNT(state), country from emp group by country.
```
__Order By:-__ It changes only order in our result set i.e sorting
```sql
Ex:- Select COUNT(state), country from emp order by country_id..
```