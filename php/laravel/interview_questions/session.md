### Ques. What is sessions?
* sessions provide a way to store information about the user across multiple requests.

##### Storing Data:-
* To store data in the session, you will typically use the request instance's **put** method or the global **session helper**:
```php
// Via a request instance...
$request->session()->put('key', 'value');
```

```php
use Session;
 
// Via the global "session" helper...
session(['key' => 'value']);
session(['location_id' => $input['location']]);
```

##### Retrieving All Session Data: -
* If you would like to retrieve all the data in the session, you may use the all method:
```php
$data = $request->session()->all();

// for particaluar key
$value = $request->session()->get('key');

// This default value will be returned if the specified key does not exist in the session.
$value = $request->session()->get('key', 'default');
// OR
$value = $request->session()->get('key', function () {
    return 'default';
});

//OR in blade file
@if(Session::has('location_id'))
<div class="alert alert-danger">
  {{ Session::get('location_id')}}
</div>
@endif

@if(session('location_id'))
    <p>Your current location is: {{ session('location_id') }}</p>
@else
    <p>No location found in session.</p>
@endif
```

```php
$startDate = Session::get('startDate');
```

##### Determining if an Item Exists in the Session: -
* To determine if an item is present in the session, you may use the **has** method. The **has** method returns **true** if the item is present and is not **null**:
```php
if ($request->session()->has('users')) {
    // ...
    dd('check the key exist or not and also check the value not null');
}
```
* To determine if an item is present in the session, even if its value is **null**, you may use the **exists** method:
```php
if ($request->session()->exists('users')) {
    // ...
    dd('only check the key exist or not');
}
```
* To determine if an item is not present in the session, you may use the **missing** method. The **missing** method returns **true** if the item is not present:
```php
if ($request->session()->missing('users')) {
    // ...
}
```

### Destroy session
```php
session()->forget('location');
```