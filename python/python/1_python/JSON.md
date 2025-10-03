### **Ques. What is Python JSON?**
* JSON **JavaScript Object Notation** is a format for structuring data. It is mainly used for storing and transferring data between the browser and the server.
* Python has a built-in package called json, which can be used to work with JSON data.
 
* **Convert JSON to Python:-** If you have a JSON string, you can parse it by using the **json.loads()** method.
 
```python
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
 
Output:- 30
```
* **Convert Python to JSON:-** If you have a Python object, you can convert it into a JSON string by using the **json.dumps()** method.
```python
 import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

Output:- {"name": "John", "age": 30, "city": "New York"}
```
* Format the Result:- Use the **indent** parameter to define the numbers of indents:
```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

Output:-
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
```
* Use the **sort_keys** parameter to specify if the result should be sorted or not:
```python
print(json.dumps(x, indent=4, sort_keys=True))

Output:-
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}
```