# PHP Array & String Function

| Array Function                        | String Function                   |
| :------------------------------------ | :-------------------------------- |
| [array_chunk](#array_chunk)           | [strlen](#strlen)                 |
| [array_key_exists](#array_key_exists) | [str_word_count](#str_word_count) |
| [array_keys](#array_keys)             | [strrev](#strrev)                 |
| [array_merge](#array_merge)           | [strpos](#strpos)                 |
| [array_push](#array_push)             | [str_replace](#str_replace)       |
| [array_rand](#array_rand)             | [strtoupper](#strtoupper)         |
| [array_slice](#array_slice)           | [strtolower](#strtolower)         |
| [array_values](#array_values)         | [ucfirst](#ucfirst)               |
| [sort](#sort)                         | [lcfirst](#lcfirst)               |
| [asort](#asort)                       | [ucwords](#ucwords)               |
| [usort](#usort)                       | [addcslashes](#addcslashes)       |
| [uasort](#uasort)                     | [addslashes](#addslashes)         |
| [uksort](#uksort)                     | [stripslashes](#stripslashes)     |
| [arsort](#arsort)                     | [explode](#explode)               |
| [ksort](#ksort)                       | [implode](#implode)               |
| [krsort](#krsort)                     | [str_split](#str_split)           |
| [rsort](#rsort)                       | [trim](#trim)                     |
| [count](#count)                       | [ltrim](#ltrim)                   |
| [in_array](#in_array)                 | [rtrim](#rtrim)                   |
| [array_search](#array_search)         | [strstr](#strstr)                 |
|                                       | [md5](#md5)                       |
|                                       | [substr](#substr)                 |
|                                       | [wordwrap](#wordwrap)             |
|                                       | [nl2br](#nl2br)                   |


### **array_chunk**
The __array_chunk()__ function splits an array into chunks of new arrays.<br>
__syntex:-__ array_chunk(array, size, preserve_key)
```php
<?php
$cars=array("Volvo","BMW","Toyota","Honda","Mercedes","Opel");
print_r(array_chunk($cars,2));
?>
output:- Array ( 
[0] => Array ( [0] => Volvo [1] => BMW ) 
[1] => Array ( [0] => Toyota [1] => Honda ) 
[2] => Array ( [0] => Mercedes [1] => Opel ) 
)
```

### array_key_exists
The __array_key_exists()__ function checks an array for a specified key, and returns true if the key exists and false if the key does not exist.<br>
__syntex:-__  array_key_exists(key,array)
```php
<?php
$a=array("Volvo"=>"XC90","BMW"=>"X5");
if (array_key_exists("Volvo",$a))
  {
  echo "Key exists!";
  }
else
  {
  echo "Key does not exist!";
  }
?>
output:- Key Exists!
```

### array_keys
The __array_keys()__ function returns an array containing the keys.
__Syntex:-__ array_keys(array,value,strict)
```php
<?php
$a=array("Volvo"=>"XC90","BMW"=>"X5","Toyota"=>"Highlander");
print_r(array_keys($a));
?>
output:-
Array
(
	[0] => Volvo
	[1] => BMW
	[2] => Toyota
)
```

### array_merge
The __array_merge()__ function merges one or more arrays into one array.
__syntex:-__ array_merge(array1,array2,array3...)
```php
<?php
$a1=array("red","green");
$a2=array("blue","yellow");
print_r(array_merge($a1,$a2));
?>
output:-
Array(
[0] => red
[1] => green
[2] => blue
[3] => yellow
)
```

### array_push
The __array_push()____ function inserts one or more elements to the end of an array.<br>
__syntex:-__ array_push(array,value1,value2...)
```php
<?php
$a=array("red","green");
array_push($a,"blue","yellow");
print_r($a);
?>
output:-
Array(
[0] => red
[1] => green
[2] => blue
[3] => yellow
)
```

### array_rand
The __array_rand()__ function returns a random key from an array, or it returns an array of random keys if you specify that the function should return more than one key.<br>
__syntex:-__ array_rand(array,number)<br>
```php
<?php
$a=array("red","green","blue","yellow","brown");
$random_keys=array_rand($a,3);
echo $a[$random_keys[0]]."<br>";
echo $a[$random_keys[1]]."<br>";
echo $a[$random_keys[2]];
?>
output:-
red
blue
yellow
```

### array_slice
The __array_slice()__ function returns selected parts of an array.<br>
syntex:-array_slice(array,start,length,preserve)<br>
```php
<?php
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,2));
?>
output:-
Array(
[0] => blue
[1] => yellow
[2] => brown
)
```

### array_values
The __array_values()__ function returns an array containing all the values of an array.<br>
syntex:-array_values(array)<br>
```php
<?php
$a=array("Name"=>"Peter","Age"=>"41","Country"=>"USA");
print_r(array_values($a));
?>
output:-
Array ( 
[0] => Peter 
[1] => 41 
[2] => USA 
)
```

### sort
The __sort()__ function sorts an indexed array in ascending order.<br>
syntex:-sort(array,sortingtype);<br>
```php
<?php
$cars=array("Volvo","BMW","Toyota");
sort($cars);
$clength=count($cars);
for($x=0;$x<$clength;$x++)
  {
  echo $cars[$x];
  echo "<br>";
  }
?>
output:-
BMW
Toyota
Volvo
```
 
### asort
The __asort()__ function sorts an associative array in ascending order, according to the value.<br>
syntex:-asort(array,sortingtype);<br>
```php
<?php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
asort($age);

foreach($age as $x=>$x_value)
   {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>
output:-
Key=Peter, Value=35
Key=Ben, Value=37
Key=Joe, Value=43
```

### usort
The __usort()__ function sorts an array using a user-defined comparison function.<br>
syntex:-usort(array,myfunction);<br>
```php
<?php
function my_sort($a,$b)
{
if ($a==$b) return 0;
  return ($a<$b)?-1:1;
}
$a=array(4,2,8,6);
usort($a,"my_sort");

$arrlength=count($a);
for($x=0;$x<$arrlength;$x++)
  {
  echo $a[$x];
  echo "<br>";
  }
?> 
output:-
2
4
6
8
```

### uasort
The __uasort()__ function sorts an array by values using a user-defined comparison function.<br>
syntex:-uasort(array,myfunction);<br>
```php
<?php
function my_sort($a,$b)
{
if ($a==$b) return 0;
  return ($a<$b)?-1:1;
}
$arr=array("a"=>4,"b"=>2,"c"=>8,d=>"6");
uasort($arr,"my_sort");
 
foreach($arr as $x=>$x_value)
   {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>
output:-
Key=b, Value=2
Key=a, Value=4
Key=d, Value=6
Key=c, Value=8
```

### uksort
The __uksort()__ function sorts an array by keys using a user-defined comparison function.<br>
syntex:-uksort(array,myfunction);<br>
```php
<?php
function my_sort($a,$b)
{
if ($a==$b) return 0;
  return ($a<$b)?-1:1;
}
$arr=array("a"=>4,"b"=>2,"c"=>8,d=>"6");
uksort($arr,"my_sort");
 
foreach($arr as $x=>$x_value)
   {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>
output:-
Key=a, Value=4
Key=b, Value=2
Key=c, Value=8
Key=d, Value=6
```

### arsort
The __arsort()__ function sorts an associative array in descending order, according to the value.<br>
syntex:-arsort(array,sortingtype);<br>
```php
<?php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
arsort($age);

foreach($age as $x=>$x_value)
   {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>
output:-
Key=Joe, Value=43
Key=Ben, Value=37
Key=Peter, Value=35
```

### ksort
The __ksort()__ function sorts an associative array in ascending order, according to the key.<br>
syntex:-ksort(array,sortingtype);<br>
```php
<?php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
ksort($age);

foreach($age as $x=>$x_value)
   {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>
output:-
Key=Ben, Value=37
Key=Joe, Value=43
Key=Peter, Value=35
```

### krsort
The __krsort()__ function sorts an associative array in descending order, according to the key.<br>
syntex:-krsort(array,sortingtype);<br>
```php
<?php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
krsort($age);

foreach($age as $x=>$x_value)
   {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>
output:-
Key=Peter, Value=35
Key=Joe, Value=43
Key=Ben, Value=37
```

### rsort
The __rsort()__ function sorts an indexed array in descending order.<br>
syntex:-rsort(array,sortingtype);<br>
```php
<?php
$cars=array("Volvo","BMW","Toyota");
rsort($cars);

$clength=count($cars);
for($x=0;$x<$clength;$x++)
  {
  echo $cars[$x];
  echo "<br>";
  }
?>
output:-
Volvo
Toyota
BMW
```

### count
The __count()__ function returns the number of elements in an array.<br>
syntex:-count(array,mode);<br>
```php
<?php
$cars=array("Volvo","BMW","Toyota");
echo count($cars);
?>
output:- 
3
```

### in_array
The __in_array()__ function searches an array for a specific value.<br>
syntex:-in_array(search,array,type)<br>
```php
<?php
$people = array("Peter", "Joe", "Glenn", "Cleveland");

if (in_array("Glenn", $people))
  {
  echo "Match found";
  }
else
  {
  echo "Match not found";
  }
?>
output:- Match found
```

### array_search
The __array_search()__ function search an array for a value and returns the key.<br>
syntex:- array_search(value, array, strict)<br>
```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"blue");
echo array_search("red",$a);
?>
output:- a
```

### **Ques. Difference between array_merge() and array_combine()?**
* The **array_merge()** function is used to merge two or more arrays into a single array.
```php
$array1 = array("subject1" => "Python","subject2" => "sql");
$array2 = array("subject3" => "c/c++","subject4" => "java");

$final = array_merge($array1, $array2);
print_r($final);

Output:-
Array
(
    [subject1] => Python
    [subject2] => sql
    [subject3] => c/c++
    [subject4] => java
)
```
* The **array_combine()** function is used to combine two arrays and create a new array by using one array for **keys** and another array for **values**.
```php
$array1 = array("subject1" ,"subject2");
$array2 = array( "c/c++", "java");
$final = array_combine($array1, $array2);

print_r($final);

Array
(
    [subject1] => c/c++
    [subject2] => java
)
```

### **Ques. How to get second last element of array in php?**
```php
<?php
$array = array(5,6,70,10,36,2);
echo $array[count($array) -2];
?>

Output:- 36
```

### **Ques. How to get common values from two array in php?**
```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("e"=>"red","f"=>"black","g"=>"purple");
$a3=array("a"=>"red","b"=>"black","h"=>"yellow");

$result=array_intersect($a1,$a2,$a3); 
print_r($result);
?>

Output:- Array ( [a] => red )
```


# String Function


### strlen
The PHP __strlen()__ function returns the length of a string.
```php
<?php
echo strlen("Hello world!");
?> 
Output:-12
```

### str_word_count
The PHP __str_word_count()__ function counts the number of words in a string:
```php
<?php
echo str_word_count("Hello world!");
?> 
Output:- 2
```

### strrev
The PHP __strrev()__ function reverses a string:
```php
<?php
echo strrev("Hello world!");
?> 
Output:-dlrowolleH
```

### strpos
The PHP __strpos()__ function searches for a specific text within a string.
```php
<?php
echo strpos("Hello world!", "world");
?> 
Output:- 6
```

### str_replace
The PHP __str_replace()__ function replaces some characters with some other characters in a string.
```php
<?php
echo str_replace("world", "Dolly", "Hello world!");
?> 
Output:-Hello Dolly!
```

### strtoupper
The __strtoupper()__ function converts a string to uppercase.<br>
syntex:-strtoupper(string)<br>
```php
<?php
echo strtoupper("Hello WORLD!");
?> 
output:- HELLO WORLD!
```

### strtolower
The __strtolower()__ function converts a string to lowercase.<br>
syntex:-strtolower(string)<br>
```php
<?php
echo strtolower("Hello WORLD.");
?>
output:- hello world.
```

### ucfirst
The __ucfirst()__ function converts the first character of a string to uppercase.<br>
syntex:-ucfirst(string)<br>
```php
<?php
echo ucfirst("hello world!");
?> 
output:- Hello world!
``` 

### lcfirst
The __lcfirst()__ function converts the first character of a string to lowercase.<br>
syntex:-lcfirst(string)<br>
```php
<?php
echo lcfirst("Hello world!");
?> 
output:- hello world!
```

### ucwords
The __ucwords()__ function converts the first character of each word in a string to uppercase.<br>
syntex:-ucwords(string)<br>
```php
<?php
echo ucwords("hello world");
?> 
output:- Hello World
```

### addcslashes
The __addcslashes()__ function returns a string with backslashes in front of the specified characters.<br>
syntex:-addcslashes(string,characters)<br>
```php
<?php 
$str = addcslashes("Hello World!","W");
echo($str); 
?>
output:- Hello \World!
```

### addslashes
The __addslashes()__ function returns a string with backslashes in front of predefined characters.<br>
syntex:-addslashes(string)<br>
```php
<?php 
$str = addslashes('What does "yolo" mean?');
echo($str); 
?> 
output:- What does \"yolo\" mean?
```

### stripslashes
The __stripslashes()__ function removes backslashes<br>
Syntax: - stripslashes(string)<br>
```php
<?php
echo stripslashes("Who\'s Peter Griffin?");
?>
output:- Who's Peter Griffin?
```

### explode
The __explode()__ function breaks a string into an array.<br>
Syntax:-explode(separator,string,limit)<br>
```php
<?php
$str = "Hello world. It's a beautiful day.";
print_r (explode(" ",$str));
?> 
output:- Array ( 
[0] => Hello 
[1] => world. 
[2] => It's 
[3] => a 
[4] => beautiful 
[5] => day.
)
```

### implode
The __implode()__ function returns a string from the elements of an array.<br>
syntex:-implode(separator,array)<br>
```php
<?php
$arr = array('Hello','World!','Beautiful','Day!');
echo implode(" ",$arr);
?>
output:-
Hello World! Beautiful Day!
```

### str_split
The __str_split()__ function splits a string into an array.<br>
syntes:-str_split(string,length)<br>
```php
<?php
print_r(str_split("Hello"));
?>
output:- Array ( [0] => H [1] => e [2] => l [3] => l [4] => o )
```

### trim
The __trim()__ function removes whitespace and other predefined characters from both sides of a string.<br>
syntex:-trim(string,charlist)<br>
```php
<?php
$str = "Hello World!";
echo $str . "<br>";
echo trim($str,"Hed!");
?>
output:-
Hello World!
llo Worl
```

### ltrim
The __ltrim()__ function removes whitespace or other predefined characters from the left side of a string.<br>
syntex:-ltrim(string,charlist)<br>
```php
<?php
$str = "Hello World!";
echo $str . "<br>";
echo ltrim($str,"Hello");
?> 
output:-
Hello World!
World!
```

### rtrim
The __rtrim()__ function removes whitespace or other predefined characters from the right side of a string.<br>
syntex:-rtrim(string,charlist)<br>
```php
<?php
$str = "Hello World!";
echo $str . "<br>";
echo rtrim($str,"World!");
?>
output:-
Hello World!
Hello
```

### strstr
The __strstr()__ function searches for the first occurrence of a string inside another string.<br>
Syntax:-strstr(string,search,before_search)<br>
```php
<?php
echo strstr("Hello world! mohit","world");
?>
output:- world! mohit
```

### md5
The __md5()__ function calculates the MD5 hash of a string.<br>
Syntax:-md5(string,raw)<br>
```php
<?php
$str = "Hello";
echo md5($str);
?>
output:  8b1a9953c4611296a827abf8c47804d7
```

### substr
The __substr()__ function returns a part of a string.<br>
__Syntax:-__ substr(string,start,length)<br>
```php
<?php
echo substr("Hello world",4);
?>
output:- o world
```

### wordwrap
The __wordwrap()__ function wraps a string into new lines when it reaches a specific length.<br>
__Syntax:-__ wordwrap(string,width,break,cut)<br>
```php
<?php
$str = "An example of a long word is: Supercalifragulistic";
echo wordwrap($str,15,"<br>\n");
?>
output:-
An example of a
long word is:
Supercalifragulistic
```

### nl2br
The __nl2br()__ function inserts HTML line breaks (<br> or <br />) in front of each newline (\n) in a string.<bbr>
__syntex:-__ nl2br(string,xhtml)<br>
```php
<?php
echo nl2br("One line.\nAnother line.");
?>
output:-
One line
Another line
```

