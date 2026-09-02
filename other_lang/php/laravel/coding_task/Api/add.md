# Update or create
```php
$deviceUpdate = DeviceInfo::updateOrCreate(
                ['location_id' => $request->location_id],
                ['device_id'=> $request->device_id, 'merchant_id'=> $request->merchant_id]
            );
```

### Data save in databse
```php
use Illuminate\Support\Facades\DB;
use App\Models\ModelName;

public function deviceExceptionLogs(Request $request){
        DB::beginTransaction();
        try{
            $excep_log                = new ModelName; 
            $excep_log->field_name_1  = $request->database_field_1;
            $excep_log->field_name_2  = $request->database_field_2;
            $excep_log->save();

            return response()->json([
                'status' => True,
                'message' => "Record saved successfully!",
                'code' => 200
            ],200);
            DB::commit();
        }catch(\Throwable $e){
            DB::rollBack();
            return response()->json([
                'status' => False,
                'message' => "Oops Somthing Went Wrong!",
                'error_message' => $e->getMessage(),
                'code' => 500
            ],500);
        }
    }
```