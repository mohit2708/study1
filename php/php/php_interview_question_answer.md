# PHP Interview Questions & Answers.

### Table of Contents

|  No.  | Questions                                                                                                                           |
| :---: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   5   | [Difference between Php4 and php5?](#Ques-Difference-between-Php4-and-php5)                                                         |
|   9   | [What is Constant?](#Ques-What-is-Constant)                                                                                         |
|  10   | [What is Variable?](#Ques-What-is-Variable)                                                                                         |
|  11   | [Difference between Constant And Variable?](#Ques-Difference-between-Constant-And-Variable)                                         |
|  12   | [Difference between Echo And Print?](#Ques-Difference-between-Echo-And-Print)                                                       |
|  13   | [Php Global Variables/Superglobals?](#ques-Php-Global-Variables-Superglobals)                                                       |
|  14   | [Difference between Get and Post?](#Ques-Difference-between-Get-and-Post)                                                           |
|  15   | [Difference between Unlink and Unset?](#Ques-Difference-between-Unlink-and-Unset)                                                   |
|  16   | [Difference between Require and Include?](#Ques-Difference-between-Require-and-Include)                                             |
|  17   | [What is the difference between Single Quoted & Double Quoted?](#Ques-What-is-the-difference-between-Single-Quoted-&-Double-Quoted) |
|  18   | [Types of Error in Php?](#Ques-Types-of-Error-in-Php)                                                                               |
|  19   | [What is the difference between Single == & ===?](#Ques-What-is-the-difference-between-Single-==-&-===)                             |
|  20   | [What is the difference between $message and $$message?](#Ques-What-is-the-difference-between-$message-and-$$message)               |
|  21   | [What is Cookie?](#ques-What-is-Cookie)                                                                                             |
|  22   | [What is Session?](#ques-What-is-Session)                                                                                           |
|       | [How can we destroy a session in PHP?](#ques-How-can-we-destroy-a-session-in-PHP)                                                   |
|       | [Difference between cookie and Session?](#Ques-Difference-between-cookie-and-Session)                                               |
|  21   | [What is Oops(Object-oriented programming System)?](#)                                                                              |
|  22   | [What is Advantage of Oops(Object-oriented programming System)?](#)                                                                 |
|  23   | [What is class?](#Ques-What-is-class)                                                                                               |
|  24   | [What is object?](#ques-What-is-object)                                                                                             |
|  25   | [What is Encapsulation?](#Ques-What-is-Encapsulation)                                                                               |
|  26   | [What is Abstraction?](#Ques-What-is-Abstraction)                                                                                   |
|  27   | [What is Interface?](#Ques-What-is-Interface)                                                                                       |
|  28   | [What is the difference between Abstract class Interface?](#ques-What-is-the-difference-between-Abstract-class-Interface)           |
|  29   | [What is Polymorphism?](#Ques-What-is-Polymorphism)                                                                                 |
|  30   | [What is Inheritance?](#Ques-What-is-Inheritance)                                                                                   |
|  31   | [What is Static class?](#Ques-What-is-Static-class)                                                                                 |
|  32   | [What is Constructor?](#Ques-What-is-Constructor)                                                                                   |
|  33   | [What is Destructor?](#Ques-What-is-Destructor)                                                                                     |
|       | [What does isset() function?](#ques-What-does-isset()-function)                                                                     |


### **Ques. What is Constant?**
* A constant is a name or an identifier for a simple value. A Constant value cannot be changed during the execution of the Script.
* A valid constant name starts with a letter or underscore (no $ sign before the constant name).

**Syntex** define(name, value, case-insensitive)
```php 
<?php
 define("GREETING", "Welcome to mohit");
 echo GREETING;
?>
Output:- Welcome to mohit 
```
**[⬆ Back to Top](#table-of-contents)**

### **Ques. What is Variable?** 
* Variable temporary data hold Karta hai.
* A variable starts with the $ sign, followed by the name of the variable.
* A variable name must start with a letter or the underscore character.
* A variable name cannot start with a number.
* Variable names are case-sensitive ($age and $AGE are two different variables).
**[⬆ Back to Top](#table-of-contents)**

### **Ques. Difference between Constant And Variable?**
* There is no need to write a dollar sign ($) before a constant, whereas in Variable one has to write a dollar sign.
* Constants cannot be defined by simple assignment, they may only be defined using the define() function.
* Constants may be defined and accessed anywhere without regard to variable scoping rules.
* Once the Constants have been set, may not be redefined or undefined.
**[⬆ Back to Top](#table-of-contents)**

### **Ques. Difference between Echo And Print?**
|                                                          Echo                                                          |                                                               Print                                                                |
| :--------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |
| Echo is a statement i.e. used to display the output. It can be used with parentheses echo or without parentheses echo. | Print is also a statement i.e. used to display the output. It can be used with parentheses print ( ) or without parentheses print. |
|                                             Echo does not return any value                                             |                                                       Print always return 1                                                        |
|                                               Echo is faster than print                                                |                                                     Print is slower than echo                                                      |
|                                    echo can pass multiple string separated as ( , )                                    |                                           using print can doesn’t pass multiple argument                                           |
|                                                   Echo is statement                                                    |                                                         Print is function                                                          |
**[⬆ Back to Top](#table-of-contents)**

### **Ques. Php Global Variables (Superglobals)?**
predefined array varible  by php
* $GLOBALS
* $_SERVER
* $_REQUEST
* $_POST
* $_GET
* $_FILES
* $_ENV
* $_COOKIE
* $_SEESION
**[⬆ Back to Top](#table-of-contents)**

### **Ques. Difference between Get and Post?**
|                                   Get                                    |                               Post                                |
| :----------------------------------------------------------------------: | :---------------------------------------------------------------: |
|      Get method  ki value url mai query string ka rup show hoti hai      |        post mai value hidden variable ka rup mai jati hai.        |
|     The get method is restricted to send upto 1024 characters only.      | The post method can be used to send ASCII as well as binary data. |
|                Get method ki value bookmark kar sakte hai                |         post method ki value bookmark nahi kar sakte hai.         |
| Get method secure nahi hota hai  We can send 1024 bytes using GET method |         but POST method can transfer large amount of data         |
**[⬆ Back to Top](#table-of-contents)**

### **Ques. Difference between Include and Require?**
* If the file is not found by include(), A warning will be issued, but the script will continue.
* If the file is not found by require(), it will cause a fatal error and stop the execution of the script.

__Example:-__ "include(a.php)"
**[⬆ Back to Top](#table-of-contents)**

### **Ques. Difference between Unlink and Unset?**
* Unlink is used to delete the file used in the context.
	__Ex:-__ unlink(“index.html”);
* Unset is used to unset or destroy the variable.
	__Ex:-__ unset($var);
**[⬆ Back to Top](#table-of-contents)**

### **Ques. What is the difference between Single Quoted & Double Quoted?**
* Single quoted mai value parse nahi hoti.
* Double quoted mai value parse ho jati hai.
```php
$s = "dollars";
echo 'This costs a lot of $s.'; // This costs a lot of $s.
echo "This costs a lot of $s."; // This costs a lot of dollars.
```


* Using Variables:
  * **Single quotes:** If you use single quotes, PHP treats everything inside them as plain text. Even if you put a variable like $name, it won't be shown as the actual value of the variable but as is: $name.
  * **Double quotes:** If you use double quotes, PHP looks for variables inside them. If it finds $name, it will replace it with the actual value stored in the $name variable.

* Special Symbols:
  * **Single quotes:** Most special symbols like \n (new line) or \t (tab) won't work as intended within single quotes. They'll show up as they are.
  * **Double quotes:** Special symbols like \n or \t will work inside double quotes, and PHP will replace them with actual line breaks or tabs.

* Speed:
  * **Single quotes:** Using single quotes is usually a bit faster for PHP because it doesn't have to check for variables or special symbols.
  * **Double quotes:** Double quotes might be a tiny bit slower because PHP has to look for variables and special symbols.
  
```php
$name = "Alice";

// Single-quoted string
echo 'Hello $name';  // Output: Hello $name

// Double-quoted string
echo "Hello $name";  // Output: Hello Alice

// Escape sequences
echo 'Line 1\nLine 2';  // Output: Line 1\nLine 2
echo "Line 1\nLine 2";  // Output:
// Line 1
// Line 2
```

**[⬆ Back to Top](#table-of-contents)**
### **Ques. Types of Error in Php?**
* __Notice:-__ Undefined varible,  does not stop the execution of script..
* __Fettel:-__ Undefined  function, this kind of error stop the execution of script
* __Warning:-__ file error(missing  included are required file)
* __Parse:-__ syntex Error, this kind of error stop the execution of script

**[⬆ Back to Top](#table-of-contents)**
### **Ques. What is the difference between Single == & ===?**

* ==:-  Check the value.
* ===:- Check the value and datatype.

**[⬆ Back to Top](#table-of-contents)**
### **Ques. What is the difference between $message and $$message?**
* $message stores variable data while $$message is used to store variable of variable.
* $message is variable whereas $$message is reference variable
__EX:-__
```php
<?php
$hello = "mohit";
$message = "Hello";
$$message = ?
?>
Output:- mohit 
```
**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Cookie?
Php cookie is a small piece of information, which is stored on the client browser.
**Ex:-** Remember me.

**How to set cookie:-**        Setcookie("name", "value", time()+3600);<br>
__How to Retrieve a cookie:-__ echo $_cookie["user"];<br>
__How to unset Cookie:-__      Setcookie(“sample”, “ram”, time()-3600);<br>

##### Two types of cookie:-
__Persistent Cookie:-__ A persistent cookie is a cookie which is store information for certain time in a browser. By default cookie are temporary and are erased if we close the browser.

**Non Persistent Cookie:-** Non persistent cookies are stored in ram on the server, and destroyed when the browser is closed. Ex:- login

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Session ?
Session is way to store information to be used across multiple pages. It stores information on the server.
```php
Create session:- 			session_start(); 
Set value into session:- 		$_SESSION['USER_ID']=1; 
Remove data from a session:- 	unset($_SESSION['USER_ID'];
```

**[⬆ Back to Top](#table-of-contents)**
### Ques. How can we destroy a session in PHP?
We can destroy a session by:
```php
<?php
	session_destroy();
?>
```
To delete a speciﬁc session variable, we use:-
```php
<?php
	seesion_unset($_seesion['variable_name']);
?>
```

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is difference between seesion_unregister and session_unset ?
The session_unregister() function unregister a global variable from the current session and the session_unset() function frees all session variables.

### Ques. Difference between cookie and Session ?
|                          Cookie                          |                                           Session                                           |
| :------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
| Cookie are stored on the client side in text file format |                            Session are stored on the server Side                            |
|          Cookie can not hold multiple variables          |                            Session can hold multiple variables.                             |
|              We can set expiry for a cookie              |                 session only remains active as long as the browser is open                  |
|                                                          | Users do not have access to the data you stored in Session,Since it is stored in the server |
|         cookies using for user activity tracking         |                       Session is mainly used for login/logout purpose                       |

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Array?
* Array is used to store multipal value in single value
* It stores the collection of datatype.
* An array is a special varibale, which can hold more than one value at a time.

__Three Types Of Array__
1. Indexed Array:-<br>
2. Multidimensional Array:-<br>
3. Associative Array:-<br>



**[⬆ Back to Top](#table-of-contents)**
### Ques. How we can retrive the data in the result set of the mysql using Php?
Mysql_fetch_row:- It fetch array 
Mysql_fetch_object:-
Mysql_fetch_array:-
Mysql_fetch_assoc:-


**[⬆ Back to Top](#table-of-contents)**
### Ques. What is the difference between mysqli_fetch_object() and mysqli_fetch_array?
The mysqli_fetch_object() function collects the first single matching record where mysqli_fetch_array() collects all matching records from the table in an array.
 

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is .htaccess file?
.htaccess is a configuration file used to alter the default behavior of a Apache web server software. Most common usage is to redirect the http request to some URLs based on some conditions. For example, we can hide the .html or .php extensions of the URLs to make it SEO friendly

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Timestamp?
A timestamp is the current time of event that is recorded by a computer.

**[⬆ Back to Top](#table-of-contents)**
### Ques. What does PEAR stand for?
PEAR means "PHP Extension and Application Repository". It extends PHP and provides a higher level of programming for web developers.

**[⬆ Back to Top](#table-of-contents)**
### Ques. How to find the length of an array in php?
 count() or sizeof() function to get the number of elements or value in an array.
```php
<?php
$days = array("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");
echo count($days);
echo "<br>";
echo sizeof($days);
?>
```

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is the output of the following Code?
```php
$a = '1';
$b = &$a;
$b = "2$b";
echo $a.", ".$b;
Output:- 21, 21
```

### Ques. What is the use of header function in php ?
The header() function sends a raw HTTP header to a client browser. We can use header() function for redirection of pages. It is important to notice that header() must be called before any actual output is seen.
PHP header are bits of information that are sent to a computer before anything else, like a web page is sent
THey tell the computer the information it needs so that it can execute commands when the rest of the information is received. 

### Ques. What is MVC ?
Ans. The Model-view-controller (MVC) is an architectural pattern that separates an application into three main logical components: the model, the view, and the controller.
·         Control mai hum logic rakhte hai
·         Model mai hum database ke function rakhte hai
·         View mai hum html part rakhta hai.

### Ques. What is Ajax?
Ans. AJAX = Asynchronous JavaScript and XML.<br>
AJAX is a technique for creating fast and dynamic web pages. <br>
AJAX allows web pages to be updated asynchronously by exchanging small amounts of data with the server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.<br>
```php
$.Ajax({
  url:
  type:
  data:
  sucess: function(data){
    -----
  }
  error: function(error)
  {

  }
});
```

### Ques. What are the 3 scope levels available in php  /  What is difference type of visibility ? / what are access modifiers  ? 
__Public:-__ Public method or variable can be accessible from anywhere, Means a public method or variable of a class can be called outside of the class or in a subclass. 

__Private:-__ A private  method or variable of a class can only be called inside that class only in which it is declared.

__Protected:-__ A protected method or variable can only be called in that class & its subclass.

**[⬆ Back to Top](#table-of-contents)**
### Ques. Difference between two dates in Php ?
A timestamp is the current time of an event that is recorded by a computer.
```php
<?php
   $now = time();
   $your_date = strtotime("2017-01-15");
   $datediff = $now - $your_date;
   echo floor($datediff / (60 * 60 * 24));
?>
```

**[⬆ Back to Top](#table-of-contents)**
### Ques. What are the formatting and printing strings available in php  ?
   
* printf(): Display a formatted string.
* sprintf(): Saves a formatted string in a variable.
* fprintf(): prints a formatted string to a file.
* number_format(): Formats number as string.
```php
$today = date("F j, Y, g:i a"); // March 10, 2001, 5:16 pm 
$today = date("m.d.y"); // 03.10.01 
$today = date("j, n, Y"); // 10, 3, 2001 
$today = date("Ymd"); // 20010310 
$today = date('h-i-s, j-m-y, it is w Day'); // 05-16-18, 10-03-01, 1631 1618 6 Satpm01 $today = date('\i\t \i\s \t\h\e jS \d\a\y.'); // it is the 10th day. 
$today = date("D M j G:i:s T Y"); // Sat Mar 10 17:16:18 MST 2001 
$today = date('H:m:s \m \i\s\ \m\o\n\t\h'); // 17:03:18 m is month 
$today = date("H:i:s"); // 17:16:18 
$today = date("Y-m-d H:i:s"); // 2001-03-10 17:16:18 (the MySQL DATETIME format)
```

###  Ques. What is PDO ?
Ans.  


### Ques. What is the relation between Classes and Objects ?
They look very much same but are not same.
A class is a definition, while an object is an instance of the class.
A class is a blueprint while objects are actual objects existing in the real world.
Suppose we have a class Person which has attributes and methods like name, age, height, weight, color etc.
Class Person is just a prototype, now we can create real-time objects of class Person.
#Example: Ajay is real time object of class Person, which have name=Ajay, age=23, height=170cm, weight=60kg and color=black etc.
Class
A way to bind data and associated functions together.
Class have many objects.
Class is a template for creating objects.
It is logical existence.
Memory space is not allocated, when it is created.
Definition (Declaration) is created once.
Class is declared using "class" keyword.
Object
Basic runtime entity in object oriented environment.
Object belongs to only class.
Object are a implementation of class.
It is physical existence.
Memory space is allocated when it is created.
It is created many times as you required.
Object is the instance or variable of class.
Ques:- What is Member Variable and Member function?
Member Variable − These are the variables defined inside a class. This data will be invisible to the outside of the class and can be accessed via member functions. These variables are called attribute of the object once an object is created.
Member function − These are the function defined inside a class and are used to access object data.





PHP 5 introduces abstract classes and methods.
Classes defined as abstract may not be instantiated
Classes that contains at least one abstract method must also be abstract.
Methods defined as abstract simply declare the method's signature - they cannot define the implementation. Abstract methods cannot be defined as private.
Classes which are inheriting it's parent class must provides implementations for the abstract methods.
abstract class TV {
 
   private $isOn = false;
   abstract function getBrand();
   public function turnOnTV() {
       $this->isOn = true;
   }
   public function turnOffTV() {
       $this->isOn = false;
   }
}
class Panasonic extends TV {
   public function getBrand(){
       return "Panasonic";
   }
}
class Sony extends TV {
   public function getBrand(){
       return "Sony";
   }
}




### Ques. How to get IP address from an HTTP request ?
```php
$_SERVER['REMOTE_ADDR'];
```

### Ques. How to get IP address of the web server in php ?
```php
$_SERVER['SERVER_ADDR'];
```

### Ques. how to create a mySql connection ?
```
mysql_connect("host_name", "User_name", "Password") ;
mysql_select_db("db_name");
```

### Ques. how to stop the execution of php Script ?
The exit() function is used to stop the execution of PHP script.

### Ques. how to upload file in php ?
The move_uploaded_file() function is used to upload file in PHP.<br>
```php
move_uploaded_file($source_path,$des_path);
```

### **Ques. How to get value in the url?**
$sort = $_GET[‘url’]

### **Magic Method**
* Magic Method apne aap ek special event par call ho jata hai.<br>
ex:- get, set, isset, unset, tosting, clone, sleep, wakeup, invoice, Autoload
* magic method are member function that are available to all instance of class. magic method always start with "__"<br>
ex: ```__construct```
* all magic method need to be declared as public.
* various magic method used be defined within the class or program scope.

### **Ques. What We can ceil() and floor() function in php?**
__Ceil()__ is used to find nearest maximum values of passing value.
```php
$no = 6.5;
$ans = ceil($no);
Echo $ans;
Output:- 7
```
__Floor()__ is used to find nearest minimum values of  passing value.
```php
$no = 6.5;
$ans = ceil($no);
Echo $ans;
Output:- 6
```

### **Ques. Find The Php Information ?**
```php
<?php
   echo phpinfo();
?>
```

**[⬆ Back to Top](#table-of-contents)**
### **Ques. What is the differance between explode and split?**
* **Split** The Split function the string into an array using a regular expression and return an array.<br>
* Split regular expression ke sath work karta hai.
```php
$a = split(':', india : pakistan : srilanka : usa)
print_r($a);
```
* **Explode** The explode function splits the string by string. 
* explode dalimeter char ke sath work karta hai.
```php
$a = explode('and','india and pakistan and usa');
print_r($a);
```

### **Ques. How can we get the browser properties using PHP?**
```php
$_SERVER['HTTP_USER_AGENT']
```

### **Ques. What does isset() function?**
The isset() function checks if the variable is defined and not null.

### **Ques. How can we submit a form without a submit button?**
```php
document.formname.submit()
```

### **Ques. mysqli_real_escape_string() function?**
The mysqli_real_escape_string() function escape special character in a string for use in an sql statement.
```php 
$fname = mysqli_real_escape_string($con, $_post['fname']);
```

###

```
Q:-
function changevalue(&$y)
	{ 
		 $y = $y + 7;  
	}  
	$num = 8; 
	changevalue($num); 
	echo $num;
```
