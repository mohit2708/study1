### What are Django Forms?
* Django Forms are a built-in framework for creating HTML forms, handling user input, validating submitted data, and processing or saving that data. Django provides Form for custom forms and ModelForm for forms based on database models.
* "Django Form is a class used to take user input, validate it, display errors, and process the data securely."
* **Example:** Login Form, Registration Form, Contact Form.


#### Why use Django Forms?
* Validation automatically (is_valid())
* Prevents invalid data
* Shows error messages
* Easier than manual form handling
* Helps protect against security issues

#### Example
```python
# Form.py file 

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
```


### What is is_valid()?
* Form ke data ko validate karta hai.
```python
if form.is_valid():
    print("Valid Data")
```
* Agar saare rules pass ho gaye to True return karega.