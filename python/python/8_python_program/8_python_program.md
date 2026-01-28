### Table of Contents

|  No.  | Questions                                                                                      |
| :---: | ---------------------------------------------------------------------------------------------- |
|  16   | [Sorting multidimensional array by name](#sorting-multidimensional-array-by-name)              |
|       | [Find the first letter of the string](#find-the-first-latter-of-the-strig)                     |

|  No.  | [Other Program]()                                                                                        |
| :---: | -------------------------------------------------------------------------------------------------------- |
|       | [generate a random number between 0 and 9](#Program-to-generate-a-random-number-between-0-and-9)         |
|       | [Get a Substring of a String](#Get-a-Substring-of-a-String)                                              |
|       | [Count number of characters in a string](#count-number-of-characters-in-a-string)                        |
|       | [convert a list to string](#program-to-convert-a-list-to-string)                                         |
|       | [Interchange first and last elements in a list](#ques-interchange-first-and-last-elements-in-a-list)     |

|  No.  | [Array Program](#array-programs)         |
| :---: | ---------------------------------------- |
|   1   | [find sum of array?](#find-sum-of-array) |
<div style="page-break-before: always;"></div>



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

### **Find the first latter of the strig?**
```python
name = "Mohit Saxena"
words = name.split()

firstw = ""
for word in words:
    firstw += word[0]
print(' '.join(list(firstw)))

----------OR----------
name = "Mohit Saxena"
words = name.split()

firstw = ""
for word in words:
    firstw += word[0]+" "

firstw = firstw.strip()  # Remove the trailing space
print(firstw)   # Output:- MS
```

<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->


### **Ques. program to convert a list to string**
```python
def listToString(s):
    blank =""
    for element in s:
        blank = blank + ' ' + element
    print(blank)

s = ['Hello', 'mohit', 'saxena']
listToString(s)

Output:- Hellomohitsaxena
```
* Using list comprehension 
```python
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join([str(elem) for elem in s])
print(listToStr)

Output:- I want 4 apples and 18 bananas
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




### **Ques. Count the number of vowels in a string?**
```python
na = input("Enter a string: ")
count = 0
for i in na:
    if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='O' or i=='U' or i=='u'):
        count = count+1
print("Number of vowels ", count)

Output:- 
Enter a string: Mohit saxena
Number of vowels  4
```

### Ques. To identify if the Character is vowel or consonant?
```python
def vowel_or_consonant(string):
    vowel = 'aeiouAEIOU'
    for i in string:
        if i in vowel:
            print('Vowel')
        else:
            print('consonant')
vowel_or_consonant('a')

Output:- Vowel

# Method 2
l = input("Enter the character: ")
if l.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")
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


### Python program to convert a list to string
```python
def listToString(s):
    blank =""
    for element in s:
        blank = blank + ' ' + element
    print(blank)

s = ['Hello', 'mohit', 'saxena']
listToString(s)

Output:- Hellomohitsaxena
------------------------------------------------------------------

# Using list comprehension 
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join([str(elem) for elem in s])
print(listToStr)

Output:- I want 4 apples and 18 bananas
----------------------------------------------------------------

# Using .join() method 
def listToString(s):
    str1 = " "
    return (str1.join(s))
    
s = ['Hello', 'Mohit', 'Saxena']
print(listToString(s))

Output:- Hello Mohit Saxena
----------------------------------------------------------------

# Using map()
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join(map(str, s))
print(listToStr)
```


### **Ques. Solve the classic FizzBuzz problem: Print numbers from 1 to 100, but for multiples of 3 print "Fizz," for multiples of 5 print "Buzz," and for multiples of both 3 and 5, print "FizzBuzz."**
```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```


https://prepinsta.com/python-program/find-a-number-is-palindrome-or-not/

<div style="page-break-before: always;"></div>

# Array/List Programs:
### **Find sum of array/list?**
```python
arr = [3,2,4]

# -- using for loop
sum = 0
for i in arr:
    sum = i + sum
print(sum)  # Output:- 9

# -- using sum function
print(sum(arr)) # Output:- 9
```

### **Find Largest Element in an Array/list?**
```python
arra = [10, 324, 45, 90, 9808]

# -- using for loop
n = len(arra)
max = arra[0]
for i in range(1, n):
    if arra[i] > max:
        max = arra[i]
print(max)  # output:- 9808

# -- Using inbuild function
print(max(arra))    # Output:- 9808

# -- Using sort function
arra.sort()
print(arra[-1]) # Output:- 9808
```
<div style="page-break-before: always;"></div>

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


### add one digit 
```python
def add_one_to_digits(digits):
    # Start from the last digit
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:  # If the current digit is less than 9
            digits[i] += 1  # Just add 1
            return digits
        else:  # If the current digit is 9
            digits[i] = 0  # Set it to 0 and carry over 1

    # If we've exhausted all digits and still have a carry
    return [1] + digits  # Prepend 1 to the list (e.g., from 999 to 1000)

# Example input
example_list = [1,2,7]
result = add_one_to_digits(example_list)

print("Output:", result) # Output: [1, 2, 8]
```