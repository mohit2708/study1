### Update data
```php
/**
     * Update
     *
     * @param  mixed $request
     * @return void
     */
    public function update(Request $request) {
        try{
            $validator = Validator::make($request->all(), [ 
                'campaign_id'          => 'required',
            ]);
        
            if ($validator->fails()) {
                return response()->json($validator->errors(), 422);
            }
            $campaign                     =Campaign::find($request->input('campaign_id'));
            $campaign->lead_type          = $request->input('lead_type') ? $request->input('lead_type') : $campaign->lead_type;
            $campaign->industry_type      = $request->input('industry_type')  ? $request->input('industry_type') : $campaign->industry_type;
            $campaign->quality_type       = $request->input('quality_type') ? $request->input('quality_type') : $campaign->quality_type;
            $campaign->area_type          = $request->input('area_type') ? $request->input('area_type') : $campaign->area_type;
            $campaign->states             = $request->input('states') ? $request->input('states') : $campaign->states;                        
            $campaign->update();
            $message = "Campaign Update Successfully!!";

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
```