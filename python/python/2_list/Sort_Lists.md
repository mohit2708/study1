### **Ques. Sort Lists?**
* Case Insensitive Sort:- By default the **sort()** method is case sensitive, resulting in all capital letters being sorted before lower case letters.
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # Output:- ['Kiwi', 'Orange', 'banana', 'cherry']

# Example2:-
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # Output:- [23, 50, 65, 82, 100]
```
* So if you want a **case-insensitive sort** function, use str.lower as a key function.
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # Output:- ['banana', 'cherry', 'Kiwi', 'Orange']
```

* **Sort Descending:-** To sort descending, use the keyword argument reverse = True.
```python
thislist = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

Output:- ['orange', 'mango', 'banana', 'Pineapple', 'Kiwi']
```

* Reverse Order:- The **reverse() method** reverses the current sorting order of the elements.
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 

Output:- ['cherry', 'Kiwi', 'Orange', 'banana']
```