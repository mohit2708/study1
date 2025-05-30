### Ques. What is Component?
* A component is a piece of code, which we can reuse in any blade template. It’s something similar to sections, layouts, and includes.
* For example, we use the same header for each template, so we can create a Header component, which we can reuse.
```php
# How to Make Component
php artisan make:component Header

# We can also make components with in subdirectories like:
php artisan make:component Forms/Button
```
* This command makes two files in your laravel project.
  * One PHP file is created with the name of Header.php inside **app/http/View/Components** directory.
  * And another HTML file is created with the name of header.blade.php inside **resources/views/components/** directory.

* This syntax is used to rendered component in HTML file:
```php
# Syntex:-
<x-ComponentName/>
```
* Step 1: First we place some HTML code in the component header.blade.php file.
```php
<div>
<h1> Header Component </h1>
</div>
```
* Step 2: Now create a users.blade.php view file in the resource folder, in which we can use the header component.
```php
<x-header />
<h1>User Page</h1>
```

* **Pass Data in Laravel Components:-**
* To pass data to balde component using below syntax: <x-alert type="error" :message="$message"/>
* Add code in header.php file inside app/http/View/Components/ directory.
```php
<?php
namespace App\View\Components;
use Illuminate\View\Component;

class Header extends Component
{
  /**
  * The alert type.
  *
  * @var string
  */
  public $type;
  public $message;

  public function __construct($type, $message)
  {
      $this->type = $type;
      $this->message = $message;
  }
}
```
* Now add this **$title** variable in **header.blade.php** component file to show passed data.
```php
<div class="alert alert-{{ $type }}">
    {{ $message }}
</div>
```