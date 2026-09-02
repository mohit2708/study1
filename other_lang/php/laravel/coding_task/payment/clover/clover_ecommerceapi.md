### Step1:-
* get the marchent id
* get the ecommerce api.
```laravel
public function cloverKeys(){
        $merchant_id = "Y6W3BKM6G47V2";
        // $token = "23452345252435235";
        $token = "3245235423453425345";
        return [$merchant_id, $token];
    }


    public function cloverPAKMSkeys(){
        $keysInfo = $this->cloverKeys();
        list($merchant_id, $token) = $keysInfo;
        $client = new \GuzzleHttp\Client();
        $pakms = $client->request('GET', 'https://scl-sandbox.dev.clover.com/pakms/apikey', [
            'headers' => [
                'accept' => 'application/json',
                'authorization' => 'Bearer ' . $token, //Ecommerce API Private Tokens
            ],
        ]);
        $resp_pakms =  json_decode($pakms->getBody(), true);
        return $resp_pakms;
    }

    public function createCloverCard(){
        $resp_pakms = $this->cloverPAKMSkeys();         # Calling pakms function 
        $apiAccessKey =  $resp_pakms['apiAccessKey'];
        // dd($resp_pakms, $apiAccessKey);
        $client = new \GuzzleHttp\Client();

        $card = $client->post('https://token-sandbox.dev.clover.com/v1/tokens', [
            'headers' => [
                'accept' => 'application/json',
                'apikey' => $apiAccessKey,
                // 'apikey' => '24e5f44ab026043ff35cc5c64cd33b49',
                'content-type'  => 'application/json'
            ],
            'json' => [
                'card' => [
                    'number' => '4242424242424242',
                    'exp_month' => '12',
                    'exp_year' => '2025',

                    'cvv' => '123',
                    'brand' => 'VISA'
                ]

            ]
        ]);
        $card_token =  json_decode($card->getBody(), true);
        return $card_token;
    }

    public function createCloverCustomer(){
        $client = new \GuzzleHttp\Client();
        $keysInfo = $this->cloverKeys();
        list($merchant_id, $token) = $keysInfo;
        $card_token = $this->createCloverCard();

        $customer = $client->post('https://sandbox.dev.clover.com/v3/merchants/'.$merchant_id.'/customers', [
            'headers' => [
                'accept' => 'application/json',
                'content-type'  => 'application/json',
                'authorization' => 'Bearer ' . $token,
            ],
            'json' => [
                'cards' => [
                    [
                        'first6' => '424242',
                        'last4' => '4242',
                        'firstName' => 'Rohit',
                        'lastName' => 'Kumar',
                        'expirationDate' => '2025',
                        'additionalInfo' => [
                            'default' => 'testing card'
                        ],
                        'cardType' => 'VISA',
                        'token' => $card_token['id'],
                        'tokenType' => 'MULTIPAY',
                        'modifiedTime' => 0,
                    ]
                ],
                'firstName' => 'Manish',
                'lastName' => 'Yadav',
                'addresses' => [
                    [
                        'address1' => 'Palson',
                        'address2' => 'Goverdhan',
                        'address3' => 'Gali No3',
                        'city' => 'Mathura',
                        'country' => 'IN',
                        'state' => 'Uttarpradesh',
                        'zip' => '28150'
                    ],
                ],
                'emailAddresses' => [
                    [
                        'emailAddress' => 'kishorp456797@yopmail.com',
                    ]
                ],
                'phoneNumbers' => [
                    [
                        'phoneNumber' => '8595118144',
                    ]
                ],
            ]
        ]);

        $created_customer = json_decode($customer->getBody()->getContents());
        return $created_customer;
        // echo "<pre>"; print_r($customers);
        // echo $customers->id;
        // echo "<br>";

    }

    public function cloverOrder(){
        $client = new \GuzzleHttp\Client();
        $keysInfo = $this->cloverKeys();
        list($merchant_id, $token) = $keysInfo;

        $customers = $this->createCloverCustomer(); # calling create customer function

        $order = $client->post('https://sandbox.dev.clover.com/v3/merchants/'.$merchant_id.'/orders', [
            'headers' => [
                'accept'        => 'application/json',
                'authorization' => 'Bearer ' . $token,
                'content-type'  => 'application/json'
            ],

            'json' => [
                'currency' => 'USD',
                'customer' => 'Kishor',
                'email' => 'kishorp456797@yopmail.com.com',
                'expand' => [
                    'string'
                ],
                'customer_id' => $customers->id,
                // 'customer_id' => 'A9624JVBE3756',
                'order_type' => 'SALE',
                'state' => 'OPEN',
                'total' => 99,
                'currency' => 'USD',
                'items' => [
                    [
                        'name' => 'samsungm30',
                        'amount' => 99,
                        'currency' => 'USD',
                        'description' => '',
                        'inventory_id' => 'string',
                        'quantity' => 1,
                        'tax_rates' => [
                            [
                                'name' => 'TAX1',
                                'rate' => 0
                            ],
                            [
                                'name' => 'TAX2',
                                'tax_amount' => 0
                            ],
                            [
                                'name' => 'TEX3',
                                'tax_rate_uuid' => '123'
                            ]
                        ],
                        'type' => 'shipping'
                    ]
                ],
                'metadata' => [
                    'additionalProp' => 'string'
                ],
                'shipping' => [
                    'address' => [
                        'city' => 'Mathura',
                        'country' => 'US',
                        'line1' => 'Palson',
                        'line2' => 'Goverdhan',
                        'postal_code' => '12345',
                        'state' => 'UP'
                    ],
                    'name' => 'M1',
                    'phone' => 'Pandey'
                ]
            ]

        ]);

        $orders = json_decode($order->getBody()->getContents());
        return $orders;
        // echo '<br>';
        // echo "<pre>"; print_r($orders);
        // echo $orders->id;
        // echo "<br>";
    }



    public function clover()
    {
        $client = new \GuzzleHttp\Client();
        $keysInfo = $this->cloverKeys();
        list($merchant_id, $token) = $keysInfo;

        $card_token = $this->createCloverCard();    # Ceeate Card Function
       
        
        if ($card_token) {      
            $customers = $this->createCloverCustomer(); # calling create customer function
            $orders = $this->cloverOrder(); 

            $charge = $client->post('https://scl-sandbox.dev.clover.com/v1/charges', [
                'headers' => [
                    'accept'        => 'application/json',
                    'authorization' => 'Bearer ' . $token,
                    'content-type'  => 'application/json'
                ],
                'json' => [
                    'amount' => 99,
                    'currency' => 'USD',
                    'source' => $card_token['id'],
                    'orderId' => $orders->id,
                    'customerId' => $customers->id,
                ]
            ]);
        }

        // echo "<br>";
        $status = json_decode($charge->getBody()->getContents());
        echo "<pre>"; print_r($status);
        echo "<br>";
        die;
    }
```