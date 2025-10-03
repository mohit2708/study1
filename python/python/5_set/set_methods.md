### **Ques. Set Methods?**
| Method                        | Description                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------ |
| add()                         | Adds an element to the set                                                     |
| copy()                        | Returns a copy of the set                                                      |
| difference()                  | Returns a set containing the difference between two or more sets               |
| difference_update()           | Removes the items in this set that are also included in another, specified set |
| isdisjoint()                  | Returns whether two sets have a intersection or not                            |
| issubset()                    | Returns whether another set contains this set or not                           |
| issuperset()                  | Returns whether this set contains another set or not                           |
| remove()                      | Removes the specified element                                                  |
| discard()                     | Remove the specified item                                                      |
| pop()                         | Removes an element from the set                                                |
| clear()                       | Removes all the elements from the set                                          |
| union()                       | Return a set containing the union of sets                                      |
| update()                      | Update the set with the union of this set and others                           |
| intersection()                | Returns a set, that is the intersection of two other sets                      |
| intersection_update()         | Removes the items in this set that are not present in other, specified set(s)  |
| symmetric_difference()        | Returns a set with the symmetric differences of two sets                       |
| symmetric_difference_update() | inserts the symmetric differences from this set and another                    |
<div style="page-break-before: always;"></div>

* **add():-** Adds an element to the set.
```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # Output:- {'cherry', 'orange', 'apple', 'banana'}

# Example2:- Try to add an element that already exists:
thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)  # Output:- {'apple', 'banana', 'cherry'}
```

* **clear():-** Removes all the elements from the set.
```python
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # Output:- set()
```

* **copy():-** Returns a copy of the set.
```python
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)    # Output:- {'banana', 'apple', 'cherry'}
```

* **difference():-** Returns a set containing the difference between two or more sets.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)     

print(z)    # Output:- {'cherry', 'banana'}

# Example2:- Reverse the first example. Return a set that contains the items that only exist in set y, and not in set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x) 

print(z)    # Output:- {'microsoft', 'google'}
```
<div style="page-break-before: always;"></div>

**difference_update():-**
* Removes the items in this set that are also included in another, specified set.
* The difference_update() method removes the items that exist in both sets.
* The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
  
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)    # Output:- {'banana', 'cherry'}
```

* **discard():-**
* Remove the specified item.
* This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

```python
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)  # Output:- {'cherry', 'apple'}
```

* **intersection():-** Returns a set, that is the intersection of two other sets
```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)   # Output:- {'c'}
```
<div style="page-break-before: always;"></div>

* **intersection_update():-** Removes the items in this set that are not present in other, specified set(s).
* The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)    # Output:- {'c'}
```

* **isdisjoint():-** Returns whether two sets have a intersection or not.
* Return True if no items in set x is present in set y.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) 

print(z)    # Output:- True
```

* **issubset():-** Returns whether another set contains this set or not
* Return True if all items in set x are present in set y.
```python
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) 

print(z)    # Output:- True
```

* **issuperset():-** Returns whether this set contains another set or not
* Return True if all items set y are present in set x:
```python
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)    # Output:- True
```
<div style="page-break-before: always;"></div>

* **pop():-** The pop() method removes a random item from the set.
```python

fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)   # Output:- {'apple', 'banana'}
```

* **remove():-** The remove() method removes the specified element from the set.
* This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)   # Output:- {'cherry', 'apple'}
```

* **symmetric_difference():-** Return a set that contains all items from both sets, except items that are present in both sets.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)    # Output:- {'google', 'microsoft', 'banana', 'cherry'}
```

* **symmetric_difference_update():-** Remove the items that are present in both sets, AND insert the items that is not present in both sets.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) 

print(x)    # Output:- {'google', 'banana', 'microsoft', 'cherry'}
```
<div style="page-break-before: always;"></div>

* **union():-** Return a set containing the union of sets
```python
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z) 

print(result)   # Output:- {'b', 'e', 'f', 'd', 'c', 'a'}
```

* **update():-** The update() method updates the current set, by adding items from another set (or any other iterable).
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print(x)    # Output:- {'microsoft', 'banana', 'cherry', 'google', 'apple'}
```