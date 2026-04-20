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