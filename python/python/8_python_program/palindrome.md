|  No.  | Palindrome                                                                          |
| :---: | ---------------------------------------------------------------------------------- |
|   1   | [To Check if a String is a Palindrome](#ques-to-check-if-a-string-is-a-palindrome) |
|   2   | [To Check if a Number is a Palindrome](#ques-to-check-if-a-number-is-a-palindrome) |

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