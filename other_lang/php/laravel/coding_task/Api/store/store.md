### store data by rashmimohit
```php
use Illuminate\Support\Facades\Validator;
/**
 * store
 *
 * @param  mixed $request
 * @return void
 */
public function store(Request $request) {
    try{
        $data = $request->all();

        $validator = Validator::make($request->all(), [ 
            'industry_type'          => 'required',
        ]);
    
        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        $Campaign                     = new Campaign;
        $Campaign->industry_type      = $data['industry_type'];
        $Campaign->lead_type          = $data['lead_type'];
        $Campaign->quality_type       = $data['quality_type'];
        $Campaign->area_type          = $data['area_type'];
        $Campaign->states             = $data['states'];;            
        $Campaign->save();
        if($campaign->id)
        {
            $insertFilterResponse = $this->createUpdateFilterSet($request->all());
        }

        $message = "Campaign Create Successfully!!";

    }catch(\Throwable $e){
        $message = "Oops Somthing Went Wrong!";
        return response()->json([
            'success' => False,
            'message' => $e->getMessage(),
            'status' => 500
        ],500);
    }
    return response()->json([
        'success' => True,
        'message' => $message,
        'status' => 200
    ],200);
}

/**
 * createUpdateFilterSet
 *
 * @param  mixed $data
 * @return void
 */
public function createUpdateFilterSet($data)
{
    try
    {
        $reqParamArray = array();
        $reqParamArray['Key'] = 'afe24aebdcfda2f47c5926392436ba240b13ce78fbfa4393cfba6afd1f155d9f';
        $reqParamArray['API_Action'] = "insertUpdateFilterSet";
        $reqParamArray['Mode'] = $request->mode_type;
        $reqParamArray['Format'] = "json";
        $reqParamArray['TYPE'] = $request->lead_type;
        $reqParamArray['Partner_ID'] = $request->partner_id;

        $params['Request'] = $reqParamArray;
        $data = json_encode($params);

        $client = new Client([
            'headers' => ['Content-Type' => 'application/json']
        ]);
        $response = $client->post('https://askarileads.leadportal.com/apiJSON.php', 
                ['body' => $data]
        );
        $response = $response ? (json_decode($response->getBody(), true)) : "No Data Available";

        return response()->json([
            'success' => True,
            'message' => "Insert/Update filter set successfully",
            'data' => $response['response'],
            'status' => 200
        ],200);
    }
    catch(\Exception $e)
    {
        return $e->getMessage();
    }
}
```

### validation error
```php
public function validateRegistration(Request $request)
    {
        return Validator::make($request->all(), [
            'first_name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => [
                'required',
                'string',
                'min:6',
                function ($attribute, $value, $fail) {
                    if (!preg_match('/[A-Z]/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one uppercase letter.');
                    }
                    if (!preg_match('/[a-z]/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one lowercase letter.');
                    }
                    if (!preg_match('/\d/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one number.');
                    }
                    if (!preg_match('/[!@#$%^&*()\-_=+{};:,<.>]/', $value)) {
                        $fail('The ' . $attribute . ' must contain at least one special character.');
                    }
                },
            ],
            'confirm_password' => 'required|string|same:password',
        ]);
    }

```