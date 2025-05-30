### Create seeder
```laravel
php artisan make:seeder UsersTableSeeder
```
### Writing Seeders
```laravel
<?php
 
use Illuminate\Database\Seeder;
use Illuminate\Database\Eloquent\Model;
use DB;
 
public function run()
{
    $users = [
        ['name' => 'Stepha1n de Vries', 'email' => 'st1ephan-v@gmail.com', 'password' => bcrypt('carroqtz124')],
        ['name' => 'John d1oe', 'email' => 'johndo1e@gmail.com', 'password' => bcrypt('carrotqz1243')],
    ];

    DB::table('users')->upsert($users, 'email');

}
```
### Calling Additional Seeders
```php
/**
 * Run the database seeds.
 *
 * @return void
 */
public function run()
{
    $this->call([
        EmployeeSeeder::class,
        UsersTableSeeder::class,
        OtherNewSeeder::class,
    ]);
}
```

### Running all Seeders
```php
php artisan db:seed
```

### Running single seeders
```php
php artisan db:seed --class=UsersTableSeeder
```


