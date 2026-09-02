### Code Sniffer
* open xampp->shell->cd php
```php
pear install --alldeps PHP_CodeSniffer
```

### Run this file
```php
phpcs --standard=PSR2 --extensions=php,module D:\xampp7.3\htdocs\laravel_test\inform\app\Http\Controllers\ConnectionController.php > D:\Reports\ConnectionController.txt
```

### Remove the with space
```php
phpcbf E:\OceansideBeachService-HOTT\branches\source_code\app\Http\Controllers\Api\QrCodeController.php
```