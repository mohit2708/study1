### 🧠 **Numpy Questions List**
1. [What is NumPy?](/python/python_lib/numpy.md#ques-what-is-numpy)
2. [How to install Numpy?](/python/python_lib/numpy.md#installation-of-numpy)
3. [Checking NumPy Version?](/python/python_lib/numpy.md#checking-numpy-version)
4. [Creating Arrays](/python/python_lib/numpy.md#creating-arrays)
5. [What is array slicingAccess?](/python/python_lib/numpy/Slicing_access.md)
6. [Why do we use NumPy?](/python/python_lib/numpy.md#why-do-we-use-numpy)
7. [What are the advantages of NumPy?](/python/python_lib/numpy.md#what-are-the-advantages-of-numpy)
8. [What is an ndarray?](/python/python_lib/numpy.md#what-is-an-ndarray)
9. [Difference between List and NumPy Array?](/python/python_lib/numpy.md#difference-between-list-and-numpy-array)
10. [Why is NumPy faster than Python lists?](/python/python_lib/numpy.md#ques-why-is-numpy-faster-than-lists)
11. [How do you **create a NumPy array**?](/python/python_lib/numpy/create_NumPy_array.md#how-do-you-create-a-numpy-array)
12. What is **scalar array**?
What is the difference between array(), zeros(), ones(), and empty()?
What is the shape of an array?
What is the size of an array?
What is the ndim attribute?
What is dtype in NumPy?
How do you check the data type of a NumPy array?
What is array indexing?
Difference between shallow copy and deep copy in NumPy?

Intermediate Level
What is vectorization in NumPy?
Why is vectorization faster than loops?
What is broadcasting?
Explain NumPy broadcasting rules.
Difference between reshape() and resize()?
What is the difference between flatten() and ravel()?
What is the difference between copy() and view()?
How do you transpose a NumPy array?
Difference between transpose() and swapaxes()?
What is fancy indexing?
What is boolean indexing?
How do you filter data using conditions?
What is masking in NumPy?
How do you concatenate arrays?
Difference between concatenate(), stack(), hstack(), and vstack()?
Array Operations
How do you perform element-wise operations?
Difference between element-wise multiplication and matrix multiplication?
What does dot() do?
Difference between dot() and matmul()?
How do you find the sum of all elements?
How do you calculate mean, median, and standard deviation?
What is axis in NumPy functions?
Difference between axis=0 and axis=1?
How do you find minimum and maximum values?
How do you sort a NumPy array?
Random Module
How do you generate random numbers in NumPy?
Difference between rand(), randn(), and randint()?
What is a random seed?
Why do we use np.random.seed()?
How do you shuffle an array?
Advanced Level
What are Universal Functions (ufuncs)?
Give examples of ufuncs.
What is the difference between apply_along_axis() and vectorization?
What are structured arrays?
What is memory optimization in NumPy?
Why is NumPy memory efficient?
What is contiguous memory?
What is stride in NumPy?
What are strides used for?
What is the difference between C-order and Fortran-order arrays?
What is memory alignment in NumPy?
What is NumPy's internal storage format?
Matrix Related Questions
How do you create a matrix in NumPy?
Difference between array and matrix?
How do you find the transpose of a matrix?
How do you calculate the determinant?
How do you find the inverse of a matrix?
What is eigenvalue and eigenvector?
How do you perform matrix multiplication?
Difference between * and @ operators?
What is Singular Value Decomposition (SVD)?
What is Linear Algebra module in NumPy?
Scenario-Based Interview Questions
How would you replace loops using NumPy?
How would you handle a large dataset efficiently using NumPy?
How would you remove missing values from a NumPy array?
How would you find duplicate values in an array?
How would you find unique values in an array?
How would you normalize data using NumPy?
How would you find the top N values in an array?
How would you merge multiple arrays?
How would you convert a Python list into a NumPy array?
How would you improve the performance of numerical calculations?
Frequently Asked Interview Questions
1. What is NumPy?

Answer: NumPy (Numerical Python) is a Python library used for fast numerical computations and multi-dimensional array operations.

2. Why is NumPy faster than Python lists?

Answer: NumPy stores data in contiguous memory and performs operations using optimized C code, making it much faster than Python lists.

3. What is Broadcasting?

Answer: Broadcasting allows NumPy to perform arithmetic operations on arrays of different shapes without explicitly copying data.

4. Difference between flatten() and ravel()?
flatten()	ravel()
Returns a copy	Returns a view (if possible)
More memory	Less memory
Changes don't affect original	Changes may affect original
5. Difference between copy() and view()?
copy()	view()
Creates new memory	Shares memory
Independent object	References original data
Changes don't affect original	Changes affect original
6. What is Vectorization?

Answer: Vectorization means performing operations on entire arrays at once without using explicit Python loops, resulting in better performance.

Ye 20–25 questions sabse zyada puche jaate hain:

NumPy, ndarray, dtype, shape, ndim, indexing, slicing, vectorization, broadcasting, copy vs view, flatten vs ravel, reshape, axis, fancy indexing, boolean indexing, concatenate, stack, dot vs matmul, random seed, ufuncs, matrix multiplication, determinant, inverse, memory optimization.