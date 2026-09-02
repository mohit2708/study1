### single Image upload api
```php
public function profileUpdate(Request $request)
    {
        $current_user_details = getCurrentUserInfo();
        $getUserDetails = User::with(['userDetails'])->findOrFail($current_user_details['id']);
        
        // Get the new file name
        $fileName = $this->getImageName($request);  # Get Image name
        $filePath = $this->createDirectory();       # Create directory in public folder
        $this->imageUploadInDirectory($request,$fileName,$filePath);
        
        // If there's an old profile image, delete it
        if ($getUserDetails->userDetails->first()->profile_image) {
            $oldImagePath = public_path($filePath . $getUserDetails->userDetails->first()->profile_image);
            if (file_exists($oldImagePath)) {
                unlink($oldImagePath);  // Delete the old profile image
            }
        }

        // Update the profile image in the database
        UserDetail::where('user_id', $current_user_details['id'])->update(['profile_image' => $fileName]);

        // Generate the public URL for the image
        $imageUrl = asset($filePath . $fileName);

        // Convert the image into a base64 string
        $fullPath = public_path($filePath . $fileName);  // Full path in the public directory
        $imageContent = file_get_contents($fullPath);  // Read the image file content
        $base64Image = base64_encode($imageContent);   // Encode the image content as base64

        // Return response
        return response()->json([
            'success' => true,
            'status' => 200,
            'message' => 'Profile image updated successfully!',
            'image_url' => $imageUrl,     // Public URL of the image
            'image_base64' => $base64Image, // Base64 encoded image string
        ], 200);
    }


    /**
     * Get Image name from the imagefile
     */
    static function getImageName($request){
        $originalFileName = pathinfo($request->file('profile_image')->getClientOriginalName(), PATHINFO_BASENAME);
        $timestamp = now()->format('Ymd_His');
        $fileName = $timestamp . '_' . $originalFileName;
        return $fileName;
    }

    /**
     * Create Directory in public folder
     */
    static function createDirectory(){
        // Define the storage path
        $filePath = 'uploads/profile/';

        // Ensure the directory exists
        // if (!File::exists(storage_path('app/public/' . $filePath))) {
        //     File::makeDirectory(storage_path('app/public/' . $filePath), 0755, true);
        // }

        if (!file_exists(public_path($filePath))) {
            mkdir(public_path($filePath), 0777, true);  // Create the directory with proper permissions
        }

        return $filePath;
    }

    /**
     * image store in public folder
     */
    static function imageUploadInDirectory($request,$fileName,$filePath){
        $request->file('profile_image')->move(public_path($filePath), $fileName);
    }
```