|  No.  | [js Validation]()                                         |
| :---: | --------------------------------------------------------- |
|       | [validation only number](#validation-only-number)         |
|       | [chracter limit in text box](#chracter-limit-in-text-box) |

|  No.  | [Questions]()                                                                                     |
| :---: | ------------------------------------------------------------------------------------------------- |
|       | [hide the text field according to select option](#hide-the-text-field-according-to-select-option) |
|       | [Get width and height of screen size?](#get-width-and-height-of-screen-size)                      |
|       | [Date validation not select before today date](#date-validation-not-select-before-today-date)     |

## Common Validations:

### validation only number.
* Input only Number in text field you can add "only_number" class in your text field.
```javascript
$(function () {
    $(".only_number").on("input", function (e) {
        $(this).val(
            $(this)
                .val()
                .replace(/[^0-9]/g, "")
        );
    });
});
```

### chracter limit in text box
```javascript
$('.char_limit').keyup(function() {
    var len = this.value.length;
    if (len >= 20) {
        this.value = this.value.substring(0, 20);
    }
    $('#charLeft').text(20 - len);
});
```

### hide the text field according to select option
```html
<select class="form-select" aria-label="Default select example" id="duration" name="duration">
    <option value="">-- Select Duration --</option>
    <option value="1_hour" data-duration="1_hour">1 Hour</option>
    <option value="2_hour" data-duration="2_hour">2 Hour</option>
    <option value="3_hour" data-duration="3_hour">3 Hour</option>
    <option value="1_day" data-duration="1_day">1 Day</option>
    <option value="10_day" data-duration="10_day">10 Day</option>
    <option value="20_day" data-duration="20_day">20 Day</option>
    <option value="custom_duration" data-duration="custom_duration">Custom in Days</option>
</select>
```
```javascript
$(function() {
    $("#duration").change(function() {
        let get_duration = $(this).find(':selected').attr('data-duration')
        if (get_duration == 'custom_duration') {
            $("#custom_duration").prop("readonly", false);
            $('#custom_duration').css('cursor', '');
        } else {
            $("#custom_duration").prop("readonly", true);
            $("#custom_duration").val('');
            $('#custom_duration').css('cursor', 'not-allowed');
        }
    });
});
```




### Get the data by single day(Today).
```javascript
$("#getJobToday").click(function(){
    $("#loderBox").show();
    var date = new Date();
    var year = date.getFullYear();
    var month = (date.getMonth() + 1).toString().padStart(2, '0');
    var day = date.getDate().toString().padStart(2, '0');

    var currentdate = year + '-' + month + '-' + day;

    $.ajax({
        url: baseurl + "/jobDateRangePicker",
        type: "POST",
        data: {
            _token: $('meta[name="csrf-token"]').attr("content"),
            current_date: currentdate
        },
        dataType: "JSON",
        success: function (response) {               
            $('#getdate').html(response.date);
            $("#myhtmldata").html(response.html)
            $("#loderBox").hide();
        },
    });
});
```

### Get the data by week.
```javascript
$("#getJobWeek").click(function(){
    $("#loderBox").show();
    var curr = new Date; // get current date
    var first = curr.getDate() - curr.getDay(); // First day is the day of the month - the day of the week
    var last = first + 6; // last day is the first day + 6

    var firstday = new Date(curr.setDate(first)).toUTCString();
    var lastday = new Date(curr.setDate(last)).toUTCString();

    var changefirstday = new Date(firstday);
    var fdyear = changefirstday.getFullYear();
    var fdmonth = (changefirstday.getMonth() + 1).toString().padStart(2, '0');
    var fdday = changefirstday.getDate().toString().padStart(2, '0');
    var firstday = fdyear + '-' + fdmonth + '-' + fdday;


    var changelastday = new Date(lastday);
    var ldyear = changelastday.getFullYear();
    var ldmonth = (changelastday.getMonth() + 1).toString().padStart(2, '0');
    var ldday = changelastday.getDate().toString().padStart(2, '0');
    var lastday = ldyear + '-' + ldmonth + '-' + ldday;


    $.ajax({
        url: baseurl + "/jobDateRangePicker",
        type: "POST",
        data: {
            _token: $('meta[name="csrf-token"]').attr("content"),
            firstday: firstday,
            lastday: lastday
        },
        dataType: "JSON",
        success: function (response) {               
            $('#getdate').html(response.date);
            $("#myhtmldata").html(response.html)
            $("#loderBox").hide();
        },
    });
});
```

### Get the data by month.
```javascript
$("#getJobMonth").click(function(){
    var date = new Date();
    var mfirstDay = new Date(date.getFullYear(), date.getMonth(), 1);
    var mlastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);

    var changefirstday = new Date(mfirstDay);
    var mfyear = changefirstday.getFullYear();
    var mfmonth = (changefirstday.getMonth() + 1).toString().padStart(2, '0');
    var mfday = changefirstday.getDate().toString().padStart(2, '0');
    var mfirstday = mfyear + '-' + mfmonth + '-' + mfday;
    console.log(mfirstday);

    alert(mfirstDay);
    alert(mlastDay);
});

function getWeekStartEnd(date) { 
    const startOfWeek = new Date(date);
    startOfWeek.setDate(startOfWeek.getDate() - startOfWeek.getDay());
    const endOfWeek = new Date(date);
    endOfWeek.setDate(endOfWeek.getDate() + (6 - endOfWeek.getDay()));
    return { start: startOfWeek, end: endOfWeek };
} 
```


### all checked sub checked
```javascript
function deliver_all_check() {
    $(".dcheckAll").on("click", function (e) {
        if (this.checked) {
            $(".deliver_sub_chk").prop("checked", true);
        } else {
            $(".deliver_sub_chk").prop("checked", false);
        }
    });
    $(".deliver_sub_chk").click(function () {
        var numberOfCheckboxes = $(".deliver_sub_chk").length;
        var numberOfCheckboxesChecked = $(".deliver_sub_chk:checked").length;
        if (numberOfCheckboxes == numberOfCheckboxesChecked) {
            $(".dcheckAll").prop("checked", true);
        } else {
            $(".dcheckAll").prop("checked", false);
        }
    });
}
```


### Convert time 24 to AM/PM
```javascript
function convertToAMPM(time) {
    // Split the time string into hours, minutes, and seconds
    let timeParts = time.split(":");
    let hours = parseInt(timeParts[0]);
    let minutes = parseInt(timeParts[1]);
    let seconds = parseInt(timeParts[2]);

    // Determine AM or PM
    let ampm = hours >= 12 ? "PM" : "AM";

    // Convert to 12-hour format
    if (hours > 12) {
        hours -= 12;
    }

    // Format the time as HH:MM:SS AM/PM
    let formattedTime = hours.toString().padStart(2, '0') + ":" + 
                        minutes.toString().padStart(2, '0') + " " + ampm;

    return formattedTime;
}
```

### Get width and height of screen size
```javascript
function getScreenSize() {
    var screenSize = {
        width: screen.width,
        height: screen.height
    };
    return screenSize;
}

window.onload = function() {
    var screenSize = getScreenSize();
    alert("Screen Width: " + screenSize.width);
    alert("Screen Height: " + screenSize.height);
};
```


### Date validation not select before today date.
```javascript
<input type="date" class="valid" id="start_date" name="start_date" aria-invalid="false">

<script>
    // Get today's date
    const today = new Date();
    // Format the date to YYYY-MM-DD
    const dd = String(today.getDate()).padStart(2, '0');
    const mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
    const yyyy = today.getFullYear();
    const formattedDate = `${yyyy}-${mm}-${dd}`;

    // Set the min attribute of the input
    document.getElementById('start_date').setAttribute('min', formattedDate);
</script>
```