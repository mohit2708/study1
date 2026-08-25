|  No.  | Questions                                                                   |
| :---: | --------------------------------------------------------------------------- |
|       | [What is laravel?](#ques-what-is-laravel)                                   |
|       | [What is the Features of Laravel?](#what-is-the-features-of-laravel)        |
|       | [Why Use Laravel?](#why-use-laravel)                                        |
|       | [Why Use Laravel](#why-use-laravel)                                         |
|       | [Pros of Laravel Framework](#pros-of-laravel-framework)                     |
|       | [Cons of laravel Framework](#cons-of-laravel-framework)                     |
|       | [What databases supported in Laravel](#what-databases-supported-in-laravel) |
|       | [Install Laravel with composer?](#install-laravel-with-composer)            |



|       | [What is the templating engine used in Laravel?](#ques-what-is-the-templating-engine-used-in-laravel)                                         |
|       | [How to put Laravel applications in maintenance mode?](#ques-how-to-put-laravel-applications-in-maintenance-mode)                             |
|       | [List some Aggregates methods provided by query builder in Laravel?](#ques-list-some-aggregates-methods-provided-by-query-builder-in-laravel) |


<div style="page-break-before: always;"></div>

### 🎯**Ques. What is Laravel?**
* Laravel is a free and open-source **PHP web application framework** used to build modern, secure, and scalable web applications quickly.
* It follows the **MVC (Model-View-Controller)** architecture pattern, which helps organize code and makes applications easier to maintain.
* It is created by **Taylor Otwell**
* The first version of laravel is released on 9 June 2011.
* the latest stable Laravel version is Laravel **13**, released on **March 17, 2026**. It requires PHP 8.3 or higher.


#### **What is the Features of Laravel?**
1. MVC Architecture – Separates business logic, UI, and data.
2. Eloquent ORM – Easy database operations using PHP models.
3. Routing – Clean and simple URL management.
4. Blade Templating Engine – Dynamic and reusable views.
5. Authentication & Authorization – Built-in login and access control.
6. Middleware – Filter HTTP requests.
7. Migration & Seeder – Manage database schema and sample data.
8. Artisan CLI – Command-line tool for development tasks.
9. Queue System – Handle background jobs.
10. Security – Protection against SQL Injection, CSRF, XSS, etc.
* Inbuilt CRSF (cross-site request forgery ) Protection.
* Inbuilt paginations
* middleware
* Query builder available
* Reverse Routing
* Restful Controllers
* Autamatic Pagination
* Unit Testing
* Homestead
* Route caching 
* IOC (Inverse of Control) Container Or service container.

#### Why Use Laravel?
* Laravel is used to build web applications, REST APIs, e-commerce websites, CRM systems, ERP systems, and enterprise applications quickly and securely.
* Main Reasons to Use Laravel
  * **Rapid Development**:- Many features are built-in, reducing development time.
  * **MVC Architecture**:- Keeps code organized and easy to maintain.
  * **Database Management**:- Eloquent ORM simplifies database operations.
  * **Authentication & Authorization**:- Login, registration, roles, and permissions can be implemented easily.
  * **Security**:- Protection against SQL Injection, CSRF, and XSS attacks.
  * REST API Development:- Easy creation of APIs for mobile and web applications.
  * Artisan CLI:- Generates controllers, models, migrations, and more with simple commands.
  * Caching & Queues:- Improves application performance.
  * Large Community Support:- Extensive documentation and packages available.
  * Faster development
  * Clean code structure
  * Large community support


#### Pros of Laravel Framework
1. Laravel framework has in-built lightweight blade template engine to speed up compiling task and create layouts with dynamic content easily.<br>
2. Hassles code reusability.<br>
3. Eloquent ORM with PHP active record implementation<br>
4. Built in command line tool “Artisan” for creating a code skeleton , database structure and build their migration.

#### Cons of laravel Framework 
1. Development process requires you to work with standards and should have real understanding of programming<br>
2. Laravel is new framework and composer is not so strong in compare to npm (for node.js), ruby gems and python pip.<br>
3. Development in laravel is not so fast in compare to ruby on rails.<br>
4. Laravel is lightweight so it has less inbuilt support in compare to django and rails. But this problem can be solved by integrating third party tools, but for large and very custom websites it may be a tedious task.


### 🎯**What databases supported in Laravel?**
* PostgreSQL
* SQL Server
* SQLite
* MySQL


### 🎯**Install Laravel with composer?**
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


### How to check laravel version?
```php
# bash
php artisan --version
php artisan -V

# From within the Application Code
echo app()->version();

# In a Blade template
{{ app()->version() }}
```
<div style="page-break-before: always;"></div>

### What is the vendor folder?
* The vendor folder is where Laravel **stores all the third-party packages** and **dependencies installed through Composer**.
* The vendor folder contains the Laravel framework and all third-party packages installed through Composer. It is automatically generated when running composer install and includes the Composer autoloader (vendor/autoload.php) used to load classes automatically.

#### When you run:
```php
composer install
# (OR) 
composer update
```
* Composer downloads all required packages and stores them inside the vendor folder.

#### If vendor folder is deleted?
```php
composer install
```
* Composer will recreate the vendor folder using the dependencies listed in composer.json and composer.lock

<div style="page-break-before: always;"></div>

### Explain Laravel's request lifecycle.
* In Laravel, a request enters through public/index.php, is processed by the HTTP Kernel and middleware, matched to a route, handled by a controller, interacts with models if needed, and then returns a response to the browser.
* Step-by-Step Explanation
1. Request Enters **public/index.php**
   * This is the **entry point** of every Laravel application.
   * It loads Composer autoload files and starts Laravel.
2. Bootstrap the Application
   * Laravel loads configuration files.
   * Environment variables **(.env)** are loaded.
   * Service providers are registered.
3. HTTP Kernel Handles Request
   * The request is passed to the HTTP Kernel.
   * The kernel manages middleware execution.
4. Middleware Execution
   * Middleware checks or modifies requests before they reach controllers.
   * Examples:
     * Authentication
     * CSRF Protection
     * CORS
     * Logging
5. Route Matching
   * Laravel finds the matching route.
6. Controller Execution
   * The controller method is executed.
7. Model & Database Interaction
   * Laravel uses Eloquent ORM to fetch or save data.
8. Response Generation
   * The controller returns:
     * View
     * JSON
     * Redirect
     * File Download
<div style="page-break-before: always;"></div>

```php
Browser Request
       │
       ▼
public/index.php
       │
       ▼
Bootstrap Application
       │
       ▼
Service Providers
       │
       ▼
HTTP Kernel
       │
       ▼
Middleware
       │
       ▼
Routes
       │
       ▼
Controller
       │
       ▼
Model / Database
       │
       ▼
Response
       │
       ▼
Browser
```
<div style="page-break-before: always;"></div>

### What is Artisan?
* **Artisan** is **Laravel's command-line tool** used to automate development tasks such as creating controllers, models, migrations, running migrations, clearing cache, and executing custom commands.

| Command                                       | Purpose                          |
| --------------------------------------------- | -------------------------------- |
| php artisan serve                             | Start Laravel development server |
| php artisan make:controller UserController    | Create a controller              |
| php artisan make:model User                   | Create a model                   |
| php artisan make:migration create_users_table | Create a migration               |
| php artisan migrate                           | Run migrations                   |
| php artisan db:seed                           | Run seeders                      |
| php artisan route:list                        | Show all routes                  |
| php artisan cache:clear                       | Clear application cache          |
| php artisan config:clear                      | Clear config cache               |
<div style="page-break-before: always;"></div>

### **What is Composer?**
* Composer is a **dependency management tool for PHP** that helps developers install and manage third-party libraries and project dependencies automatically.

#### Why Use Composer?
* Install PHP packages easily
* Manage project dependencies
* Update libraries with a single command
* Autoload classes automatically
* Maintain consistent project versions

#### Example
* Install project dependencies:
```php
composer install
```

* Add a new package:
```php
composer require laravel/sanctum
```

* Update dependencies:
```php
composer update
```
<div style="page-break-before: always;"></div>


### 🎯**What is Service Container?**
* The Service Container is Laravel's **Dependency Injection (DI) container**. It is responsible for managing class dependencies and **automatically injecting them when needed**.
* Laravel Service Container is a dependency injection and object management system. It is used to resolve class dependencies and automatically inject required objects into controllers, services, and other classes.
* its manage the class depandancy, hame bar bar kisi service ka or class ka object nahi banana padta hai.
* sevice container sabhi services ke object rakhta hai.

#### Why Use Service Container?
* Reduces manual object creation
* Supports Dependency Injection
* Makes code loosely coupled
* Improves testing and maintainability


### **Service Provider**
* A Service Provider in Laravel is a class **used to register and configure services** in the Service Container. 
* The register() method is mainly used for container bindings, while the boot() method is used for initialization after services have been registered.
* **HINDI:-** Laravel mein Service Provider ek class hoti hai jahan hum application ke services ko register aur configure karte hain.

#### Service Provider mein mainly do methods hoti hain:
1. **register():-** Services ko Service Container mein register karne ke liye.
2. **boot():-** Service register hone ke baad additional configuration/setup karne ke liye.

### Service Container + Service Provider ka practical example
1. app/Services/EmailService.php
```php
<?php

namespace App\Services;

class EmailService
{
    public function send($email, $message)
    {
        return "Email sent to {$email}: {$message}";
    }
}
```

2. app/Providers/EmailServiceProvider.php
```php
<?php

namespace App\Providers;

use App\Services\EmailService;
use Illuminate\Support\ServiceProvider;

class EmailServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->app->singleton(EmailService::class, function ($app) {
            return new EmailService();
        });
    }

    public function boot()
    {
        //
    }
}
```

* $this->app->singleton(...):- EmailService ko Service Container mein register kar raha hai.

3. Provider ko register karo
* bootstrap/providers.php
```php
<?php

return [
    App\Providers\AppServiceProvider::class,
    App\Providers\EmailServiceProvider::class,
];
```

4. Create controller
* app/Http/Controllers/EmailController.php
```php
<?php

namespace App\Http\Controllers;

use App\Services\EmailService;

class EmailController extends Controller
{
    public function send(EmailService $emailService)
    {
        return $emailService->send(
            'user@gmail.com',
            'Welcome to Laravel'
        );
    }
}
```
