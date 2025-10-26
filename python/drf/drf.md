### What is API?
* Api Stands for **Application programing interface**.
* It acts as a two way communication bridge between frontend and backend.


### ModelSerializer
* The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.

### when i want to all field requird
```python
from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'  # or specify the fields you want to include
```

### when i don't want to all field requird
```python
from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)  # Make name required

    class Meta:
        model = Students
        fields = ['name', 'other_field1', 'other_field2']  # Specify the fields you want to include
        # If you want to include all fields except for some, you can use:
        # exclude = ['field_to_exclude1', 'field_to_exclude2']


# example
from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)  # Make name required
    phone_no = serializers.CharField(required=True)  # Make phone_no required

    class Meta:
        model = Students
        fields = ['name', 'phone_no', 'roll_no', 'message', 'city']  # Include all fields
```