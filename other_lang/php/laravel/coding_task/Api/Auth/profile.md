```php
# Model file
/*************************
    * Get user Data    by id *
    **************************
    */
    public static function getUserDataByID($current_user_details = null)
    {
        if ($current_user_details) {
            return User::where('id', $current_user_details['id'])->first();
        } else {
            return User::get();
        }
    }




public function getLoginUserDetils(Request $request){
        try{
            $current_user_details = getCurrentUserInfo();
            $getUserData        = User::getUserDataByID($current_user_details);
            $getUserDetailsData = UserDetail::getUserDetailsDataByID($current_user_details);

            $filteredUserDetailsData = [
                'first_name'        => $getUserData['first_name'] ?? null,
                'last_name'         => $getUserData['last_name'] ?? null,
                'email'             => $getUserData['email'] ?? null,
                'phone'             => $getUserData['phone'] ?? null,
                'phone_verified_at' => $getUserData['phone_verified_at'] ?? null,
                'password_verified' => $getUserData['password_verified'] ?? null,
                'created_by'        => $getUserData['created_by'] ?? null,
                'address'           => $getUserDetailsData['address'] ?? null,
                'state'             => $getUserDetailsData['state'] ?? null,
                'city'              => $getUserDetailsData['city'] ?? null,
                'zip'               => $getUserDetailsData['zip'] ?? null,
            ];
            // dd($getUserDetailsData);

            if ($getUserData) {
                return response()->json([
                    'message' => 'Data Found',
                    'status' => true,
                    'status_code' => 200,
                    'user_data' => $filteredUserDetailsData
                ], 200);
            } else {
                return response()->json([
                    'message' => 'Data Not Found',
                    'status' => false,
                    'status_code' => 404, // Use 404 for not found
                    'user_data' => null
                ], 404);
            }
        } catch (\Exception $e) {
            \Log::error('Error fetching user details: ' . $e->getMessage());
            return response()->json([
                'message' => 'An error occurred while processing your request',
                'status' => false,
                'status_code' => 500 // Use 500 for internal server errors
            ], 500);
        }
    }
```