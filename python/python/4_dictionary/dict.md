### Dictionaries
* Dictionary items are **ordered**, **changeable**, and **does not allow duplicates**.
* Dictionaries are written with curly **brackets{}**, and have keys and values.
* Dictionaries are **changeable**, meaning that we can change, add or remove items after the dictionary has been created.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "electric": False,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'electric': False,'colors': ['red', 'white', 'blue']}
```

- **Length:-** use the **len()** function. - print(len(thisdict))


- **dict() Constructor:-** It is also possible to use the **dict()** constructor to **make a dictionary**.
```python
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
Output:- {'name': 'John', 'age': 36, 'country': 'Norway'}
```
- **Check if Key Exists:-**
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

Output:- Yes, 'model' is one of the keys in the thisdict dictionary
```


