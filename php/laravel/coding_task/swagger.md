**Install the swagger:-**
```php
cmd:- composer require "darkaonline/l5-swagger" --ignore-platform-reqs
cmd:- php artisan vendor:publish --provider "L5Swagger\L5SwaggerServiceProvider"
cmd:- php artisan l5-swagger:generate
```

```php
It will return an error:-
	Required @OA\Info() not found

We can add the code in app/Http/Controllers/Controller.php
	/**
	 * @OA\Info(
	 *    title="Your super  ApplicationAPI",
	 *    version="1.0.0",
	 * )
	 */
	class Controller extends BaseController
	{
		use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
	}
	
cmd:- php artisan l5-swagger:generate

```