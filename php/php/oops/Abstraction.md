### Ques. What is Abstraction?
* Hiding internal details and showing functionality is known as abstraction. 
* Abstract class is a class which contains at least one or more abstract methods.
* Abstract method is a method which is declared, but not defined.
* Abstract class ka hum obj nahi bana sakte hai... agar banate hai to fatal error dega: cannot instance abstract class.
* Agar hame abstract class ke function ko call karni hai to inherit karke call karenge.
* abstract class mai kam sa kam 1 abstract method hona chaiye.
```php
<?php
abstract class testParent
{
        	public function abc()
        	{
        	echo "mohit";
        	}
}
class testChild extends testParent
{
        	public function xyz()
        	{
        	echo "saxena";
        	}
}
$a = new testChild();
$a -> abc();
?>
```
#### What is the need of abstract class?
Suppose we were modeling the behavior of animals, by creating a class hierarchy that started with a base class called Animal.
Animals are capable of doing different things like flying, digging and walking, but there are some common operations as well like eating and sleeping.
Some common operations are performed by all animals, but in a different way as well.
When an operation is performed in a different way, it is a good candidate for an abstract method (forcing subclasses to provide a custom implementation).
