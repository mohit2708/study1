### delete data
```php
public function destroy(Request $request) {
        try{
            $campaign = Campaign::findOrFail($request->campaign_id);
            $result = $campaign->delete();
            if($result){
                return response()->json([
                    'success' => True,
                    'message' => "Campaign has been deleted",
                    'status' => 200
                ],200);
            }
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