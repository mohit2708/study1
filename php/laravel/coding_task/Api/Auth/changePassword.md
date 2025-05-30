### Change Password Api?
```php
    /**
     * @OA\Post(
     * path="/api/change_password",
     * summary="Change Password",
     * description="Change Password API",
     * operationId="Change Password",
     * tags={"Auth"},
     * security={ {"apiAuth": {} }},
     * @OA\RequestBody(
     *    required=true,
     *    description="Change Password API",
     *    @OA\JsonContent(
     *       required={"old_password","new_password","confirm_password"},
     *       @OA\Property(property="old_password", type="integer", example="1123456789"),
     *       @OA\Property(property="new_password", type="integer", example="11223344"),
     *       @OA\Property(property="confirm_password", type="integer", example="11223344"),
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

/******************
    * Change Password *
    ******************/
    public function changePassword(Request $request){
        $user = Auth::user();
        $input = $request->all();
        $rules = array(
            'old_password' => 'required',
            'new_password' => [
                'required',
                'min:6',
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
            'confirm_password' => 'required|same:new_password',
        );
        $validator = Validator::make($input, $rules);
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 400);
        }
        try {
            if ((Hash::check(request('old_password'), Auth::user()->password)) == false) {
                return response()->json([
                    'success' => false,
                    'message' => 'Check your old password, Old password is incorrect.',
                    'status' => 400,
                ], 400);

            } else if ((Hash::check(request('new_password'), Auth::user()->password)) == true) {
                return response()->json([
                    'success' => false,
                    'message' => 'Please enter a password which is not similar then current password.',
                    'status' => 400,
                ], 400);
            } else {
                User::where('id', $user->id)->update(['password' => Hash::make($input['new_password'])]);
                return response()->json([
                    'success' => true,
                    'message' => 'Password updated successfully.',
                    'status' => 200,
                ], 200);
            }
        }catch (\Exception $ex) {
            return response()->json([
                'success' => False,
                'message' => $e->getMessage(),
                'status' => 500
            ],500);
        }
    }
```