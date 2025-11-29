### Login Functinality
#### View file
```python
def login_view(request):
    
    # Handal If user already logged in → redirect to home
    if request.session.get('customer_id'):
        return redirect("dashboard")
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(email=email)

            if check_password(password, customer.password):
                # request.session['customer_id'] = customer.id
                request.session['customer_id'] = str(customer.id)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid password")
        except Customer.DoesNotExist:
            messages.error(request, "Email not found")

    return render(request, "auth/login.html")
```

#### Html file
```python
<!DOCTYPE html>
<html>
<body>
    <h2>Login</h2>

    <form method="POST">
        {% csrf_token %}
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="password" name="password" placeholder="Password" required><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
```
#### urls
```python
from car_app.views import auth_view, dashboard_views

path("login/", auth_view.login_view, name="login"),
```