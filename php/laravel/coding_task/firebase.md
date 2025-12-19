### Install Firebase in Laravel
```php
composer require kreait/laravel-firebase
```

### **Publish the Configuration (Optional)**

```php
php artisan vendor:publish --provider="Kreait\Laravel\Firebase\ServiceProvider" --tag=config
```

## Firebase Account
### How to Create a Firebase Account (Step-by-Step)
- **Open the Firebase website:** https://firebase.google.com/
- Click “Get Started”
- Login With Google Account
- Create a New Project
  - Click "Add project"
  - Enter your project name
  - Example: my-laravel-app
  - You can disable Google Analytics (optional)
  - Click Create project
- After Project is Created → Open Firebase Console
  - Click Continue to enter the console.
- 🚀 Firebase Account is Now Created

### Enable Cloud Messaging (Required for Push Notification)
- Inside your Firebase project:
- Go to “Project Settings” :- (bottom left gear icon)
- Click “Cloud Messaging” tab
  - Here you will find:
    - Server Key (FCM key)
    - Sender ID
- Laravel will use the service account JSON, not the server key.

### Generate Service Account JSON
- Steps:
  - Console → Project Settings
  - Tab → Service accounts
  - Click “Generate new private key”
  - A service-account.json file will download
- You will need to place this file in:
  - create the downloaded file rename - downloaded_or_rename_file_name
  - and **create the folder** firebase inside the **/storage/app**
  - The path in .env must match exact filename

```php
/storage/app/firebase/downloaded_or_rename_file_name.json
```

### After creating folder → Add in .env
```php
# Replace /full/path/to/ with the actual path where your serviceAccountKey.json is located.
FIREBASE_CREDENTIALS=/storage/app/firebase/service-account.json
```

## Create Model + Migration
```php
php artisan make:model UserDeviceToken -m
```

### Edit Migration
```php
public function up()
{
    Schema::create('user_device_tokens', function (Blueprint $table) {
        $table->id();
        $table->unsignedBigInteger('user_id');
        $table->string('fcm_token')->unique();
        $table->string('device_type')->nullable(); // android / ios / web
        $table->string('device_id')->nullable();   // optional
        $table->timestamps();

        $table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');
    });
}

```

### Run the migration
```php
php artisan migrate --path=/database/migrations/2025_11_19_105525_create_user_device_tokens_table.php
```

### save the token behalf of user_id
- by api for mobile team
- we can save staticaly save toke for testing
```php
public function storeMobileToken(Request $request)
{
    $request->validate([
        'user_id' => 'required|exists:users,id',
        'fcm_token' => 'required|string'
    ]);

    // Save OR Update Token
    UserDeviceToken::updateOrCreate(
        [
            'user_id' => $request->user_id,
            'device_id' => $request->device_id,
        ],
        [
            'fcm_token' => $request->fcm_token,
            'device_type' => $request->device_type,
        ]
    );

    return response()->json([
        'message' => 'Token saved successfully'
    ]);
}
```


### Create Service in your project

- app/Services/FirebaseService.php

```php
<?php

// app/Services/FirebaseService.php
namespace App\Services;

use Kreait\Firebase\Factory;
use Kreait\Firebase\Messaging\CloudMessage;
use Kreait\Firebase\Messaging\Notification;
use Kreait\Firebase\Exception\MessagingException;
use Psr\Log\LoggerInterface;
use Illuminate\Support\Facades\Log;

class FirebaseService
{
    protected $messaging;

    public function __construct()
    {
        $credentialsPath = config('services.firebase.credentials');

        $firebase = (new Factory)
            ->withServiceAccount(base_path($credentialsPath));
        $this->messaging = $firebase->createMessaging();
    }

    /**
     * Send notification to one or multiple FCM tokens.
     *
     * @param string|array $tokens Single token string or array of tokens
     * @param string $title
     * @param string $body
     * @return array|string Report or error message
     */
    public function sendNotification($tokens, string $title, string $body)
    {
        // Normalize tokens to array
        if (is_string($tokens)) {
            $tokens = [$tokens];
        } elseif ($tokens instanceof \Illuminate\Support\Collection) {
            $tokens = $tokens->filter()->values()->toArray();
        } elseif (!is_array($tokens)) {
            return 'Invalid tokens parameter';
        }

        // Remove empty / null tokens
        $tokens = array_values(array_filter($tokens));
        if (empty($tokens)) {
            Log::channel('push_notification')->warning('No tokens provided to sendNotification');
            return 'No tokens found';
        }

        Log::channel('push_notification')->info('Sending push notification', [
            'count' => count($tokens),
            //'tokens' => $tokens, // avoid logging full tokens in production
            'title' => $title,
            'body'  => $body,
        ]);

        $notification = Notification::create($title, $body);
        // $message = CloudMessage::new()->withNotification($notification);
        foreach($tokens as $token){
            $message = CloudMessage::withTarget('token', $token)
            ->withNotification($notification);
             Log::channel('push_notification')->info('Push Notification result', ['msg' =>$message]);
            $success = $this->messaging->send($message);
        }
        
        return $success;
        // try {
            // Use sendMulticast for multiple tokens (works for 1 token too)
            $report = $this->messaging->sendMulticast($message, ['tokens' =>$tokens]);
            // $report = $this->messaging->se
        dd($report);

            // Report is an object; you can extract useful parts
            $result = [
                'successCount' => $report->successes()->count(),
                'failureCount' => $report->failures()->count(),
                // optionally include failure reasons (careful with verbosity)
            ];

            Log::channel('push_notification')->info('Push Notification result', $result);

            return $result;
        // } catch (MessagingException $e) {
        //     Log::channel('push_notification')->error('Firebase MessagingException', ['error' => $e->getMessage()]);
        //     return ['error' => $e->getMessage()];
        // } catch (\Throwable $e) {
        //     Log::channel('push_notification')->error('Firebase general error', ['error' => $e->getMessage()]);
        //     return ['error' => $e->getMessage()];
        // }
    }
    
}
```

### Create Controller

- App\Http\Controllers\notification;

```php
<?php

namespace App\Http\Controllers\notification;

use App\Http\Controllers\Controller;
use App\Services\FirebaseService;
use App\Models\UserDeviceToken;
use Illuminate\Http\Request;

class PushNotificationController extends Controller
{

    public function sendNotifiactionToMobile(Request $request)
    {
        // Example: get all device tokens (non-null)
        $userId = "19390";
        $tokens = UserDeviceToken::where("user_id", $userId)->pluck("fcm_token")->first();
        // $tokens = "cIvEKW3zS8OjCi61AQVPVT:APA91bFm9i86h7kFn2Fv847dQ8wvlikp0MWUbvK0M8NkCNZL0nZK83QLBgB4oimB_WZEIJ7vM5AFCrUwl9PPhPf9xzaiaTHIKoEOsn_Hzo0kA19E9o6F7i0";
        $tokens = "eEAst40BQhiBwu0DX6nRNN:APA91bF-Ht0BsmhYTPoBqlLeEGn7i0jYMnRGNTt7tgA67QsosG0YkIREKFjwTizBqNLpW6Ag4XTS921asfIC6Hf1OLZ-F8hUZ4678yyZCp1PC7Jj6Oo3lPI";

        // For testing a single token you can override:
        // $tokens = ['cIKqbZ-RRca39eV5VGrBeu:APA91b...'];

        $title = $request->input('title', 'New Customer Created by mohit');
        $body  = $request->input('body', 'Customer has been added.');

        if (empty($tokens)) {
            return response()->json(['message' => 'No device tokens found'], 422);
        }

        $firebase = new FirebaseService();

        $result = $firebase->sendNotification($tokens, $title, $body);

        return response()->json([
            'message' => 'Customer created & notification sent',
            'result' => $result,
        ]);
    }
}
```

### Create Route

```php
Route::get('/send-notification-to-mobile', [PushNotificationController::class, 'sendNotifiactionToMobile']);
```

Note:- convert your code into api accordingly.

- **Refrence:-** [https://200oksolutions.com/blog/integrating-firebase-push-notifications-into-your-laravel-application/](https://200oksolutions.com/blog/integrating-firebase-push-notifications-into-your-laravel-application/)