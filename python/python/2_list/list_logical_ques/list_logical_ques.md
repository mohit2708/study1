
|  No.  | Questions                                                                                                                             |
| :---: | ------------------------------------------------------------------------------------------------------------------------------------- |
|       | [find the single number(unique-element) of the list?](#ques-find-the-single-numberunique-element-of-the-list)                         |
|       | [Interchange first and last elements in a list?](#ques-interchange-first-and-last-elements-in-a-list)                                 |
|       | [Swap Two Elements in a List?](#swap-two-elements-in-a-list)                                                                          |
|       | [find the even number from the list?](#ques-find-the-even-number-from-the-list)                                                       |
|       | [Print duplicate list, Find Even Or Odd Number?](#ques-print-duplicate-list-find-even-or-odd-number)                                  |
|       | [even values from a list using list comprehension?](#ques-even-values-from-a-list-using-list-comprehension)                           |
|       | [Find the duplicate element from list?](#find-the-duplicate-element-from-list)                                                        |
|       | [Remove duplicate item from list using List comprehension?](#ques-remove-duplicate-item-from-list-using-list-comprehension)           |
|       | [Convert a list into string?](#ques-convert-a-list-into-string)                                                                       |
|       | [Write a program to print a list in reverse order?](#ques-write-a-program-to-print-a-list-in-reverse-order)                           |
|       | [find the max, min number from the list user input?](#ques-find-the-max-min-number-from-the-list-user-input)                          |
|       | [find the sum of list elements?](#ques-find-the-sum-of-list-elements)                                                                 |
|       | [Generate a number list between two ranges?](#ques-generate-a-number-list-between-two-ranges)                                         |
|       | [Remove elements in a list after a specific index?](#ques-remove-elements-in-a-list-after-a-specific-index)                           |
|       | [Remove elements in a list before  a specific index?](#ques-remove-elements-in-a-list-before--a-specific-index)                       |
|       | [Count the elements of a specific object in a list?](#ques-count-the-elements-of-a-specific-object-in-a-list)                         |
|       | [Multiply a Python List by a Number Using a for loop?](#ques-multiply-a-python-list-by-a-number-using-a-for-loop)                     |
|       | [Multiply a Python List by a Number Using a list comprehension?](#ques-multiply-a-python-list-by-a-number-using-a-list-comprehension) |
|       | [Convert a list into a tuple?](#ques-convert-a-list-into-a-tuple)                                                                     |
|       | [Find to common/Intersect element in two list?](#ques-find-to-commonintersect-element-in-two-list)                                    |
|       | [Get the difference between two List using comprehension?](#ques-get-the-difference-between-two-list-using-comprehension)             |
|       | [How to iterate over 2+ lists at the same time?](#ques-how-to-iterate-over-2-lists-at-the-same-time)                                  |
|       | [Sort the list on the basis of length?](#ques-sort-the-list-on-the-basis-of-length)                                                   |
|       | [How would you convert a list to an array?](#ques-how-would-you-convert-a-list-to-an-array)                                           |



### **Ques. find the single number(unique element) of the list?**
```python
mylist = [1,2,2,3,3,4,5,5,5,6,6,6,6]
new_list = []
for num in mylist:
    if(mylist.count(num) == 1):
        new_list.append(num)

print(new_list) # Output:-[1, 4]

# Using Comp
print([num for num in mylist if mylist.count(num)==1]) # Output:-[1, 4]
```
<div style="page-break-before: always;"></div>


### **Ques. find the even number from the list?**
```python
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ansList = []
unique_lst = []
for num in numberList:
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            ansList.append(num)
# ansList = list(dict.fromkeys(ansList)) # remove duplicate item using dict method
# ansList = [*set(ansList)] # remove duplicate item convert into set.
for ele in ansList:
    if ele not in unique_lst:
        unique_lst.append(ele)
print(unique_lst)
```

### **Ques. Print duplicate list, Find Even Or Odd Number?**
```python
list = [9,3,6,4,7,3,1,4]
duplicate = []
even = []
odd = []
for i in list:
    if list.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
    elif i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(duplicate)    # Output:- [3, 4]
print(even)     # Output:- [6, 4]
print(odd)      # Output:- [9, 7, 3, 1]

# Using List comprehension
[duplicate.append(i) for i in list if list.count(i) > 1 and i not in duplicate]
print(duplicate)
```

### Find the duplicate element from list?
```python
list = [9,3,6,4,7,3,1,4]
duplicate = []
for i in list:
    if list.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
   
print(duplicate)    # Output:- [3,4]
```

```python
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

Output:- 2 3 4 5
```

### Ques. even values from a list using list comprehension?
```python
# normal function
lstnum = [12, 18, 14,17,15,6]
evenNum = []
for ele in lstnum:
    if ele%2==0:
        evenNum.append(ele)
print(evenNum)

# comprehension
evenNum1 = [ele for ele in lstnum if ele%2==0]
print(evenNum1)

Output:- [12, 18, 14, 6]
```
<div style="page-break-before: always;"></div>



### Ques. Remove duplicate item from list using List comprehension?
```python
lstnum = [12, 36, 56, 36, 36, 50, 56, 12] 
unique_lst = [] 

[unique_lst.append(ele) for ele in lstnum if ele not in unique_lst]  
print ("unique elements list  : " ,unique_lst)
```


### Ques. Convert a list into string?
```python
list = ['my','name','is','Mohit','Saxena']
listtostring = ' '.join(list)
print('list after shuffling =',listtostring)

Output:-
list after shuffling = my name is Mohit Saxena
```


### Ques. find the max, min number from the list user input?
```python
number = int(input('enter the number of items in list '))
list = []
for num in range(number):
    item = int(input('Entered number '))
    list.append(item)
print('entered list=', list)
print('Max Number= ', max(list))
print('min number= ', min(list))

Output:-
enter the number of items in list 5
Entered number 6
Entered number 4
Entered number 15
Entered number 85
Entered number 5
entered list= [6, 4, 15, 85, 5]
Max Number=  85
min number=  4
```

### Ques. find the sum of list elements?
```python
num = [12, 36, 56, 36, 36, 50, 56, 12]
sum = 0
for ele in range(len(num)):
    sum = sum + num[ele]
print(sum)

Output:- 294
```

### Ques. Generate a number list between two ranges?
```python
listnum = list(range(1, 7))
print ("list between two range : " ,listnum)

Output:- list between two range :  [1, 2, 3, 4, 5, 6]
```

### Ques. Remove elements in a list after a specific index?
```python
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
remove_item = li[:10]
print(remove_item)
#=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Ques. Remove elements in a list before  a specific index?
```python
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
li[15:]
#=> [16, 17, 18, 19, 10]
```

### Ques. Count the elements of a specific object in a list?
* The count() method returns the number of occurrences of a specific object.
```python
pets = ['dog','cat','fish','fish','cat']
index = pets.count('fish')
print(index)    # Output:- 2
```


### **Ques. Multiply a Python List by a Number Using a for loop?**
```python
numbers = [1, 2, 3, 4, 5]
multiplied = []
for number in numbers:
    multiplied.append(number * 2)
print(multiplied)
Output:- [2, 4, 6, 8, 10]
```


### **Ques. Multiply a Python List by a Number Using a list comprehension?**
```python
numbers = [1, 2, 3, 4, 5]
multiplied = [number * 2 for number in numbers]
print(multiplied)
Output:- [2, 4, 6, 8, 10]
```

### Ques. **Convert a list into a tuple?**
* Using **tuple()** builtin function 
```python
list = [1,2,3,4]
result = tuple(list)
print(type(result))

Output:- <class 'tuple'>
```

* Using **loop** inside the tuple
```python
sample_list = ['Compile', 'With', 'Favtutor']
tuple1 = tuple(i for i in sample_list)
print(tuple1)

Output:- ('Compile', 'With', 'Favtutor')
```

* **Unpack** list inside the parenthesis
```python
sample_list = ['Compile', 'With', 'Favtutor']

#unpack list items and form tuple
tuple1 = (*sample_list,)

print(tuple1)
print(type(tuple1))

Output:- 
('Compile', 'With', 'Favtutor')
<class 'tuple'>
```


### Ques. Find to common/Intersect element in two list?
```python
listnum = ['C++',2,3,6,7,5,'C#']
listnum1 = ['C++',5,6,7,'C#']
intersect_res= []
for ele in listnum:
    if ele in listnum1:
        intersect_res.append(ele)
print(intersect_res)

# Using comprehension
intersect_res = [item for item in listnum if item in listnum1]
 
print('intersect of two list =',intersect_res)  # output:- ['C++', 6, 7, 5, 'C#']
```

### Ques. Get the difference between two List using comprehension?
```python
lstnum = [15, 78, 4]
lstnum1 = [80, 4, 89]
diffra = []
for num in lstnum:
    if num not in lstnum1:
        diffra.append(num)

print(diffra)   # Output:- Output:- [15, 78]
```


### **Ques. How to iterate over 2+ lists at the same time?**
```python
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(name, animal, age)
for name,animal,age in z:
    print("%s the %s is %d" % (name, animal, age))

Output:-
Snowball the Cat is 1
Chewy the Dog is 2
Bubbles the Fish is 2
Gruff the Goat is 6
```

### **Ques. Combine 2 lists into a list of tuples with the zip function?**
```python
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
print(list(zip(name,animal)))

Output:- [('Snowball', 'Cat'), ('Chewy', 'Dog'), ('Bubbles', 'Fish'), ('Gruff', 'Goat')]
```

### **Ques. Sort the list on the basis of length?**
```python
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2
      
lst = ["rohan", "amy", "sapna", "muhammad", "aakash", "raunak", "chinmoy"]
print(Sorting(lst))

Output:- ['amy', 'rohan', 'sapna', 'aakash', 'raunak', 'chinmoy', 'muhammad']
```

### **Ques. How to Zip two lists**
* Using map() + __add__ 
```python
test_list1 = [[1, 3], [4, 5], [5, 6]]
test_list2 = [[7, 9], [3, 2], [3, 10]]

print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

res = list(map(list.__add__, test_list1, test_list2))

print("The modified zipped list is : " + str(res))

Output:- 
The original list 1 is : [[1, 3], [4, 5], [5, 6]]
The original list 2 is : [[7, 9], [3, 2], [3, 10]]
The modified zipped list is : [[1, 3, 7, 9], [4, 5, 3, 2], [5, 6, 3, 10]]
```

### **Ques. List Sorting in descending order?**
```python
list = [24,55,78,64,25,12,22,11,1,2,44]
list.sort(reverse = True)
print(list)

# 2nd Option Using For Loop
# list = [24,55,78,64,25,12,22,11,1,2,44]
list = []
intlistTot = int(input("Total Number of List Items to Sort = "))
for i in range(1, intlistTot + 1):
    intlistvalue = int(input("Please enter the %d List Item = "  %i))
    list.append(intlistvalue)
    
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if(list[i] < list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    
print(list)

Output:- [78, 64, 55, 44, 25, 24, 22, 12, 11, 2, 1]
```



### **Ques. Check if a list contains an element?**
* The in operator will return True if a specific element is in a list.
```python
li = [1,2,3,'a','b','c']
'a' in li 

Output:- True
```

### **Ques. Find the index of the 1st matching element?**
* you want to find the first “apple” in a list of fruit. Use the **index()** method.
```python
fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
a = fruit.index('apple') #=> 2
b = fruit.index('pear') #=> 0
```

### **Ques.  Iterate over both the values in a list and their indices?**
* enumerate() adds a counter to the list passed as an argument.
```python
grocery_list = ['flour','cheese','carrots']
for id,val in enumerate(grocery_list):
    print("%s: %s" % (id, val))

Output:- 
0: flour
1: cheese
2: carrots
```

### **Ques. How to manipulate every element in a list with list comprehension?**
```python
# using comprehension
li = [0,25,50,100]
b = [i+1 for i in li]
print(b)

# Using for loop
for i in li:
    a = i+1;
    print(a)

Output:-
[1, 26, 51, 101]
1
26
51
101
```


### Replace elements in String list?
```python
s = ["Tutor","joes","Computer","Education"]
print("Before Swap :",s)
res = [sub.replace("joes","Joe's").replace("Computer", "Software").replace("Education", "Solutions") for sub in s]
print ("After Swap : ",res)

Output:-
Before Swap : ['Tutor', 'joes', 'Computer', 'Education']
After Swap :  ['Tutor', "Joe's", 'Software', 'Solutions']
```

### **Ques. How would you convert a list to an array?**
* Python list is a linear data structure that can hold heterogeneous elements(hold items of different data types). Python does not have a built-in array data type. If you want to create an array in Python, then use the numpy library.
* To install **numpy** in your system, type the following command.
```python
python3 -m pip install numpy
```
* <strong>1. Using numpy.array()</strong>
```python
import numpy as np

elon_list = [11, 21, 19, 18, 29]
elon_array = np.array(elon_list)

print(elon_array)
print(type(elon_array))
                       
Output:- 
[11 21 19 18 29]
<class 'numpy.ndarray'>

# 2. Using numpy.asarray()
import numpy as np

elon_list = [11, 21, 19, 18, 29]
elon_array = np.asarray(elon_list)

print(elon_array)
print(type(elon_array))

Output:- [11 21 19 18 29]
<class 'numpy.ndarray'>
```

### Split the strings and store into a list
```python
string = input("Enter string: ")
lst = string.split()  
print('The list is:', lst)

Output:-
Enter string: my name is mohit saxena
The list is: ['my', 'name', 'is', 'mohit', 'saxena']
```