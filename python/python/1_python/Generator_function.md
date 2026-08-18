### **Ques. What is Generator Functions?**
* Generator Function is a function which returns values ​​one by one and saves memory.
* Normal function uses **return**, while generator function uses **yield**.
* The **difference** between **yield** and **return** is that yield **returns a value and pauses the execution** while maintaining the internal states, whereas the **return statement returns a value and terminates the execution** of the function.
* Generator function is a function which gives the next value when called repeatedly and saves memory.
* Generator are functions that returns a sequens of value. we use **yield** statement to return the from function.
* Yield statement returns the element from a generator function into a genrater object.(EX:- yield a)
* This function is used to retrieve element by element from a generator object.(Ex:- next(gen_obj))
* A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values.
* In a generator function, a __yield__ statement is used rather than a return statement.
* The generator function cannot include the return keyword. If you include it, then it will terminate the function. 
* A generator is a Python function that produces values one at a time using the yield keyword. Unlike a normal function that returns all results at once, a generator pauses its execution after yielding a value and resumes from the same point when the next value is requested. This makes generators memory-efficient and suitable for processing large datasets.


#### Features of Generator Function:
* Uses the yield keyword.
* Memory efficient → does not keep the entire list in memory.(Memory efficient होता है → पूरी list memory में नहीं रखता।)
* Can generate infinite series (infinite values).(Infinite series (अनंत values) generate कर सकता है।)
* Can be easily used with iteration (loop).(Iteration (loop) के साथ आसानी से इस्तेमाल किया जा सकता है।)

#### Example
```python
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))    # Output:- 1
print(next(gen))    # Output:- 2
print(next(gen))    # Output:- 3
```

#### yield kya hota hai?
* It returns a yield value but does not completely terminate the function.(yield value return karta hai but function ko completely terminate nahi karta.)
```python
def test():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")
    yield 30

g = test()

print(next(g))
print(next(g))
print(next(g))

# Output:-
Start
10
Middle
20
End
30
```

#### return vs yield
* return terminates the function and returns a result, whereas yield pauses the function and produces a value while preserving its execution state so that it can resume later.
| `return`                                 | `yield`                               |
| ---------------------------------------- | ------------------------------------- |
| Function ko terminate karta hai          | Function ko pause karta hai           |
| Usually complete result return karta hai | One value at a time produce karta hai |
| Function execution end ho jata hai       | Execution state preserve hoti hai     |
| Large data ke liye less memory-efficient | Large data ke liye memory-efficient   |
| Normal function                          | Generator function                    |

#### How do you create a generator?
* There are mainly two ways to create a generator.
1. Method 1: Generator Function:- yield use karke:
```python
def count():
    for i in range(5):
        yield i

for value in count():
    print(value)

# Output:-
0
1
2
3
4
```

2. Method 2: **Generator Expression**:- List comprehension jaisa syntax hota hai.
```python
# List comprehension
numbers = [x * x for x in range(5)]     # Output:- [0, 1, 4, 9, 16]

# Generator expression
numbers = (x * x for x in range(5)) # Ye generator object create karega.

# Output:-
print(numbers) # <generator object <genexpr> at 0x...>
print(next(numbers))    # Outpout:- 0
print(next(numbers))    # Outpout:- 1
```
```python
[] → List
() → Generator expression
```
--- 

#### next() kya karta hai?
* next() generator se next available value leta hai.
```python
def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()

print(next(g))  # Output:- 10
print(next(g))  # Output:- 20
print(next(g))  # Output:- 30
print(next(g))  # Output:- will raise error: StopIteration
```

#### Generator with for loop
* Usually generators ke saath manually next() use nahi karte.
* for loop internally next() call karta hai until StopIteration.
```python
def numbers():
    for i in range(5):
        yield i

for num in numbers():
    print(num)

# Output:-
0
1
2
3
4


def squares(n):
    for i in range(1, n+1):
        yield i * i

for value in squares(5):
    print(value)

# Output:-
1
4
9
16
25
```

#### Generator Memory Efficient kyun hai?
* Interview:- Generators don't store all generated values in memory. They generate each value only when requested, using lazy evaluation.
* Suppose humein 10 million numbers process karne hain.
  
```python
# List
numbers = [x for x in range(10_000_000)]
# Ye approximately 10 million values ko memory mein store karega.
```

```python
# Generator
numbers = (x for x in range(10_000_000))
# Generator ek time par required value produce karta hai.

# Conceptually:
Request value
     ↓
Generate value
     ↓
Process value
     ↓
Generate next value
     ↓
Process value
# Isliye memory usage significantly lower ho sakta hai.
```

#### Generator Function vs Normal Function
* Normal function
```python
# Example 1
def square(n):
    return n * n

result = square(5)  # Output:- 25

# Example 2
def normal_func():
    return [1, 2, 3, 4, 5]

# This will return the entire list at once.
print(normal_func())    # Output:- [1, 2, 3, 4, 5]
```

* Generator function
```python
def generator_func():
    for i in range(1, 6):
        yield i   # return नहीं, yield

# 👉 यहाँ yield हर बार next() call करने पर अगली value return करेगा।
gen = generator_func()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

#### Generator Pipeline
* Generators ko chain bhi kar sakte hain.
```python
def numbers():
    for i in range(10):
        yield i


def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


for num in even_numbers(numbers()):
    print(num)


# Output:-
0
2
4
6
8
# Ye lazy processing pipeline ka example hai.
```

#### Generator vs Iterator
* for interview:- A generator is a special type of iterator created using a generator function or generator expression.
* Iterator
  * Iterator ek object hai jo __iter__() aur __next__() methods provide karta hai.
```python
numbers = iter([1, 2, 3])

print(next(numbers))
```
* Generator
  * Generator ek easy way hai iterator create karne ka.
```python
def numbers():
    yield 1
    yield 2
    yield 3
```
* Every generator is an iterator, but every iterator is not a generator.

#### List vs Generator
| Feature    | List          | Generator                  |
| ---------- | ------------- | -------------------------- |
| Evaluation | Eager         | Lazy                       |
| Memory     | More          | Less                       |
| Values     | All at once   | One at a time              |
| Reusable   | Yes           | Usually one-time iteration |
| `len()`    | Yes           | No directly                |
| Indexing   | Yes           | No                         |
| Large data | Less suitable | Very suitable              |
| Creation   | `[]`          | `yield` / `()`             |


#### Can Generator be reused?
* NO
```python
def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

for x in g:
    print(x)

for x in g:
    print(x)

# Output first loop
1
2
3

# Output second loop
nothing # Because generator is already exhausted.
```

#### yield with return
* Generator function mein return bhi use kar sakte hain.
* return ke baad generator stop ho jayega.
```python
def test():
    yield 1
    yield 2
    return
```
* You can also return a value:
```python
def test():
    yield 1
    yield 2
    return "Done"
```

#### Q4. Is a generator an iterator?
* Yes. A generator is a special type of iterator. It implements the iterator protocol and provides __next__() behavior automatically.

#### Q5. Is every iterator a generator?
* No. Every generator is an iterator, but every iterator is not a generator.

#### Q7. What is lazy evaluation?
* Lazy evaluation means values are calculated only when they are requested rather than calculating everything upfront.
  

#### Real-world Example:
1. Large File
* Suppose ek file mein 10 GB data hai.
```python
with open("large_file.txt") as file:
    data = file.readlines()

# use karte hain, to bahut saari lines memory mein load ho sakti hain.

# Generator approach:
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

for line in read_file("large_file.txt"):
    print(line) # Yahan file ki lines ko one-by-one process kiya ja sakta hai.
```


* Generator with Loop
```python
def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = mygenerator()
print(next(gen))
print(gen.__next__())  # 2 option to write the next function
print(next(gen))
print(next(gen))

Output:- 
First item
10
Second item
20
Last item
30
Traceback (most recent call last):
File "<string>", line 22, in <module>
StopIteration

---------------------------------------------------------
# 2nd Option
gen = mygenerator()
while True:
    try:
        print ("Received on next(): ", next(gen))
    except StopIteration:
        break
Output:-
First item
Received on next():  10
Second item
Received on next():  20
Last item
Received on next():  30

# Example 2:-
def bhai(a,b):
    yield a+b
    yield a-b
result = bhai(3,2)
print(next(result))
print(next(result))

Output:- 
5
1

# Example 3:-
def numberPrint():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1
values = numberPrint()
for i in values:
    print(i)

Output:-
1
4
9
16
25
36
49
64
81
100
```
