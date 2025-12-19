### **Ques. What is Python JSON?**
* JSON **JavaScript Object Notation** is a format for structuring data.
* JSON is a lightweight data-interchange format that's easy for humans to read and write, and easy for machines to parse and generate.
* It is mainly used for storing and transferring data between the browser and the server.
* Python has a built-in package called json, which can be used to work with JSON data.
* It's commonly used for:
  * Web APIs
  * Configuration files
  * Data exchange between applications
* Convert Python objects to JSON (serialization)
* Convert JSON to Python objects (deserialization)

#### JSON Common function:-
| Function     | Description                          |
| ------------ | ------------------------------------ |
| json.dumps() | Convert Python object to JSON string |
| json.dump()  | Write JSON to a file                 |
| json.loads() | Convert JSON string to Python object |
| json.load()  | Read JSON from a file                |

### Examples:-
1. **json.dumps()** – Serialize **Python object** to a **JSON string**
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

2. **json.dump()** – Serialize **Python object** and write directly to a **file**
```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "is_member": True
}

# Write JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file)
```

3. **json.loads()** – Parse a **JSON string** into a **Python object**
```python
import json

# JSON string
json_string = '{"name": "mohit", "age": 30, "is_member": true}'

# Convert JSON string to Python dict
data = json.loads(json_string)

print(data) # Output:- {'name': 'mohit', 'age': 30, 'is_member': True}
print(data["name"])  # Accessing a value mohit
```

4. json.load() – Read JSON from a file and parse it into a Python object
```python
import json

# Assume 'data.json' contains: {"name": "Alice", "age": 30, "is_member": true}

# Open and load JSON from file
with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["age"])  # Accessing a value
```

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

### find question from the gpt
```
Basic Python JSON Interview Questions

What is JSON? How is it different from a Python dictionary?

What are the key functions in Python’s json module?

What's the difference between json.dump() and json.dumps()?

How do you convert a JSON string into a Python object?

How do you write a Python dictionary to a JSON file?

How do you read JSON data from a file into a Python object?

Can you store non-string keys in a JSON object? Why or why not?

🔹 Practical / Coding Questions

Convert the following Python dictionary to a JSON string:

data = {'name': 'Bob', 'age': 25, 'active': True}


Given a JSON string, extract a specific field:

json_str = '{"user": {"id": 1, "name": "John"}}'
# Extract the user's name


How do you pretty-print a JSON string with indentation?

Write a program to read a JSON file and count how many users are in it.

Given a JSON string with nested data, access a deeply nested value.

🔹 Intermediate to Advanced Questions

What happens if the JSON string is invalid when you call json.loads()? How do you handle it?

Can you serialize a Python datetime object with the json module? Why or why not? How do you handle it?

How can you customize JSON encoding for a Python object (e.g., a class instance)?

What is the difference between json.load() and pickle.load()? When would you use each?

How do you ensure Unicode characters (like emojis or non-English letters) are properly encoded in JSON?

What are some common pitfalls when working with JSON in Python?

🔹 Bonus / Conceptual

Is JSON a secure format? What are the risks (e.g., with eval())?

What is the MIME type of JSON data when sending it in an HTTP request?

(Answer: application/json)
```