### Forget Password
```php
/**
     * @OA\Post(
     * path="/api/forgot_password",
     * summary="Forgot Password",
     * description="Forgot Password API",
     * operationId="Forgot Password",
     * tags={"Auth"},
     * security={ {"apiAuth": {} }},
     * @OA\RequestBody(
     *    required=true,
     *    description="Forgot Password API",
     *    @OA\JsonContent(
     *       required={"email"},
     *       @OA\Property(property="email", type="string", example="anuj@yopmal.com"),
     *    ),
     * ),
     * @OA\Response(
     *    response=400,
     *    description="Wrong credentials response",
     *    @OA\JsonContent(
     *       @OA\Property(property="code", type="integer", example="400"),
     *       @OA\Property(property="status", type="boolean", example="false"),
     *       @OA\Property(property="message", type="string", example="Invalid Data"),
     *        )
     *     )
     * )
     */

    public function forgot_password(Request $request)
    {
        $validator = Validator::make($request->all(), [ 
            'email' => 'required|email',
        ]);
        
        //Send failed response if request is not valid
        if ($validator->fails()) {
            return response()->json(['error' => $validator->messages()], 200);
        }

        $user = DB::table('users')->where('email', '=', $request->email)
                ->first();
            
        if (isset($user) < 1) {
            return response()->json([
                'status' => false,
                'status_code' => '400',
                'message' => "Email does not exist!",
            ], 201);
        }

        $credentials = request()->validate(['email' => 'required|email']);

        Password::sendResetLink($credentials);

        return response()->json([
            'status' => true,
            'status_code' => '200',
            'message' => "A reset link has been sent to your email address..",
        ], 200);

        die();


        try {
            //Check if the user exists start
            $user = DB::table('users')->where('email', '=', $request->email)
                ->first();
            
            if (isset($user) < 1) {
                return response()->json([
                    'status' => false,
                    'status_code' => '400',
                    'message' => "Email does not exist!",
                ], 201);
            }
            //Check if the user exists end

            // $submit_forget_password = new UserService();
            $forget_password = $this->submitForgetPasswordForm($request);
            if($forget_password  == 1){
                return response()->json([
                    'status' => true,
                    'status_code' => '200',
                    'message' => "A reset link has been sent to your email address..",
                ], 200);
            }else{
                return response()->json([
                    'status' => false,
                    'status_code' => '400',
                    'message' => $forget_password,
                ], 400);
            }
        } catch (\Exception $e) {
            // \Log::info(Config::get('custom.log.forgetPassword'), ['message' => $e->getMessage()]);
            return response()->json([
                'status' => false,
                'status_code' => '400',
                'message' => "Somting went Wrong!",
            ], 400);
        }
    }
```