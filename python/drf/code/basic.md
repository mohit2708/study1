### home view
```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def getHome(request):
    if request.method == 'GET':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working!!!',
            'method_called': 'You called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working!!!',
            'method_called': 'You called POST method'
        })
    elif request.method == 'PATCH':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working!!!',
            'method_called': 'You called PATCH method'
        })
    elif request.method == 'PUT':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working!!!',
            'method_called': 'You called PUT method'
        })
    elif request.method == 'DELETE':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working!!!',
            'method_called': 'You called DELETE method'
        })
    else:
        return Response({
            'status' : 400,
            'message': 'Yes! Django rest framework is working!!!',
            'method_called': 'You called invalid method'
        })
```

### create serializers.py file in your app
```python
from rest_framework import serializers

```