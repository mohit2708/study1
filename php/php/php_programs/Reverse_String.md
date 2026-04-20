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