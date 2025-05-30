### logout
```python
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')
```

```python
def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/accountshtml')
```