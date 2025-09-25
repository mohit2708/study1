### **Ques. Slicing Strings?**
* We can return a range of characters by using the slice syntax.
* Specify the start index and the end index, separated by a colon, to return a part of the string.
```python
b = "Hello, World!" 

print(b[2:5])   # Output:- llo  -- Slice from the start position and end position
print(b[:5])    # Output:- Hello  -- Slice From the Start: Get the characters from the start to position (5 not included)
print(b[2:])    # Output:- llo, World! -- Slice To the End: Get the characters from position 2, and all the way to the end.
print(b[-5:-2]) # Output:- orl -- Negative Indexing: Get the characters from position 2, and all the way to the end.
print(b[:-1])   # Output:- Hello, World
```