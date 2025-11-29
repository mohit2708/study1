### **Ques. Change or Update List Items?**
- **Change Item Value:-** To change the value of a **specific item**, refer to the index number.
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)     # Output:- ['apple', 'blackcurrant', 'cherry']
```

- **Change a Range of Item Values:-** To change the value of items within a **specific range**, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
* 1 se 2 wale range ke element hut jaynge
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)     # Output:- ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```