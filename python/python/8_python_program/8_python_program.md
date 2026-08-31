|  No.  | even or odd program                                                              |
| :---: | -------------------------------------------------------------------------------- |
|   1   | [Print Hello World](#ques-print-hello-world)                                     |
|   2   | [Swap Two variables](#swap-two-variables)                                        |
|   3   | [Even or odd:- check number](#ques-program-to-check-if-a-number-is-even-or-odd)  |
|   4   | [Even or odd:- without any condition?](#check-even-or-odd-without-any-condition) |
|   5   | [Even or odd:- Print number](#print-the-even-number-and-odd-number)              |
|   6   | [Prime Number:- Check Number?](#ques-check-prime-number-or-not)                  |
|   7   | [Prime Number:- Print Number?](#ques-prime-number-print-between-lower-to-upper)  |
|   8   | [Reverse:- string?](#reverse-string)                                             |
|   9   | [Reverse:- reverse a word sentence?](#how-to-reverse-a-word-sentence)            |
|  10   | [Reverse:- Number?](#reverse-a-number)                                           |
|       | [Armstrong number or not](#ques-check-number-is-an-armstrong-number-or-not)      |


<div style="page-break-before: always;"></div>

### Ques. Print Hello World?
```python
print('Hello World!!!')

Output:- Hello World!!!
```
<div style="page-break-before: always;"></div>

### Swap Two variables
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

# 2 option using function
def evenOrOdd(n):
    if n%2 == 0:
        print('even Number hai')
    else:
        print('Odd Number hai')
evenOrOdd(6)
```

### **Check even or odd without any condition?**
```python
# Type 1
number = 61
result = ["even", "odd"]
print(result[number%2])

# Type 2
def check_even_odd(n):
    return ("Even" * (n & 1 == 0)) or ("Odd")
    # return ("Even" * (n %2==0)) or ("Odd")

# Test the function
number = 5
result = check_even_odd(number)
print(f"The number {number} is {result}.")  # Output:- The number 5 is Odd.
```
<div style="page-break-before: always;"></div>

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

# Output:- 3 is a prime number
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

### **Reverse string?**

- **Using for loop**
```python
string = 'mohit'
blank =''
for i in string:
    blank = i + blank
print(blank)    # Output:- tihom
```

- **Using while loop**
```python
str = "mohit"
reverse_String = ""
count = len(str)
while count > 0:
    reverse_String += str[ count - 1 ]
    count = count - 1
print (reverse_String) # Output:- tihom
```

- Using the slice ([]) operator
```python
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "mohit"  
print ("The original string  is : ",s)   
print (reverse(s))  # Output:- tihom
```

- Using reversed function with join
```python
def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string

s = "mohit"  
  
print ("The original string is : ",s)   
print (reverse(s) ) # Output:- tihom
```
<div style="page-break-before: always;"></div>

### **How to reverse a word sentence?**
* using reversed() function
```python
inputsentence = input("Please input  a sentence : ")
splitString = inputsentence.split()      # ['i', 'love', 'Mohit', 'Saxena']
reversedString = reversed(splitString)
print(" ".join(reversedString))

# Output:- i love Mohit Saxena
# Saxena Mohit love i
```

* using split
```python
str = "sky is blue"
str_split = str.split()
new_str = str_split[::-1]
str =" ".join(new_str)
print(str)  # Output:- blue is sky
```

- option **using** for **loop**

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

### **Reverse a Number**

- using a **while loop**
```python
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10 # Get the last digit
    Reverse = (Reverse *10) + Reminder  # Append it to the result
    Number = Number //10    # Remove the last digit from original

print("Reverse of entered number is = %d" %Reverse)

# Output:-
Please Enter any Number: 68765
Reverse of entered number is = 56786
```

- Using String **slicing**
```python
num = 9412
reversed_num = int(str(num)[::-1])
print(reversed_num)  # Output: 2149
```

- using append
```python
num = 54321
digit_array = []

for digit in str(num):
    digit_array.append(int(digit))

print(digit_array)  # Output: [5, 4, 3, 2, 1]
```
<div style="page-break-before: always;"></div>

- Using Recursion
```python
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

# Output:- 
Enter the number: 1284
Reverse of entered number is = 4821
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

### **Two given words are anagrams**
* An anagram means both words contain the same characters with the same frequency, but possibly in a different order.
* Example
```python
hello
oellh
```
```python
def anagram(str1, str2):

    # First checks if both words have the same length.
    if len(str1) != len(str2):
        return False

    # Then for each character, checks whether it appears the same number of times in both words.
    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            return False

    return True


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if anagram(word1, word2):
    print("Anagrams")
else:
    print("Not Anagrams")
```

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