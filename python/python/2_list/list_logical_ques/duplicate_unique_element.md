### **Find the duplicate element from list?**
```python
list = [9,3,6,4,7,3,1,4]
duplicate = []
for i in list:
    if list.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
   
print(duplicate)    # Output:- [3,4]
```

```python
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

Output:- 2 3 4 5
```

### Find the Unique element from the list?
### Remove the duplicate element from the list?
* Method 1: Using set()
```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(unique_numbers) # Output:- [1, 2, 3, 4, 5]
```

* Method 2: Preserve Original Order
```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)
```

* Method 3: Find Element Appearing Only Once
```python
numbers = [1, 2, 2, 3, 4, 4, 5]

for num in numbers:
    if numbers.count(num) == 1:
        print(num)

# Output:- 1 3 5
```

### **Find the Duplicate list and Unique list?**
- Using a for Loop
```python
mylist = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
duplicate_list = []

for x in mylist:
    if x not in unique_list:
        unique_list.append(x)
    else:
        duplicate_list.append(x)

print(unique_list)  # Output: [1, 2, 3, 4, 5]
print(duplicate_list) # Output: [2, 4]
```

- Using set
```python
mylist = ["a", "b", "a", "c", "c"]
unique_list = list(set(mylist))
print(unique_list)  # Output order may vary: ['b', 'c', 'a']
```