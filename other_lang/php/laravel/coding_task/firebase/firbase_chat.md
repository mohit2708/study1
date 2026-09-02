Route
```php
Route::get('/chat', [ChatBotController::class, 'index1']);
Route::post('/chat/send', [ChatBotController::class, 'send']);
```

```php
public function index1(User $user)
    {
        return view('chat.chat', [
            'users' => User::where('id', '!=', auth()->id())->get()
        ]);
    }
```

### blade file
- real time chat with online show
```php
<!DOCTYPE html>
<html>
<head>
    <title>Real Time Chat</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Firebase -->
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-database-compat.js"></script>

    <style>
        .user-item { cursor:pointer; padding:10px; border-bottom:1px solid #ddd; }
        .user-item:hover { background:#f5f5f5; }
        #chat-box { height:400px; overflow-y:auto; border:1px solid #ddd; padding:10px; }
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
</style>


<div class="container mt-4">
    <div class="row">

        <!-- LEFT SIDE: USER LIST -->
        <div class="col-sm-6 border">
            <h5>Users</h5>
                   <div id="userList">
                    @foreach($users as $user)
                        <div class="user-item" id="user-{{ $user->id }}"
                            onclick="openChat({{ $user->id }}, '{{ $user->name }}')">
                            <span class="status-dot bg-secondary"></span>
                            {{ $user->name }} ---- ----{{$user->email}}
                        </div>
                    @endforeach
        </div>
        </div>



        <!-- RIGHT SIDE: CHAT BOX -->
        <div class="col-sm-6">
            <h5 id="chatUser">Select User</h5>
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

<script>
    let chatId = null;
/* ================= FIREBASE CONFIG ================= */
// const firebaseConfig = {
//     apiKey: "API_KEY",
//     authDomain: "PROJECT.firebaseapp.com",
//     databaseURL: "https://PROJECT-default-rtdb.firebaseio.com",
//     projectId: "PROJECT",
// };


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



</body>
</html>

```


### some time database rules issue
- Go to Firebase Console → Realtime Database → Rules
```php
{
  "rules": {
    ".read": true,
    ".write": true
  }
}

# or----
{
  "rules": {
    "typing": {
      "$chatId": {
        "$userId": {
          ".read": "auth != null",
          ".write": "auth != null && auth.uid === $userId"
        }
      }
    },
    "chats": {
      "$chatId": {
        ".read": "auth != null",
        ".write": "auth != null"
      }
    },
    "status": {
      "$user": {
        ".read": true,
        ".write": "auth != null"
      }
    }
  }
}

```