
### **Interchange first and last elements in a list?**
- Without temp varibale
```python
list = [12, 35, 9, 56, 24]
list[0] = list[-1]
list[-1] = list[0]
print(list) # Output:- [24, 35, 9, 56, 24]
```

- With temp variable
```python
list = [12, 35, 9, 56, 24]
length = len(list)
temp = list[0]
list[0] = list[length - 1]
list[length - 1] = temp
print(list) # Output:- [24, 35, 9, 56, 12]
```

- Using comma function
```python
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))    # Output:- [24, 35, 9, 56, 12]
```


- Using * operand.
```python
list = [1, 2, 3, 4]

a, *b, c = list

print(a)
print(b)
print(c)

Output:-
1
[2, 3]
4
```


- Using * operand 2 approch.
```python
def swapList(list):
    start, *middle, end = list
    list = [end, *middle, start]
    return list

newList = [12, 35, 9, 56, 24]
print(swapList(newList))    # Output:- [24, 35, 9, 56, 12]
```