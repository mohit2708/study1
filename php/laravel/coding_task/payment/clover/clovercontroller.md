```php
public function generateToken(Request $request){
    $client = new Client();

    try {
        $response = $client->post(
            'https://api.clover.com/v3/merchants/{merchant_id}/tokens', [
            'headers' => [
                'Authorization' => 'Bearer {your_access_token}',
                'Content-Type' => 'application/json',
            ],
            'json' => [
                'card' => [
                    'number' => $request->input('card_number'),
                    'exp_month' => $request->input('exp_month'),
                    'exp_year' => $request->input('exp_year'),
                    'cvv' => $request->input('cvv'),
                ],
            ],
            ]
        );

        $data = json_decode($response->getBody()->getContents(), true);

        return response()->json(
            [
            'success' => true,
            'token' => $data['id'],
            ]
        );
    } catch (\Exception $e) {
        return response()->json(
            [
            'success' => false,
            'message' => $e->getMessage(),
            ], 500
        );
    }
}
```
```php
public function getBearerToken()
    {
        $client = new Client();
        dd($client);
        try {
            $response = $client->post(
                'https://sandbox.dev.clover.com/oauth/token', [
                'form_params' => [
                    'client_id' => '{your_client_id}',
                    'client_secret' => '{your_client_secret}',
                    'grant_type' => 'client_credentials',
                ],
                ]
            );

            $data = json_decode($response->getBody()->getContents(), true);

            return response()->json(
                [
                'success' => true,
                'access_token' => $data['access_token'],
                ]
            );
        } catch (\Exception $e) {
            return response()->json(
                [
                'success' => false,
                'message' => $e->getMessage(),
                ], 500
            );
        }
    }
```
```php
/***********************************
     * Create a notification for an app *
     * ***********************************
     */
    public function appNotification(Request $request)
    {

        $app_id         = "YW3KK3G2AH3A0";
        $app_secret     = "e2cb2605-5c43-c10f-5112-d6223bc57208";
        $merchant_id    = "KKR1SFW45GE91";
        
        $curl = curl_init();

        curl_setopt_array(
            $curl, [
            CURLOPT_URL => "https://sandbox.dev.clover.com/v3/apps/" . $app_id . "/merchants/" . $merchant_id . "/notifications",
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_ENCODING => "",
            CURLOPT_MAXREDIRS => 10,
            CURLOPT_TIMEOUT => 30,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => "POST",
            CURLOPT_HTTPHEADER => [
                "authorization: Bearer " . $app_secret,
                "content-type: application/json"
            ],
            ]
        );

        $response = curl_exec($curl);
        $err = curl_error($curl);

        curl_close($curl);

        if ($err) {
            echo "cURL Error #:" . $err;
        } else {
            echo $response;
        }


    }
```