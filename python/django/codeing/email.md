### **setting.py**
```python
# Add this code
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'janicahanover@gmail.com'
EMAIL_HOST_PASSWORD = 'dwglkfflvxoxzywr'
```

### **Urls.py**
```python
path('send_email/', views.send_email, name='send_email'),
```

### **Views.py**
```python
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

def send_email(request):
    subject = 'Subject of the Email'
    message = 'This is the message body of the email.'
    from_email = 'your_email@gmail.com'
    recipient_list = ['mksaxena27@yopmail.com']

    send_mail(subject, message, from_email, recipient_list)
    
    # Optionally, you can also specify a fail_silently parameter:
    # send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
    return HttpResponse('Email sent successfully.')


def send_email_template(request):
    subject = 'Subject of the Email'
    template = 'registration_function_based/email_template.html'
    context = {'variable': 'Value for the template'}

    message = render_to_string(template, context)
    from_email = 'your_email@gmail.com'
    recipient_list = ['mksaxena27@yopmail.com']

    send_mail(subject, message, from_email, recipient_list, html_message=message)
    
    return HttpResponse('Email sent successfully.')
```