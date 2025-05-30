### insert data by model
```php
$offuser                = new Model; 
$offuser->offuser_name  = $request->off_name;
$offuser->save();
```

```php
DB::table('users')
    ->updateOrInsert(
        ['email' => 'john@example.com', 'name' => 'John'], // matching record
        ['votes' => '2']    // update record
    );
```

# Project

### URL
```php
# Route
Route::get('/customer/add', [App\Http\Controllers\Admin\CustomerController::class, 'create'])->name('customer.create');
Route::post('/customer/store', [App\Http\Controllers\Admin\CustomerController::class, 'store'])->name('customer.store');
```
```php
# controller file
/**
* Show the form for creating a new resource.
*
* @return Response
*/
public function create(){  
    return view('admin.customer.add');
}


/**
* Store a newly created resource in storage.
*
* @return Response
*/
public function store(Request $request){
    try{
        $request->validate([
            'first_name' => 'required|string|between:2,10',
            'last_name' => 'required|string|between:2,10',
            'email' => 'required|string|email|max:100|unique:users',
            'phone_number' => 'required|min:10|max:15',
            'password' => 'required|string|min:6',
            'confirm_password' => 'required|min:6|same:password',
        ],[
            'first_name.required' => 'Name field is required.',
            'email.required' => 'Email field is required.',
            'email.email' => 'Email field must be email address.'
        ]);
        $save_customer                  = new Model;
        $save_customer->first_name      = $request->first_name;
        $save_customer->gender          = $request->gender;
        $save_customer->language        = implode(',', (array) $request->language);  # save checkbox
        $save_customer->city            = $request->city;
        $save_customer->message         = $request->message;
        $save_customer->save();

    return redirect('customer/list')->with('success', 'Customer Added successfully!');
    }catch(\Exception $e){
        DB::rollback();
        Log::error($e->getMessage(), $e->getTrace());
        return redirect()->back()->with('error', 'Error occurs! Please try again!');
    }
}
```


```php
# blade file
<form method="post" id="customer_form" action="{{ route('customer.store') }}">
{!! csrf_field() !!}
<div class="card-body">
    <div class="row">
        <div class="col-6">
            <div class="form-group">
                <label>First Name:<span style="color:red">*<span></label>
                <input type="text" class="form-control" id="first_name" name="first_name"
                    placeholder="Enter your first name">

                <!-- Way 2: Display Error Message -->
                @error('first_name')
                    <span class="text-danger">{{ $message }}</span>
                @enderror
                 <!-- Way 3: Display Error Message -->
                @if ($errors->has('first_name'))
                    <span class="text-danger">{{ $errors->first('first_name') }}</span>
                @endif

            </div>
        </div>
        <div class="col-6">
            <div class="form-group flex-row">
                <label>Gender:<span style="color:red">*<span></label>
                <input type="radio" id="male" name="gender" value="male" /><label>Male</label>
                <input type="radio" id="female" name="gender"
                    value="female" /><label>Female</label>
            </div>
        </div>
        <div class="col-6">
            <div class="form-group flex-row">
                <label>Language:<span style="color:red">*<span></label>
                <input type="checkbox" name="language[]" value="hindi"><label>Hindi</label>
                <input type="checkbox" name="language[]" value="english"><label>English</label>
            </div>
        </div>
        <div class="col-6">
            <div class="form-group">
                <label>State:<span style="color:red">*<span></label>
                <select class="form-control" name="state" id="state">
                    <option value="volvo">Volvo</option>
                    <option value="saab">Saab</option>
                    <option value="mercedes">Mercedes</option>
                    <option value="audi">Audi</option>
                </select>
            </div>
        </div>
        <div class="col-12">
            <div class="form-group">
                <label>Message:<span style="color:red">*<span></label>
                <textarea class="form-control" id="message" name="message" rows="3" cols="1"
                    placeholder="Enter your message"></textarea>
            </div>
        </div>

    </div>
</div>

<div class="card-footer">
    <button type="submit" class="btn btn-danger">Back</button>
    <button type="submit" class="btn btn-info float-right">Submit</button>
</div>
</form>

<script>
$('#customer_form').validate({
    rules: {
        first_name: {
            required: true,
        },
        email: {
            required: true,
            email: true,
        },
        phone_number: {
            required: true,
        },
        gender: {
            required: true,
        },
        language: {
            required: true,
        },
        state: {
            required: true,
        },
    },
    messages: {
        first_name: {
            required: "Please enter your first name",
        },
        email: {
            required: "Please enter a email address",
            email: "Please enter a valid email address"
        },
        phone_number: {
            required: "Please enter your phone number",
        },
        gender: {
            required: "Please select your gender",
        },
        language: {
            required: "Please select your language",
        },
        state: {
            required: "Please select your state",
        },
    },
    errorElement: 'span',
    errorPlacement: function(error, element) {
        error.addClass('invalid-feedback');
        element.closest('.form-group').append(error);
    },
    highlight: function(element, errorClass, validClass) {
        $(element).addClass('is-invalid');
    },
    unhighlight: function(element, errorClass, validClass) {
        $(element).removeClass('is-invalid');
    }
});
</script>
```

# Update or create
```php
$deviceUpdate = DeviceInfo::updateOrCreate(
                ['location_id' => $request->location_id],
                ['device_id'=> $request->device_id, 'merchant_id'=> $request->merchant_id]
            );
```