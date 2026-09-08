### Get list API through gazal
```php
/**
 * getLeadDetails
 *
 * @param  mixed $request
 * @return void
 */
public function getLeadDetails(Request $request){
    try
    {
        $reqParamArray = array();
        $reqParamArray['Key'] = 'afe24aebdcfda2f47c5926392436ba240b13ce78fbfa4393cfba6afd1f155d9f';
        $reqParamArray['API_Action'] = "getLeadDetails";
        $reqParamArray['Format'] = "json";
        $reqParamArray['Lead_Type'] = $request->lead_type;

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
            'message' => "Leads List get successfully",
            'data' => $response['response'],
            'status' => 200
        ],200);
    }
    catch(\Exception $e){
        return $e->getMessage();
    }
}
```