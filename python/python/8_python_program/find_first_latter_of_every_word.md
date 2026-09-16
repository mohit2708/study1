### **Find the first latter of the Word?**
```python
# .strip() लगाने से वह आखिरी का एक्स्ट्रा स्पेस हट जाता है और रिजल्ट सिर्फ "M S" बचता है।
name = "Mohit Saxena"
words = name.split()

firstw = ""
for word in words:
    firstw += word[0]+" "

firstw = firstw.strip()  # Remove the trailing space
print(firstw)   # Output:- M S

# ----------OR----------
name = "Mohit Saxena"
words = name.split()

firstw = ""
for word in words:
    firstw += word[0]
print(' '.join(list(firstw))) # Output:- M S
```