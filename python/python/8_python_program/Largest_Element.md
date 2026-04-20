### Find Largest Element in an Array/list?
- Using For Loop
```python
arra = [10, 324, 45, 90, 9808]

n = len(arra)
max = arra[0]
for i in range(1, n):
    if arra[i] > max:
        max = arra[i]
print(max)  # output:- 9808
```
- Using inbuild function
```python
print(max(arra))    # Output:- 9808
```

- Using sort function
```python
arra.sort()
print(arra[-1]) # Output:- 9808
```