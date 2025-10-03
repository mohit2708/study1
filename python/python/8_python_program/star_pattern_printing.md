### **Star Printing Programs**
```python
def startPrint(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print()
n = 5
startPrint(n)

Output:-
* 
* * 
* * * 
* * * * 
* * * * *
```

```python
for i in range(5):
  for j in range(0, 5-i):
    print("* ", end=" ")
  print()

Output:-
* * * * *
* * * *
* * *
* *
*
```

```python
str1 = input("enter the string: ")
len = len(str1)
for i in range(len):
    for j in range(i+1):
        print(str1[i], end="")
    print()

Output:-
enter the string: Mohit
M
oo
hhh
iiii
ttttt
```

```python
str1 = input("enter the string: ")
len = len(str1)
for i in range(len):
    for j in range(i+1):
        print(str1[j], end="")
    print()

Output:-
enter the string: mohit
m
mo
moh
mohi
mohit
```
```python
rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
```

