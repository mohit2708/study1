### Table of Contents

|  No.  | Questions                                                                                      |
| :---: | ---------------------------------------------------------------------------------------------- |
|   1   | [Hello World](#ques-print-hello-world)                                                         |
|   2   | [swap two variables](#ques-swap-two-variables)                                                 |
|   3   | [check if a number is Even or odd](#ques-program-to-check-if-a-number-is-even-or-odd)          |
|   4   | [Print the even number and odd number](#print-the-even-number-and-odd-number)                  |
|   5   | [Check Prime Number Or Not?](#ques-check-prime-number-or-not)                                  |
|   6   | [Prime Number Print between lower to upper?](#ques-prime-number-print-between-lower-to-upper)  |
|   7   | [Reverse string?](#ques-reverse-string)                                                        |
|   8   | [How to reverse a word sentence](#ques-how-to-reverse-a-word-sentence)                         |
|   9   | [Reverse a Number](#ques-reverse-a-number)                                                     |
|  10   | [To Check if a String is a Palindrome](#ques-to-check-if-a-string-is-a-palindrome)             |
|  11   | [To Check if a Number is a Palindrome](#ques-to-check-if-a-number-is-a-palindrome)             |
|  12   | [Find the Factorial of a Number](#ques-find-the-factorial-of-a-number)                         |
|  13   | [find Fibonacci series up to n](#ques-find-fibonacci-series-up-to-n)                           |
|  14   | [check number is an Armstrong number or not](#ques-check-number-is-an-armstrong-number-or-not) |
|  15   | [list Sorting using bubble sort](#list-sorting-using-bubble-sort)                              |
|       | [Star Print](#star-printing)                                                                   |
|  16   | [Sorting multidimensional array by name](#sorting-multidimensional-array-by-name)              |

|  No.  | [Other Program]()                                                                                        |
| :---: | -------------------------------------------------------------------------------------------------------- |
|       | [generate a random number between 0 and 9](#Program-to-generate-a-random-number-between-0-and-9)         |
|       | [Get a Substring of a String](#Get-a-Substring-of-a-String)                                              |
|       | [How to reverse a sentence in Python input by User?](#How-to-reverse-a-sentence-in-Python-input-by-User) |
|       | [Count number of characters in a string](#count-number-of-characters-in-a-string)                        |
|       | [convert a list to string](#program-to-convert-a-list-to-string)                                         |
|       | [Interchange first and last elements in a list](#ques-interchange-first-and-last-elements-in-a-list)     |

|  No.  | [Array Program](#array-programs)         |
| :---: | ---------------------------------------- |
|   1   | [find sum of array?](#find-sum-of-array) |
<div style="page-break-before: always;"></div>


### [Ques. Print Hello World?](#table-of-contents)
```python
print('Hello World!!!')

Output:- Hello World!!!
```

### **Ques. swap two variables?**
```python
a = 11
b = 7

# -- Using a Temporary variable
temp = a
a = b
b = temp

print(a) # 7
print(b) # 11

# -- Without a temporary variable
a, b = b, a

print(a) # 7
print(b) # 11

# -- Using arithmetic operators
a = a + b # a = 18, b = 7
b = a - b # a = 18, b = 11
a = a - b # a = 7,  b = 11

print(a) # 7
print(b) # 11

# -- Using multiplication and division operator
# To Swap the values of two variables using Addition and subtraction operator  
P = P * Q    
Q = P / Q   
P = P / Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)

# -- XOR swap
P = P ^ Q    
Q = P ^ Q   
P = P ^ Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)
```
<div style="page-break-before: always;"></div>

### **Ques. Program to check if a number is Even or odd?**
```python
# 1 Option
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# 2 option
def evenOrOdd(n):
    if n%2 == 0:
        print('even Number hai')
    else:
        print('Odd Number hai')
evenOrOdd(6)
```

### **Print the even number and odd number**
```python
num = int(input("Enter a number: "))
even = []
odd = []
for i in range(2,num+1):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(even) # Output:- [2, 4, 6, 8, 10, 12, 14]
print(odd)  # Output:- [3, 5, 7, 9, 11, 13, 15]
```
<div style="page-break-before: always;"></div>

### **Ques. Check Prime Number Or Not?**
```python
num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")

Output:- 3
3 is a prime number
```

### **Ques. Prime Number Print between lower to upper**
```python
lower = int(input(" Please Enter the Minimum Value: "))
upper = int(input(" Please Enter the Maximum Value: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

Output:- 
11
13
17
19
```
<div style="page-break-before: always;"></div>

### **Ques. Reverse string?**
```python
# -- Using for loop
string = 'mohit'
blank =''
for i in string:
    blank = i + blank
print(blank)    # Output:- tihom

# -- Using while loop
str = "mohit"
reverse_String = ""
count = len(str)
while count > 0:
    reverse_String += str[ count - 1 ]
    count = count - 1
print (reverse_String) 

Output:- tihom

# -- Using the slice ([]) operator
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "mohit"  
print ("The original string  is : ",s)   
print (reverse(s))  

Output:- tihom

# -- Using reversed function with join
def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string

s = "mohit"  
  
print ("The original string is : ",s)   
print (reverse(s) )  

Output:- tihom
```
<div style="page-break-before: always;"></div>

### **Ques. How to reverse a word sentence?**
```python
inputsentence = input("Please input  a sentence : ")
splitString = inputsentence.split()      # ['i', 'love', 'Mohit', 'Saxena']
reversedString = reversed(splitString)
print(" ".join(reversedString))

Output:- i love Mohit Saxena
Saxena Mohit love i
```
* 2 option
```python
str = "sky is blue"
str_split = str.split()
new_str = str_split[::-1]
str =" ".join(new_str)
print(str)

Output:- blue is sky
```

* 3 option using for loop
```python
my_str = input("Please enter your own String : ")
str = ''
for i in my_str:
    str = i + str
print("\nThe Original String is: ", my_str)
print("The Reversed String is: ", str)

Output:-
The Original String is:  i love Mohit Saxena
The Reversed String is:  anexaS tihoM evol i
```
<div style="page-break-before: always;"></div>

### **Ques. Reverse a Number**
```python
# using a while loop
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print("Reverse of entered number is = %d" %Reverse)

Output:-
Please Enter any Number: 68765
Reverse of entered number is = 56786

# Using String slicing
num = 9412
print(str(num)[::-1])

Output:-
num = 2149

# Using Recursion
num = int(input("Enter the number: "))  
revr_num = 0    # initial value is 0. It will hold the reversed number  
def recur_reverse(num):  
    global revr_num   # We can use it out of the function  
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(num // 10)  
    return revr_num  
  
  
revr_num = recur_reverse(num)  
print("Reverse of entered number is = %d" % revr_num)

Output:- 
Enter the number: 1284
Reverse of entered number is = 4821
```
<div style="page-break-before: always;"></div>


### **Ques. To Check if a String is a Palindrome**
```python
def isPalindrome(string):
    rev = string[::-1]
    # rev = ''.join(reversed(string))    # 2nd Option to reversed string
    # print(rev)
    if(rev == string):
        print("The string is a palindrome!");
    else:
        print("The string isn't a palindrome!");

s = "malayalam"
# s = "Mohit saxena"
isPalindrome(s)

Output:- The string is a palindrome!
```

```python
x = "malayalam"
 
w = ""
for i in x:
    w = i + w 
if (x == w):
    print("Yes")
else:
    print("No")

Output:- Yes
```

### **Ques. To Check if a Number is a Palindrome**
```python
num = int(input("Enter a number:"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp%10
    reverse = (reverse*10)+remainder
    temp = temp//10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
```
<div style="page-break-before: always;"></div>






### **[Ques. Find the Factorial of a Number?](#table-of-contents)**
* factorial of 6 is 6*5*4*3*2*1 which is 720.
```python
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial) 

Output:- 
Enter a number: 6
The factorial of 6 is 720
```
<div style="page-break-before: always;"></div>

### **Ques. Find Fibonacci series up to n**
```python
def fibonacci(n):
    first = 0
    second = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return second
    else:
        print(first)
        print(second)
        for i in range(2, n):
            third = first + second
            first = second
            second = third
            print(third)

fibonacci(9)

Output:- 0 1 1 2 3 5 8 13 21
```
* Using While Loop
```python
def fibonacci(n):
    first = 0
    second = 1
    count = 0
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return second
    else:
        while count < n:
            print(first)  
            third = first + second  
           # At last, we will update values  
            first = second  
            second = third  
            count += 1
fibonacci(9)
```
<div style="page-break-before: always;"></div>

### **Ques. Check number is an Armstrong number or not?**
* 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3) = 153
* 1634 = (1 * 1 * 1 * 1) + (6 * 6 * 6 * 6) + (3 * 3 * 3 * 3) + (4 * 4 * 4 * 4) = 1634
```python
num = int(input("Enter a number: "))
len = len(str(num))
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum = sum + digit ** len
   temp = temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

Output:- 
Enter a number: 1634
1634 is an Armstrong number
```
<div style="page-break-before: always;"></div>

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
                # list[j], list[j+1] = list[j+1], list[j]

sortUsingBubbleSort(list)
print(list)

Output:- [-7, -6, -2, 2, 3, 4, 6]
```
<div style="page-break-before: always;"></div>

# Star Printing
### **Star Printing Programs**
```python
def startPrint(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print()
n = 5
startPrint(n)

Output:-
* 
* * 
* * * 
* * * * 
* * * * *
```

```python
str1 = input("enter the string: ")
len = len(str1)
for i in range(len):
    for j in range(i+1):
        print(str1[i], end="")
    print()

Output:-
enter the string: Mohit
M
oo
hhh
iiii
ttttt
```

```python
str1 = input("enter the string: ")
len = len(str1)
for i in range(len):
    for j in range(i+1):
        print(str1[j], end="")
    print()

Output:-
enter the string: mohit
m
mo
moh
mohi
mohit
```
```python
rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
```

```python
for i in range(5):
  for j in range(0, 5-i):
    print("* ", end=" ")
  print()

Output:-
* * * * *
* * * *
* * *
* *
*
```
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