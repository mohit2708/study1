### Difference between null=True and blank=True?
- null=True is **for the database** and blank=True is for **forms and validation**
- When working with Django models, you may come across two common field options: null=True and blank=True. 
- In Django model null=True and blank=True look similer but they save different purposes.

#### null=True
- Database lavel concept
- Allows the database column to store NULL
- Used when no value exists in the database
- If no value provided, the database stores NULL.
```python
age = models.IntegerField(null=True)
```

#### blank=True
- form-level / validation level concept
- Allows the field to be empty in form and admin
- Used during validation
```python
name = models.CharField(max_length=10, blank=True)
```

- **Notes:-**
  - Avoid null=True for CharField & TextField