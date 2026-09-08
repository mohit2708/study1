|  No.  | [Swap Number](../0.0_php_questions.md)                                       |
| :---: | ---------------------------------------------------------------------------- |
|   1   | [Swap Number with temporary variable?](#swap-number-with-temporary-varibale) |
|   2   | [Swap Number Without Third Variable?](#Swap-Number-Without-Third-Variable)   |

### Swap Number with temporary varibale?
```php
function abc($a,$b){
    echo "Value of a: $a</br>";
    echo "Value of b: $b</br>";
    $temp   =   $a;
    $a      =   $b;
    $b      =   $temp;
    echo "Value of a: $a</br>";
    echo "Value of b: $b</br>";
}
$n1 = 4;
$n2 = 2;
abc ($n1,$n2);
```

### Swap Number Without Third Variable?
```php
$a = 5;
$b = 9;

$a =  $a + $b;  // 5 + 6 = 11
$b = $a - $b;   // 11 - 6 = 5
$a = $a - $b;  // 11 - 5 = 6

echo $a . ',' . $b;
```

