### Install Packege
```php
composer require pusher/pusher-php-server
```

### Set env file
```php
BROADCAST_DRIVER=pusher
PUSHER_APP_ID=2077344
PUSHER_APP_KEY=258da326056b69ffc370
PUSHER_APP_SECRET=95143ddd8f0cae49e791
PUSHER_APP_CLUSTER=ap2
VITE_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
VITE_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
```

### Route in web
```php
Route::get('/pusher-test', function () {
    return view('test-notification');
});
```

### In Blade file
```php
<!DOCTYPE html>
<html>
<head>
    <title>Pusher Test</title>
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Pusher -->
    <script src="https://js.pusher.com/8.2/pusher.min.js"></script>
    <!-- Echo -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/laravel-echo/1.15.0/echo.iife.js"></script>

</head>
<body class="p-4">

    <h2>Pusher Notification Test11</h2>
    <p id="status">Connecting...</p>

    <!-- BOOTSTRAP MODAL -->
    <div class="modal fade" id="notifyModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">

                <div class="modal-header bg-primary text-white">
                    <h5 class="modal-title" id="modalTitle">Notification</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>

                <div class="modal-body">
                    <table class="table table-bordered">
                        <tr>
                            <th>User ID</th>
                            <td id="tblUserId"></td>
                        </tr>
                        <tr>
                            <th>Heading</th>
                            <td id="tblHeading"></td>
                        </tr>
                        <tr>
                            <th>Link</th>
                            <td>
                                <a href="#" target="_blank" id="tblLink">Open</a>
                            </td>
                        </tr>
                    </table>
                    <p id="modalMessage"></p>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-success" id="modalOk">OK</button>
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancel</button>
                </div>

            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

<script>

    Pusher.logToConsole = true;

    const echo = new Echo({
        broadcaster: 'pusher',
        key: "{{ env('PUSHER_APP_KEY') }}",
        cluster: "{{ env('PUSHER_APP_CLUSTER') }}",
        forceTLS: true,
    }); 

    document.getElementById("status").innerText = "Connected to Pusher";

    // Bootstrap Modal instance
    var notifyModal = new bootstrap.Modal(document.getElementById('notifyModal'));

    echo.channel('notice-channel')
        .listen('NoticeCreated', (data) => {
            console.log("Event received:", data);
            
            let title = data.title ?? "New Notification For Chat";
            let message = data.message ?? JSON.stringify(data);

            document.getElementById('tblUserId').innerText = data.notice.user_id;

            // Set values inside modal
            document.getElementById('modalTitle').innerText = title;
            // document.getElementById('modalMessage').innerText = message;

            // Show popup
            notifyModal.show();
        });

    // OK button clicked
    document.getElementById("modalOk").onclick = function () {
        notifyModal.hide();
        alert("You clicked OK!");
    };

</script>

</body>
</html>

```


### route API
```php
use App\Http\Controllers\NoticeController;

Route::post('/send-notice', [NoticeController::class, 'sendNotice']);


<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Notice;
use App\Events\NoticeCreated;

class NoticeController extends Controller
{
    public function sendNotice(Request $request)
    {
        // dd($request->user_id);   // i fond user id
        $notice = Notice::create([
            'user_id' => $request->user_id,
            'notice_heading' => $request->heading,
            'notice_title'   => $request->title,
            'notice_date'    => now(),
            'notice_link'    => $request->link,
            'notice_section' => $request->section,
        ]);
        // dd($notice); // but i can not fond user id

        broadcast(new NoticeCreated($notice))->toOthers();

        return response()->json(['status' => 'sent']);
    }
}

- api response
{
    "user_id" : 23,
    "heading": "New Message11",
    "title": "Request for chat",
    "link": "https://example.com/details1",
    "section": "general1"
}
```

### Model file
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Notice extends Model
{
    // use HasFactory;
    protected $table = 'notifications'; // your existing table

    protected $primaryKey = 'notice_id';

    public $timestamps = false; // because your table has no created_at

    protected $fillable = [
        'user_id',
        'notice_heading',
        'notice_title',
        'notice_date',
        'notice_link',
        'notice_section',
    ];
}
```

### App/events/noticecreated.php
```php
<?php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;

class NoticeCreated implements ShouldBroadcast
{
    public $notice;

    public function __construct($notice)
    {
        $this->notice = $notice;
    }

    public function broadcastOn()
    {
        return new Channel('notice-channel');
    }
}

```