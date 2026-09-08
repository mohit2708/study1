### Login Api
```php
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;
use Validator;
use JWTAuth;

/**
 * User Login.
 *
 * @return \Illuminate\Http\JsonResponse
 */
public function login(Request $request)
{
    $credentials = [
            'phone' => $request->phone,
            'password' => $request->password
        ];

    //valid credential
    $validator = Validator::make($credentials, [
        'email' => 'required|email',
        'password' => 'required|string|min:6|max:50'
    ]);
    if ($validator->fails()) {
        return response()->json(['error' => $validator->messages(), 'status' => 442], 422);
    }

    $loginDetails = User::where('phone', $credentials['phone'])->first();
    if (!$loginDetails) {
        return response()->json([
            'success' => false,
            'message' => 'No user found with this phone number.',
        ], 404);
    }

    //Creat token
    try {
        // Attempt to authenticate the user and generate a token
        if (!$token = JWTAuth::attempt($credentials)) {
            return response()->json([
                'success' => false,
                'message' => 'Login credentials are invalid.',
                'status' => 400
            ], 400);
        }            
    } catch (JWTException $e) {
        return response()->json([
            'success' => false,
            'message' => 'Could not create token.',
        ], 500);
    }

    $password_verified = $loginDetails->password_verified == 1 ? true : false;

    if($loginDetails->phone_verified_at){
        $loginDetails['token'] = $token;
        return response()->json(['success' => true,'status' => 200,'phone_verified'=>true,'password_verified'=>$password_verified,'message' => 'User get successfully!','loginDetails' => $loginDetails,
        ],200);
    }else{
        $this->sentOtpOnPhone($request);
        $loginDetails['token'] = $token;
        return response()->json(['success' => true,'status' => 200,'phone_verified'=>false,'password_verified'=>$password_verified,'message' => 'Otp has been sent on register phone number!','loginDetails' => $loginDetails,
        ],200);            
    }    
}
```
