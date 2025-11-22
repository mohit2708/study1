### Remove List Items

- using **remove()** method :-
    - remove() method the **first instance of a matching object**.
    - Remove **Specified Item** from the List using remove() method.
    - If item **not exist** in remove method then **show the error.**

```python
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)     # Output:- ['apple', 'cherry', "banana"]
```

```python
thislist.remove("banana1")
print(thislist) # Output:- error item not in the list
```

- using **pop()** method :-
    - pop() method removes an item at a **specified index**.
    - If no index is specified, it removes the **last item**.

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)     # Output:- ['apple', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]

thislist.pop()
print(thislist)     # Output:- ['apple', 'banana']
```

- using **del** keyword :-
    - del keyword removes an item at a **specified index**.
    - Can also **delete the entire list**.

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)     # Output:- ['banana', 'cherry']

del thislist        # Deletes the entire list
```

- using **clear()** method :-
    - clear() method **empties the list** but the list still exists.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)     # Output:- []
```