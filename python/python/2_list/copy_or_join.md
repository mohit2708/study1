### **Ques. Copy Lists?**
* You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
* So Two method of the copy below.
* **copy() method**
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

Output:- ['apple', 'banana', 'cherry']
```

* **list() method**
```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

Output:- ['apple', 'banana', 'cherry']
```
<div style="page-break-before: always;"></div>

### **Ques. Join Lists?**
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