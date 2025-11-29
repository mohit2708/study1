###  Loop Tuples
* Loop Through a Tuple 
```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
Output:- 
apple
banana
cherry
```
* Loop Through the Index Numbers
```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
Output:-
apple
banana
cherry
```
*  Using a While Loop
```python
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
Output:- 
apple
banana
cherry
```