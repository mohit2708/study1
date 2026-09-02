### Table of Contents

|  No.  | Questions                                                                  |
| :---: | -------------------------------------------------------------------------- |
|   1   | [Swap Number?](#Swap-Number)                                               |
|   2   | [Swap Number Without Third Variable?](#Swap-Number-Without-Third-Variable) |
|   3   | [Reverse String?](#Reverse-String)                                         |
|   4   | [Revers number?](#Revers-number)                                           |
|   5   | [Check the Prime Number or not?](#Check-the-Prime-Number-or-not)           |
|   6   | [Print the prime number?](#Print-the-prime-number)                         |
|   9   | [Find The Number Even Or Odd?](#Find-The-Number-Even-Or-Odd)               |
|   7   | [Fibonacci Number print?](#Fibonacci-Number-print)                         |
|   8   | [Print The Matrix?](#Print-The-Matrix)                                     |
|  10   | [Highest Value in the array?](#Highest-Value-in-the-array)                 |
|       | [String Pattern](#string-Pattern)                                          |
|       | [Highest Value in the array?](#Highest-Value-in-the-array)                 |

|       | [Find the largest first, second, third, fourth and fifth largest number from the array](#find-the-largest-first-second-third-fourth-and-fifth-largest-number-from-the-array) |


### **Swap Number?**
```php
function abc($a,$b){
    echo "Value of a: $a</br>";
    echo "Value of b: $b</br>";
    $temp=$a;
    $a=$b;
    $b=$temp;
    echo "Value of a: $a</br>";
    echo "Value of b: $b</br>";
}
$n1 = 4;
$n2 = 2;
abc ($n1,$n2);
```
**[⬆ Back to Top](#table-of-contents)**

### **Swap Number Without Third Variable?**
```php
$a = 5;
$b = 9;

$a =  $a + $b;  // 5 + 6 = 11
$b = $a - $b;   // 11 - 6 = 5
$a = $a - $b;  // 11 - 5 = 6

echo $a . ',' . $b;
```
**[⬆ Back to Top](#table-of-contents)**

### **Reverse String?**
```php
$s = 'mohit saxena';		
$l = strlen($s);
for($i=$l-1; $i>=0; $i--){
    echo $s[$i];
}

Output:- anexas tihom

--------------------------------------------------------------------
# 2 Option
$str = 'Mohit Saxena';
$length = strlen($str);

$rev = '';
for($i = $length-1; $i >= 0; $i--) {
    $rev .= $str[$i]; 
}
echo $rev;

Output:- anexaS tihoM
```
**[⬆ Back to Top](#table-of-contents)**

### **Revers number?**
```php
# Type 1st:-
$num = 2039;
$revnum = 0;
while ($num != 0){
    $revnum = $revnum * 10 + $num % 10;
    $num = (int)($num / 10); 
} 
echo "Reverse number: $revnum";

--------------------------------------------------------------------------
# Type 2nd:-

$num = 23456;  
$revnum = 0;  
while ($num > 1){  
    $rem = $num % 10;  
    $revnum = ($revnum * 10) + $rem;  
    $num = ($num / 10);   
}  
echo "Reverse number of 23456 is: $revnum";  
```
**[⬆ Back to Top](#table-of-contents)**

### Match the Two words same or not
```php
function check_name($str1,$str2)
{
    $first = str_split($str1);
            sort($first);
            $first_name=implode($first);

    $second = str_split($str2);
            sort($second);
            $second_name=implode($second);
    
    if($first_name==$second_name){
        return "Match";
    }else{
        return "Do not Match";
    }              
 }

$result= check_name('mohit','himt');
echo $result;
```
**[⬆ Back to Top](#table-of-contents)**

### **Check the Prime Number or not?**
```php
function IsPrime($n){
    for($x=2; $x<$n; $x++){
        if($n %$x ==0){
            return 0;
        }
        return 1;
    }  
    $a = IsPrime(7);  
    if ($a==0)  
        echo 'This is not a Prime Number.....'."\n";  
    else  
        echo 'This is a Prime Number..'."\n";
}
Output :-  This is a Prime Number..
```
**[⬆ Back to Top](#table-of-contents)**

### **Print the prime number?**
```php
function primeno($n){
    for($i=1;$i<=$n;$i++){  //numbers to be checked as prime
        $counter = 0; 
        for($j=1;$j<=$i;$j++){ //all divisible factors
            if($i % $j==0){
                $counter++;
            }
        }
        if($counter==2){
            echo $i." is Prime <br/>";
        }
    }
}

primeno(100);
```
**[⬆ Back to Top](#table-of-contents)**

### **Find The Number Even Or Odd?**
```php 
function evenOrOdd($n){
if($n%2==0)
    {
        echo 'even number'; 
    }
    else 
    {
        echo 'odd number';	
    }
}
$a = '5';
evenOrOdd($a);
Output:- odd number
```
**[⬆ Back to Top](#table-of-contents)**

### **Fibonacci Number print?**
###### Type 1st:-
```php
$count = 0 ;
$f1 = 0;
$f2 = 1;
echo $f1." , ";
echo $f2." , ";
while ($count < 20 )
{      
    $f3 = $f2 + $f1 ;
    echo $f3." , ";
    $f1 = $f2 ;
    $f2 = $f3 ;
    $count = $count + 1;
}
Output :- 
0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144 , 233 , 377
-------------------------------------------------------------------------

###### Type 2nd:-

define('NUM',5);
$a = 0;
$b = 1;
echo "$a $b "; // 0 1
for($i=1; $i<= NUM-2; $a=$b, $b=$c, $i++ ){
    echo $c = $a+$b;
    echo " ";
}

Output :- 0, 1, 1, 2
-------------------------------------------------------------------------

##### Type 3rd:-
$first = 0;
$second = 1;
echo "Fibonacci Series \n";
echo $first.' '.$second.' ';
for($i = 2; $i < 12; $i++){
    $third = $first + $second;
    echo $third.' ';
    $first = $second;
    $second = $third;
}

Output :- Fibonacci Series 0 1 1 2 3 5 8 13 21 34 55 89
```
**[⬆ Back to Top](#table-of-contents)**

### **Print The Matrix?**
```php
for($i=0;$i<3;$i++){ 
	for($j=0;$j<3;$j++)
	{
		if($i==$j)
		{
			echo 1;
		}
		else
		{
			echo 0;
		}     
	} 
	echo '<br/>';
}
Output:- 
1 0 0 
0 1 0 
0 0 1
```
**[⬆ Back to Top](#table-of-contents)**



### **Program to find Palindrome Number?**
```php
<?php 
function check_palindrome($n){
    $inpt = $n;
    $sum = 0; 
    while(floor($inpt)) {
        $newnum = $inpt % 10;
        $sum = $sum * 10 + $newnum;
        $inpt = $inpt/10;
    }
    return $sum;
}
 
$input = 12321;
$num = check_palindrome($input);
  
if($input==$num){
    echo "Palindrome number";
}else{
    echo "Not a Palindrome";
}
```


### **Program to find Palindrome string?**
```php
$str = 'level';
$strLen = strlen($str)-1;
$revStr = '';
for($i=$strLen; $i>=0; $i--){
    $revStr.=$str[$i];
}
if($revStr == $str)
    echo 'Palindrome';
else
    echo "Not Palindrome";
```

### Print the Odd Number
```php
function oddNumber($s,$e)
{
for($i=$s; $i<=$e; $i+=2){
    echo '<pre>';
    echo $i;
}
}
oddNumber(1,16);
Output:- 1 3 5 7 9 11 13 15
```
 

# Array Questions

### **Remove Duplicate Elements or Values from Array**
```php
$inputArray = array(1, 4, 2, 1, 6, 4, 9, 7, 2, 9);
$uniqueArry = array();

foreach ($inputArray as $val){
    if(!in_array($val,$uniqueArry)){
        $uniqueArry[] = $val;
    }
}
print_r($uniqueArry);

Output:- Array ( [0] => 1 [1] => 4 [2] => 2 [3] => 6 [4] => 9 [5] => 7 )
--------------------------------------------------------------------------------

# 2 type
$givenArray = array(2,5,2,10,4,5,8,16);
$uniqueArry = array();
 
foreach($givenArray as $val) { //Loop1 
    foreach($uniqueArry as $uniqueValue) { //Loop2 
        if($val == $uniqueValue) {
            continue 2; // Referring Outer loop (Loop 1)
        }
    }
    $uniqueArry[] = $val;
}
print_r($uniqueArry);

Output:- Array ( [0] => 2 [1] => 5 [2] => 10 [3] => 4 [4] => 8 [5] => 16 )
```
**[⬆ Back to Top](#table-of-contents)**

### **Find duplicate values in array**
```php
$givenArray = array(16, 2,5,2,10,4,5,8,16);
$duplicateValues = array();
$uniqueValues = array();
 
foreach($givenArray as $val) {    
    if (!isset($uniqueValues[$val])) {
         $uniqueValues[$val] = $val;
    } else {
        $duplicateValues[] = $val;
    }
  
}
print_r($duplicateValues);

Output:- Array ( [0] => 2 [1] => 5 [2] => 16 )
```
**[⬆ Back to Top](#table-of-contents)**


### **Sort an Array / Using Bubble sort**
```php
function bubbleSort(array $arr)
{
    $n = count($arr);
    for ($i = 1; $i<$n; $i++)
		{
        for ($j = $n-1; $j>= $i; $j--) 
		{
			if($arr[$j-1] > $arr[$j]) 
			{
				$tmp = $arr[$j-1];
                $arr[$j-1] = $arr[$j];
                $arr[$j] = $tmp;
            }
        }
    }
     return $arr;
}
echo '<pre>'; 
$arr = array(255,1,22,3,45,5);
$result = bubbleSort($arr);
print_r($result);

Output:- 1 3 5 22 45 255
```
**[⬆ Back to Top](#table-of-contents)**

### **Minimum value in array:-**
```php
# using For each loop
$a = array(10, 44, 5, 6, 68, 9);
$blank = $a[0];
foreach($a as $v){
    if($blank > $v)
    $blank = $v;
}
echo $blank;
------------------------------------------------------

# 2nd Option  using For loop
$a = array(15,10,20,100,25,30);
$max = max($a);
$l = count($a);
for ($i=0; $i<$l; $i++){
    $chek = $a[$i];	
    if($chek<$max){
        $z = $chek;
        $max = $z;	
    }
}
echo $z;
```
**[⬆ Back to Top](#table-of-contents)**


### **Higest value in array(Array max value):-**
```php
     $a = array(1, 44, 5, 6, 68, 9);
     $blank = 0;
     foreach($a as $v)
    {
        if($blank < $v)
        $blank = $v;
    }
 echo $blank;
----------------------------------------------
# Type 2
 $a =array(2,44,5,6,68,9);
 $l = count($a);
 $res=0;
for($i=0;$i<$l;$i++){	
  if($res<$a[$i]){
      $res=$a[$i];
    }
}
echo $res;
```
**[⬆ Back to Top](#table-of-contents)**

### **Find the largest first, second, third, fourth and fifth largest number from the array**
```php
$array1 = array(2,4,2,3,3,6,5,9,3,15,4,5,6,9);
$first_highest = 0;
$second_highest = 0;
$third_highest = 0;

foreach($array1 as $key=>$val) {
	if($val > $first_highest) {
        $second_highest = $first_highest;
    	$first_highest = $val;     
    }else if($val > $second_highest && $val != $first_highest) {
    	$second_highest = $val;
    }else if($val > $third_highest && $val != $first_highest && $val != $second_highest) {
    	$third_highest = $val;
    }
}

print_r($first_highest);
echo "<br />";
print_r($second_highest);
echo "<br />";
print_r($third_highest);

Output:-
15
9
6
//////////////////////////////////////////////
$array1 = array(2,4,2,3,3,6,5,9,11,3,15,4,5,6,9);
$maxV = $minV = $thirdLN = $fourthLN = $fifthLN = 0;
foreach($array1 as $key=>$val) {
	if($val > $maxV) {
    	$fifthLN = $fourthLN;
    	$fourthLN = $thirdLN;
    	$thirdLN = $minV;
        $minV = $maxV;
        $maxV = $val;
        
    } else if($val > $minV && $val != $maxV) {
    	$minV = $val;
    } else if($val > $thirdLN && $val != $maxV && $val != $minV) {
    	$thirdLN = $val;
    } else if($val > $fourthLN && $val != $maxV && $val != $minV && $val != $thirdLN) {
    	$fourthLN = $val;
    } else if($val > $fifthLN && $val != $maxV && $val != $minV && $val != $thirdLN && $val != $fourthLN) {
    	$fifthLN = $val;
    }

}
echo "<pre>";
print_r($fifthLN);
echo "<br />";
print_r($fourthLN);
echo "<br />";
print_r($thirdLN);
echo "<br />";
print_r($minV);
echo "<br />";
print_r($maxV);
```


**[⬆ Back to Top](#table-of-contents)**

### **Print Even number from the given array**
```php
$array1 = [2,5,4,2,6,9,4,2,5,8];
$blank_array = array();
foreach($array1 as $key => $val) {
   if(($val % 2) == 0) {
   $blank_array[] = $val;
   }
}

echo "<pre>";
print_r($blank_array);
```

### **Print Even number from the given array And remove the Duplicate array**
```php
$evenNo = [];
foreach($blank_array as $key => $val) {
    if($val%2 == 0) {
        $evenNo[$val] = $val;
    }
}
print_r($evenNo);
?>
```

### **Print odd number from the given array**
```php
$array1 = [2,3,6,9,1,7,4,3,5];
$array2 = array();
foreach($array1 as $key => $val) {
   if(($val % 2) == 1) {
   $array2[] = $val;
   }

}

echo "<pre>";
print_r($array2);
```


### **Print odd number from the given array And remove the Duplicate array**
```php
$arr = [2,5,4,2,6,9,4,2,5,8];
$oddNo = [];
foreach($arr as $key => $val) {
    if($val%2 == 1) {
        $oddNo[$val] = $val;
    }
}
print_r($oddNo);
```

### **Add space after 2 character:- //my-na-me-is-mo-hi-ts**
```php
<?php
$str = "my name is mohit saxena";
$len = strlen($str);
for($i=0; $i<$len; $i++)
{
	if($i%2==0 && $i!=0)
	{
		echo "-";
	}
	echo $str[$i];
}
?>
```

### String Pattern
```php		
for($i=0;$i<=5;$i++){	
    for($j=1;$j<=$i;$j++){	
        echo $i;		
    }			
    echo '<br>';		
} 			
?>			

Output:- 		
1			
22			
333			
4444			
55555			
```

```php
<?php
for($i=0;$i<=5;$i++){
for($j=1;$j<=$i;$j++){
echo "1";
}
echo '<br>';
} 
?>

Output:-
1
11
111
1111
11111
```


```php
<?php
 for($i=0;$i<=5;$i++){
 for($j=1;$j<=$i;$j++){
 echo $j;
 }
 echo '<br>';
} 
?>
Output:-
1
12
123
1234
12345
```


```php
<?php
 for($i=0;$i<=5;$i++){			
 for($j=5-$i;$j>=1;$j--){		
 echo "*&nbsp&nbsp;";			
 }								
 echo "<br>";
}
?>

Output:-
* * * * *
* * * *
* * *
* *
*
```

```php
<?php
	for($i=0;$i<=5;$i++)			
	{					
	for($j=1;$j<=$i;$j++)		
	{					
	echo "* ";				
	}					
	echo "<br>";
	}
?>

Output:-
*
* *
* * *
* * * *
* * * * *
```

```php
<?php
for ($row = 1; $row <= 5; $row++)
{		
echo "* </br>";	
}
?>
Output:-
*
*
*
*
*
```

```php
<?php
for ($row = 1; $row <= 5; $row++)
{				
 for ($col = 1; $col <= 5; $col++)
  {
   echo '* ';
  }
   echo "</br>";
}
?>

Output:-
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### Sort multidimensional array by name
```php
<?php

$abc = [
    ["name" => "mohit", "age" => 30],
    ["name" => "abhinav", "age" => 36],
    ["name" => "rohit", "age" => 25]
];

// Bubble sort by "name" key
$n = count($abc);
for ($i = 0; $i < $n - 1; $i++) {
    for ($j = 0; $j < $n - $i - 1; $j++) {
        if ($abc[$j]["name"] > $abc[$j + 1]["name"]) {
            // Swap $abc[$j] and $abc[$j+1]
            $temp = $abc[$j];
            $abc[$j] = $abc[$j + 1];
            $abc[$j + 1] = $temp;
        }
    }
}
print_r($abc);
// Print the sorted array
foreach ($abc as $person) {
    echo "Name: " . $person["name"] . ", Age: " . $person["age"] . "\n";
}
?>

```

```php
<?php
$num =23;
for( $j = 2; $j <= $num; $j++ )
{
	for( $k = 2; $k < $j; $k++ )
	{
		if( $j % $k == 0 )
		{
			break;
		}
	}
	if( $j == $k )
	echo $j;
}
?>
Output:- 2 3 5 7 11 13 17 19 23
```









### Greatest Number
```php
 <?php
function abc($a,$b)
{
	if($a>$b)							{
		echo $a;
	}
	else
	{
		echo $b;
	}
}
$n1 = 21;
$n2 = 20;
abc ($n1,$n2);
?>
Output:- 21
```

### Array mai 1 position & 4 position ki value ko add karna
```php
<?php
function add($x,$y) 
{
		$u = array(5,3,4,6,9);			
		$x1 = $u[$x];
		$y1 = $u[$y];
		 $sum = $x1 + $y1;
		 echo $sum;	
}
add(1,4);
?>
Output:- 12
```


   
### c
    ```php
    <?php
    $count ='a';			// a
    for($i=0;$i<5;$i++)		// b
    {	echo $count;		// c
        echo '<br>';		// d
        $count++;
    }
    ?> 
    ```

```php
<?php
for ($i=2; $i<=100; $i+=2)		//Find all even numbers between 1 to 100
{
	echo $i." ";
} 
?>
```

```php
<?php 
$myarray = array(8,7,5,14,4,5,9,11,9,10);			// array ki even location wale number add jo jae
$c = count($myarray);
$x = 0;
for ($i=0; $i<$c; $i++) 
{ 
	echo '<pre>';
	echo  $i;
	if ($i % 2 == 0) 
	{
		$sum = $myarray[$i] + $x;
		$x = $sum;
		echo $x;
	}
	else 
	{
		echo "odd\n";
	}
}
?>
```


```php
<?php
function add($n1) 
{	//$a = count($n1);			// array ke sare no add karne ke liye
	$b = 0;
	for($i=0; $i<3 ;$i++)		// array ke 1 to 3 number add ho jae
	{	 $x = $n1[$i];
		 $y = $b + $x;
		 $b = $y;

		 echo '<pre>';
		 echo $b;
	}
}
$x = array(5,5,4,6,1);
add($x);
?>
```

```php
string mai 3 ka baad dot(....) ho jae....
<?php
function abc($a)
{ $l = strlen($a);
  $str='';
 for($i=0; $i<$l; $i++) 
	{						
	 $m = $a[$i];
	 $str = $str.$m;	
	 if(strlen($str)>=4)
	  {
		echo $str.'------';
		break;
	  }
	}
}
$x = 'abcdefgh';
abc ($x);
?>
Output:-
abc------
```

```php
<?php
 for ($i=1; $i<=5; $i++){
 echo "The Number is: ".$i."<br/>";
 } 
 ?>
Output:-
The Number is: 1<br>
The Number is: 2<br>
The Number is: 3<br>
The Number is: 4<br>
The Number is: 5<br>
```


https://phpgurukul.com/php-programming-logical-interview-questions-answers/
For Array logic questions link
https://www.mostlikers.com/p/php-logical-interview-questions-and.html
https://www.tutsmake.com/php-logical-interview-questions-and-answers-for-1235-year-experience/

https://www.bestinterviewquestion.com/php-arrays
programmes
https://www.letsknowit.com/php-programming-questions

https://www.w3resource.com/php-exercises/php-for-loop-exercises.php

https://tutorialdeep.com/php/print-pyramid-star-patterns-php/









print odd number but remove the dublicate odd number
$arr = [2,5,4,2,6,9,4,2,5,8];
$oddNo = [];
foreach($arr as $key => $val) {
    if($val%2 == 1) {
        $oddNo[$val] = $val;
    }
}


print_r($oddNo);

Q7:- Check given number is prime or not.
Ans:- Prime number:-A number that is divisible only by itself and 1 is called prime number (e.g. 2, 3, 5, 7, 11).
$num = 11;  
$count=0;  

for ($i = 1; $i <= $num; $i++) {
	if(($num % $i) == 0) {
    	$count ++;
    }
}

if($count == 2) {
 	echo $num. " Number is prime";
} else {
	echo $num. " Number is not prime";
}

Q8:- Print 1 to 100 prime numbers
Ans:-
function primeno($n){

  for($i=1;$i<=$n;$i++){  //numbers to be checked as prime

          $counter = 0; 
          for($j = 1; $j <= $i; $j++) { //all divisible factors


                if($i % $j==0) { 

                      $counter++;
                }
          }

        //prime requires 2 rules ( divisible by 1 and divisible by itself)
        if($counter==2){

               print $i." is Prime <br/>";
        }
    }
} 

primeno(100);  //find prime numbers from 1-100


Q9:- Print 1 to 100 alternate prime numbers.
Ans:-
function primeno($n){
  $alternate = 0;
  for($i=1;$i<=$n;$i++){  //numbers to be checked as prime

          $counter = 0; 
          for($j=1;$j<=$i;$j++){ //all divisible factors


                if($i % $j==0){ 

                      $counter++;
                }
          }

        //prime requires 2 rules ( divisible by 1 and divisible by itself)
        if($counter==2){
	if($alternate == 1) {
                $alternate = 0;
                } else {
             		print $i." is Prime <br/>";
                    $alternate = 1;
                }
                 
               
        }
    }
} 

primeno(100);  //find prime numbers from 1-100

Q:-Print prime no only given number by the user like if suppose user enter 5 then it should print 5 prime no.
Ans:-
<?php

function primeNo($n) {
    $length = $n*$n;
    for($i=2; $i <= $length; $i++) {
        $count = 0;
        for($j=1; $j<=$i; $j++) {
            if($i % $j == 0) {
                $count++;
            }            
        }
        if($count == 2) {
            $n--;
            echo $i. " is a prime no". "\n";
        }
        if($n==0)  {
            break;
        }
        
    }
}

primeNo(5);
OUTPUT:-
2 is a prime no
3 is a prime no
5 is a prime no
7 is a prime no
11 is a prime no

Q:- What is the output below.
$search = "Hello";

$string = "Hello welcome to in Chetu India";

if(strpos($search, $string)) {
    echo "found";
}else {
    echo "not found";
}
Ans:- not found because “Hello” is the zero position and strpos return position of a string.

Q:- Sorting array in php.
Ans:-
    $array = array(1, 6, 23, 10, 3, 2, 15,7);
    $total = count($array);
    for ($i=0; $i < $total; $i++) { 
        for ($j=$i+1; $j < $total; $j++) { 
            if($array[$i] > $array[$j]) {
                $temp = $array[$i];
                $array[$i] = $array[$j];
                $array[$j] = $temp;
            }
        }
    }
    echo '<pre>';
    echo "Ascending Sorted Array is: "; 
    print_r($array);
or
$arr = [3,5,10,66,22,31,5,7,34,1,9];
for($i = 0; $i < count($arr); $i++) {
    for($j=0; $j< count($arr)-1; $j++) {
        if($arr[$j] > $arr[$j+1]) {
            $temp = $arr[$j];
            $arr[$j] = $arr[$j+1];
            $arr[$j+1] = $temp;
        }
    }
}
print_r($arr);die;

7.show only duplicate values from an array without built-in function PHP. ex array $arr = array(8,9,10,3,4,8,7,9,11,3);
Ans:-
<?php
$arr = array(8,9,10,3,4,8,7,9,11,3);
foreach($arr as $key => $val)
{
  unset($arr[$key]); 
  if (in_array($val,$arr))
  {
    echo $val . ",";
  }
} 


1. Write a Function that combines two lists by alternatingly taking element. For example Given two lists [a, b, c] and [1, 2, 3] the function should return [a, 1, b, 2, c, 3]
Ans:-
<?php
    
    $arr = array(‘a’,’b’,’c’);
    $arr1 = array(1,2,3);
    $new_array = array();

    for ($i=0; $i < count($arr); $i++)
    { 
        $new_array[] = $arr[$i];
        $new_array[] = $arr1[$i];

    }
    echo '<pre>'; print_r($new_array);
?>
Q:- Sum numberic value from array if array has string and numberic value.
Ans:-
$a = ['w',3,'tk','nm', 5,8,'4','9klp','lk'];
$sum = 0;
foreach($a as $key => $val) {
    
   if(is_numeric($val)) {
       $sum = $sum+ $val;
   } 
}
echo $sum;

Q:- Write a program to concatenate two strings character by character. e.g : JOHN + SMITH = JSOMHINTH
Ans
$str = 'JOHN';
$str2 = 'SMITH';

$arr = str_split($str);
$arr2 = str_split($str2);

// Find the longest string
$max = max(array(strlen($str), strlen($str2)));
or
$max = max(count($arr1), count($arr2));

$result = '';

for($i = 0; $i < $max; $i++){
    // Check if array key exists. If so, add it to result
    if (array_key_exists($i, $arr)){
        $result .= $arr[$i];
    }

    if (array_key_exists($i, $arr2)){
        $result .= $arr2[$i]; 
    }
}

echo $result; //JSOMHINTH



Q:- count occurence of character in a string
exp:-aabbccca
output:-a3,b2,c3

$str = "cdcdcdcdeeeefe";

$arr = str_split($str);
$result = array_count_values($arr);
//print_r($result);die;

$order = '';
foreach($result as $key=>$value) {
    $order .= $key.$value;
    
}

print_r($order);die;

OR Method 2
$str = 'aabbccca';
$arr = str_split($str);
$newArr = [];
foreach($arr as $key=> $val) {
    $newArr[$val][] = $val;
}
$string = '';
foreach($newArr as $k => $v) {
    $string .= $k.count($v);
}

print_r($string);

Factorial progamme usign recursive function

function fact ($n)  
{  
    if($n <= 1)   
    {  
        return 1;  
    }  
    else   
    {  
        return $n * fact($n - 1);  
    }  
}  
  
echo "Factorial of 6 is " .fact(6);  

Q:-$a = "PHP";
$b = $a + 1;
echo $b;





Q:-


      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1


Ans:-
<?php
for($i = 1; $i <= 4; $i++) {
    for($j=1; $j <= 4-$i; $j++) {
        
        echo ' ';
        
    }
    for($k=1; $k<=$i; $k++){
        echo $k. " ";
    }
    for($m=($i-1); $m>=1; $m--){
        echo $m . " ";
    }

    echo "\n";
}

Q:-Given a number and arrya find all possible combinations that sum of the given numbers.
Ans:-
$arr = [1,2,1,1,1];
$target = 3;
for($i=0; $i < count($arr); $i++) {
$sum = 0;
for($j = $i; $j < count($arr); $j++) {
$sum += $arr[$j];
if($sum === $target){
for($k = $i; $k <= $j; $k++) {
echo $arr[$k]. " ";
}
echo "\n";
}
}
}




Q7:- Check given number is prime or not.
Ans:- Prime number:-A number that is divisible only by itself and 1 is called prime number (e.g. 2, 3, 5, 7, 11).
$num = 11;  
$count=0;  

for ($i = 1; $i <= $num; $i++) {
	if(($num % $i) == 0) {
    	$count ++;
    }
}

if($count == 2) {
 	echo $num. " Number is prime";
} else {
	echo $num. " Number is not prime";
}

Q8:- Print 1 to 100 prime numbers
Ans:-
function primeno($n){
  for($i=1;$i<=$n;$i++){  //numbers to be checked as prime
          $counter = 0; 
          for($j = 1; $j <= $i; $j++) { //all divisible factors
                if($i % $j==0) { 
                      $counter++;
                }
          }
        //prime requires 2 rules ( divisible by 1 and divisible by itself)
        if($counter==2){
               print $i." is Prime <br/>";
        }
    }
} 

primeno(100);  //find prime numbers from 1-100


Q9:- Print 1 to 100 alternate prime numbers.
Ans:-
function primeno($n){
  $alternate = 0;
  for($i=1;$i<=$n;$i++){  //numbers to be checked as prime

          $counter = 0; 
          for($j=1;$j<=$i;$j++){ //all divisible factors


                if($i % $j==0){ 

                      $counter++;
                }
          }

        //prime requires 2 rules ( divisible by 1 and divisible by itself)
        if($counter==2){
	if($alternate == 1) {
                $alternate = 0;
                } else {
             		print $i." is Prime <br/>";
                    $alternate = 1;
                }
                 
               
        }
    }
} 

primeno(100);  //find prime numbers from 1-100


Q:- What is the output below.
$search = "Hello";

$string = "Hello welcome to in Chetu India";

if(strpos($search, $string)) {
    echo "found";
}else {
    echo "not found";
}
Ans:- not found because “Hello” is the zero position and strpos return position of a string.





============================+++=========================++++++++++++++++++++++++++
```PHP
Q2:- Find largest and second largest number from the array
Ans:-
$array1 = array(2,4,2,3,3,6,5,9,3,15,4,5,6,9);
$maxV = $minV = 0;
foreach($array1 as $key=>$val) {
	if($val > $maxV) {
    	$minV = $maxV;
    	$maxV = $val;
        
    } else if($val > $minV && $val != $maxV) {
    	$minV = $val;
    }

}
echo "<pre>";
print_r($minV);
echo "<br />";
print_r($maxV);

