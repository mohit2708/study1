### **Ques. Join Two Set?**

* **NOTE:-** Note: Both union() and update() will exclude any duplicate items.

* The **union()** method combines elements from two or more sets into a new set, eliminating duplicates.
```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

# Using the union() method
union_set_method = set1.union(set2)
print(union_set_method)  # Output:  {'c', 'a', 1, 2, 3, 'b'}

# Using the | operator
union_set_operator = set1 | set2
print(union_set_operator)  # Output: {'c', 'a', 1, 2, 3, 'b'}		
```

* The **update()** method to add elements from another set or any other iterable (like lists, tuples, or dictionaries) into an existing set. 
```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
      
output:- {'b', 'c', 1, 'a', 2, 3}
```

* The **intersection()** intersection() method returns a **new set** with an element that is **common** to all set
```python
# syntex
# Using the intersection() method
set.intersection(set1, set2 ... etc.)
OR
# Using the & operator
set & set1 & set2 ... etc.
```
```python
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}

# intersection of two sets
print(set1.intersection(set2))  # Output:- {4, 6}
print(set1 & set2)              # Output:- {4, 6}
 
# intersection of three sets
print(set1.intersection(set2, set3)) # Output:- {4, 6}
```

* The **intersection_update()** method will keep only the items that are present in both sets.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
      
output:- {'apple'}
```

* The **symmetric_difference()** method will return a new set, that contains only the elements that are NOT present in both sets.
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using the symmetric_difference() method
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

# Using the ^ operator
symmetric_difference_set2 = set1 ^ set2
print(symmetric_difference_set2) # Output: {1, 2, 3, 6, 7, 8}
```

* The **symmetric_difference_update()** method will keep only the elements that are NOT present in both sets.
```python
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}

set1.symmetric_difference_update(set2)
print(set1)

output:- {2, 5, 7, 8}
```