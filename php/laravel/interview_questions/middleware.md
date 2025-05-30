|  No.  | [Middleware]()                                                   |
| :---: | ---------------------------------------------------------------- |
|       | [What is middleware?](#ques-what-is-middleware)                  |
|       | [How to create middleware?](#how-to-create-middleware)           |
|       | [Registering Middleware?](#registering-middleware)               |
|       | [Grouping middleware in routes?](#grouping-middleware-in-routes) |

### Ques. What is middleware?
* Middleware is a technique for filtering HTTP requests. Laravel includes a middleware that checks whether application user is authenticated or not.


### How to create middleware?
* The middleware that you create can be seen at **app/Http/Middleware** directory.
```php
php artisan make:middleware MiddlewareName
```
```php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class MiddlewareName
{
    public function handle(Request $request, Closure $next)
    {
        if (auth()->check() && (auth()->user()->role_id=='1' || auth()->user()->role_id=='2')) {
            return $next($request);
        }
        return redirect('/admin/login');
        // return $next($request);
    }
}
```
#### Registering Middleware
* The middleware can be registered at **app/Http/Kernel.php**.
```php
protected $routeMiddleware = [
    'auth' => \App\Http\Middleware\Authenticate::class,
    'auth.basic' => \Illuminate\Auth\Middleware\AuthenticateWithBasicAuth::class,
    'guest' => \App\Http\Middleware\RedirectIfAuthenticated::class,
    'anyname' => \App\Http\Middleware\MiddlewareName::class,   # add this line
];
```

### Grouping middleware in routes?
* In **routes/web.php** or **routes/api.php** file.
```php
Route::group(['middleware' => ['my-middleware']], function () {
    Route::get('/example', 'ExampleController@index');
    Route::post('/example', 'ExampleController@store');
});

# add miltipal middleware
Route::group(['middleware' => ['my-middleware', 'another-middleware']], function () {
    // Your routes here
});
```