### Chat with firbase and video calling
```php
@extends('home')
@section('content')
    <!-- <title>Real Time Chat</title> -->
    <!-- Firebase -->
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-database-compat.js"></script>
    <script src="https://sdk.twilio.com/js/video/releases/2.28.1/twilio-video.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

    <style>
        .user-item { cursor:pointer; padding:10px; border-bottom:1px solid #ddd; }
        .user-item:hover { background:#f5f5f5; }
        #chat-box {
            height: calc(100vh - 300px);
            overflow-y: auto;
            border: 1px solid #ddd;
            padding: 10px;
            background: #fff;
        }
        #userList {
            height: calc(100vh - 200px);    /* same as chat box or whatever you want */
            overflow-y: auto;
            border-top: 1px solid #ddd;
        }
button.btn.audio-btn {
    background-color: #6d6d6d;
}
    </style>
</head>
<body>
    <style>
.status-dot {
    width:10px;
    height:10px;
    border-radius:50%;
    display:inline-block;
    margin-right:6px;
}
.online { background:green; }
.offline { background:gray; }
/* user chat css start here */
.user_btn {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}
h5#chatUser {
    margin: unset;
}
.chat_flex_wrap {
    background: #e1ffe1;
    padding: 20px;
    box-sizing: border-box;
    border-radius: 10px;
    border: 1px solid #eee;
}
.section_wrap {
    background: #fff;
    padding: 20px;
    box-sizing: border-box;
    border-radius: 10px;
}
.btn_flex button {
    background: #0db40e;
    color: #fff;
}
.btn_flex button:focus, .btn_flex button:hover{
border: 1px solid #0db40e;
background: unset;
color: #0db40e;
}

button.btn.audio-btn:focus,button.btn.audio-btn:hover {
   border: 1px solid #6d6d6d;
background: unset;
color: #6d6d6d;
}
.left_panel h5 {
    background: #eee;
    padding: 12px 10px;
    border-radius: 4px 4px 0 0;
    margin: unset;
}
div#video-modal .modal-body div#video-chat-window video {
    width: 100%;
}
div#video-chat-window {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}
div#video-chat-window {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

div#video-modal .modal-header {
    background: #5b5b5b;
    color: #fff;
}

div#video-modal .modal-header h1#exampleModalLabel {
    color: #fff;
}

div#video-modal .modal-header button.btn-close {
    color: #fff;
    filter: invert(1);
    opacity: 1;
}
/* user chat css start here */
</style>

<!-- <button onclick="getAccessToken()">Join Room</button> -->


<div class="section_wrap">
    <div class="row">

        <!-- LEFT SIDE: USER LIST -->
        <div class="col-sm-6">
           <div class="left_panel">
                <h5>Users</h5>
                   <div id="userList">
                    @foreach($users as $user)
                        <div class="user-item" id="user-{{ $user->id }}"
                            onclick="openChat({{ $user->id }}, '{{ $user->name }}')">
                            <span class="status-dot bg-secondary"></span>
                            {{ $user->id }} - {{ $user->name }} - {{$user->email}} 
                        </div>
                    @endforeach
        </div>
           </div>
        </div>



        <!-- RIGHT SIDE: CHAT BOX -->
        <div class="col-sm-6">
            <div class="chat_flex_wrap">
<div class="user_btn">
                <h5 id="chatUser">Select User</h5>
                <div class="btn_flex">
                    <button class="btn video-btn" type="button" onclick="getAccessToken()" data-bs-toggle="modal" data-bs-target="#video-modal">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-video"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M15 10l4.553 -2.276a1 1 0 0 1 1.447 .894v6.764a1 1 0 0 1 -1.447 .894l-4.553 -2.276v-4" /><path d="M3 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2l0 -8" /></svg>
                    </button>
                  <!--   <button class="btn audio-btn" type="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-phone"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" /></svg>
                    </button> -->
                </div>
</div>
            <small id="typingIndicator" class="text-muted" style="display:none;">
                typing...
            </small>
            <div id="chat-box"></div>

            <div class="mt-2 d-flex">
                <input type="text" id="message" class="form-control" placeholder="Type message">
                <button class="btn btn-primary ms-2" onclick="sendMessage()">Send</button>
            </div>
        </div>
        </div>
</div>
    </div>

<div class="modal fade" id="video-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
       <div id="video-chat-window"></div>
      </div>
      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div> -->
    </div>
  </div>
</div>

<script>
    let chatId = null;
    /* ================= FIREBASE CONFIG ================= */
    const firebaseConfig = {
      apiKey: "AIzaSyCU1D_8jmXBr2N2_nl8TS3dTcx7bHp0gGk",
      authDomain: "dispatchchannel-a74d0.firebaseapp.com",
      databaseURL: "https://dispatchchannel-a74d0-default-rtdb.firebaseio.com",
      projectId: "dispatchchannel-a74d0",
    };

    firebase.initializeApp(firebaseConfig);

    /* ================= Script for Online ================= */
    const userId = {{ auth()->id() }};

    const userStatusRef = firebase.database().ref('status/user_' + userId);
    const connectedRef = firebase.database().ref('.info/connected');

    connectedRef.on('value', function(snapshot) {
        if (snapshot.val() === true) {

            userStatusRef.onDisconnect().set({
                state: 'offline',
                last_seen: Date.now()
            });

            userStatusRef.set({
                state: 'online',
                last_seen: Date.now()
            });
        }
    });
    /* ================= End Script for Online ================= */

    const database = firebase.database();

    /* ================= GLOBAL VARS ================= */
    const senderId = {{ auth()->id() }};
    let receiverId = null;
    let chatRef = null;

    /* ================= OPEN CHAT ================= */
    function openChat(userId, userName) {
        receiverId = userId;
        document.getElementById('chatUser').innerText = userName;
        document.getElementById('chat-box').innerHTML = '';
        alert(receiverId);

        const chatId = senderId < receiverId
            ? senderId + "_" + receiverId
            : receiverId + "_" + senderId;

        chatRef = database.ref("chats/" + chatId);

        chatRef.off(); // remove old listeners

        chatRef.on("child_added", function(snapshot) {
            const msg = snapshot.val();

            let align = msg.sender_id == senderId ? 'text-end' : 'text-start';
            let bg = msg.sender_id == senderId ? 'bg-primary text-white' : 'bg-info';

            document.getElementById('chat-box').innerHTML += `
                <div class="${align}">
                    <span class="badge ${bg} m-1">${msg.message}</span>
                </div>
            `;

            document.getElementById('chat-box').scrollTop =
                document.getElementById('chat-box').scrollHeight;
        });
    }

    /* ================= SEND MESSAGE ================= */
    function sendMessage_before_typing() {
        if (!receiverId) {
            alert('Select a user');
            return;
        }

        let message = document.getElementById('message').value;
        if (message.trim() === '') return;

        chatRef.push({
            sender_id: senderId,
            receiver_id: receiverId,
            message: message,
            timestamp: Date.now()
        });

        document.getElementById('message').value = '';
    }

    function sendMessage() {
        if (!receiverId) return;

        let message = document.getElementById('message').value;
        if (message.trim() === '') return;

        chatRef.push({
            sender_id: senderId,
            receiver_id: receiverId,
            message: message,
            timestamp: Date.now()
        });

        // stop typing
        firebase.database()
            .ref('typing/' + chatRef.key + '/' + senderId)
            .set(false);

        document.getElementById('message').value = '';
    }

</script>


<script>
    /* ================= Script for Online ================= */
    const users = @json($users->pluck('id'));

    users.forEach(function(uid) {
        const statusRef = firebase.database().ref('status/user_' + uid);

        statusRef.on('value', function(snapshot) {
            const data = snapshot.val();
            const el = document.getElementById('user-' + uid);

            if (!el) return;

            const dot = el.querySelector('.status-dot');

            if (data && data.state === 'online') {
                dot.className = 'status-dot online';
                moveUserToTop(el);
            } else {
                dot.className = 'status-dot offline';
            }
        });
    });

    function moveUserToTop(element) {
        const parent = document.getElementById('userList');
        parent.prepend(element);
    }
</script>


<script>
    let typingTimeout = null;

    document.getElementById('message').addEventListener('input', function () {
        if (!chatRef) return;

        const typingRef = firebase.database()
            .ref('typing/' + chatRef.key + '/' + senderId);

        typingRef.set(true);

        clearTimeout(typingTimeout);
        typingTimeout = setTimeout(() => {
            typingRef.set(false);
        }, 1000);
    });


    const typingRef = firebase.database()
        .ref('typing/' + chatId + '/' + receiverId);

    typingRef.on('value', function(snapshot) {
        if (snapshot.val() === true) {
            document.getElementById('typingIndicator').style.display = 'block';
        } else {
            document.getElementById('typingIndicator').style.display = 'none';
        }
    });



    window.addEventListener('beforeunload', function () {
        if (chatRef) {
            firebase.database()
                .ref('typing/' + chatRef.key + '/' + senderId)
                .set(false);
        }
    });

</script>

<script>
    let room = null;
    let accessToken = null;
    let roomName = null;
    let localTracks = [];

    // 1️⃣ Get token from Laravel
    function getAccessToken() {
        if (!receiverId) {
            alert('Select a user first');
            return;
        }
        console.log('Receiver ID being sent:', receiverId);
        axios.get(`/api/twilio_access_token/${receiverId}`)
            .then(res => {
                accessToken = res.data.token;
                roomName = res.data.roomName;

                if (typeof accessToken !== 'string') {
                    throw new Error('Invalid access token');
                }

                connectToRoom();
            })
            .catch(err => {
                console.error('Token error:', err);
            });
    }

    // 2️⃣ Connect to Twilio room (SAFE CONFIG)
    function connectToRoom() {
        Twilio.Video.connect(accessToken, {
            name: roomName,   // ✅ dynamic room name from API
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

            // Local tracks
            room.localParticipant.tracks.forEach(publication => {
                if (publication.track) {
                    container.appendChild(publication.track.attach());
                }
            });

            // Existing participants
            room.participants.forEach(participant => {
                attachParticipantTracks(participant);
            });

            // New participant
            room.on('participantConnected', participant => {
                attachParticipantTracks(participant);
            });

            // Participant left
            room.on('participantDisconnected', participant => {
                detachParticipantTracks(participant);
            });

            // Cleanup
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
@endsection
```

### Controller
- for chat function
```php
public function index(User $user){
    $specialUser = User::where('id', 19430)->first();

    $users = User::where('id', '!=', auth()->id())
        ->where('role','admin')
        ->get();

    if ($specialUser) {
        $users->push($specialUser);
    }

    return view('techAssist.chat', compact('users'));
}
```

### API