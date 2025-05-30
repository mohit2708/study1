### Install Composer
```php
composer create-project laravel/laravel projectName
```

### Install migration
php artisan migrate:fresh



### Create controller
```php
php artisan make:controller Admin\user\UserController
```

### try catch
```php
 try{

 }catch(\Exception $e){
    DB::rollback();
    return redirect()->back()->with('error', 'Error occurs! Please try again!');
}
```

