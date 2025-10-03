### **Ques. Find Fibonacci series up to n**
```python
def fibonacci(n):
    first = 0
    second = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return second
    else:
        print(first)
        print(second)
        for i in range(2, n):
            third = first + second
            first = second
            second = third
            print(third)

fibonacci(9)

Output:- 0 1 1 2 3 5 8 13 21
```
* Using While Loop
```python
def fibonacci(n):
    first = 0
    second = 1
    count = 0
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return second
    else:
        while count < n:
            print(first)  
            third = first + second  
           # At last, we will update values  
            first = second  
            second = third  
            count += 1
fibonacci(9)
```