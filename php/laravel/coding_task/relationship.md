### 
```php
# user model
public function userDetails()
    {
        return $this->hasMany(UserDetail::class,'user_id');
    }

    public function bookings()
    {
        return $this->hasMany(Booking::class,'user_id');
    }

    public function advanceBooking()
    {
        return $this->hasMany(AdvanceBooking::class,'user_id');
    }

    public function bookingTransaction()
    {
        return $this->hasMany(BookingTransaction::class,'user_id');
    }
```
### Get
```php
$getUserDetails = User::with(['userDetails','bookings','advanceBooking','bookingTransaction'])->findOrFail($current_user_details['id']);

# With Specific Field
$getUserDetails = User::select(['id', 'name', 'email']) // specify fields for User
    ->with([
        'userDetails:id,user_id,phone,address', // specify fields for userDetails
        'bookings:id,user_id,booking_date,status', // specify fields for bookings
        'advanceBooking:id,user_id,advance_amount,booking_date', // specify fields for advanceBooking
        'bookingTransaction:id,booking_id,transaction_amount,transaction_date' // specify fields for bookingTransaction
    ])
    ->findOrFail($current_user_details['id']);

# some code
$bookingNotes = $user->userDetails->first()->booking_notes;

// Loop through all related UserDetails
foreach ($user->userDetails as $detail) {
    echo $detail->booking_notes . '<br>';
}


// Get all booking notes from userDetails using pluck
$bookingNotes = $user->userDetails->pluck('booking_notes');
dd($bookingNotes); // This will display all booking notes in the collection


# Full Code
$getUserDetails = User::with(['userDetails','bookings','advanceBooking','bookingTransaction'])->findOrFail($current_user_details['id']);
$userDetail             = $getUserDetails->userDetails->first();
$advance_bookings       = $getUserDetails->advanceBooking->first();
$booking_transactions   = $getUserDetails->bookingTransaction->first();

$plan_name = NULL; // Default value
if ($advance_bookings) {
    $get_plan_name = Plan::where('id', $advance_bookings['plan_name'])->first('name');
    $plan_name = $get_plan_name ? $get_plan_name->name : NULL;
}
// if ($getUserDetails->userDetails->isNotEmpty()){}
$userInfo = [
    'user_id'           => $getUserDetails['id'] ?? null,
    'first_name'        => $getUserDetails['first_name'] ?? null,
    'last_name'         => $getUserDetails['last_name'] ?? null,
    'email'             => $getUserDetails['email'] ?? null,
    'phone'             => $getUserDetails['phone'] ?? null,
    'phone_verified_at' => $getUserDetails['phone_verified_at'] ?? null,
    'password_verified' => $getUserDetails['password_verified'] ?? null,
    'created_by'        => $getUserDetails['created_by'] ?? null,
    'address'           => $userDetail['address'] ?? null,
    'state'             => $userDetail['state'] ?? null,
    'city'              => $userDetail['city'] ?? null,
    'zip'               => $userDetail['zip'] ?? null,
];

$userPlanInfo = [
    'plan_name'        => $plan_name,
    'start_date'       => $advance_bookings['start_date'] ?? null,
    'end_date'         => $advance_bookings['end_date'] ?? null,
    'amount'           => $booking_transactions['amount'] ?? null,
    'umbrella'         => $advance_bookings['umbrella'] ?? null,
    'chair'            => $advance_bookings['chair'] ?? null,
];

```