# List Methods
| Method    | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| append()  | Adds an element at the end of the list                                       |
| insert()  | Adds an element at the specified position                                    |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| copy()    | Returns a copy of the list                                                   |
| count()   | Returns the number of elements with the specified value                      |
| index()   | Returns the index of the first element with the specified value              |
| pop()     | Removes the element at the specified position                                |
| remove()  | Removes the item with the specified value                                    |
| clear()   | Removes all the elements from the list                                       |
| reverse() | Reverses the order of the list                                               |
| sort()    | Sorts the list                                                               |


* **append():-** Adds an element at the end of the list
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) 

Output:- ['apple', 'banana', 'cherry', 'orange']

# Example2:-
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

Output:- ['apple', 'banana', 'cherry', ["Ford", "BMW", "Volvo"]]
```
* **extend():-** Add the elements of a list (or any iterable), to the end of the current list
```python
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
                        
output:- ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
```
* **insert():-** Adds an element at the specified position
```python
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

Output:- ['apple', 'orange', 'banana', 'cherry']
```

* **copy():-**	Returns a copy of the list
```python
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

Output:- ['apple', 'banana', 'cherry']
```
* **count():-** Returns the number of elements with the specified value
```python
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

Output:- 2
```
* **index():-**	Returns the index of the first element with the specified value
```python
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)  # Output:- 3
```
* **pop():-** Removes the element at the specified position
* if you do not specify the index, the **pop()** method removes the last item.
```python                       
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)
print(fruits)
                        
output:- 
banana
['apple', 'cherry']
```
* **remove():-** Removes the item with the specified value
```python
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits) # Output:- ['apple', 'cherry']
```

* **clear():-**	Removes all the elements from the list
```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits) # Output:- []
```
* **reverse():-** Reverses the order of the list
```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output:- ['cherry', 'banana', 'apple']
```
* **sort():-**	Sorts the list
```python
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

Output:- ['BMW', 'Ford', 'Volvo']

# Parameter Values in sort()
 1. reverse:- optional. reverse=True will sort the list descending. Default is reverse=False
 2. key	Optional. A function to specify the sorting criteria(s)

Example:- 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

Output:- ['Volvo', 'Ford', 'BMW']

Example2:-
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

Output:- ['VW', 'BMW', 'Ford', 'Mitsubishi']
                        
Example3:- 
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
                        
Output:- ['Mitsubishi', 'Ford'', 'BMW', 'VW']
 
Example4:- 
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)

Output:- 
[{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
```