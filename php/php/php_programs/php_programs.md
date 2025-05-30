
|  No.  | [Questions](../0.0_php_questions.md)                                                                                     |
| :---: | ------------------------------------------------------------------------------------------------------------------------ |
|       | [Reverse String?](#Reverse-String)                                                                                       |
|       | [Revers number?](#Revers-number)                                                                                         |
|       | [Match the Two words same or not/Check whether two Strings are anagram of each other?](#match-the-two-words-same-or-not) |
|       | [Print The Matrix](#print-the-matrix)                                                                                    |
|       | [Fibonacci Number print](#fibonacci-number-print)                                                                        |
|       | [Find The Number Even Or Odd?](#find-the-number-even-or-odd)                                                             |
|       | [Print the Odd Number](#print-the-odd-number)                                                                            |
|       | [Print even number between 1 to 100](#print-even-number-between-1-to-100)                                                |
|       | [Program to find Palindrome Number?](#program-to-find-palindrome-number)                                                 |
|       | [Program to find Palindrome string?](#program-to-find-palindrome-string)                                                 |


### Reverse String?
```php
$s = 'mohit saxena';		
$l = strlen($s);
for($i=$l-1; $i>=0; $i--){
    echo $s[$i];
}

Output:- anexas tihom
```
* 2nd Method
```php
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


### Revers number?
```php
# Type 1st:-
$num = 2039;
$revnum = 0;
while ($num != 0){
    $revnum = $revnum * 10 + $num % 10;
    $num = (int)($num / 10); 
} 
echo "Reverse number: $revnum";
```
* 2nd Method
```php
$num = 2314056;  
$revnum = 0;  
while ($num > 1){  
    $rem = $num % 10;  
    $revnum = ($revnum * 10) + $rem;  
    $num = (int)($num / 10);   
}  
echo "Reverse number of 23456 is: $revnum";  

Output:- Reverse number of 23456 is: 6504132
```

### Match the Two words same or not
```php
function matchSortedWords($word1, $word2) {
    // Convert both words to arrays of characters
    $arr1 = str_split($word1);
    $arr2 = str_split($word2);
    // Sort the arrays
    sort($arr1);
    sort($arr2);

    // Convert arrays back to strings
    $sortedWord1 = implode('', $arr1);
    $sortedWord2 = implode('', $arr2);

    // Compare the sorted versions of both words
    if ($sortedWord1 === $sortedWord2) {
        echo "$word1 and $word2 are the same after sorting.\n";
    } else {
        echo "$word1 and $word2 are not the same after sorting.\n";
    }
}

// Words to be compared
$word1 = 'mohit';
$word2 = 'hoimt';

// Call the function to compare
matchSortedWords($word1, $word2);

Output:- mohit and hoimt are the same after sorting.
```
**[⬆ Back to Top](#table-of-contents)**

### Print The Matrix?
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
    echo "\n";
}

Output:- 
1 0 0 
0 1 0 
0 0 1
```

### Fibonacci Number print?
* Type 1st:-
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
```
* 2nd Type
```php
define('NUM',5);
$a = 0;
$b = 1;
echo "$a $b "; // 0 1
for($i=1; $i<= NUM-2; $a=$b, $b=$c, $i++ ){
    echo $c = $a+$b;
    echo " ";
}

Output :- 0, 1, 1, 2
```
* 3rd Type
```php
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

### Find The Number Even Or Odd?
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

### Print the Odd Number
```php
function oddNumber($s,$e)
{
for($i=$s; $i<=$e; $i+=2){
    echo ' ';
    echo $i;
}
}
oddNumber(1,16);
Output:- 1 3 5 7 9 11 13 15
```

### Print even number between 1 to 100
```php
<?php
for ($i=2; $i<=100; $i+=2)
{
	echo $i." ";
} 
?>

Output:-
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
32 34 36 38 40 42 44 46 48 50 52 54 56 58
60 62 64 66 68 70 72 74 76 78 80 82 84 86
88 90 92 94 96 98 100
```


### Program to find Palindrome Number?
```php
function check_palindrome($n){
    $sum = 0; 
    while($n > 0) {
        $newnum = $n % 10;
        $sum = $sum * 10 + $newnum;
        $n = intval($n / 10);
    }
    return $sum;
}

$input = 12321;
$num = check_palindrome($input);
  
if($input == $num){
    echo "Palindrome number";
}else{
    echo "Not a Palindrome";
}
```

### Program to find Palindrome string?
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