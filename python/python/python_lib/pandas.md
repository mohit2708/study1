|  No.  | [Python Interview Questions](./0.0_python_questions.md)     |
| :---: | ----------------------------------------------------------- |
|       | [what is pandas?](#what-is-pandas)                          |
|       | [Install pandas?](#install-pandas)                          |
|       | [Checking Pandas Version](#checking-pandas-version)         |
|       | [Creating an Empty DataFrame](#creating-an-empty-dataframe) |


### **Install Jupyter Notebook**
* Install the classic Jupyter Notebook with:
```python
pip install notebook
```
* To run the notebook:
```python
jupyter notebook
```

### **What is pandas?**
* Pandas is a Python library used for data manipulation and analysis.
* It provides data structures and functions to handle numerical tables and time series data efficiently.
* The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes **McKinney** in **2008**.

### **Install Pandas**
```python
pip install pandas
```
* upgrade pandas
```python
pip install --upgrade pandas
```

### **Checking Pandas Version**
```python
import pandas as pd

print(pd.__version__)   # Output:- 2.2.2
```

### Pandas provides two types of classes for handling data:
1. **Series**: a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc.
2. **DataFrame**: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.

### Import Pandas
```python
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
Output:- 
    cars    passings
0   BMW         3
1   Volvo       7
2   Ford        2
```
* **alias:** In Python alias are an alternate name for referring to the same thing.
```python
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
```


### Creating an Empty DataFrame
```python
import pandas as pd
df = pd.DataFrame()
print(df)

Output:-
Empty DataFrame
Columns: []
Index: []
```

### Creating a DataFrame from a List
```python
import pandas as pd

lst = ['mohit', 'is', 'good', 'boy']

df = pd.DataFrame(lst)
print(df)

Output:-
        0
0   mohit
1     is
2   good
3    boy
```

### Creating DataFrame from dict of Numpy Array
```python
import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

Output:-
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
```

### Creating a DataFrame from a List of Dictionaries
```python
import pandas as pd

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict)

print(df)

Output:-
     name  degree  score
0  aparna     MBA     90
1  pankaj     BCA     40
2  sudhir  M.Tech     80
3   Geeku     MBA     98
```



### what is concat?
* The pandas. concat() function concatenates and combines multiple DataFrames or Series into a single, unified DataFrame or Series.

### Pandas

* Install pandas
```python
pip install pandas
```



### Pandas Dataframe/Series.head() method
* Pandas head() method is used to return top n (**5 by default**) rows of a data frame or series. but you can specify a different number as an argument.
```python
import pandas as pd

# Sample DataFrame
data = {'col_1': [1, 2, 3, 4, 5, 6], 
        'col_2': ['A', 'B', 'C', 'D', 'E', 'F']}
df = pd.DataFrame(data)

# Get the first 3 rows
print(df.head(3))
# Expected Output:
#    col_1 col_2
# 0      1     A
# 1      2     B
# 2      3     C

# Get the first 5 rows (default)
print(df.head())
# Expected Output:
#    col_1 col_2
# 0      1     A
# 1      2     B
# 2      3     C
# 3      4     D
# 4      5     E
```


### Dataframe/Series.tail() method
* The tail() method in Pandas is used to retrieve the last n rows of a DataFrame or Series. By default, it returns the last **5 rows** if no argument is specified.
```python
import pandas as pd

# Creating a DataFrame
data = {'col_1': [3, 2, 1, 0, 4], 'col_2': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Retrieving the last 2 rows
last_two_rows = df.tail(2)
print(last_two_rows)
# Expected Output
#    col_1 col_2
# 3      0     d
# 4      4     e

# Retrieving the last 5 rows
last_five_rows = df.tail()
print(last_five_rows)
# Expected Output
#    col_1 col_2
# 0      3     a
# 1      2     b
# 2      1     c
# 3      0     d
# 4      4     e
```

### DataFrame describe() Method
* describe() method in Pandas is used to generate descriptive statistics of DataFrame columns. It gives a quick summary of key statistical metrics like **mean**, **standard deviation**, **percentiles**, and more. By default, describe() works with numeric data but can also handle categorical data, offering tailored insights based on data type.
#### Parameters:
* **percentiles**: A list of numbers between 0 and 1, specifying which percentiles to return. The default is None, which returns the 25th, 50th, and 75th percentiles.
* **include**: A list of data types to include in the summary. You can specify data types such as int, float, object (for strings), etc. The default is None, meaning all numeric types are included.
* **exclude**: A list of data types to exclude from the summary. This parameter is also None by default, meaning no types are excluded.
```python
count: Total number of non-null values in the column.
mean: Average value of the column.
std: Standard deviation, showing how spread out the values are.
min: Minimum value in the column.
25%: 25th percentile (Q1).
50%: Median value (50th percentile).
75%: 75th percentile (Q3).
max: Maximum value in the column.
```
```python
import pandas as pd
data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.describe())

Output:-
                0          1          2
count   3.000000   3.000000   3.000000
mean   10.666667  17.666667   7.333333
std     2.081666   2.516611   4.041452
min     9.000000  15.000000   3.000000
25%     9.500000  16.500000   5.500000
50%    10.000000  18.000000   8.000000
75%    11.500000  19.000000   9.500000
max    13.000000  20.000000  11.000000
```

# Pandas Series
### What is a Series?
* It is a **one-dimensional** labeled array that can hold data of any type, such as integers, strings, floats, or Python objects. 
* A Series can be thought of as a single column of a table or a spreadsheet. 
* Pandas Series is a fundamental data structure in the Python library pandas.
```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)
print(myvar)

# Output:
0    1
1    7
2    2
dtype: int64

# ---------------------
print(myvar[0])       # Output:- 1
```

### Create Labels
```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Output:-
x    1
y    7
z    2
dtype: int64

# ---------------------
print(myvar["y"])       # Output:- 7
```

### Key/Value Objects as Series
```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)


# Output:-
day1    420
day2    380
day3    390
dtype: int64
```
* To **select** only **some of the items** in the **dictionary**, **use** the **index** argument and specify only the items you want to include in the Series.
```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

# Output:-
day1    420
day2    380
dtype: int64
```