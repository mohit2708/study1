### create serializers.py file in your app
```python
# include on top
from rest_framework import serializers # its compulsory
from api.models import Todo # add model
```
* show all fields
```Python
class TodoSerializer(serializers.ModelSerializer):   # create class any name(TodoSerializer) and call view
    class Meta:
        model = Todo
        fields ="__all__" 
```
* only show particular field
```python
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['todo_title', 'todo_description']
```
* exclude particular field
```python
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['uid', 'created_at', 'updated_at']
```