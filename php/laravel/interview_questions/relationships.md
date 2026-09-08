### Table of Contents

|  No.  | Questions                                               |
| :---: | ------------------------------------------------------- |
|   1   | [One to One Relationships](#one-to-one-relationships)   |
|   1   | [One to Many Relationships](#one-to-many-relationships) |
|   1   | [Has One Through](#has-one-through) |
|   1   | [Has One Through 2 example](#has-one-through-2-example) |


### One to One Relationships
* jab kisi table ka relation ek hi table se ho jaise user table ka relation profile table se hi hota hai.

* Step 1: Create the Models and Migrations
```php
php artisan make:model User -m
php artisan make:model Profile -m
```
* Step 2: Define the Migrations
```php
// database/migrations/xxxx_xx_xx_create_users_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('users');
    }
}


// database/migrations/xxxx_xx_xx_create_profiles_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateProfilesTable extends Migration
{
    public function up()
    {
        Schema::create('profiles', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->string('phone')->nullable();
            $table->text('address')->nullable();
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('profiles');
    }
}

```

* Step 3: Define the Relationship in the Models
```php
# user Model
// app/Models/User.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    use HasFactory;

    public function profile()
    {
        return $this->hasOne(Profile::class);
    }
}

# Profile Model
// app/Models/Profile.php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Profile extends Model
{
    use HasFactory;

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}

```

* Step 4: Running the Migrations
```php
php artisan migrate
```

* Step 5: Using the Relationship
```php
# Creating a Profile for a User:
$user = User::create(['name' => 'John Doe', 'email' => 'johndoe@example.com']);

$profile = new Profile(['phone' => '1234567890', 'address' => '123 Main St']);
$user->profile()->save($profile);

# Accessing the Profile of a User:
$user = User::find(1);
echo $user->profile->phone; // Outputs the phone number associated with the user's profile

# Accessing the User of a Profile:
$profile = Profile::find(1);
echo $profile->user->name; // Outputs the name of the user associated with the profile
```

### One to Many Relationships
* A single model is the parent to one or more child models. For example, a blog post may have an infinite number of comments. 

* Step 1: Create the Models and Migrations
```php
php artisan make:model Post -m
php artisan make:model Comment -m
```

* Step 2: Define the Migrations
```php
// database/migrations/xxxx_xx_xx_create_posts_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePostsTable extends Migration
{
    public function up()
    {
        Schema::create('posts', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->text('body');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('posts');
    }
}

# // database/migrations/xxxx_xx_xx_create_comments_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCommentsTable extends Migration
{
    public function up()
    {
        Schema::create('comments', function (Blueprint $table) {
            $table->id();
            $table->foreignId('post_id')->constrained()->onDelete('cascade');
            $table->string('author');
            $table->text('content');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('comments');
    }
}
```

* Step 3: Define the Relationship in the Models
```php
// app/Models/Post.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

    public function comments()
    {
        return $this->hasMany(Comment::class);
    }
}


// app/Models/Comment.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Comment extends Model
{
    use HasFactory;

    public function post()
    {
        return $this->belongsTo(Post::class);
    }
}

```

* Step 4: Running the Migrations
```php
php artisan migrate
```

* Step 5: Using the Relationship
```php
$post = Post::create(['title' => 'My First Post', 'body' => 'This is the body of my first post.']);

$comment1 = new Comment(['author' => 'Jane Doe', 'content' => 'Great post!']);
$comment2 = new Comment(['author' => 'John Smith', 'content' => 'Thanks for sharing.']);

$post->comments()->saveMany([$comment1, $comment2]);
```
```php
$post = Post::find(1);

foreach ($post->comments as $comment) {
    echo $comment->content; // Outputs each comment's content
}
```
```php
$comment = Comment::find(1);
echo $comment->post->title; // Outputs the title of the post associated with the comment
```

### Has One Through
* Step 1: Create the Models and Migrations
```php
mechanics
    id - integer
    name - string
 
cars
    id - integer
    model - string
    mechanic_id - integer
 
owners
    id - integer
    name - string
    car_id - integer
```

Step 2: Define the Relationships in the Models
```php
// app/Models/Mechanic.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Mechanic extends Model
{
    use HasFactory;

    public function carOwner(): HasOneThrough
    {
        return $this->hasOneThrough(
            Owner::class,
            Car::class,
            'mechanic_id', // Foreign key on the cars table...
            'car_id', // Foreign key on the owners table...
            'id', // Local key on the mechanics table...
            'id' // Local key on the cars table...
        );
    }
}

// app/Models/Car.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Car extends Model
{
    use HasFactory;

    public function mechanic()
    {
        return $this->belongsTo(Mechanic::class);
    }

    public function owner()
    {
        return $this->hasOne(Owner::class);
    }
}


// app/Models/Owner.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Owner extends Model
{
    use HasFactory;

    public function car()
    {
        return $this->belongsTo(Car::class);
    }
}


```
* Step 4: Using the Relationship
```php
$mechanic = Mechanic::create(['name' => 'Mike']);

$car = new Car(['model' => 'Toyota']);
$mechanic->cars()->save($car);

$owner = new Owner(['name' => 'John Doe']);
$car->owner()->save($owner);


$mechanic = Mechanic::find(1);
echo $mechanic->owner->name; // Outputs the name of the owner associated through the car

```



### Has One Through 2 example
* Step 1: Create the Models and Migrations
```php
- User
    - id
    - country_id
    - name
- Profile
    - id
    - user_id
    - bio
- Country
    - id
    - name
```
* Step 2: Define the Relationship in the Models
```php
// app/Models/Country.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Country extends Model
{
    use HasFactory;

    public function profile()
    {
        return $this->hasOneThrough(Profile::class, User::class);
    }
}


// app/Models/User.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    use HasFactory;

    public function profile()
    {
        return $this->hasOne(Profile::class);
    }

    public function country()
    {
        return $this->belongsTo(Country::class);
    }
}


// app/Models/Profile.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Profile extends Model
{
    use HasFactory;

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}

```

* Step 3: Using the Relationship
```php
$country = Country::create(['name' => 'USA']);

$user = new User(['name' => 'John Doe']);
$country->users()->save($user);

$profile = new Profile(['bio' => 'Software Developer']);
$user->profile()->save($profile);


$country = Country::find(1);
echo $country->profile->bio; // Outputs the bio of the profile associated through the user

```
