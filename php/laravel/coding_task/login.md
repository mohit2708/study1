```php
public function login(LoginValidation $request)
    {
        // dd($request->all());
        try {
            $input = $request->all();
            if (auth()->attempt(array('email' => $input['email'],
                                    'password' => $input['password'],
                                    'is_active' => '1',
                                    'location_id' => $input['location'],
                                    'role_id' => '2')
                                )
                )
            {
                return redirect()->route('home');
            } else {
                return redirect()->back()->withInput($request->input())->with('error', 'Invalid credentials!');
            }
        } catch (exception $e) {
            return redirect()->back()->with('error', 'Error occurs! Please try again!');
        }      
        
    }
```