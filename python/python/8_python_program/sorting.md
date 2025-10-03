### **list Sorting using bubble sort**
```python
list = [3,-6,2,4,6,-2,-7]

def sortUsingBubbleSort(list):
    length = len(list)
    for i in range(length):
        for j in range(0, length-i-1):
            if list[j] > list[j+1]:
                temp        = list[j]
                list[j]     = list[j+1]
                list[j+1]   = temp
                # list[j], list[j+1] = list[j+1], list[j]   # in one line and remove above 3 lines

sortUsingBubbleSort(list)
print(list) # Output:- [-7, -6, -2, 2, 3, 4, 6]
```