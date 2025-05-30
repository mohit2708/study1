### get list
```php
/**
     * getCampaignList
     *
     * @param  mixed $request
     * @return void
     */
    public function getCampaignList(Request $request){
        try{
            $campaignData = ModelName::orderBy('id','desc')->get();
            $campaignData = ModelName::get();
            return response()->json([
                'success' => True,
                'message' => "Campaign List get successfully",
                'data' => $campaignData,
                'status' => 200
            ],200);
        }
        catch(\Exception $e)
        {
            return response()->json([
                'success' => False,
                'message' => $e->getMessage(),
                'status' => 500
            ],500);
        }
    }
```
