### Ques. Add Items of set?

* **add() method:-** To add one item to a set use the add() method.
```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
      
Output:- {'cherry', 'orange', 'apple', 'banana'}
```

* Try to **add** an element that **already exists**.
```python
thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)

Output:- {'banana', 'apple', 'cherry'}
```

* **update() method:-** 
  * To add items from another set into the current set, use the update() method.
  * **Add Any Iterable:-** The object in the **update()** method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
      
output:- {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
```
```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
      
Output:- {'banana', 'cherry', 'apple', 'orange', 'kiwi'}
```