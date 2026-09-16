### **find the length/Count number of characters in a string**
* To get the length of a string, use the **len()** function.
```python
a = "Hello, World!"
print(len(a))   

Output:- 13
```

* Without function
```python
na = input("Enter a string: ")
a = 0
for i in na:
    if i!=" ":
        a = a+1
print(a)

Output:-
Enter a string: mohit saxena
11
```

```python
string = "My Name is Mohit Saxena";
count = 0;

for i in range(0, len(string)):
    if(string[i] != ' '):
        count = count + 1;
print("Total number of characters in a string: " + str(count));     # Output:- 19
```