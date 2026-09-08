```php
<?php

namespace App\Http\Controllers\Api;

use PHPOpenSourceSaver\JWTAuth\Facades\JWTAuth;
use Illuminate\Support\Facades\Storage;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\File;
use Illuminate\Http\Request;
use App\Models\User;

class TechnicianController extends Controller
{

    public function getImageUrl(Request $request){
        $user_auth = JWTAuth::parseToken()->authenticate();
        $directoryName = $user_auth->id;


         $users = User::where('role', 'technician')
            ->whereIn('status', ['active', 'pending'])
            ->where(function($query) use ($user_auth) {
                $query->where('created_by', $user_auth->id)
                    ->orWhere('created_by', $user_auth->created_by);
            })
            ->join('user_address', 'users.id', '=', 'user_address.user_id')
            ->select('users.*', 'user_address.*')  // Selecting all user and address fields, adjust as needed
            ->get();

            foreach ($users as $user) {
                // if (File::exists(public_path('images/Uploads/users/' . $user->id . '/'.$user->user_image))) {
                if (isset($user->user_image)) {
                    $user->image_url = asset('images/Uploads/users/' . $user->id . '/'.$user->user_image);
                } else {
                    $user->image_url = 'http://18.223.179.82/images/login_img_bydefault.png'; // default image url
                }
            }

            return response()->json([
                'status' => true,
                'result' => $users,
                'message' => 'Technician list successfully',
            ], 200);
    }
    
}
```