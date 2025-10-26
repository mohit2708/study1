* Staging Token:- 9dca13ce-5f03-ea6f-3f63-0d4a91258d30
* Stagging MID:-  F6W3VKM6G13V1

### Create a refund(refund api)
```
Page URL:- https://docs.clover.com/dev/reference/createrefund
API Url:- https://scl-sandbox.dev.clover.com/v1/refunds
```
### Get a single refund Details
* Requered Merchant identifier (mId) and Refund identifier (refundId)
```
Page URL:- https://docs.clover.com/dev/reference/paygetrefund-3
Api URL:- https://sandbox.dev.clover.com/v3/merchants/{mId}/refunds/{refundId}
Method:- GET
```

### Get a single payment
```
Page URL:- https://docs.clover.com/dev/reference/paygetpayment
API URL:- https://sandbox.dev.clover.com/v3/merchants/{mId}/payments/{payId}
Method:- GET
```

### device notification
```
https://www.clover.com/v3/apps/GW67H8PKRC3RT/devices/ee31503f-0524-4deb-74ce-aae482d42e64/notifications
Set Headers:

Go to the Headers tab.

Add the following headers:

Key: authorization, Value: Bearer 646771e9-1124-7418-1d5c-aee0c9ff6c15

Key: Content-Type, Value: application/json
------------
Go to the Body tab.

Select raw (this will let you enter raw JSON data).

In the dropdown on the right side, select JSON as the format.

Paste the following JSON data in the body section:
```

### Get a charge 
```
Page URl:- https://docs.clover.com/dev/reference/getchargescharge
Api URL:- https://scl-sandbox.dev.clover.com/v1/charges/{chargeId}
```

### **AppNotification**
```php
public function appNotification(Request $request)
{
    $app_id = "YW3KK3G2AH3A0";
    $app_secret = "e2cb2605-5c43-c10f-5112-d6223bc57208";
    $merchant_id = "KKR1SFW45GE91";

    $curl = curl_init();

    curl_setopt_array($curl, [
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
    ]);

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