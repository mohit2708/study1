### notification
- when mobile call to web

### Find is the YOUR_VAPID_KEY
- 1️⃣ Open Firebase Console
- 2️⃣ Select project: project_name-a74d0
- 3️⃣ Click ⚙️ Project settings
- 4️⃣ Open Cloud Messaging tab
- 5️⃣ Scroll to Web Push certificates
```php
Web Push certificates
--------------------------------
Key pair
Public key:  BLxxxxxxxxxxxxxxxxx
```

### Must add script in public folder
```php
//  public/firebase-messaging-sw.js

importScripts('https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging-compat.js');

firebase.initializeApp({
    apiKey: "AIzaSyCU1D_8jmXBr2N2_nl8TS3dTcx7bHp0gGk",
    authDomain: "dispatchchannel-a74d0.firebaseapp.com",
    projectId: "dispatchchannel-a74d0",
    messagingSenderId: "908042904984",
    appId: "1:908042904984:web:d79e3b7c26c039f4ce77ed"
});

// firebase.messaging();
const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
    if (payload.data.type === 'incoming_call') {
        self.registration.showNotification(
            payload.notification.title,
            {
                body: payload.notification.body,
                data: payload.data
            }
        );
    }
});
```

### Add script after login -> page
```php
<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getMessaging, getToken } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging.js";

const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    messagingSenderId: "SENDER_ID",
    appId: "APP_ID",
};

const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);

// Ask permission + get token
Notification.requestPermission().then(permission => {
    if (permission === 'granted') {
        getToken(messaging, {
            vapidKey: "YOUR_VAPID_KEY"
        }).then((token) => {
            if (token) {
                saveTokenToServer(token);
            }
        });
    }
});

function saveTokenToServer(token) {
    fetch('/save-fcm-token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': '{{ csrf_token() }}'
        },
        body: JSON.stringify({
            fcm_token: token
        })
    });
}
</script>

```

### Token save into the database
```php
// routes/web.php
Route::post('/save-fcm-token', [App\Http\Controllers\FCMController::class, 'save'])
    ->middleware('auth');


// controller
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Auth;

class FCMController extends Controller
{
    public function save(Request $request)
    {
        $request->validate([
            'fcm_token' => 'required|string'
        ]);

        $user = Auth::user();

        $user->fcm_token = $request->fcm_token;
        $user->save();

        return response()->json(['message' => 'Token saved']);
    }
}


```
