### Add validation
```php
$validator = Validator::make($credentials, [
    'first_name'    => 'required|string|max:255',
    'email'         => 'required|string|email|max:255|unique:users',
    'phone_number'  => 'required|unique:users,phone',   # phone number already exist.
    'password'      => 'required|string|min:6|max:50'
    'password' => [
                'required',
                'string',
                'min:6',
                'max:50',
                function ($attribute, $value, $fail) {
                    if (!preg_match('/[A-Z]/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one uppercase letter.');
                    }
                    if (!preg_match('/[a-z]/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one lowercase letter.');
                    }
                    if (!preg_match('/\d/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one number.');
                    }
                    if (!preg_match('/[!@#$%^&*()\-_=+{};:,<.>]/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one special character.');
                    }
                },
            ],
    'confirm_password' => 'required|string|same:password',
]);

if ($validator->fails()) {
    return response()->json(['error' => $validator->messages()], 200);
}
```


### using rule 
* First, create a custom validation rule using the Artisan command:
```php
php artisan make:rule UniqueEmailForRole
```
* Implement the Custom Rule
```php
namespace App\Rules;

use Illuminate\Contracts\Validation\Rule;
use Illuminate\Support\Facades\DB;

class UniqueEmailForRole implements Rule
{
    protected $roleId;
    protected $userId;

    public function __construct($roleId, $userId = null)
    {
        $this->roleId = $roleId;
        $this->userId = $userId;
    }

    public function passes($attribute, $value)
    {
        $query = DB::table('users')
            ->where('email', $value)
            ->where('role_id', $this->roleId);

        if ($this->userId) {
            $query->where('id', '!=', $this->userId);
        }

        return $query->count() === 0;
    }

    public function message()
    {
        return 'The email is already taken for the specified role.';
    }
}
```
* Use the Custom Rule in Your Validation
```php
use App\Rules\UniqueEmailForRole;
use Illuminate\Support\Facades\Validator;

$roleId = 4; // Specify the role ID you want to check against

$request->validate([
    'first_name' => 'required|string|between:2,100',
    'email' => [
        'required',
        'string',
        'email',
        'max:100',
        new UniqueEmailForRole($roleId, $request->id), // Use the custom rule
    ],
    'phone' => 'required|max:20',
    'beachlocation' => 'required|array',
]);
```