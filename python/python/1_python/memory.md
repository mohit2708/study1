### What is Object Interning in Python?
* "Object Interning is a **Python optimization technique** where immutable objects are reused instead of creating multiple copies, which saves memory and improves performance."
* Object Interning ek optimization technique hai jisme Python kuch objects ko memory me sirf ek baar store karta hai aur baar-baar wahi object reuse karta hai.
* Object Interning ek memory optimization technique hai jisme Python same immutable objects (jaise small integers aur kuch strings) ko memory me sirf ek baar store karta hai aur zarurat padne par usi object ko reuse karta hai.
* Python generally **-5 se 256** tak ke integers ko intern karke rakhta hai.
 
#### Advantage of Object Interning
* Memory bachti hai
* Comparisons fast hote hain
* Performance improve hoti hai

#### Example of Object Interning
```python
# Example 1: Small Integers Interning
a = 100
b = 100

print(a is b)

# Output:- True
```

```python
# Example 2: Large Integers
a = 1000           | a = int("1000")
b = 1000           | b = int("1000")
                   |
print(a is b)      | print(a is b)

# Output:- True    | # Output:- False

# Becuse Kyuki alag objects create hue hain.
```

```python
# Example 3: String Interning
a = "hello"
b = "hello"

print(a is b)

# Output:- True
```

### What is a Memory Leak in Python?
* Memory Leak ka matlab hai ki program ki memory use hone ke baad properly release nahi ho rahi, jiski wajah se application ka memory usage continuously badhta rehta hai.
* Python me **Garbage Collector (GC) automatically unused objects ko clean karta hai**, isliye memory leaks comparatively kam hote hain. Lekin Python me bhi memory leaks ho sakte hain.