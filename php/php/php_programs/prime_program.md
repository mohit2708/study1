|  No.  | Prime Programs                                                   |
| :---: | ---------------------------------------------------------------- |
|   1   | [Check the Prime Number or not?](#Check-the-Prime-Number-or-not) |
|   2   | [Print the prime number?](#Print-the-prime-number)               |

### Check the Prime Number or not?
```php
function isPrime($num) {
    // Prime numbers must be greater than 1
    if ($num <= 1) {
        return false;
    }
    // Check divisibility from 2 to sqrt($num)
    for ($i = 2; $i <= sqrt($num); $i++) {
        if ($num % $i == 0) {
            return false;  // If divisible, it's not a prime
        }
    }
    return true;  // If no divisors found, it's a prime
}

// Input number
$num = 28;

if (isPrime($num)) {
    echo "$num is a prime number\n";
} else {
    echo "$num is not a prime number\n";
}
Output :-  28 is not a prime number
```


### Print the prime number?
```php
// Function to check if a number is prime
function isPrime($num) {
    if ($num <= 1) {
        return false;
    }

    for ($i = 2; $i <= sqrt($num); $i++) {
        if ($num % $i == 0) {
            return false;
        }
    }

    return true;
}

// Function to print prime numbers in a given range
function printPrimes($start, $end) {
    echo "Prime numbers between $start and $end are: \n";

    for ($i = $start; $i <= $end; $i++) {
        if (isPrime($i)) {
            echo $i . " ";
        }
    }
    echo "\n";
}

// Define the range
$start = 1;
$end = 50;

// Call the function to print primes
printPrimes($start, $end);
```
