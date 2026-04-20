### js file
```php
/* ================= FIREBASE CONFIG ================= */
const firebaseConfig = {
  apiKey: "AIzaSyCU1D_8jmXBr2N2_nl8TS3dTcx7bHp0gGk",
  authDomain: "dispatchchannel-a74d0.firebaseapp.com",
  databaseURL: "https://dispatchchannel-a74d0-default-rtdb.firebaseio.com",
  projectId: "dispatchchannel-a74d0",
  messagingSenderId: "908042904984",
  appId: "1:908042904984:web:d79e3b7c26c039f4ce77ed"
};

firebase.initializeApp(firebaseConfig);
const database = firebase.database();

/* ================= GLOBAL VARS ================= */
const senderId = window.Laravel.userId;
// let receiverId = null;
window.receiverId = null;
let chatRef = null;
let typingTimeout = null;
let lastMessageDate = null;
let unreadCounts = {};
let chatListener = null;


function sendCallLog(type, status, duration = null) {
    if (!chatRef) return;

    chatRef.push({
        sender_id: senderId,
        receiver_id: receiverId,
        call_type: type,
        call_status: status,
        duration: duration,
        timestamp: Date.now()
    });
}



/* ================= ONLINE STATUS ================= */
const userStatusRef = firebase.database().ref('status/user_' + senderId);
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

/* ================= OPEN CHAT ================= */
function openChat(userId, userName) {

    lastMessageDate = null;
    window.receiverId = userId;

    // reset unread count for this user
    unreadCounts[userId] = 0;
    updateUnreadBadge(userId);

    document.getElementById('chatUser').innerText = userName;
    document.getElementById('chat-box').innerHTML = '';

    const chatId = senderId < receiverId
        ? senderId + "_" + receiverId
        : receiverId + "_" + senderId;

    const newChatRef = database.ref("chats/" + chatId);

    /* DETACH OLD LISTENER SAFELY */
    if (chatListener && chatRef) {
        chatRef.off('child_added', chatListener);
    }

    chatRef = newChatRef;

    /* MARK MESSAGES AS READ */
    chatRef.once("value", function (snapshot) {
        snapshot.forEach(function (child) {
            const msg = child.val();

            if (msg.receiver_id == senderId && !msg.read) {
                child.ref.update({ read: true });
            }
        });
    });

    /* DEFINE LISTENER (STORE IT) */
    chatListener = function (snapshot) {

        const msg = snapshot.val();

        /* ✅ IF CHAT IS OPEN → MARK INSTANT READ */
        if (msg.receiver_id == senderId && !msg.read) {
            snapshot.ref.update({ read: true });
        }

        const msgDate = new Date(msg.timestamp).toDateString();

        if (lastMessageDate !== msgDate) {
            lastMessageDate = msgDate;

            const label = getDateLabel(msg.timestamp);

            document.getElementById('chat-box').innerHTML += `
                <div class="text-center my-2">
                    <span class="badge bg-secondary">${label}</span>
                </div>
            `;
        }

        let align = msg.sender_id == senderId ? 'text-end' : 'text-start';
        let bg = msg.sender_id == senderId ? 'bg-primary text-white' : 'bg-info';

        const time = formatTime(msg.timestamp);

        let content = '';

        /* 📞 CALL LOG */
        if (msg.call_type) {

            const icon = msg.call_type === 'video' ? '📹' : '📞';

            if (msg.call_status === 'started') {
                content = `${icon} ${msg.call_type} call started`;
            }

            if (msg.call_status === 'missed') {
                content = `${icon} Missed ${msg.call_type} call`;
            }

            if (msg.call_status === 'ended') {

                let durationText = '';

                if (msg.duration) {
                    const min = Math.floor(msg.duration / 60);
                    const sec = msg.duration % 60;
                    durationText = ` (${min}:${sec.toString().padStart(2, '0')})`;
                }

                content = `${icon} ${msg.call_type} call ended${durationText}`;
            }

            document.getElementById('chat-box').innerHTML += `
                <div class="text-center my-2">
                    <span class="badge bg-light text-dark">${content}</span>
                </div>
            `;
        }

        /* 📎 FILE MESSAGE */
        else if (msg.file_url) {

            content = `
                <a href="${msg.file_url}" target="_blank" class="text-white">
                    📎 ${msg.file_name}
                </a>
            `;

            document.getElementById('chat-box').innerHTML += `
                <div class="${align}">
                    <div class="d-inline-block m-1">
                        <div class="badge ${bg}">${content}</div>
                        <div class="small text-muted text-${align === 'text-end' ? 'end' : 'start'}">
                            ${time}
                        </div>
                    </div>
                </div>
            `;
        }

        /* 💬 TEXT MESSAGE */
        else {

            content = msg.message;

            document.getElementById('chat-box').innerHTML += `
                <div class="${align}">
                    <div class="d-inline-block m-1">
                        <div class="badge ${bg}">${content}</div>
                        <div class="small text-muted text-${align === 'text-end' ? 'end' : 'start'}">
                            ${time}
                        </div>
                    </div>
                </div>
            `;
        }

        document.getElementById('chat-box').scrollTop =
        document.getElementById('chat-box').scrollHeight;
        const isNearBottom = chatBox.scrollHeight - chatBox.scrollTop - chatBox.clientHeight < 100;
        if (isNearBottom) {
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    };

    /* 🔥 ATTACH LISTENER */
    chatRef.on("child_added", chatListener);

    listenTyping(chatId);
}

/* ================= SEND MESSAGE ================= */
function sendMessage() {
    if (!receiverId) return;

    let message = document.getElementById('message').value;
    if (message.trim() === '') return;

    // chatRef.push({
    //     sender_id: senderId,
    //     receiver_id: receiverId,
    //     message: message,
    //     timestamp: Date.now()
    // });
    chatRef.push({
        sender_id: senderId,
        receiver_id: receiverId,
        message: message,
        timestamp: Date.now(),
        read: false
    });

    firebase.database()
        .ref('typing/' + chatRef.key + '/' + senderId)
        .set(false);

    document.getElementById('message').value = '';
    document.getElementById('message').style.height = 'auto';
}

/* ================= TYPING ================= */
document.addEventListener("DOMContentLoaded", function () {

    /* ================= Add Emoji start ================= */
    // Add variables
    const messageInput = document.getElementById('message');
    const emojiBtn = document.getElementById('emojiBtn');
    const pickerContainer = document.getElementById('emojiPicker');
    // Add Emoji Mart picker code
    const picker = new EmojiMart.Picker({
        theme: 'light',
        previewPosition: 'none',
        onEmojiSelect: (emoji) => {
            insertAtCursor(messageInput, emoji.native);
        }
    });

    pickerContainer.appendChild(picker);

    emojiBtn.addEventListener('click', () => {
        pickerContainer.style.display =
            pickerContainer.style.display === 'none' ? 'block' : 'none';
    });
    // Close picker when clicking outside
    document.addEventListener('click', function (e) {
        if (!pickerContainer.contains(e.target) && e.target !== emojiBtn) {
            pickerContainer.style.display = 'none';
        }
    });
    /* ================= End Emoji start ================= */

    // const messageInput = document.getElementById('message');

    // Typing indicator (your existing code)
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

    // ENTER to send message
    messageInput.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // stop new line
            sendMessage();      // call your existing function
        }
    });
});

function listenTyping(chatId) {
    const typingRef = firebase.database()
        .ref('typing/' + chatId + '/' + receiverId);

    typingRef.on('value', function(snapshot) {
        document.getElementById('typingIndicator').style.display =
            snapshot.val() === true ? 'block' : 'none';
    });
}

/* ================= USER ONLINE LIST ================= */
function initUserStatus(users) {
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
}



function moveUserToTop(element) {
    const parent = document.getElementById('userList');
    parent.prepend(element);
}


function formatTime(ts) {
    const date = new Date(ts);

    const hours = date.getHours();
    const minutes = date.getMinutes().toString().padStart(2, '0');

    const ampm = hours >= 12 ? 'PM' : 'AM';
    const hour12 = hours % 12 || 12;

    return `${hour12}:${minutes} ${ampm}`;
}


function formatDateTime(ts) {
    const date = new Date(ts);

    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();

    const hours = date.getHours();
    const minutes = date.getMinutes().toString().padStart(2, '0');

    const ampm = hours >= 12 ? 'PM' : 'AM';
    const hour12 = hours % 12 || 12;

    return `${day}/${month}/${year} ${hour12}:${minutes} ${ampm}`;
}


function getDateLabel(ts) {
    const msgDate = new Date(ts);
    const today = new Date();
    const yesterday = new Date();
    yesterday.setDate(today.getDate() - 1);

    const isToday =
        msgDate.toDateString() === today.toDateString();

    const isYesterday =
        msgDate.toDateString() === yesterday.toDateString();

    if (isToday) return "Today";
    if (isYesterday) return "Yesterday";

    return msgDate.toLocaleDateString('en-GB', {
        day: '2-digit',
        month: 'short',
        year: 'numeric'
    });
}


function updateUnreadBadge(userId) {
    const badge = document.getElementById('unread-' + userId);
    if (!badge) return;

    const count = unreadCounts[userId] || 0;

    if (count > 0) {
        badge.innerText = count;
        badge.classList.remove('d-none');
    } else {
        badge.classList.add('d-none');
    }
}

function markMessageAsRead(msgRef) {
    msgRef.update({
        read: true
    });
}

function loadInitialUnread(users) {

    users.forEach(function (uid) {

        const chatId = senderId < uid
            ? senderId + "_" + uid
            : uid + "_" + senderId;

        const ref = database.ref("chats/" + chatId);

        ref.once("value", function (snapshot) {

            let count = 0;

            snapshot.forEach(function (child) {

                const msg = child.val();

                if (
                    msg.receiver_id == senderId &&
                    msg.read !== true
                ) {
                    count++;
                }
            });

            unreadCounts[uid] = count;
            updateUnreadBadge(uid);
        });
    });
}

function listenForNewMessages(users) {

    users.forEach(function (uid) {

        const chatId = senderId < uid
            ? senderId + "_" + uid
            : uid + "_" + senderId;

        const ref = database.ref("chats/" + chatId);

        ref.limitToLast(1).on("child_added", function (snapshot) {

            const msg = snapshot.val();

            if (!msg) return;

            // only if message is for me
            if (msg.receiver_id == senderId) {

                // if chat open → mark read instantly
                if (window.receiverId == uid) {
                    snapshot.ref.update({ read: true });
                    return;
                }

                // avoid counting already read
                if (msg.read === true) return;

                unreadCounts[uid] = (unreadCounts[uid] || 0) + 1;
                updateUnreadBadge(uid);

                const el = document.getElementById('user-' + uid);
                if (el) moveUserToTop(el);
            }
        });
    });
}


function insertAtCursor(input, text) {
    const start = input.selectionStart;
    const end = input.selectionEnd;

    input.value =
        input.value.substring(0, start) +
        text +
        input.value.substring(end);

    input.selectionStart = input.selectionEnd = start + text.length;
    input.focus();
}

```
### blad file
```php
@extends('home')
@section('content')
    <!-- <title>Real Time Chat</title> -->


<!-- Firebase -->
<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-database-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-storage-compat.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/emoji-mart@latest/css/emoji-mart.css" />
<script src="https://cdn.jsdelivr.net/npm/emoji-mart@latest/dist/browser.js"></script>


<!-- Twilio -->
<script src="https://sdk.twilio.com/js/video/releases/2.28.1/twilio-video.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<link rel="stylesheet" href="{{ asset('admin/tech_assist/chat.css') }}">

<style>
    .audio-avatar {
    display: flex;
    justify-content: center;
}

.avatar-circle {
    width: 120px;
    height: 120px;
    background: #0d6efd;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.avatar-circle i {
    font-size: 48px;
    color: #fff;
}

.audio-controls button {
    min-width: 110px;
}


.user-item {
    cursor: pointer;
    padding: 8px;
    border-bottom: 1px solid #eee;
}

.user-item:hover {
    background: #f5f5f5;
}

.unread-badge {
    font-size: 12px;
    min-width: 22px;
    text-align: center;
}


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
                        <!-- <div class="user-item" id="user-{{ $user->id }}"
                            onclick="openChat({{ $user->id }}, '{{ $user->name }}')">
                            <span class="status-dot bg-secondary"></span>
                            {{ $user->id }} - {{ $user->name }} - {{$user->email}} 
                        </div> -->
                        <div class="user-item" id="user-{{ $user->id }}"
                            onclick="openChat({{ $user->id }}, '{{ $user->name }}')">

                            <div class="avatar">
                                {{ strtoupper(substr($user->name, 0, 1)) }}
                            </div>

                            <div class="user-info">
                                <div class="user-name">{{ $user->name }}</div>
                                <div class="user-email">{{ $user->email }}</div>
                            </div>

                            <span class="status-dot bg-secondary"></span>
                            <!-- UNREAD BADGE -->
                            <span class="unread-badge badge bg-danger d-none" id="unread-{{ $user->id }}">0</span>
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
                        @if (!request()->is('customer-support'))

                            <!-- <button class="btn video-btn" type="button" onclick="getAccessToken()" data-bs-toggle="modal" data-bs-target="#video-modal"> -->
                            <button class="btn video-btn" type="button" onclick="startVideoCall()">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-video"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M15 10l4.553 -2.276a1 1 0 0 1 1.447 .894v6.764a1 1 0 0 1 -1.447 .894l-4.553 -2.276v-4" /><path d="M3 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2l0 -8" /></svg>
                            </button>

                            <button class="btn audio-btn" type="button" onclick="startAudioCall()">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-phone"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" /></svg>
                            </button>
                        @endif
                    </div>
                </div>
                <small id="typingIndicator" class="text-muted" style="display:none;">
                    typing...
                </small>
                <div id="chat-box"></div>

            <!-- <div class="mt-2 d-flex">
                <input type="text" id="message" class="form-control" placeholder="Type message">
                <button class="btn btn-primary ms-2" onclick="sendMessage()">Send</button>
            </div> -->
            <div class="mt-2 d-flex align-items-end position-relative">
                <label for="fileInput" class="btn btn-light me-2 mb-0">📎</label>
                <input type="file" id="fileInput" hidden>

                <button class="btn btn-light me-2" id="emojiBtn">😊</button>

                <!-- EMOJI PANEL -->
                <div id="emojiPicker"
                     style="position:absolute; bottom:60px; left:0; display:none; z-index:1000;">
                </div>

                <textarea id="message"
                          class="form-control"
                          placeholder="Type message"
                          rows="1"
                          style="resize:none; overflow:hidden;"></textarea>

                <button class="btn btn-primary ms-2" onclick="sendMessage()">Send</button>
            </div>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="video-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <!-- <div class="modal-body">
       <div id="video-chat-window"></div>
      </div> -->
      <div class="modal-body text-center">
        <!-- VIDEO CONTAINER -->
        <div id="video-chat-window"></div>
        <!-- AUDIO CALL UI -->
        <div id="audio-call-ui" style="display:none;">
            <div class="audio-avatar">
                <div class="avatar-circle">
                    <i class="bi bi-person-fill"></i>
                </div>
            </div>
            <h4 id="audio-caller-name" class="mt-3">User</h4>
            <p id="call-status" class="text-muted">Calling...</p>
            <div class="audio-controls mt-4">
                <button class="btn btn-secondary" onclick="toggleMute()" id="muteBtn">
                    🎤 Mute
                </button>
                <button class="btn btn-danger ms-3" onclick="endCall()">
                    End Call
                </button>
            </div>
        </div>
    </div>

      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>

      </div> -->
      <div class="modal-footer">
          <button type="button" class="btn btn-danger" onclick="endCall()"> End Call </button>
    </div>
    </div>
  </div>
</div>


<!-- Incoming Call Modal -->
<div class="modal fade" id="noti-video-modal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content">

      <div class="modal-header">
        <h5>Incoming Video Call</h5>
      </div>

      <div class="modal-body text-center">
        <p><b id="caller-name">Someone</b> is calling…</p>

        <button class="btn btn-success" onclick="acceptCall()">Accept</button>
        <button class="btn btn-danger" onclick="rejectCall()">Reject</button>
      </div>

    </div>
  </div>
</div>


<script>
    window.Laravel = {
        userId: {{ auth()->id() }},
        users: @json($users->pluck('id'))
    };
</script>
<script src="{{ asset('admin/tech_assist/chat') }}.js"></script>
<script src="{{ asset('admin/tech_assist/video-call.js') }}"></script>
<script>
    // document.addEventListener("DOMContentLoaded", function () {
    //     initUserStatus(window.Laravel.users);
    // });
    document.addEventListener("DOMContentLoaded", function () {
        initUserStatus(window.Laravel.users);

        loadInitialUnread(window.Laravel.udsers);   // ✅ first load correct count
        listenForNewMessages(window.Laravel.users); // ✅ realtime updates
    });
</script>
@endsection
```