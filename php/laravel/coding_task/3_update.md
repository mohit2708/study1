
|  No.  | Tables                                   |
| :---: | ---------------------------------------- |
|       | [update data by DB?](#update-data-by-db) |
|       | [update data in two table?](#update-data-in-two-table) |


### update data by DB
```php
DB::table('table_name')
    ->where('id', $request->job_id)
    ->update(['cal_add_job' => 1,'cal_add_job' => 1]);
```

### update data in two table?
```php
    public function update(Request $request){
    	$update_customer = Customer::where('id', $request->update_customer_id)->first();
    	if ($update_customer) {
		    $update_customer->first_name 		= trim($request->first_name);
		    $update_customer->last_name 		= trim($request->last_name);
		    $update_customer->save();

		    $update_advance_booking = AdvanceBooking::where('customer_id', $update_customer->id)->first();
		    if ($update_advance_booking) {
		    	$update_advance_booking->plan_name 		= $request->duration;
	            $update_advance_booking->remaining_days = ($request->days < $request->used_days) ? 0 : $request->remaining_days;
	            $update_advance_booking->save();
		    }           
            
		}
		else {
		    return response()->json(['error' => 'User not found.'], 404);
		}
		return redirect('customer/list')->with('success', 'Customer Update successfully!');
    }
```

```php
public function changePasswordWithoutAjax(Request $request){
        // dd($request->all());
        try {
        $request->validate([
            'new_password' => 'required|string|min:6',
            'confirm_password' => 'required_with:new_password|same:new_password|min:6',
        ]);

        // Update the user's password
        $user = User::find($request->user_id);
        if (!$user) {
            return response()->json(['success' => false, 'message' => 'User not found']);
        }
        User::whereId($request->user_id)->update([
            'password' => Hash::make($request->new_password)
        ]);
        return redirect('user/list')->with('success', 'Password changed successfully!');
        }catch (Exception $e) {
            Log::error($e->getMessage(), $e->getTrace());
        }
    }
```

# Project

```php
# Controll file

/**
* Update the specified resource in storage.
*
* @param  int  $id
* @return Response
*/
use Illuminate\Validation\Rule;

public function update(Request $request){
    try{
        $request->validate([
            'first_name'        => 'required|string|between:2,100',
            'email' => ['required','string','email','max:100',Rule::unique('users')->ignore($request->id),],
            'phone' => 'required|max:20',
            'beachlocation' => 'required'
        ]);
        $update_staff                 = User::find($request->id);
        $update_staff->location_id    = $request->beachlocation;
        $update_staff->email          = $request->email;
        $update_staff->update();
        return redirect('staff/list')->with('success', 'Staff updated successfully!');
    }catch (Exception $e) {
        Log::error($e->getMessage(), $e->getTrace());
    }	
}
```

```php
$booking = Booking::where('id',$request->booking_id)->update(["closed_by"=>$user_id]);
```


### blade file
```php
# text box
<div class="form-group">
    <label>First Name: <span style="color: red;">*</span></label>
    <input type="text" name="first_name"
        class="form-control @error('first_name') is-invalid @enderror"
        id="first_name" value="{{ $data_admin->first_name }}"
        placeholder="Enter your first name">
    @error('first_name')
    <span class="invalid-feedback" role="alert">
        <strong>{{ $message }}</strong>
    </span>
    @enderror
</div>

# Select option
<label>Duration Type:<span style="color: red;">*</span></label>
<select class="form-control @error('duration_type') is-invalid @enderror"
    id="duration_type" name="duration_type"
    value="{{ $data_plan->duration_type }}">
    <option value="">-- Select your Duration Type --</option>
    <option value="day" {{ ( $data_plan->duration_type == 'hour' ) ? 'selected' : '' }}>Hour</option>
    <option value="day" {{ ( $data_plan->duration_type == 'day' ) ? 'selected' : '' }}>Day </option>
    <option value="month" {{ ( $data_plan->duration_type == 'month' ) ? 'selected' : '' }}>Month </option>
    <option value="year" {{ ( $data_plan->duration_type == 'year' ) ? 'selected' : '' }}>Year </option>
</select>
```

# Update or create
```php
$deviceUpdate = DeviceInfo::updateOrCreate(
                ['location_id' => $request->location_id],
                ['device_id'=> $request->device_id, 'merchant_id'=> $request->merchant_id]
            );
```