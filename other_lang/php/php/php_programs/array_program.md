|  No.  | Questions                                                                                                                                        |
| :---: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|       | [Find duplicate and unique values in array?](#find-duplicate-and-unique-values-in-array)                                                         |
|       | [Minimum value in array?](#minimum-value-in-array)                                                                                               |
|       | [Highest value in array(Array max value)?](#highest-value-in-arrayarray-max-value)                                                               |
|       | [Print Even number from the given array?](#print-even-number-from-the-given-array)                                                               |
|       | [Print Even number from the given array And remove the Duplicate array?](#print-even-number-from-the-given-array-and-remove-the-duplicate-array) |
|       | [Print odd number from the given array?](#print-odd-number-from-the-given-array)                                                                 |
|       | [Print odd number from the given array And remove the Duplicate array?](#print-odd-number-from-the-given-array-and-remove-the-duplicate-array)   |

### Find duplicate and unique values in array?
```php
$givenArray = array(16,2,5,2,10,4,5,8,16);
$duplicateValues = array();
$uniqueValues = array();
 
foreach($givenArray as $val) {    
    if (!isset($uniqueValues[$val])) {
         $uniqueValues[$val] = $val;
    } else {
        $duplicateValues[] = $val;
    }
  
}
print_r($uniqueValues);
print_r($duplicateValues);

Output:- Array ( [0] => 2 [1] => 5 [2] => 16 )
```


### Minimum value in array?
```php
# using For each loop
$a = array(10, 44, 5, 6, 68, 9);
$blank = $a[0];
foreach($a as $v){
	if($blank > $v)
	$blank = $v;
}
echo $blank;
```
* 2nd Option  using For loop
```php
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

### Highest value in array(Array max value)?
```php
	 $a = array(1, 44, 5, 6, 68, 9);
	 $blank = 0;
	 foreach($a as $v)
	{
		if($blank < $v)
		$blank = $v;
	}
 echo $blank;
```
* Type 2
```php
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


### Print Even number from the given array?
```php
$array1 = [2,5,4,2,6,9,4,2,5,8];
$blank_array = array();
foreach($array1 as $key => $val) {
   if(($val % 2) == 0) {
   $blank_array[] = $val;
   }
}

print_r($blank_array);

Output:-
Array
(
    [0] => 2
    [1] => 4
    [2] => 2
    [3] => 6
    [4] => 4
    [5] => 2
    [6] => 8
)
```

### Print Even number from the given array And remove the Duplicate array
```php
$evenNo = [];
foreach($blank_array as $key => $val) {
    if($val%2 == 0) {
        $evenNo[$val] = $val;
    }
}
print_r($evenNo);

Output:-
Array
(
    [2] => 2
    [4] => 4
    [6] => 6
    [8] => 8
)
```

### Print odd number from the given array
```php
$array1 = [2,3,6,9,1,7,4,3,5];
$array2 = array();
foreach($array1 as $key => $val) {
   if(($val % 2) == 1) {
   $array2[] = $val;
   }

}
print_r($array2);

Output:-
Array
(
    [0] => 3
    [1] => 9
    [2] => 1
    [3] => 7
    [4] => 3
    [5] => 5
)
```


### Print odd number from the given array And remove the Duplicate array
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