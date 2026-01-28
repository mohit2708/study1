### Create model with migration
```php
php artisan make:model ModelName -m
```

### Create model with migration and controller
```php
php artisan make:model ModelName -mc
```

### Model
```php

// These fields are allowed to be filled via an array
    protected $fillable = [
        'title',
        'content',
        'status',
    ];

// To allow all fields (Disable protection)
protected $guarded = [];


protected $guarded = ['id', 'password'];
```