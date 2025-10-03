### **Ques. Strings Method OR Change/Modify String?**
```python
# capitalize(): Converts the first character of the string to uppercase and the rest to lowercase.
txt = "hello, world!"
a = txt.capitalize()
print(a)   # Output:- Hello word!

txt = "30 is my age."
x = txt.capitalize()
print (x)   # 30 is my age

# count(sub): Returns the number of occurrences of a substring in the string.
text = "hello world"
print(text.count("o"))  # Output: 2

# **Upper Case:-** it method returns the string in upper case:
a = "Hello, World!"
print(a.upper())    # Output:- HELLO, WORLD!

# **lower():** Converts all characters in the string to lowercase.
a = "Hello, World!"
print(a.lower())    # Output:- hello, world!

# title(): Converts the first character of each word to uppercase and the rest to lowercase.
text = "hello world"
print(text.title())  # Output: "Hello World"


# The **replace()** method replaces a string with another string.
print(a.replace("H", "J"))  # Output:- Jello, World!

# **strip() method**:- The strip() method **removes** any **whitespace** from the **beginning or** the **end**.
b = "      Hello, World!     "
print(b.strip())    # Output:- "Hello, World!"

# lstrip
b = "      Hello, World!     "
print(b.lstrip())    # Output:- "Hello  "

# rstrip
b = "      Hello, World!     "
print(b.rstrip())    # Output:- "    Hello"

# The **split()** method splits the string into substrings if it finds instances of the separator
b = a.split(",")    # Output:- ['Hello', ' World!']
```
<div style="page-break-before: always;"></div>

```python
# **join(iterable):** Joins elements of an iterable (like a list) into a single string with a specified separator.
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

# startswith(prefix): Returns True if the string starts with the specified prefix, otherwise False.
# it is case sensitive
text = "hello world"
print(text.startswith("hello"))  # Output: True

# endswith(suffix): Returns True if the string ends with the specified suffix, otherwise False.
# it is case sensitive
text = "hello world"
print(text.endswith("world"))  # Output: True

# isalpha(): Returns True if all characters in the string are alphabetic and there is at least one character, otherwise False.
text = "hello"
print(text.isalpha())  # Output: True

# isdigit(): Returns True if all characters in the string are digits and there is at least one character, otherwise False.
text = "12345"
print(text.isdigit())  # Output: True

# isalnum(): Returns True if all characters in the string are alphanumeric (either letters or numbers) and there is at least one character, otherwise False.
text = "hello123"
print(text.isalnum())  # Output: True
```
<div style="page-break-before: always;"></div>

### **Ques. When would you use rfind()?**
* **rfind()** is like find() but it starts **searching from the right** of a string and return the first matching substring.
```python
story = 'The price is right said Bob. The price is right.'
story.rfind('is')   # Output:- 39
```