### Create new table
```php
php artisan make:migration create_table_names_table
```
```php
public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('role_id')->nullable();
            $table->unsignedBigInteger('location_id')->nullable();
            $table->integer('added_by')->nullable();
            $table->text('states')->nullable();
            $table->longText('exceptionlog')->nullable();
            $table->string('name');
            $table->string('email')->unique();
            $table->time('start_time')->nullable();
            $table->date('start_date')->nullable();
            $table->enum('is_advanced',['0','1'])->default('0')->comment("0=not advanced, 1=is advanced");
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();

            $table->foreign('role_id')->references('id')->on('roles')->onDelete('cascade');
            $table->foreign('location_id')->references('id')->on('locations')->onDelete('cascade');
        });
    }

```
```php
php artisan migrate
php artisan migrate --path=/database/migrations/2023_11_07_134624_create_cities_table.php
```


### Create new field in exsting table.
```php
php artisan make:migration add_extra_fields_users
```
```php
public function up()
{
    Schema::table('users', function (Blueprint $table) {
        $table->tinyInteger('gender')->default(0);
        $table->string('mobile_no')->nullable();
    });
}
```
```php
public function down()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('gender');
            $table->dropColumn('mobile_no');
        });
    }
```
* In Model File
```php
protected $fillable = [
        'name',
        'email',
        'password',
        'mobile_no',
        'gender'
    ];
```
```php
php artisan migrate
```




### Create model with migration
```php
php artisan make:model ModelName -m
```

### Create model with migration and controller
```php
php artisan make:model ModelName -mc
```

### All Create
```php
php artisan make:model ModelName -a
-----------------------------------
model
controller
seeder
migration
factory
```


### Laravel Migrations Generator
* Install
```php
composer require --dev kitloong/laravel-migrations-generator
```

* Laravel Setup
```php
Laravel will automatically register service provider for you.
```

* To create migrations for all the tables
```php
php artisan migrate:generate

# You can specify the tables you wish to generate using:
php artisan migrate:generate --tables="table1,table2,table3,table4,table5"

# You can also ignore tables with:
php artisan migrate:generate --ignore="table3,table4,table5"
```



php artisan migrate --path=/database/migrations/2023_10_04_171556_create_virtual_clipboards_table.php
php artisan migrate --path=/database/migrations/2023_11_07_134624_create_cities_table.php


