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
