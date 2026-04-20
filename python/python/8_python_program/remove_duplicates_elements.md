### Find the Duplicate list and Unique list
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