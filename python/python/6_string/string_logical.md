### **Ques. Looping Through a String?**
```python
for x in "Mohit":
  print(x) 

Output:-
M
o
h
i
t  
```

### **Ques. Extract numbers from string?**
```python
new_string = "Germany26China47Australia88"
 
emp_str = ""
for m in new_string:
    if m.isdigit():
        emp_str = emp_str + m
print("Find numbers from string:",emp_str)

Output:- Find numbers from string: 264788

# 2 Example
new_str = "Micheal 89 George 94"

emp_lis = []
for z in new_str.split():
   if z.isdigit():
      emp_lis.append(int(z))

print("Find number in string:",emp_lis)

Output:- Find number in string: [89, 94]
```
<div style="page-break-before: always;"></div>

### **Ques. Reversed the String?**
* Using **slice** method and through function
```python
txt = "Hello World"[::-1]
print(txt) # Output:- dlroW olleH

# Example 2:- Using Function
def my_function(x):
  return x[::-1]

mytxt = my_function("Hello World")
print(mytxt)    # Output:- dlroW olleH
```

* using **reversed()** function
```python
string = "Hello, World!"
print("".join(reversed(string)))

Output:- !dlroW ,olleH
```
 
* using for loop
```python
s = input("Enter a string: ")
reversed_str = ""

for char in s:
    reversed_str = char + reversed_str
print(reversed_str)  # Output: "olleh"
```

### **Reversed word in string?**
```python
str = input("enter the string: ") # sky is blue
split = str.split()
split = split[::-1]
finalstr = " ".join(split)
print(finalstr) # Output:- Output:- blue is sky
```

### **Check for Palindrome**
```python
s = "madam"
reversed_str = ""
# Reverse the string using a loop
for char in s:
    reversed_str = char + reversed_str
# Check if the original string is equal to the reversed string
if s == reversed_str:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
    
# Output:- 'madam' is a palindrome.
```

<div style="page-break-before: always;"></div>

### **Ques. Remove vowels from a string?**
```python
string = 'Hello mohit saxena'
vowels = ('a','e','i','o','u')
new_string = ''
for ele in string:
    if ele not in vowels:
        new_string = new_string + ele
print(new_string)

# Using comprehension
print(''.join([c for c in string if c not in vowels]))

Output:- Hll mht sxn
```



### **Ques. Find repeated characters in a string python?**
```python
string = "Great responsibility";  
  
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            string = string[:j] + '0' + string[j+1:];  
 
    if(count > 1 and string[i] != '0'):  
        print(string[i]);

output:- r
e
t
s
i
```
<div style="page-break-before: always;"></div>

### **Ques. Count the frequency of each character?**
```python
# using "in" operater
str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)

Output:- 
Enter the string: HheLlo
{'H': 1, 'h': 1, 'e': 1, 'L': 1, 'l': 1, 'o': 1}
Enter the string: Hello My name is Mohit Saxena
{'H': 1, 'e': 3, 'l': 2, 'o': 2, ' ': 5, 'M': 2, 'y': 1, 'n': 2, 'a': 3, 'm': 1, 'i': 2, 's': 1, 'h': 1, 't': 1, 'S': 1, 'x': 1}
----------------------------------------------------------------------------

# Use of “get()” function

```

### **Count Vowels and Consonants?**
```python
s = "Hello World"

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in s:
    if char.isalpha():  # Check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
```

### **Remove duplicate characters from a string**
```python
s = "programming"

unique_chars = ""
for char in s:
    if char not in unique_chars:
        unique_chars += char

print(unique_chars)  # Output: "progamin"
```