### List
* List items are **ordered**, **changeable**, and **allow duplicate** values. and written with **square brackets[]** and List items can be of any data type. **Ex:-** list = ["abc", 34, True, 40, "male"]
* **length:-** using **len** function Ex:- print(len(thislist))
* **Check if Item Exists:-** using **in** Ex:- if "apple" in thislist:
#### **Add List Items:-** 
* **Append:-** End of the list **Ex:-** thislist.append("orange") 
* **Insert:-** Specified index **Ex:-** thislist.insert(1, "orange")
* **Extend** Add any iterable **Ex:-** thislist.extend(sets)
```python
thislist = ["apple", "banana", "cherry"]

# Append Method:- Add an item to the **end of the list**, use the **append()** method.
thislist.append("orange")
print(thislist) # Output:- ['apple', 'banana', 'cherry', 'orange']

# Insert method:- The **insert()** method inserts an item at the ***specified index***.
thislist.insert(1, "orange")
print(thislist) #Output:- ['apple', 'orange', 'banana', 'cherry']

# Extend method:- The **extend()** method does not have to append lists, you can **add any iterable** object (list, tuples, sets, dictionaries etc.).
sets = ("mango", "pineapple", "papaya")
thislist.extend(sets)
print(thislist) #Output:- ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```
#### **Change or Update List Items?**
- **Change Item Value:-** 
  - To change the value of a **specific item**, refer to the index number.
  - To change the value of items within a **specific range**
```python
# for specific item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)     # Output:- ['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"] # 1 se 2 wale range ke element hut jaynge
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)     # Output:- ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```

#### **Copy Lists?**
* We cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
* Using **copy() method**
* Using **list() method**
```python
thislist = ["apple", "banana", "cherry"]

# Using copy() method
mylist = thislist.copy()
print(mylist) # Output:- ['apple', 'banana', 'cherry']

# Using list() method
mylist = list(thislist)
print(mylist) # Output:- ['apple', 'banana', 'cherry']
```


#### **Join Lists?**
* using the **plas(+)** operator.
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)    # Output:- ['a', 'b', 'c', 1, 2, 3]
```
* Using **append** method all the items from list2 into list1, one by one.
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)    # Output:- ['a', 'b', 'c', 1, 2, 3]
```
* The **extend()** method adds the specified list elements (or any iterable) to the end of the current list.
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)    # Output:-['a', 'b', 'c', 1, 2, 3]
```