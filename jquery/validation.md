### try
```
<input type="text" id="price" placeholder="Enter price">
<div id="message"></div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  $('#price').on('keydown', function(e) {
    // Allow control keys: backspace, delete, tab, escape, enter, arrows, home/end
    if (
      $.inArray(e.keyCode, [8, 9, 27, 13, 37, 38, 39, 40, 46]) !== -1 ||
      // Allow Ctrl/cmd+A, Ctrl/cmd+C, Ctrl/cmd+V, Ctrl/cmd+X
      ((e.keyCode === 65 || e.keyCode === 67 || e.keyCode === 86 || e.keyCode === 88) && (e.ctrlKey === true || e.metaKey === true))
    ) {
      return; // allow these keys
    }

    var currentVal = $(this).val();
    var cursorPos = this.selectionStart;
    var hasDot = currentVal.indexOf('.') !== -1;

    // Allow digits 0-9
    if ((e.keyCode >= 48 && e.keyCode <= 57) || (e.keyCode >= 96 && e.keyCode <= 105)) {
      // If there's a dot, check decimals count after dot
      if (hasDot) {
        var dotIndex = currentVal.indexOf('.');
        var decimals = currentVal.substring(dotIndex + 1);

        // If cursor is after dot, restrict if decimals >= 2
        if (cursorPos > dotIndex && decimals.length >= 2) {
          e.preventDefault();
          return;
        }
      }
      return; // allow digit
    }

    // Allow one dot (.) only if not first char and not already present
    if (e.key === '.') {
      if (currentVal.indexOf('.') === -1 && currentVal.length > 0) {
        return; // allow dot
      }
    }

    // Otherwise prevent
    e.preventDefault();
  });

  $('#price').on('keyup', function() {
    var price = $(this).val();
    var regex = /^\d+(\.\d{1,2})?$/;

    if (price === "") {
      $('#message').text('');
      return;
    }

    if (regex.test(price)) {
      $('#message').text('Valid price').css('color', 'green');
    } else {
      $('#message').text('Invalid price! Format: 25 or 25.23').css('color', 'red');
    }
  });
</script>

```