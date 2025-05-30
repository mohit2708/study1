```python
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')
```

```python
def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        # cheching for valid login
        if user is not None:
            dj_login(request, user)
            messages.success(request, " Successfully logged in")
            return redirect("/accountshtml")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("/accountshtml")
    return HttpResponse('404 - NOT FOUND ')
```