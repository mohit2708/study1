### Python Types Intro
* Python has support for optional "type hints" (also called "type annotations").

#### title() Method:
* Converts the first letter of each one to upper case with title().
```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("mohit", "saxena"))

Output:- Mohit Saxena
```