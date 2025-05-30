### model.py
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    # Add other fields as needed
        
    class Meta:
        db_table = 'auth_user'
```

### html file
```python
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
</head>
<body>
    <h1>Sign Up</h1>
    <form method="post">
        {% csrf_token %}
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name">
        {% if error.first_name %}
            <p style="color: red;">{{ error.first_name }}</p>
        {% endif %}
        <br>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        {% if error.username %}
            <p style="color: red;">{{ error.username }}</p>
        {% endif %}
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="password1">Password:</label>
        <input type="password" id="password1" name="password1" required>
        <br>
        <label for="password2">Confirm Password:</label>
        <input type="password" id="password2" name="password2" required>
        {% if error.password %}
            <p style="color: red;">{{ error.password }}</p>
        {% endif %}
        <br>
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required>
        <br>
        <label for="gender">Gender:</label>
        <input type="text" id="gender" name="gender" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>
        <br>
        <input type="submit" value="Sign Up">
    </form>
</body>
</html>
```

### view.py
```python
from accountsFunctionBased.models import User
from django.contrib.auth import authenticate, login

def sign_up(request):
    if request.method == 'POST':
        # Get the data from the form
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']

        error = {}

        # Basic form validation (you can add more validation as needed)
        if password1 != password2:
            error['password'] = 'Passwords do not match'
        elif User.objects.filter(username=username).exists():
            error['username'] = 'Username already exists'
        else:
            # Create a new user
            user = User.objects.create_user(
                first_name=first_name,
                username=username,
                email=email,
                password=password1
            )

            # Noraml save data without modification
            
            # user = User.objects.create_user(username=username, email=email, password=password1)
            # user.save()

            # Save the extra fields (age, gender, phone) in the user object
            user.age = age
            # user.gender = gender
            # user.phone = phone

            user.save()

            

            # Log the user in after successful sign-up
            user = authenticate(username=username, password=password1)
            login(request, user)

            return redirect('signup')  # Create a new view for signup success

        return render(request, 'accounts/signup.html', {'error': error})

    else:
        return render(request, 'accounts/signup.html')
```