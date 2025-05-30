|  No.  | [Numpy]()                                               |
| :---: | ------------------------------------------------------- |
|       | [What is Numpy?](#ques-what-is-numpy)                   |
|       | [Installation of NumPy?](#installation-of-numpy)        |
|       | [Checking NumPy Version?](#ques-checking-numpy-version) |
<div style="page-break-before: always;"></div>

### **Ques. What is Numpy?**
* NumPy is short for "Numerical Python".
* NumPy is a Python library. it is used for working with arrays.
* NumPy was created in **2005** by **Travis Oliphant**.

### **Installation of NumPy?**
* If you have Python and PIP already installed on a system, then installation of NumPy is very easy.
```python
# Open cmd
C:\Users\Your Name> pip install numpy
```
* Once NumPy is installed, import it in your applications by adding the import keyword:
```python
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

Output:- [1 2 3 4 5]
```
* Create an **alias** with the as keyword while importing:
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

Output:- [1 2 3 4 5]
```

### **Ques. Checking NumPy Version?**
```python
import numpy as np
print(np.__version__)

Output:- 1.16.3
```
<div style="page-break-before: always;"></div>

### Ques. Why is NumPy Faster Than Lists?




