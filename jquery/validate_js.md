### validation js
```js
/******************************
Create Method for validate js *
*******************************
*/
$(document).ready(function() {
    // Check if the text box contains spaces
    jQuery.validator.addMethod("remove_space", function(value, element) {
        if (/\s/.test(value)) {
            return false;
        }else {
            return true; 
        }
    }, "Please enter a valid password without spaces.");

    // Email formatting check
    jQuery.validator.addMethod("validate_email1", function(value, element) {

        if (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value)) {
            return true;
        } else {
            return false;
        }
    }, "Please enter a valid email address.");

});


$(document).ready(function() {
    // Define validation rules and messages for admin add form
    var addAdminFromValidationRules = {
        first_name: {
            required: true,
            whitespace: true
        },
        last_name: {
            required: true,
            whitespace: true
        },
        email: {
            email: true,
            required: true,
            validate_email1: true,
        },
        phone_number: {
            required: true,
            minlength: 10,
        },
        password: {
            required: true,
            whitespace: true,
            minlength: 6,
            remove_space: true
        },
        confirm_password: {
            required: true,
            whitespace: true,
            remove_space: true,
            equalTo: "#password"
        },
        // Add more validation rules as needed
    };

    var addAdminFromValidationMessages = {
        first_name: {
            required: "Please enter your first name",
        },
        last_name: {
            required: "Please enter your last name",
        },
        email: {
            required: "Please enter your email address",
            email: "Please enter a valid email address"
        },
        phone_number: {
            required: "Please enter your phone number",
            minlength: "Phone number must be at least 10 digits",
        },
        password: {
            required: "Please enter your password",
            minlength: "Password must be at least 6 characters",
        },
        confirm_password: {
            required: "Please confirm your password",
            equalTo: "Password and confirm password do not match"
        },
    };

    // Initialize validation on form submit and keyup events
    $('#clicksubmitButton, #addadminfrom').on('click keyup', function() {
        $("#addadminfrom").validate({
            rules: addAdminFromValidationRules,
            messages: addAdminFromValidationMessages
        });
    });
});
```

### ### validation js long process

```js
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
            },
            password: {
                required: true,
                minlength:6
            },
            confirm_password: {
              required: true,
              equalTo: "#password"
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
            },
            password: {
                required: "Please enter your password",
                minlength: "password must be at least 6 characters",
            },
            confirm_password: {
                required: "Please enter confirm your password",
                equalTo: "Password and confirm password do not match"
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


### Custom Validation
```js
$(document).ready(function() {
    $('#updatepassword').on('click', function() {
        // Perform your validation checks here
        var newPassword = $('#new_password').val();
        var confirmPassword = $('#confirm_password').val();
        $("#new_password_error_msg, #confirm_password_error_msg").html('');
        
        // Check for empty fields
        if (newPassword === '' || confirmPassword === '') {
            $("#new_password_error_msg").html('Please enter your password').css("color", "red");
            $("#confirm_password_error_msg").html('Please enter your confirm password')
                .css("color", "red");
            return;
        }
        
        // Check for password length
        if (newPassword.length < 6 || confirmPassword.length > 20) {
            $("#new_password_error_msg, #confirm_password_error_msg").html(
                    'Password must be between 6 and 20 characters.')
                .css("color", "red");
            return;
        }

        // Check for spaces in password
        if (/\s/.test(newPassword)) {
            $("#new_password_error_msg").html('Password cannot contain spaces').css("color", "red");
            return;
        }

        // Check if both passwords are the same
        if (newPassword !== confirmPassword) {
            $('#confirm_password_error_msg').html('Passwords do not match.').css("color", "red");
            return;
        }

        // If validation passes, submit the form
        $('#changePasswordForm').submit();
    });
});
```