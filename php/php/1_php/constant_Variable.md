### **Ques. What is Constant?**
* A constant is a name or an identifier for a simple value. A Constant value cannot be changed during the execution of the Script.
* A valid constant name starts with a letter or underscore (no $ sign before the constant name).

**Syntex** define(name, value, case-insensitive)
```php 
<?php
 define("GREETING", "Welcome to mohit");
 echo GREETING;
?>
Output:- Welcome to mohit 
```

### **Ques. What is Variable?** 
* Variable temporary data hold Karta hai.
* A variable starts with the **$** sign, followed by the name of the variable.
* A variable name must **start with a letter or the underscore character**.
* A variable name **cannot** start with a **number**.
* Variable names are **case-sensitive** ($age and $AGE are two different variables).


### **Ques. Difference between Constant And Variable?**
* There is no need to write a dollar sign ($) before a constant, whereas in Variable one has to write a dollar sign.
* Constants cannot be defined by simple assignment, they may only be defined using the define() function.
* Constants may be defined and accessed anywhere without regard to variable scoping rules.
* Once the Constants have been set, may not be redefined or undefined.