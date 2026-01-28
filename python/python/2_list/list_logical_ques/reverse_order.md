### Ques. Write a program to print a list in reverse order?
- **using slice method**
```python
def revlist(list):
    return list[::-1]
    
list = [24,55,78,64,25,12,22,11,1,2,44]
print(revlist(list))    # Output:- [44, 2, 1, 11, 22, 12, 25, 64, 78, 55, 24]
```

* **Using For loop**
```python
list1 = [1, 2, 4, 5, 8, 9]
list2 = []
for item in list1:
    list2.insert(0, item)
print(list2)    # Output:- [9, 8, 5, 4, 2, 1]
```