### **Ques. Interchange first and last elements in a list?**
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

### **Swap Two Elements in a List?**
* using **comma** assignment
```python
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))  # Output:- [19, 65, 23, 90]
```

* Using **temp** variable
```python
def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))  # Output:- [19, 65, 23, 90]
```

* Using **enumerate**
```python
def swapPositions(lis, pos1, pos2):
    for i, x in enumerate(lis):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    lis[pos1] = elem2
    lis[pos2] = elem1
    return lis
 
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))  # Output:- [19, 65, 23, 90]
```