```php
function connectToRoom_befor-video-call() {
    const isAudio = callType === 'audio'; // voice
    Twilio.Video.connect(accessToken, {
        name: roomName,
        audio: true,
        // video: { width: 640, height: 480, frameRate: 24 }
        video: isAudio ? false : { width: 640, height: 480, frameRate: 24 }
    })
    .then(joinedRoom => {

        room = joinedRoom;

        const container = document.getElementById('video-chat-window');
        container.innerHTML = '';

        if (callType === 'audio') {
            container.style.display = 'none';
        } else {
            container.style.display = 'block';
        }

        // local tracks
        // room.localParticipant.tracks.forEach(pub => {
        //     if (pub.track) container.appendChild(pub.track.attach());
        // });
        room.localParticipant.tracks.forEach(pub => {
            if (!pub.track) return;

            if (callType === 'audio' && pub.track.kind === 'video') return;

            container.appendChild(pub.track.attach());
        });

        // remote tracks
        room.participants.forEach(attachParticipantTracks);
        room.on('participantConnected', attachParticipantTracks);
        room.on('participantDisconnected', detachParticipantTracks);
    })
    .catch(err => console.error('Connection failed:', err));
}
```