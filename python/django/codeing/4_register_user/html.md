### HTML Templates
- **Create folder:** your_app/templates/
- signup.html
```python
<h2>Signup</h2>

<form method="POST">
    {% csrf_token %}
    First Name: <input type="text" name="first_name"><br>
    Last Name: <input type="text" name="last_name"><br>
    Username: <input type="text" name="user_name"><br>
    Email: <input type="email" name="email"><br>
    Password: <input type="password" name="password"><br>
    <button type="submit">Signup</button>
</form>

<a href="/login/">Login</a>

{% for message in messages %}
<p style="color:red;">{{ message }}</p>
{% endfor %}

```