
### Table of Contents

### Ques. What is JavaScript?
* JavaScript is a scripting language. It is different from Java language. It is object-based, lightweight, cross-platform translated language. It is widely used for client-side validation.

### Ques. JavaScript String Search?
* There are many types of function.
1. The **indexOf()** method returns the index (position) the first occurrence of a string in a string.
    ```javascript
    <p id="demo"></p>

    <script>
    let text = "Please locate where 'locate' occurs!";
    let index = text.indexOf("locate");
    document.getElementById("demo").innerHTML = index; 
    </script>

    Output:- 7
    ```
    ```javascript
    <p id="demo"></p>

    <script>
    let text = "Please locate where 'locate' occurs!";
    let index = text.indexOf("locate",15);
    document.getElementById("demo").innerHTML = index; 
    </script>
    ```

2. The **lastIndexOf()** method returns the index of the last occurrence of a specified text in a string:
    ```javascript
    <p id="demo"></p>

    <script>
    let text = "Please locate where 'locate' occurs!";
    let index = text.lastIndexOf("locate");
    document.getElementById("demo").innerHTML = index; 
    </script>

    Output:- 21
    ```
    **Note:-** Both **indexOf()**, and **lastIndexOf()** return **-1** if the text is not found:
    ```javascript
    <p id="demo"></p>

    <script>
    let text = "Please locate where 'locate' occurs!";
    let index = text.indexOf("John");
    document.getElementById("demo").innerHTML = index;
    </script>
    ```

3. The **search()** method searches a string for a string (or a regular expression) and returns the position of the match.


### Ques. JavaScript String Methods?
1. The **length** property returns the length of a string.
    ```javascript
    <p id="demo"></p>

    <script>
    let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    document.getElementById("demo").innerHTML = text.length;
    </script>

    Output:- 26
    ```

2. **slice()** extracts a part of a string and returns the extracted part in a new string.
```javascript
<p id="demo"></p>

<script>
let text = "Apple, Banana, Kiwi";
let part = text.slice(7,13);
document.getElementById("demo").innerHTML = part; 
</script>

Output:- Banana

# Example2:- 
<script>
let text = "Apple, Banana, Kiwi";
let part = text.slice(7)
document.getElementById("demo").innerHTML = part;
</script>

Output:- Banana, Kiwi

# Example3:- 
<script>
let text = "Apple, Banana, Kiwi";
let part = text.slice(-11);
document.getElementById("demo").innerHTML = part;
</script>

Output:- anana, Kiwi

# Example4:-
<script>
let text = "Apple, Banana, Kiwi";
let part = text.slice(-12,-6)
document.getElementById("demo").innerHTML = part;
</script>

Output:- Banana
```

3. String substring()
4. String substr()
5. String replace()
6. String replaceAll()
7. String toUpperCase()
```javascript
var str = "mohit";
var str = str.toUpperCase();    //MOHIT
alert(str);
```
8. String toLowerCase()
```javascript
var str = "mohit";
var str = str.toLowerCase();     //mohit
alert(str);
```
9.  String concat()
10. String trim()
11. String trimStart()
12. String trimEnd()
13. String padStart()
14. **String padEnd()**
15. **String charAt()**
16. **String charCodeAt()**
17. **String split()**

### Ques. Is javascript a statically typed or a dynamically typed language?


### Ques. What are the different data types present in javascript?
* JavaScript provides different data types to hold different types of values. There are two types of data types in JavaScript.
1. **Primitive data type**
   * **String -** It represents a series of characters and is written with quotes. A string can be represented using a single or a double quote.
        ```javascript
        var str = "Vivek Singh Bisht"; //using double quotes
        var str2 = 'John Doe'; //using single quotes
        ```
    * **Number -** It represents a number and can be written with or without decimals.
        ```javascript
        var x = 3; //without decimal
        var y = 3.6; //with decimal
        ```
    * **BigInt -** This data type is used to store numbers which are above the limitation of the Number data type. It can store large integers and is represented by adding “n” to an integer literal.
        ```javascript
        var bigInteger =  234567890123456789012345678901234567890;
        ```
2. **Non-primitive (reference) data type**


### Ques. Difference between “ == “ and “ === “ operators?
* Both are comparison operators. The difference between both the operators is that “==” is used to compare values whereas, “ === “ is used to compare both values and types.
    ```javascript
    var x = 2;
    var y = "2";
    (x == y)  // Returns true since the value of both x and y is the same
    (x === y) // Returns false since the typeof x is "number" and typeof y is "string"
    ```

### Ques. Difference between let, var and Const?
* **var:-** If we declare a varibale with var, then we can also declare it again with the same name, and if we want to re-assign its value then we can do that too.
* **Let:-** If we declare a varibale with let, then we cannot declare it again with the same name, But can re-assign its value.
* **Const:-** If we declare a varibale with const, then we can neither declare it again not can re-assign its value.

### Ques. What is NaN property in JavaScript?
* It represents a value that is **not a number**. It can be used to check whether a number entered is a valid number or not a number.
```javascript
isNaN("Hello")  // Returns true
isNaN(345)   // Returns false
isNaN('1')  // Returns false, since '1' is converted to Number type which results in 0 ( a number) 
isNaN(true) // Returns false, since true converted to Number type results in 1 ( a number)
isNaN(false) // Returns false
isNaN(undefined) // Returns true
```
### Ques. What is Hoisting?
* Hoisting is a javascript mechanism where **variables** and **function** declarations are moved to the top of their scope before the code excutions.
* In JavaScript, a variable can be declared after it has been used.
* a variable can be used before it has been declared.
* variables and function declarations kahi par ho wo upar rakh deta hai apne aap before the code excution.
```javascript
x = 5; // Assign 5 to x

elem = document.getElementById("demo"); // Find an element
elem.innerHTML = x;                     // Display x in the element

var x; // Declare x     it line moved to top automatically
```

### Ques. What is strict mode?
* "use strict"; Defines that JavaScript code should be executed in "strict mode".
* The purpose of "use strict" is to indicate that the code should be executed in "strict mode".
* Not Allowed in Strict Mode:-
  * Using a variable, **without declaring** it, is not allowed:
    ```javascript
    <script>
    "use strict";
    x = 3.14;  
    </script>
    ```
  * Using an object, without declaring it, is not allowed:
    ```javascript
    "use strict";
    x = {p1:10, p2:20};
    ```

### Ques. what is this keyword?
* “This” keyword refers to an object that is executing the current piece of code.
*  It references the object that is executing the current function.
```javascript
# Object's Method
<p id="demo"></p>

<script>
# Create an object:
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

// Display data from the object:
document.getElementById("demo").innerHTML = person.fullName();
</script>
---------------------------------------------------------------
# Example 2:- Global Scope
<script>
var myVar = 100;

function WhoIsThis() {
    var myVar = 200;

    alert(myVar); // 200
    alert(this.myVar); // 100
}

WhoIsThis(); // inferred as window.WhoIsThis()

var obj = new WhoIsThis();
alert(obj.myVar); 
</script>
```



### Ques. What is the difference between window.onload and document.onload?
* **document.onload:-** It gets fired prior to loading of images and other external content. document.onload event is fired before the window.onload.
* **window.onload:-** It gets fired when the complete page loads, which includes images, scripts, css, etc.

### Ques. What is the difference between setTimeout() and setInterval()?
* **setTimeout( function, duration) −** This function calls function after duration milliseconds from now. This goes for one execution. Let’s see an example −
* It waits for 2000 milliseconds, and then runs the callback function alert(‘Hello’) −
    ```javascript
    setTimeout(function() { alert('Hello');}, 2000);
    ```
* **setInterval(function, duration) −** This function calls function after every duration milliseconds. This goes for unlimited times. Let’s see an example −
* It triggers the alert(‘Hello’) after every 2000 milliseconds, not only once.
    ```javascript
    setInterval(function() { alert('Hello');}, 2000);
    ```

### Ques. What is the difference between getter and setter in JavaScript?
* **getter** methods are used to access the properties of an object.
```javascript
const student = {
    firstName: 'Mohit',
    // accessor property(getter)
    get getName() {
        return this.firstName;
    }
};

// accessing data property
console.log(student.firstName); // Mohit
// accessing getter methods
console.log(student.getName); // Mohit
// trying to access as a method
console.log(student.getName()); // error
```

* **setter** methods are used to change the values of an object.
```javascript
const student = {
    firstName: 'Mohit',
    
    //accessor property(setter)
    set changeName(newName) {
        this.firstName = newName;
    }
};

console.log(student.firstName); // Mohit

// change(set) object property using a setter
student.changeName = 'Saxena';

console.log(student.firstName); // Saxena
```

* **Object.defineProperty():-** Object.defineProperty() method to add getters and setters.
```javascript
const student = {
    firstName: 'Monica'
}

// getting property
Object.defineProperty(student, "getName", {
    get : function () {
        return this.firstName;
    }
});

// setting property
Object.defineProperty(student, "changeName", {
    set : function (value) {
        this.firstName = value;
    }
});

console.log(student.firstName); // Monica

// changing the property value
student.changeName = 'Sarah';

console.log(student.firstName); // Sarah
```



### Ques. Map, Reduce, and Filter?
* **Map:-** The map() method is used for creating a new array from an existing one, applying a function to each one of the elements of the first array.
* **Syntex:-**
```javascript
var new_array = arr.map(function callback(element, index, array) {
    // Return value for new_array
}[, thisArg])
```

### Ques. What is Closure?
A closure is a feature of JavaScript that allows inner functions to access their outer scope.
A Closer is a an inner function that has access to the outer(enclosing) function's variables.
For every closure we have three scope:
local scope(Own scope)
Outer functions scope
Global Scope



### Ques. What is Promise?
* Promises are useful when you have to handle more than one asynchronous task, one after another.
* A Promise is a special JavaScript object. A promise is a good way to handle asynchronous operations.
* A promise may have one of **three** states.
  * **Pending**
  * **Fulfilled**
  * **Rejected**
* A promise starts in a pending state. That means the process is not complete. If the operation is successful, the process ends in a fulfilled state. And, if an error occurs, the process ends in a rejected state.
    ```javascript
    // Create a promise
    const count = true;
    let countValue = new Promise(function (resolve, reject) {
        if (count) {
            resolve("There is a count value.");
        } else {
            reject("There is no count value");
        }
    });

    console.log(countValue);

    Output:- Promise {<resolved>: "There is a count value."}
    ```
* You can perform an operation after a promise is resolved using methods **then()**, **catch()** and **finally()**.
* The **then()** method is used with the callback when the promise is successfully fulfilled or resolved.
    ```javascript
    let countValue = new Promise(function (resolve, reject) {
    resolve("Promise resolved");
    });
    countValue
    .then(function successValue(result) {
        console.log(result);
    })
    .then(function successValue1() {
        console.log("You can call multiple functions this way.");
    });
    ```
* The **catch()** method is used with the callback when the promise is rejected or if an error occurs. For example,
    ```javascript
    let countValue = new Promise(function (resolve, reject) {
    reject('Promise rejected'); 
    });
    countValue.then(
        function successValue(result) {
            console.log(result);
        },
    )
    // executes if there is an error
    .catch(
        function errorValue(result) {
            console.log(result);
        }
    )
    ```

A JavaScript callback is a function which is to be executed after another function has finished execution.
Any function that is passed as an argument to another function so that it can be executed in that other function is called as a callback function.

### Ques. What is Currying Function?
* Currying is an advanced technique of working with functions.


### Ques. What is Debouncing?
* Scheduling your function to be triggered at a specific time.
* Debouncing is a programming pattern or a technique to restrict the calling of a time-consuming function frequently, by delaying the execution of the function until a specified time to avoid unnecessary CPU cycles, and API calls and improve performance.
* Debouncing in JavaScript is a practice used to improve browser performance. There might be some functionality in a web page that requires time-consuming computations. If such a method is invoked frequently, it might greatly affect the performance of the browser, as JavaScript is a single-threaded language.
* A Debounce function is a higher-order function that returns another function, to create closure around the function parameters (func, timeout) and the timer variable.
* func: is a function that you want to execute after the debounce time.
* timeout: The amount of time you want the debounce function to wait after the last received action before executing func.
* timer: The value used to indicate a running debounce.
* The common use cases are **Search box suggestions**, **text-field auto-saves**, and **eliminating double-button clicks**.
* Here in the debounce function, we are taking two arguments, the first is the function and the second is the delay time or the timeout time. 

What is the difference between null and undefined in JavaScript?
What is the difference between substr() and substring() in JavaScript?


### Throttling  
    ```javascript
    <button id="clickmebutton" onclick=newFun()>Click me!</button>

    <script>
    const mythrottle=(fn,d)=>{
    return function(...args){
        document.getElementById("clickmebutton").disabled=true;
    setTimeout(()=>{
        fn();
    },d) 
    }  
    }

    const newFun = mythrottle(()=>{
    document.getElementById("clickmebutton").disabled=false;
    console.log('User Clicked....');
    },2000)
    </script>
    ```