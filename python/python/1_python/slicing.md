### **What is slicing in Python?**
* Slicing is a technique used to **extract a portion("hissa" ya "part") of a sequence** (such as a string, list, or tuple) using the syntax sequence[start:stop:step].
  * **start** → Starting index (inclusive)
  * **stop** → Ending index (exclusive)
  * **step** → Increment/decrement value

#### Example
```python
text = "Python"

print(text[0:3]) # Output:- Pyt
print(text[:3])  # Output:-	Pyt
print(text[2:])	 # Output:- thon
print(text[:])	 # Output:- Python
print(text[::2]) # Output:- Pto
print(text[::-1])# Output:- nohtyP  # Reverse a String
```

```python
# String Slicing
name = "Mohit"
print(name[0:3]) # Output:- Moh

# List Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # Output:- [20, 30, 40]
```