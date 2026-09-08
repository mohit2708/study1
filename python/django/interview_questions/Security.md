### 🎯 **What is CSRF? (Cross-Site Request Forgery)?**
* CSRF (Cross-Site Request Forgery) is a **web security attack** where a malicious website tricks a logged-in user into performing unwanted actions on another website without their knowledge.
* Because browsers automatically send:
  * Session Cookies
  * Authentication Cookies
* with every request to the same website.

#### How Django Prevents CSRF?
* Django generates a **CSRF Token** and verifies it for every POST, PUT, PATCH, and DELETE request.
```python
<form method="post">
    {% csrf_token %}
    <button type="submit">Save</button>
</form>
```

#### When the form is submitted:
* Browser sends the CSRF token.
* Django compares it with the token stored in the user's session/cookie.
* If tokens match → Request allowed.
* If not → 403 Forbidden.

### 🎯 **What is XSS? (Cross-Site Scripting)?**
* XSS (Cross-Site Scripting) ek security attack hai jisme attacker **website me malicious JavaScript code inject kar deta hai**, jo dusre users ke browser me execute ho jata hai.
* Django templates by default data ko **escape** karte hain:

### 🎯 **CSRF vs XSS**
* CSRF: User se bina permission ke request bhejna.
* XSS: Website me malicious JavaScript inject karke user ke browser me chalana.
* Easy yaad rakhne ka tarika:
  * CSRF = Fake Request Attack
  * XSS = Script Injection Attack

| Feature          | CSRF                                                            | XSS                                              |
| ---------------- | --------------------------------------------------------------- | ------------------------------------------------ |
| Full Form        | Cross-Site Request Forgery                                      | Cross-Site Scripting                             |
| Attack Type      | Fake Request Attack                                             | Script Injection Attack                          |
| Target           | Web Application                                                 | User's Browser                                   |
| How it Works     | User ko bina permission ke request bhejne par majboor karta hai | Website me malicious JavaScript inject karta hai |
| Goal             | Unauthorized actions perform karna                              | Data steal karna, session hijack karna           |
| Example          | Password change, money transfer                                 | Cookie theft, fake login form                    |
| Uses User Login? | Haan, user logged-in hona chahiye                               | Zaroori nahi                                     |
| Prevention       | CSRF Token                                                      | Input Validation, Output Escaping, CSP           |


### 🎯 **What is SQL Injection?**
* SQL injection is an attack in which the attacker manipulates or accesses the database by injecting a malicious SQL query.
* SQL Injection ek attack hai jisme attacker **malicious SQL query inject karke database ko manipulate ya access kar leta hai**.

#### Agar login query aise likhi ho:
```sql
SELECT * FROM users
WHERE username = 'admin'
AND password = '1234';

-- After ataack
SELECT * FROM users
WHERE username = 'admin'
AND password = '' OR '1'='1';

-- '1'='1' hamesha true hota hai, isliye login bypass ho sakta hai.
```
* Isliye ORM use karne par SQL Injection ka risk bahut kam ho jata hai.

#### How does Django prevent SQL Injection?
* Django prevents SQL Injection by using parameterized queries through its ORM. User input is treated as data rather than executable SQL code.
* Django SQL Injection se bachne ke liye parameterized queries use karta hai. Django ORM user input ko SQL query ke code se separate rakhta hai.
* ⚠️ Important: Raw SQL likhte waqt bhi Django ke parameterized methods use karne chahiye. Directly string concatenate nahi karna chahiye:
```python
# ❌ Unsafe
cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")

# ✅ Safe
cursor.execute(
    "SELECT * FROM users WHERE name = %s",
    [name]
)
```

### 🎯 **What is Clickjacking?**
* Clickjacking is a security attack where an attacker tricks a user into clicking on a hidden or disguised element to perform an unintended action.
* Clickjacking ek security attack hai jisme attacker user ko trick karke kisi hidden ya disguised button/link par click karwa deta hai, jisse unwanted action perform ho jata hai.


#### Example
* Maan lo ek attacker website par "Claim Prize" button dikha raha hai.
* Actually us button ke upar/neeche ek hidden iframe me kisi trusted website ka button hota hai, jaise:
* **Visible:** Claim Prize 🎁
* **Actual click:** Delete Account
* User ko pata nahi chalta aur click kar deta hai.

#### Django Clickjacking Protection
* Django me built-in **X-Frame-Options middleware** hota hai jo website ko malicious iframe me load hone se protect karta hai.
```python
'django.middleware.clickjacking.XFrameOptionsMiddleware'
```

### 🎯 **What is Security Middleware?**
* Security Middleware Django ka built-in middleware hai jo web application ko common security attacks aur vulnerabilities se protect karne me help karta hai.
* Django SecurityMiddleware provides several security-related protections for a Django application, such as HTTPS redirects, HSTS, and security HTTP headers.
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ...
]
```

#### SecurityMiddleware kya karta hai?
* Ye mainly security-related HTTP headers aur HTTPS-related protections handle karta hai, jaise:
  * 🔒 HTTPS/SSL enforcement
  * 🛡️ HSTS (HTTP Strict Transport Security)
  * 🚫 Content-Type sniffing ko prevent karna
  * 🔗 Referrer Policy set karna
  * 🔐 Secure handling of redirects