### **Here are some effective ways to debug a Python project**
#### Print Statements
```python
def my_function(a, b):
    print(f"a: {a}, b: {b}")  # Debugging line
    return a + b
```

#### Use a Debugger
* Python's built-in pdb (Python Debugger) allows you to step through the code, inspect variables, and control the flow of execution interactively.
```python
import pdb
def my_function(a, b):
    pdb.set_trace()  # Execution will stop here
    return a + b
```
```python
python -m pdb my_script.py
```

#### Debugging in PyCharm:
* Set a breakpoint by clicking in the gutter next to a line number.
* Click the debug icon or press Shift + F9.
* Use the "Step Into", "Step Over", and "Continue" options to navigate through your code.

#### Debugging in VSCode:
* Set breakpoints by clicking the left margin of the code editor.
* Press F5 or click on the "Run and Debug" button.
* You can inspect variables in the "Debug" panel and interact with the code.

#### Use Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG)

def my_function(a, b):
    logging.debug(f"a: {a}, b: {b}")
    return a + b
```