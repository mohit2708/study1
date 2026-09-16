### **How do you create a NumPy array?**
* Once NumPy is installed, import it in your applications by adding the import keyword:
* NumPy array ko create karne ke liye **np.array() function** use kiya jata hai.
* NumPy ka ndarray = N-dimensional array hota hai, isliye dimensions ki koi practical limit nahi hoti (memory limit tak).

#### Syntex 
```python
import numpy as np

arr = np.array(data)
```

#### Create 0-D Arrays
#### scalar array
* NumPy mein 0D array bhi hota hai. Isse scalar array kehte hain.
* 0D array mein sirf ek single value hoti hai aur uski koi axis/dimension nahi hoti.
```python
import numpy as np
arr = np.array(42)
print(arr)  # Output:- 42
```

#### Create 1D Array
```python
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr) # Output:- [10 20 30 40]
print(type(arr))    # Output:- <class 'numpy.ndarray'>
```

#### Create 2D Array
```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)  # Output:- [[1 2 3][4 5 6]]
```

#### Create 3D Array
```python
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)      # Output:- [[[1 2 3][4 5 6]] [[1 2 3] [4 5 6]]]
```