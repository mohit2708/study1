```php
<!DOCTYPE html>
<html>
<body>

<h1>The Window Object</h1>
<h2>The alert() Method</h2>

<p>Click the button to display an alert box.</p>

<button onclick="myFunction()">Try it</button>

<script>
function myFunction() {
  alert("Hello! I am an alert box!");
}



$(document).ready( function() {
    jAlert('Example of a basic alert box in jquery', 'jquery basic alert box');
    alert('Example of a basic alert box in jquery', 'jquery basic alert box');
});
</script>

</body>
</html>
```

```php
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $("p").slideToggle();
  });
});
</script>
</head>
<body>

<p>This is a paragraph.</p>

<button>Toggle between slide up and slide down for a p element</button>

</body>
</html>
```