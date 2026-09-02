### Install Twilio
```php
composer require twilio/sdk
```

### Set configration in env file
- create the api key and secret key
```php
TWILIO_ACCOUNT_SID=ACxxxxxxxx   # live account id
TWILIO_API_KEY=SKxxxxxxxx
TWILIO_API_SECRET=xxxxxxxx
```

### create Token Function for self use and api
```php
use App\Http\Controllers\Api\TwilioController;

Route::get('/twilio_access_token',[TwilioController::class,'twilioGenerateToken']);

# Create controller
use Twilio\Jwt\AccessToken;
use Twilio\Jwt\Grants\VideoGrant;

public function twilioGenerateToken()
{
    $accountSid = env('TWILIO_ACCOUNT_SID');
    $apiKeySid = env('TWILIO_API_KEY_SID');
    $apiKeySecret = env('TWILIO_API_KEY_SECRET');

    $identity = uniqid();

    // Create an Access Token
    $token = new AccessToken(
        $accountSid,
        $apiKeySid,
        $apiKeySecret,
        3600,
        $identity
    );

    // Grant access to Video
    $grant = new VideoGrant();
    $grant->setRoom('cool room');
    $token->addGrant($grant);

    // Serialize the token as a JWT
    echo $token->toJWT();
}
```

### Blade file
```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Twilio Video Call</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Twilio Video SDK -->
    <script src="https://sdk.twilio.com/js/video/releases/2.28.1/twilio-video.min.js"></script>

    <!-- Axios -->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #video-chat-window {
            display: flex;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        video {
            width: 300px;
            height: auto;
            margin: 10px;
            border-radius: 8px;
            background: #000;
        }
    </style>
</head>
<body>

<h2>Laravel + Twilio Video Call</h2>

<button onclick="getAccessToken()">Join Room</button>

<div id="video-chat-window"></div>

<script>
    let room = null;
    let accessToken = null;

    // 1️⃣ Get token from Laravel
    function getAccessToken() {
        axios.get('/api/access_token')
            .then(response => {
                accessToken = response.data;
                connectToRoom();
            })
            .catch(error => {
                console.error('Access token error:', error);
            });
    }

    // 2️⃣ Connect to Twilio room (SAFE CONFIG)
    function connectToRoom() {
        Twilio.Video.connect(accessToken, {
            name: 'cool-room',
            audio: true,
            video: {
                width: 640,
                height: 480,
                frameRate: 24
            }
        }).then(joinedRoom => {

            room = joinedRoom;
            console.log('Connected to room:', room.name);

            const container = document.getElementById('video-chat-window');

            // 3️⃣ Attach LOCAL tracks
            room.localParticipant.tracks.forEach(publication => {
                if (publication.track) {
                    container.appendChild(publication.track.attach());
                }
            });

            // 4️⃣ Attach EXISTING remote participants
            room.participants.forEach(participant => {
                attachParticipantTracks(participant);
            });

            // 5️⃣ When new participant joins
            room.on('participantConnected', participant => {
                console.log('Participant connected:', participant.identity);
                attachParticipantTracks(participant);
            });

            // 6️⃣ When participant leaves
            room.on('participantDisconnected', participant => {
                console.log('Participant disconnected:', participant.identity);
                detachParticipantTracks(participant);
            });

            // 7️⃣ Cleanup on disconnect
            room.on('disconnected', () => {
                room.localParticipant.tracks.forEach(publication => {
                    publication.track.stop();
                });
            });

        }).catch(error => {
            console.error('Connection failed:', error);
        });
    }

    // Attach remote participant tracks
    function attachParticipantTracks(participant) {
        const container = document.getElementById('video-chat-window');

        participant.tracks.forEach(publication => {
            if (publication.isSubscribed) {
                container.appendChild(publication.track.attach());
            }
        });

        participant.on('trackSubscribed', track => {
            container.appendChild(track.attach());
        });

        participant.on('trackUnsubscribed', track => {
            track.detach().forEach(el => el.remove());
        });
    }

    // Remove participant tracks
    function detachParticipantTracks(participant) {
        participant.tracks.forEach(publication => {
            if (publication.track) {
                publication.track.detach().forEach(el => el.remove());
            }
        });
    }

    // 8️⃣ Disconnect cleanly on page close
    window.addEventListener('beforeunload', () => {
        if (room) {
            room.disconnect();
        }
    });
</script>

</body>
</html>

```