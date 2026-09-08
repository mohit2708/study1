

### Soft Deletes
#### Configration:-
* **Step 1:** Enable Soft Deletes in the Model
```php
<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;
class YourModel extends Model
{
    use SoftDeletes;
    // ... rest of your model code
}
```
* **Step 2:** Prepare the Database
```php
Schema::table('your_table_name', function (Blueprint $table) {
    $table->bigIncrements('id');
    $table->softDeletes();
    $table->timestamps();
});
```
*  **Consider Custom Column Names (Optional)**. By default, Laravel uses deleted_at for the soft delete column. If you prefer a different name, you can specify it within the softDeletes method call like this:
```php
Schema::table('your_table_name', function (Blueprint $table) {
    $table->bigIncrements('id');
    $table->softDeletes('custom_deleted_at_column_name');
    $table->timestamps();
});
```

#### Calling in controller:-
* We can get all records
```php
$user = User::get();
```

* Delete Query:
```php
$user = User::find(1);
$user->delete();
```

* Deleting permanently
```php
$user = User::find(1);
$user->forceDelete();
```

* Get Deleted Records:
```php
$user = User::withTrashed()->get(); // We can also get deleted records with soft delete.
```

* Restore Query:
```php
$user = User::onlyTrashed()->restore();
OR
$post = Post::withTrashed()->find($id);
$post->restore();
```
```php
$trash_user = User::withTrashed()
    ->where('email', 'asf@safg.vasF')
    ->where('role_id', '4')
    ->first();

if ($trash_user) {
    $trash_user->restore();
} else {
    // Optionally handle the case where the user isn't found
    echo "User not found or not trashed.";
}

```




























