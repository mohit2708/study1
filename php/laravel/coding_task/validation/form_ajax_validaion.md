### form validation using ajax
* check proper email validaion
* check white sapace not fill
* check phone number unique 
* Long way
```php
$(document).ready(function() {
    
    // enter the valid email address
    jQuery.validator.addMethod("validate_email1", function(value, element) {
        if (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value)) {
            return true;
        } else {
            return false;
        }
    }, "Please enter a valid email address.");

    // Check white space
    $.validator.addMethod("whitespace", function(value, element) {
        return !(/^\s+$/.test(value));
    }, "This field cannot consist only of spaces.");

    // chacke phone unique
    $.validator.addMethod("phoneUnique", function(value, element) {
        let isSuccess = false;
        $.ajax({
            type: "POST",
            url: "/check-phone", // Laravel route URL
            data: { phone_number: value, _token: $('meta[name="csrf-token"]').attr('content') },
            async: false,
            success: function(response) {
                isSuccess = response.isUnique;
            }
        });
        return isSuccess;
    }, "This phone number is already registered");


});

 
$('#submitButton').click(function() {
    $("#addstafffrom").validate({
        rules: {
            first_name: {
                required: true,
                whitespace: true,
            },
            last_name: {
                required: true,
                whitespace: true,
            },
            email: {
                email: true,
                required: true,
                validate_email1: true
            },
            phone_number: {
                required: true,
                minlength: 10,
                phoneUnique: true
            },
            password: {
                required: true,
                minlength:6
            },
            confirm_password: {
              required: true,
              equalTo: "#password"
            },
            beachlocation: {
                required: true,
            },
            
            
            // Add more validation rules as needed
        },
        messages: {
            first_name: {
                required: "Please enter your first name",
                whitespace: "Please enter a valid first name",
            },
            last_name: {
                required: "Please enter your last name",
                whitespace: "Please enter a valid last name",
            },
            email: {
                required: "Please enter your email address",
                email: "Please enter a valid email address"
            },
            phone_number: {
                required: "Please enter your phone number",
                minlength: "Phone number must be at least 10 digits",
                phoneUnique: "This phone number is already registered",
            },
            password: {
                required: "Please enter your password",
                minlength: "password must be at least 6 characters",
            },
            confirm_password: {
                required: "Please enter confirm your password",
                equalTo: "Password and confirm password do not match"
            },
            beachlocation: {
                required: "Please enter your beach location",
            },
            
        },        
    });
    
});


   $('#addstafffrom').keyup(function() {
    $("#addstafffrom").validate({
        rules: {
            first_name: {
                required: true,
                whitespace: true,
            },
            last_name: {
                required: true,
                whitespace: true,
            },
            email: {
                email: true,
                required: true,
                validate_email1:true,
            },
            phone_number: {
                required: true,
                minlength: 10,
                phoneUnique: true,
            },
            password: {
                required: true,
                minlength:6
            },
            confirm_password: {
              required: true,
              equalTo: "#password"
            },
            beach_location: {
                required: true,
            },
            
            // Add more validation rules as needed
        },
        messages: {
            first_name: {
                required: "Please enter your first name",
                whitespace: "Please enter a valid first name",
            },
            last_name: {
                required: "Please enter your last name",
                whitespace: "Please enter a valid last name",
            },
            email: {
                required: "Please enter your email address",
                email: "Please enter a valid email address"
            },
            phone_number: {
                required: "Please enter your phone number",
                minlength: "Phone number must be at least 10 digits",
                phoneUnique: "This phone number is already registered",
            },
            password: {
                required: "Please enter your password",
                minlength: "password must be at least 6 characters",
            },
            confirm_password: {
                required: "Please confirm your password",
                equalTo: "Password and confirm password do not match"
            },
            beach_location: {
                required: "Please enter your beach location",
            },
            
        },
        
        
    });
   
});
```

#### create route or function for check phone nuber exist or not
```php
Route::post('/check-phone', [StaffController::class, 'checkPhone'])->name('check-phone');
```
```php
public function checkPhone(Request $request)
{
    $phoneExists = User::where('phone', $request->phone_number)->exists();
    return response()->json(['isUnique' => !$phoneExists]);
}
```