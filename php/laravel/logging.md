### Create the source code in config\logging.php
```php
'payload_logs' => [
    'driver' => 'daily',
    'path' => storage_path('logs/payload/payload_' . date('Y-m-d') . '.log'),
    'level' => 'debug',
    'days' => 15,
],
```
### And call 
```php
use Illuminate\Support\Facades\Log;
 
Log::emergency($message);
Log::alert($message);
Log::critical($message);
Log::error($message);
Log::warning($message);
Log::notice($message);
Log::info($message);
Log::debug($message);


Log::channel('payload_logs')->info("device ID: {$getDeviceId}");
Log::channel('payload_logs')->info("device notification api successfully!!\n");
```