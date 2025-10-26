### Get data from the database
```python
# Create model file
from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)

    # its means show the data title name in django admin
    def __str__(self):
        return self.todo_title


# create serializers.py file in our app
from rest_framework import serializers
from students.models import Students
from api.models import Todo

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields ="__all__" 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' # all fields
        # exclude = ['uid'] # exclude field 
        fields = ['todo_title'] # only show particular field

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome),
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailsView),
    path('post-todo',views.postTodo, name="post_todo"),
    path('get-todo',views.getTodo, name="get_todo")
]


# view file
from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students
from api.models import Todo
from api.serializers import StudentSerializer, TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def postTodo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()  # Save the serializer to create the Todo instance
            return Response({
                'status': True,
                'message': 'Todo created successfully!',
                'data': serializer.data  # Optionally return the created data
            }, status=status.HTTP_201_CREATED)  # Return 201 Created status
        
        return Response({
            'status': False,
            'message': 'Validation error!',
            'errors': serializer.errors  # Return the validation errors
        }, status=status.HTTP_400_BAD_REQUEST)  # Return 400 Bad Request status

    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'An error occurred while creating the Todo.',
            'error': str(e)  # Optionally return the error message
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return 500 Internal Server Error status
```