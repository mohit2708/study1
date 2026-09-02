|  No.  | Basic PHP Questions                                                                         |
| :---: | ------------------------------------------------------------------------------------------- |
|       | [What is the PHP?](#What-is-the-PHP)                                                        |
|       | [Which is the latest version of PHP?](#latest-version-of-php)                               |
|       | [What Type of Framework in Php?](#framework-in-php)                                         |
|       | [What Type of CMS(Content Management System) in Php?](#cmscontent-management-system-in-php) |
|       | [Full Form of LAMP?](#full-form-of-lamp)                                                    |
|       | [Full Form of WAMP?](#full-form-of-wamp)                                                    |
|       | [Full Form of XAMPP?](#full-form-of-xampp)                                                  |
|       | [PHP Life Cycle](#php-life-cycle)                                                           |

<div style="page-break-before: always;"></div>

### 🎯**What is the PHP?**
* PHP is an open source server side scripting language used to develop dynamic websites. PHP  stands for Hypertext Preprocessor , also stood for Personal Home Page. It was created by Rasmus lerdorf in 1995 . It is free software released under the PHP license.
* PHP is an acronym for "PHP: Hypertext Pre-processor" And Old name of PHP personal home page. 
* Rasmus Lerdorf is known as the father of PHP. 1994
* PHP is a server side scripting language/s/w/tool commonly used for web applications. And PHP has many framework and CMS for creating a website.
* PHP is a widely-used, open source scripting language. And server side scripting language.
* PHP it is used to manage dynamic content, databases, session tracking, even build entire e-commerce sites.

### 🎯**Latest version of PHP?**
The latest stable version of PHP is 8.2 released on __________.


### 🎯**Framework in Php?**
Cakephp, Laravel, Codeigniter, Yii 2, Zend Framework, Phalcon, Slim, FuelPhp, Phpixie, etc


### 🎯**CMS(Content Management System) in Php?**
Wordpress, Joomla, Magento, Drupal, etc


### 🎯**Full Form of LAMP?**
Linux Apache MySql and Php.

### 🎯**Full Form of WAMP?**
Windows Apache MySql And Php.

### 🎯**Full Form of XAMPP?**
```php
X-OS, Apache Mysql Php Perl
X: Any of the different operating system(Windows,Linux,Mac OS X), to be read as “cross”, meaning cross-platform.
Apache(HTTP Server)
Mysql(Database)
PHP
Perl
```
<div style="page-break-before: always;"></div>

### 🎯**PHP Life Cycle?**
* PHP life cycle is the process in which a client request reaches the web server, the web server passes the PHP request to the PHP engine, PHP code is executed, required database or API operations are performed, a response is generated, and finally that response is sent back to the browser.

#### Steps
1. **User Request:-** Browser server ko request bhejta hai.
2. **Web Server:-** Apache/Nginx request receive karta hai aur identify karta hai ki ye PHP file hai.
3. **PHP Engine:-** PHP engine PHP code ko execute karta hai.
4. **Database/API interaction:-** Agar code mein database query hai: to application database se data fetch karegi.
5. **Response Generate:-** PHP execution ke baad response generate hota hai:
6. **Response Browser ko:-** Web server generated response browser ko bhej deta hai, aur browser page display karta hai.

```php
Browser
   ↓
HTTP Request
   ↓
Web Server (Apache/Nginx)
   ↓
PHP Engine / PHP-FPM
   ↓
PHP Code Execute
   ↓
Database / APIs / Files
   ↓
HTML/JSON Response
   ↓
Web Server
   ↓
Browser
```

<div style="page-break-before: always;"></div>


### 🎯**Ques. What is Constant?**
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

### 🎯**Ques. What is Variable?** 
* Variable temporary data hold Karta hai.
* variable starts with the **$** sign, followed by the name of the variable.
* variable name must **start with a letter or the underscore character**.
* variable name **cannot** start with a **number**.
* Variable names are **case-sensitive** ($age and $AGE are two different variables).


### 🎯**Ques. Difference between Constant And Variable?**
* There is **no need** to **write a dollar sign ($)** before a constant, whereas in Variable one has to write a dollar sign.
* Constants cannot be defined by simple assignment, they may only be defined using the define() function.
* Constants may be defined and accessed anywhere without regard to variable scoping rules.
* Once the Constants have been set, may not be redefined or undefined.

