### Create custom jwt middalware for check token is valid or not
* Create middalware
```php
php artisan make:middleware CustomJwtAuth
```
* Put the code
```php
namespace App\Http\Middleware;

use Closure;

# add this line
use Tymon\JWTAuth\Facades\JWTAuth;
use Tymon\JWTAuth\Exceptions\TokenExpiredException;
use Tymon\JWTAuth\Exceptions\TokenInvalidException;
use Tymon\JWTAuth\Exceptions\JWTException;

class CustomJwtAuth
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        try {
            // Attempt to authenticate the token
            $user = JWTAuth::parseToken()->authenticate();

            if (!$user) {
                return response()->json([
                    'status' => 'error',
                    'message' => 'User not found'
                ], 404);
            }
        } catch (TokenExpiredException $e) {
            // Token has expired
            return response()->json([
                'status' => 'error',
                'message' => 'Token has expired'
            ], 401);
        } catch (TokenInvalidException $e) {
            // Token is invalid
            return response()->json([
                'status' => 'error',
                'message' => 'Invalid token'
            ], 401);
        } catch (JWTException $e) {
            // Token is missing or another error occurred
            return response()->json([
                'status' => 'error',
                'message' => 'Token is missing or invalid'
            ], 401);
        }

        // Proceed with the next request if token is valid
        return $next($request);
    }
}
```
* Register Middleware in Kernel.php **app/Http/Kernel.php**
```php
protected $routeMiddleware = [
    // Other middleware
    'custom.jwt.auth' => \App\Http\Middleware\CustomJwtAuth::class,
];
```
* In Route
```php
Route::group(['middleware' => 'custom.jwt.auth'], function () {
    Route::post('/profile-update', [CustomerController::class, 'profileUpdate']);
});
```


### for old
```php
<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

use PHPOpenSourceSaver\JWTAuth\Facades\JWTAuth;
use PHPOpenSourceSaver\JWTAuth\Exceptions\TokenExpiredException;
use PHPOpenSourceSaver\JWTAuth\Exceptions\TokenInvalidException;
use PHPOpenSourceSaver\JWTAuth\Exceptions\JWTException;

class CustomJwtAuth
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        try {
            // Attempt to authenticate the token
            $user = JWTAuth::parseToken()->authenticate();

            if (!$user) {
                return response()->json([
                    'status' => 'error',
                    'message' => 'User not found'
                ], 404);
            }
        } catch (TokenExpiredException $e) {
            // Token has expired
            return response()->json([
                'status' => 'error',
                'message' => 'Token has expired'
            ], 401);
        } catch (TokenInvalidException $e) {
            // Token is invalid
            return response()->json([
                'status' => 'error',
                'message' => 'Invalid token'
            ], 401);
        } catch (JWTException $e) {
            // Token is missing or another error occurred
            return response()->json([
                'status' => 'error',
                'message' => 'Token is missing or invalid'
            ], 401);
        }

        // Proceed with the next request if token is valid
        return $next($request);
    }
}

```