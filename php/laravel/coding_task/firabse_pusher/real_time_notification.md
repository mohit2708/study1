```php
<!DOCTYPE html>
<html>
<head>
    <title>Pusher Test</title>
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Pusher -->
    <script src="https://js.pusher.com/8.2/pusher.min.js"></script>
    <!-- Echo -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/laravel-echo/1.15.0/echo.iife.js"></script>

</head>
<body class="p-4">

    <h2>Pusher Notification Test11</h2>
    <p id="status">Connecting...</p>

    <!-- BOOTSTRAP MODAL -->
    <div class="modal fade" id="notifyModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">

                <div class="modal-header bg-primary text-white">
                    <h5 class="modal-title" id="modalTitle">Notification</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>

                <div class="modal-body">
                    <table class="table table-bordered">
                        <tr>
                            <th>User ID</th>
                            <td id="tblUserId"></td>
                        </tr>
                        <tr>
                            <th>Heading</th>
                            <td id="tblHeading"></td>
                        </tr>
                        <tr>
                            <th>Link</th>
                            <td>
                                <a href="#" target="_blank" id="tblLink">Open</a>
                            </td>
                        </tr>
                    </table>
                    <p id="modalMessage"></p>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-success" id="modalOk">OK</button>
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancel</button>
                </div>

            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

<script>

    Pusher.logToConsole = true;

    const echo = new Echo({
        broadcaster: 'pusher',
        key: "{{ env('PUSHER_APP_KEY') }}",
        cluster: "{{ env('PUSHER_APP_CLUSTER') }}",
        forceTLS: true,
    }); 

    document.getElementById("status").innerText = "Connected to Pusher";

    // Bootstrap Modal instance
    var notifyModal = new bootstrap.Modal(document.getElementById('notifyModal'));

    echo.channel('notice-channel')
        .listen('NoticeCreated', (data) => {
            console.log("Event received:", data);
            
            let title = data.title ?? "New Notification For Chat";
            let message = data.message ?? JSON.stringify(data);

            document.getElementById('tblUserId').innerText = data.notice.user_id;

            // Set values inside modal
            document.getElementById('modalTitle').innerText = title;
            // document.getElementById('modalMessage').innerText = message;

            // Show popup
            notifyModal.show();
        });

    // OK button clicked
    document.getElementById("modalOk").onclick = function () {
        notifyModal.hide();
        alert("You clicked OK!");
    };

</script>

</body>
</html>

```