### Ques. What is Cookie?
Php cookie is a small piece of information, which is stored on the client browser.
**Ex:-** Remember me.

* How to **set** cookie:-
```php
    Setcookie("name", "value", time()+3600);
```
* How to **Retrieve** a cookie:-
```php
    echo $_cookie["user"];
```
* How to **unset** Cookie:-      
```php
Setcookie(“sample”, “ram”, time()-3600);
```

##### Two types of cookie:-
* **Persistent Cookie:-** A persistent cookie is a cookie which is store information for certain time in a browser. By default cookie are temporary and are erased if we close the browser.

* **Non Persistent Cookie:-** Non persistent cookies are stored in ram on the server, and destroyed when the browser is closed. Ex:- login


### Ques. What is Session ?
* Session is way to store information to be used across multiple pages. It stores information on the server.
```php
Create session:- 	        session_start(); 
Set value into session:- 	$_SESSION['USER_ID']=1; 
Remove data from a session:- 	unset($_SESSION['USER_ID'];
```

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