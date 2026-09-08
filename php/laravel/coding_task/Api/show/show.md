### show data
```php
/**
 * Show
 *
 * @param  mixed $request
 * @return void
 */
public function show(Request $request) {
    $validator = Validator::make($request->all(), [ 
        'campaign_id' => 'required|exists:campaigns,id',
    ]);

    if ($validator->fails()) {
        return response()->json($validator->errors(), 422);
    }
    try{
        $campaign_id = $request->campaign_id;
        $campaign=Campaign::findOrFail($campaign_id);
        if($campaign){
            return response()->json([
                'success' => True,
                'campaignData' => $campaign,
                'status' => 200
            ],200);
        }
    }catch(\Exception $e){
        return response()->json([
            'success' => False,
            'message' => $e->getMessage(),
            'status' => 500
        ],500);
    }
}
```