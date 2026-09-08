# Update or create
```php
$deviceUpdate = DeviceInfo::updateOrCreate(
                ['location_id' => $request->location_id],
                ['device_id'=> $request->device_id, 'merchant_id'=> $request->merchant_id]
            );
```