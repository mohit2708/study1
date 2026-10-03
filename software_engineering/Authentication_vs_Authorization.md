### **Authentication vs Authorization?**
* Authentication **verifies the identity of a user**, while authorization **determines what resources or actions that authenticated** user is allowed to access. 
* Authentication answers "Who are you?", whereas authorization answers "What are you allowed to do?"
* Dono ka simple difference:
  * Authentication = Aap kaun ho?
  * Authorization = Aapko kya karne ki permission hai?

| Authentication                   | Authorization                   |
| -------------------------------- | ------------------------------- |
| Identity verify karta hai        | Permission check karta hai      |
| "Who are you?"                   | "What can you do?"              |
| Login se related                 | Access/permissions se related   |
| Usually first step               | Authentication ke baad hota hai |
| Username/password, OTP, JWT etc. | Roles, permissions, policies    |

### **What is login()?**
* User ko authenticate karne ke baad session create karta hai.
* Kya hota hai?
  * Username/password verify hota hai.
  * User session me store ho jata hai.
  * User website me logged in ho jata hai.

### **What is logout()?**
* logout() is used to terminate an authenticated user's session and log the user out of the application.
* logout() generally means logging a user out of an application.
* It usually:
  * Ends/removes the user's session
  * Clears authentication information
  * Prevents access to protected pages until the user logs in again

#### In Python
* Django provides a built-in logout() function:
| Function   | Purpose                                                 |
| ---------- | ------------------------------------------------------- |
| `login()`  | User ko application me **authenticate/login** karta hai |
| `logout()` | User ko application se **logout** karta hai             |
