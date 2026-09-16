|  No.  | even or odd program                                                              |
| :---: | -------------------------------------------------------------------------------- |
|       | [Armstrong number or not](#ques-check-number-is-an-armstrong-number-or-not)      |

<div style="page-break-before: always;"></div>


# Not Filter
### **Sorting multidimensional array by name**
```python
abc = [
    {"name": "mohit", "age": 30},
    {"name": "abhinav", "age": 36},
    {"name": "rohit", "age": 25}
]

# Bubble sort by "name" key
n = len(abc)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if abc[j]["name"] > abc[j + 1]["name"]:
            # Swap elements
            abc[j], abc[j + 1] = abc[j + 1], abc[j]
print(abc)
# Print the sorted array
for person in abc:
    print("Name: {}, Age: {}".format(person["name"], person["age"]))
```

### **Ques. program to convert a list to string**
```python
def listToString(s):
    blank =""
    for element in s:
        blank = blank + ' ' + element
    print(blank)

s = ['Hello', 'mohit', 'saxena']
listToString(s)     # Output:- Hello mohit saxena
```

* Using list comprehension 
```python
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join([str(elem) for elem in s])
print(listToStr)    # Output:- I want 4 apples and 18 bananas
```

* Using .join() method 
```python
def listToString(s):
    str1 = " "
    return (str1.join(s))
    
s = ['Hello', 'Mohit', 'Saxena']
print(listToString(s))  

Output:- Hello Mohit Saxena
```
* Using map()
```python
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join(map(str, s))
print(listToStr)
```


### Program to generate a random number between 0 and 9?
```python
import random
print(random.randint(0,9))

Output:- 0 se 9 tak ka koi bhi number aa sakta hai.
```

### **Calculate the number of words**
* Using split method
```python
test_string = "Mohit saxena"
res = len(test_string.split())
print ("The number of words in string are : " + str(res))

Output:- 2
```
* 
```python
na = input("Enter a string: ")
space = 0
for i in na:
    if i==" ":
        space = space+1
print(space)
print(space+1)

Output:-
Enter a string: mohit saxena
1
2
```

### **Print A to Z ?**
* Using String module
```python
import string

for i in string.ascii_lowercase:
    print(i, end=" ")

Output:- a b c d e f g h i j k l m n o p q r s t u v w x y z
---------------------------------------------------------------
import string

for i in string.ascii_uppercase:
    print(i, end=" ")

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```
* Using chr() Function
```python
for i in range(97,123):
    print(chr(i), end=" ")

a b c d e f g h i j k l m n o p q r s t u v w x y z
------------------------------------------
for i in range(65,91):
    print(chr(i), end=" ")

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```


```python
latter = input("Enter any latter:- ").lower()
vowels = ['a','e','i','o','u']
if latter in vowels:
    print(f"{latter} is a vowel")
else:
    print(latter,"latter is not vowel")
```

### Ques. To check number is digit or not?
```python
number = input("Enter any number:- ")
if number.isdigit():
    print(f'{number} is digit')
else:
    print(f'{number} is not digit')
```

### QUes. Check leep year or not
```python
year = int(input("Enter any year:- "))
if (year%4 == 0):
    print(f'{year} is a leep year')
else:
    print(f'{year} is not a leep year')
```



### **Ques. Multiply two numbers without using arithmetic operator?**
```python
num1=int(input("Enter a number for num1: "))
num2=int(input("Enter a number for num2: "))
product=0
for i in range (1,num2+1):  #Python for loop
 product=product+num1       #product+=num1
print("Multiplication of numbers: ",product)

Output:- 
Enter a number for num1: 4
Enter a number for num2: 4
Multiplication of numbers:  16
```


https://prepinsta.com/python-program/find-a-number-is-palindrome-or-not/

<div style="page-break-before: always;"></div>

# Array/List Programs:

### **Find the missing number in the array/list?**
```python
def findMissingNumbers(n):
    maxnumber = max(n)
    output = []
    for i in range(1, maxnumber):
        if i not in n:
            output.append(i)
    return output
    
listOfNumbers = [5, 6, 7, 8, 9, 10,16, 11, 13, 14]
print(findMissingNumbers(listOfNumbers))    # Output:- [1, 2, 3, 4, 12, 15]
```


