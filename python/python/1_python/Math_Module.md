### **Math Module**
* Python has a built-in module that you can use for mathematical tasks.

### Math Methods
* **Arithmetic operations:** math.ceil(), math.floor(), math.fabs(), math.fmod(), math.pow(), math.sqrt(), math.trunc().
* **Trigonometric functions:** math.sin(), math.cos(), math.tan(), math.asin(), math.acos(), math.atan(), math.atan2(), math.hypot().
* **Logarithmic and exponential functions:** math.exp(), math.log(), math.log10(), math.log2().
* **Angular conversion:** math.degrees(), math.radians().
* **Constants:** math.pi, math.e, math.tau, math.inf, math.nan.

### Example
```python
result = math.sqrt(25)  # Calculates the square root of 25
print(result)  # Output: 5.0
```

### **Ques. floor() and ceil() Functions?**
### math.floor() Method
* The math.floor() method rounds a number DOWN to the nearest integer, if necessary, and returns the result.
```python
#Import math library
import math

# Round numbers down to the nearest integer
print(math.floor(0.6))          # 0
print(math.floor(1.4))          # 1
print(math.floor(5.3))          # 5
print(math.floor(-5.3))         # -6
print(math.floor(22.6))         # 22
print(math.floor(10.0))         # 10
```

### math.ceil() Method
* The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.
```python
#Import math library
import math

#Round a number upward to its nearest integer
print(math.ceil(1.4))           # 2
print(math.ceil(5.3))           # 6
print(math.ceil(-5.3))          # -5
print(math.ceil(22.6))          # 23
print(math.ceil(10.0))          # 10
```