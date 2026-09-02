### Stripe PHP package install
```php
composer require stripe/stripe-php
```
- .env में keys add करें
```php
STRIPE_KEY=pk_test_xxxxxxxxx
STRIPE_SECRET=sk_test_xxxxxxxxx
```
- config/services.php में add करें
```php
'stripe' => [
    'key' => env('STRIPE_KEY'),
    'secret' => env('STRIPE_SECRET'),
],
```
- Config cache clear करें
```php
php artisan config:clear
```
- Controller में use करें
```php
use Stripe\StripeClient;

$stripe = new StripeClient(config('services.stripe.secret'));
```
- अब आप product, price, subscription, payment intent सब बना सकते हो ✅