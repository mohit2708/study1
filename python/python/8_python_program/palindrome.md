|  No.  | Palindrome Program                                                                 |
| :---: | ---------------------------------------------------------------------------------- |
|   1   | [To Check if a String is a Palindrome](#ques-to-check-if-a-string-is-a-palindrome) |
|   2   | [To Check if a Number is a Palindrome](#ques-to-check-if-a-number-is-a-palindrome) |

### **To Check if a String is a Palindrome**
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
isPalindrome(s) # Output:- The string is a palindrome!
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

### **To Check if a Number is a Palindrome**
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

### **To Check if a List is a Palindrome**
* A palindrome list is a list that reads the same from left to right and right to left.
* [1, 2, 3, 2, 1]  # Palindrome
* [1, 2, 3, 4, 5]  # Not Palindrome
```python
# Simple approach using slicing
def is_palindrome(lst):
    return lst == lst[::-1]

numbers = [1, 2, 3, 2, 1]

if is_palindrome(numbers):
    print("Palindrome")
else:
    print("Not Palindrome")

# ==Without using slicing:
def is_palindrome(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] != lst[right]:
            return False

        left += 1
        right -= 1

    return True
```