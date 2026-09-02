### **List Methods**
                    
| S.N | Questions                                                    |
| --- | ------------------------------------------------------------ |
|     | [What is a Route?](#ques-what-is-a-route)                    |
|     | [Named Routes?](#named-routes)                               |
|     | [Accessing the Current Route?](#accessing-the-current-route) |
|     | [Route Caching?](#route-caching) |
|     | [Cross-Origin Resource Sharing (CORS)?](#cross-origin-resource-sharing-cors) |



### Ques. What is a Route?
* A route is basically an endpoint specified by a URI (Uniform Resource Identifier).
* We create the routes of the website in **web.php** and **APIs routes** in api.php inside the **routes folder**.
* The route is a way of creating a request URL for your application.
* These routes are assigned to the web middleware group, providing features like session state and CSRF protection.
```php
Route::get('/', function (){      
    return view ('welcome');
}); 
```

### Redirect Routes?
* If we are defining a route that redirects to another URI, you may use the Route::redirect method.
```php
Route::redirect('/here', '/there');
```
* By default, Route::redirect returns a 302 status code. You may customize the status code using the optional third parameter:
```php
Route::redirect('/here', '/there', 301);
```

### View Routes?
* If your route only needs to return a view, you may use the Route::view method.
```php
Route::view('/welcome', 'welcome');
```

### The Route List?
* The route:list Artisan command can easily provide an overview of all of the routes that are defined by your application:
```php
php artisan route:list
```

### Named Routes?
* Named routes allow the convenient generation of URLs or redirects for specific routes. You may specify a name for a route by chaining the name method onto the route definition:
```php
Route::get('/user/profile', [UserProfileController::class, 'show'])->name('profile');
```

### Route Groups?
* Route groups allow you to share route attributes, such as middleware, across a large number of routes without needing to define those attributes on each individual route.
* We can assign middleware to all routes within a group,
```php
Route::middleware(['first', 'second'])->group(function () {
    Route::get('/', function () {
        // Uses first & second middleware...
    });
 
    Route::get('/user/profile', function () {
        // Uses first & second middleware...
    });
});
```

### Group Controllers?
* We use the controller method to define the common controller for all of the routes within the group.
```php
use App\Http\Controllers\OrderController;
 
Route::controller(OrderController::class)->group(function () {
    Route::get('/orders/{id}', 'show');
    Route::post('/orders', 'store');
});
```

### Fallback Routes?
* Using the Route::fallback method, you may define a route that will be executed when no other route matches the incoming request.
* Typically, unhandled requests will automatically render a "404" page via your application's exception handler. However, 
* You would typically define the fallback route within your routes/web.php file, all middleware in the web middleware group will apply to the route. You are free to add additional middleware to this route as needed:
```php
Route::fallback(function () {
    // ...
});

# OR
Route::fallback('/create-payment', [ControllerName::class]);
# under controlle class 
public function __invoke(){
    return view();
}
```

### Rate Limiting?
* Rate Limiting in Laravel is a feature used to control the number of requests a client can make to your application within a specified time frame.
* Laravel’s rate limiting feature is implemented using middleware. You can define rate limits based on various parameters such as routes, IP addresses, or users. If a client exceeds the defined limit, Laravel will automatically respond with a 429 Too Many Requests HTTP status code.
  
* Go to **App\Providers\RouteServiceProvider** and write the code
```php
protected function configureRateLimiting()
{
    RateLimiter::for('api', function (Request $request) {
        return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
    });

    RateLimiter::for('customeRateLimit', function (Request $request) {
        return Limit::perMinute(6);
    });
}
```
* Apply in routes
```php
RateLimiter::for('check-rate-limit', function () {
    return "hi";
})->middalware('throttle:customeRateLimit');
```

### Accessing the Current Route
```php
use Illuminate\Support\Facades\Route;
 
$route = Route::current(); // Illuminate\Routing\Route
$name = Route::currentRouteName(); // string
$action = Route::currentRouteAction(); // string
```

### Route Caching?
* Route Caching in Laravel is a performance optimization technique that allows you to cache the routes of your application. 
* Laravel compiles all the routes into a single file and stores them in a cache, which significantly speeds up route registration by eliminating the need to parse the routes on every request.
* This command generates a cached file located at **bootstrap/cache/routes-v7.php** (or a similar version-based filename). Once cached, Laravel loads the routes from this file, making route resolution much faster.

```php
php artisan route:cache
```
* **Clear the Route Cache**: If you need to clear the cached routes (for example, after modifying the routes), you can use the command:
```php
php artisan route:clear
```

### Cross-Origin Resource Sharing (CORS)
* Cross-Origin Resource Sharing (CORS) is a security feature implemented by web browsers.
* CORS allows you to manage these cross-origin requests, defining which external domains can interact with your Laravel application.
* Laravel's CORS settings are defined in the **config/cors.php** configuration file.
* example-
```php
return [
    'paths' => ['api/*'],           //Specifies the routes for which CORS is applied (e.g., ['api/*'] for all API routes).
    'allowed_methods' => ['*'],     // Specifies which HTTP methods are allowed (e.g., ['GET', 'POST']). Using ['*'] allows all methods.
    'allowed_origins' => ['*'],     // Specifies which origins (domains) are allowed to make requests (e.g., ['https://example.com']). Using ['*'] allows all origins.
    'allowed_origins_patterns' => [], // 
    'allowed_headers' => ['*'],     // pecifies which headers are allowed in the request (e.g., ['Content-Type', 'X-Requested-With']). Using ['*'] allows all headers.
    'exposed_headers' => [],        // Specifies which headers can be exposed to the browser (empty array by default).
    'max_age' => 0,                 // Indicates how long the results of a preflight request can be cached.
    'supports_credentials' => false, // if set to true, it allows credentials (like cookies, authorization headers, or TLS client certificates) to be included in cross-origin requests.
];
```

### CSRF TOKEN?
* Laravel automatically generates a CSRF "token" for each active user session managed by the application.
* This token is used to verify that the authenticated user is the person actually making the requests to the application. 
* This token is stored in the user's session and changes each time the session is regenerated.
```php
<form method="POST" action="{{route('pay')}}">
    @csrf
</form>
# OR
<form method="POST" action="{{route('pay')}}">
    <input type="hidden" name="_token" value="{{ csrf_token() }}" />
</form>
```

### X-CSRF-TOKEN?
* store the token in an HTML meta tag:
```php
<meta name="csrf-token" content="{{ csrf_token() }}">

$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});
```