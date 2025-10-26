### validation only name
```python
# Create a Custom Validator in serializer.py file
def validate_todo_title(value):
    if not re.match("^[A-Za-z0-9 ]*$", value):  # Allow only alphanumeric characters and spaces
        raise serializers.ValidationError("Todo title must not contain special characters.")
    return value

# update code
class TodoSerializer(serializers.ModelSerializer):
    todo_title = serializers.CharField(validators=[validate_todo_title])  # Add the custom validator

    class Meta:
        model = Todo
        fields = '__all__'  # or use exclude=['uid'] if you want to exclude uid
```
