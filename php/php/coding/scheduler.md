### Scheduler function
- create the html file to test the code
- it store in local storage
```php
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Event Scheduler with Countdown</title>

<style>
body {
  font-family: Arial, sans-serif;
  padding: 20px;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #ccc;
  padding: 8px;
  vertical-align: top;
}

button {
  padding: 6px 10px;
  margin-bottom: 4px;
}

small {
  color: #555;
}

.countdown {
  font-weight: bold;
  color: #0a7;
}

/* ===== Modal ===== */
.modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.4);
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  width: 360px;
}

.days label {
  display: block;
}

.time-row {
  display: flex;
  gap: 6px;
  margin-bottom: 6px;
}

pre {
  background: #f6f6f6;
  padding: 8px;
  font-size: 13px;
}
</style>
</head>

<body>

<h2>Event Scheduler</h2>

<table>
  <thead>
    <tr>
      <th>Event</th>
      <th>Schedule</th>
      <th>Next Run</th>
      <th>Countdown</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody id="eventTable"></tbody>
</table>

<!-- ===== Modal ===== -->
<div class="modal" id="modal">
  <div class="modal-content">
    <h3>Configure Schedule</h3>

    <div class="days">
      <label><input type="checkbox" value="1"> Monday</label>
      <label><input type="checkbox" value="2"> Tuesday</label>
      <label><input type="checkbox" value="3"> Wednesday</label>
      <label><input type="checkbox" value="4"> Thursday</label>
      <label><input type="checkbox" value="5"> Friday</label>
      <label><input type="checkbox" value="6"> Saturday</label>
      <label><input type="checkbox" value="0"> Sunday</label>
    </div>

    <hr>

    <div id="timeContainer"></div>
    <button onclick="addTime()">➕ Add Time</button>

    <hr>

    <b>Cron Preview</b>
    <pre id="cronPreview">—</pre>

    <b>Schedule Preview</b>
    <div id="humanPreview">—</div>

    <br>
    <button onclick="saveSchedule()">Save</button>
    <button onclick="closeModal()">Cancel</button>
  </div>
</div>

<script>
/* ===== Constants ===== */
const EVENTS = ["Backup", "Data Sync", "Report Generation"];
const STORAGE_KEY = "eventSchedules";
const DAY_NAMES = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

let currentEvent = null;

/* ===== Storage ===== */
function loadSchedules() {
  return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
}

function saveSchedules(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

/* ===== UI Helpers ===== */
function formatTime12h(t) {
  const [h, m] = t.split(":").map(Number);
  return `${h % 12 || 12}:${m.toString().padStart(2,"0")} ${h >= 12 ? "PM" : "AM"}`;
}

function humanList(arr) {
  if (arr.length === 1) return arr[0];
  if (arr.length === 2) return `${arr[0]} and ${arr[1]}`;
  return `${arr.slice(0,-1).join(", ")} and ${arr.at(-1)}`;
}

/* ===== Cron + Human Text ===== */
function generateCron(s) {
  return s.times.map(t => {
    const [h,m] = t.split(":");
    return `${m} ${h} * * ${s.days.join(",")}`;
  });
}

function generateHuman(s) {
  return `Every ${humanList(s.days.map(d => DAY_NAMES[d]))} at ${humanList(s.times.map(formatTime12h))}`;
}

/* ===== Scheduling Logic ===== */
function getNextRun(s) {
  const now = new Date();
  let candidates = [];

  for (let d = 0; d < 7; d++) {
    const base = new Date(now);
    base.setDate(now.getDate() + d);

    if (s.days.includes(base.getDay())) {
      s.times.forEach(t => {
        const [h,m] = t.split(":").map(Number);
        const dt = new Date(base);
        dt.setHours(h, m, 0, 0);
        if (dt > now) candidates.push(dt);
      });
    }
  }
  return candidates.sort((a,b)=>a-b)[0] || null;
}

function formatCountdown(ms) {
  const total = Math.floor(ms / 1000);
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  return `${h.toString().padStart(2,"0")}:${m.toString().padStart(2,"0")}:${s.toString().padStart(2,"0")}`;
}

/* ===== Render Table ===== */
function render() {
  const tbody = document.getElementById("eventTable");
  const schedules = loadSchedules();
  tbody.innerHTML = "";

  EVENTS.forEach(ev => {
    const s = schedules[ev];
    const next = s ? getNextRun(s) : null;

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${ev}</td>
      <td>
        ${s ? generateHuman(s) + "<br><small>" + generateCron(s).join("<br>") + "</small>" : "-"}
      </td>
      <td>${next ? next.toLocaleString() : "-"}</td>
      <td class="countdown" data-event="${ev}">-</td>
      <td><button onclick="openModal('${ev}')">Schedule</button></td>
    `;
    tbody.appendChild(row);
  });
}

/* ===== Countdown Timer ===== */
setInterval(() => {
  const schedules = loadSchedules();
  document.querySelectorAll(".countdown").forEach(cell => {
    const ev = cell.dataset.event;
    const s = schedules[ev];
    if (!s) return cell.textContent = "-";

    const next = getNextRun(s);
    if (!next) return cell.textContent = "-";

    const diff = next - new Date();
    cell.textContent = diff > 0 ? formatCountdown(diff) : "00:00:00";
  });
}, 1000);

/* ===== Modal ===== */
function openModal(ev) {
  currentEvent = ev;
  document.getElementById("modal").style.display = "flex";

  document.querySelectorAll(".days input").forEach(c => c.checked = false);
  document.getElementById("timeContainer").innerHTML = "";

  const s = loadSchedules()[ev];
  if (s) {
    s.days.forEach(d =>
      document.querySelector(`.days input[value='${d}']`).checked = true
    );
    s.times.forEach(t => addTime(t));
  } else {
    addTime();
  }
  updatePreviews();
}

function closeModal() {
  document.getElementById("modal").style.display = "none";
}

function addTime(val="") {
  const div = document.createElement("div");
  div.className = "time-row";
  div.innerHTML = `
    <input type="time" value="${val}" oninput="updatePreviews()">
    <button onclick="this.parentElement.remove();updatePreviews()">❌</button>
  `;
  document.getElementById("timeContainer").appendChild(div);
}

function saveSchedule() {
  const days = [...document.querySelectorAll(".days input:checked")].map(c=>+c.value);
  const times = [...document.querySelectorAll("#timeContainer input")]
    .map(i=>i.value).filter(Boolean);

  if (!days.length || !times.length) return alert("Select days and times");

  const data = loadSchedules();
  data[currentEvent] = { days, times };
  saveSchedules(data);

  closeModal();
  render();
}

/* ===== Live Previews ===== */
function updatePreviews() {
  const days = [...document.querySelectorAll(".days input:checked")].map(c=>+c.value);
  const times = [...document.querySelectorAll("#timeContainer input")]
    .map(i=>i.value).filter(Boolean);

  if (!days.length || !times.length) {
    cronPreview.textContent = "—";
    humanPreview.textContent = "—";
    return;
  }

  const s = { days, times };
  cronPreview.textContent = generateCron(s).join("\n");
  humanPreview.textContent = generateHuman(s);
}

document.addEventListener("change", e => {
  if (e.target.matches(".days input")) updatePreviews();
});

/* ===== Init ===== */
render();
</script>

</body>
</html>
```