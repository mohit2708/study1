### Get vs Filter
#### Get
- Returns exactly one object (सिर्फ 1 record लौटाता है)
- Used when you are sure only one record exists (जब आपको पक्का पता हो कि एक ही row मिलेगी)
- get Query is on unique field (id, email, username)
- If no record → raises DoesNotExist (अगर data नहीं मिला ❌ → DoesNotExist error)
- If multiple records → raises MultipleObjectsReturned (अगर एक से ज्यादा row मिली ❌ → MultipleObjectsReturned error)

```python
user = User.objects.get(id=1)
print(user.username)
```

- Error
```python
User.objects.get(id=999)
# User.DoesNotExist

User.objects.get(is_active=True)
# MultipleObjectsReturned (if many active users)
```

#### filter()
- Returns a QuerySet (list-like collection)
- Can return:
  - 0 records ✔
  - 1 record ✔
  - multiple records ✔
- Never throws DoesNotExist or MultipleObjectsReturned
  
```python
users = User.objects.filter(is_active=True)

for user in users:
    print(user.username)

```
- If no data
```python
users = User.objects.filter(id=999)
print(users)   # <QuerySet []>
```

### Practical Usage in Real Projects
- Login by email (unique)
```python
user = User.objects.get(email=email)
```

- Get all active users
```python
users = User.objects.filter(is_active=True)
```
