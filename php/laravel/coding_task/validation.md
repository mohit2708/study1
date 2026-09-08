### Create Request Class
```php
php artisan make:request StoreUser
```
```php
<?php
  
namespace App\Http\Requests;
  
use Illuminate\Foundation\Http\FormRequest;
  
class StoreUser extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true;
    }
  
    /** 
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        return [
                'name' => 'required',
                'username' => 'required|min:8',
                'email' => 'required|email|unique:users'
            ];
    }
}
```

* Create Controller
```php
public function store(StoreUser $request)
    {
        $input = $request->all();
        $user = User::create($input);
      
        return back()->with('success', 'User created successfully.');
    }
```

