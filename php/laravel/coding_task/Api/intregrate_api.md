### Post API intrgrates
```php
use Illuminate\Support\Facades\Http;

$ai_base_url = env('AI_BASE_URL');
$payload = [
    "project_name" => $request->project_name,
    "location"     => $request->location,
    "Client"       => $request->client,
];

$response = Http::withHeaders([
    'Accept'=> '*/*',
    'User-Agent'=> 'Laravel Client',
    'Content-Type'=> 'application/json',
])
->withBody(json_encode($payload), 'application/json')
->post($ai_base_url. '/create_project');

$data = $response->json();   // convert to array
// return back()->with('message', $data['message']);
return redirect()->route('project.list')->with('toast', [
    'type' => 'success',
    'title' => 'Success',
    'message' => $data['message'] ?? 'Project created successfully!',
    'delay' => 3000
]);             
```

### Get API
```php
$ai_base_url = env('AI_BASE_URL');
// Always use a default or handle the case where the env variable might be missing
if (!$ai_base_url) {
    return back()->with('error', 'AI Base URL is not configured.');
}

try {
    $response = Http::withHeaders([
        'Accept' => '*/*',
        'User-Agent' => 'Thunder Client (https://www.thunderclient.com)', // Optional header
    ])->get($ai_base_url . '/count_projects');
    // Check if the response was successful (status code 200-299)
    if ($response->failed()) {
        // Get the error message from the response body if available, or a generic message
        $errorMessage = $response->json()['message'] ?? 'Could not connect to the AI service. Please try again later.';
        
        return back()->with('error', $errorMessage);
    }

    $data = $response->json();

    // Check if the expected data key exists in the response
    if (!isset($data['project_details'])) {
        return back()->with('error', 'Invalid response format from the AI service.');
    }

    return view('aiml.project.list', [
        'projects' => $data['project_details']
    ]);

} catch (\Exception $e) {
    // This catches low-level connection errors (e.g., DNS issues, host down)
    return back()->with('error', 'A network error occurred: ' . $e->getMessage());
}
```