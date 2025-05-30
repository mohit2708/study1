|  No.  | Questions                                                                                                                                     |
| :---: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|       | [What is laravel?](#ques-what-is-laravel)                                                                                                     |
|       | [What is the Features of Laravel?](#ques-what-is-the-features-of-laravel)                                                                     |
|       | [What are pros and cons of using Laravel Framework?](#ques-what-are-pros-and-cons-of-using-laravel-framework)                                 |
|       | [What are available databases supported by Laravel?](#ques-what-are-available-databases-supported-by-laravel)                                 |
|       | [What are the steps to install Laravel with composer?](#ques-what-are-the-steps-to-install-laravel-with-composer)                             |
|       | [What is the templating engine used in Laravel?](#ques-what-is-the-templating-engine-used-in-laravel)                                         |
|       | [How to put Laravel applications in maintenance mode?](#ques-how-to-put-laravel-applications-in-maintenance-mode)                             |
|       | [List some Aggregates methods provided by query builder in Laravel?](#ques-list-some-aggregates-methods-provided-by-query-builder-in-laravel) |

### **Ques. What is Laravel?**
* Laravel is free open source “PHP framework” based on MVC design pattern.
* It is created by **Taylor Otwell**
* The first version of laravel is released on 9 June 2011.
* The latest version of Laravel is **10.0.4 / 2 March 2023**


### **Ques. What is the Features of Laravel?**
* Inbuilt CRSF (cross-site request forgery ) Protection.
* Inbuilt paginations
* middleware
* Eloquent ORM
* Query builder available
* Reverse Routing
* Restful Controllers
* Migration
* Database Seeding/Database Migration
* Autamatic Pagination
* Unit Testing
* Homestead
* Query builder 
* Route caching 
* IOC (Inverse of Control) Container Or service container.


### **Ques. What are pros and cons of using Laravel Framework?**
#### Pros of using Laravel Framework
1. Laravel framework has in-built lightweight blade template engine to speed up compiling task and create layouts with dynamic content easily.<br>
2. Hassles code reusability.<br>
3. Eloquent ORM with PHP active record implementation<br>
4. Built in command line tool “Artisan” for creating a code skeleton , database structure and build their migration
#### Cons of using laravel Framework 
1. Development process requires you to work with standards and should have real understanding of programming<br>
2. Laravel is new framework and composer is not so strong in compare to npm (for node.js), ruby gems and python pip.<br>
3. Development in laravel is not so fast in compare to ruby on rails.<br>
4. Laravel is lightweight so it has less inbuilt support in compare to django and rails. But this problem can be solved by integrating third party tools, but for large and very custom websites it may be a tedious task.


### **Ques. What are available databases supported by Laravel?**
* PostgreSQL
* SQL Server
* SQLite
* MySQL


### **Ques. What are the steps to install Laravel with composer?**
Laravel installation steps:-
* Download composer from https://getcomposer.org/download (if you don’t have a composer on your system)
* Open cmd
* Goto your htdocs folder.
```php
C:\xampp\htdocs> composer create-project laravel/laravel projectname
```
* If you install some particular version, then you can use
```php
composer create-project laravel/laravel project_name "8.0"
```
* If you did not mention any particular version, then it will install with the latest version.



### **Ques. What is the templating engine used in Laravel?**
* The templating engine used in Laravel is __Blade__.
* **Displaying data** If you want to print the value of a variable, then you can do so by simply enclosing the variable within the **curly brackets.**
* **Syntax:-**
```php
{{$variable}}
```

### Ques. How to put Laravel applications in maintenance mode?
Laravel applications can be put into maintenance mode using the below command:
```php
php artisan down
```
And can put the application again on live using the below command:
```php
php artisan up
```

### Ques. List some Aggregates methods provided by query builder in Laravel?
* count() 
* max() 
* min() 
* avg() 
* sum()