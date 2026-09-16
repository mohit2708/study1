### Access Array/Array Slicing
### **How do I access or Slicing elements in a NumPy array?**
* Slicing in python means taking elements from one given index to another given index.
* We pass slice instead of index like this: **[start:end]**.
* We can also define the step, like this: **[start : end : step]**.
* If we don't pass start its considered 0
* If we don't pass end its considered length of array in that dimension
* If we don't pass step its considered 1
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[0])           # output:- 1
print(arr[1])           # output:- 2
print(arr[2] + arr[3])  # Output:- 4+3=7

print(arr[1:5])     # Output:- [2 3 4 5]
print(arr[4:])      # Output:- [5 6 7]
print(arr[:4])      # Output:- [1 2 3 4]
print(arr[-3:-1])   # Output:- [5 6]
print(arr[1:5:2])   # Output:- [2 4]
print(arr[::2])     # Output:- [1 3 5 7]

# -----Slicing 2-D Arrays------
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0, 1])    # Output:- 2
print(arr[1, 4])    # Output:- 10
print(arr[1, -1])   # Output:- 10   Negative index

print(arr[1, 1:4])      # Output:- [7 8 9]
print(arr[0:2, 2])      # Output:- [3 8]
print(arr[0:2, 1:4])    # Output:- [[2 3 4][7 8 9]]

# -----Access 3-D Arrays-----
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])     # Output:- 6
```