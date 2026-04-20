### Ques. What is Interface?
* An interface is a description of action that object can do.
* jo interface mai function honge wo class mai hona jaruri hai.
* Purpose of interface is to allow the computer to enforce these properties and to know that an object of type t.
```php
<?php
interface abc
{
	public function a();
	public function b();
}
class xyz implements abc
{  	public function a()
	{
    	echo "mohit";
	}
  	public function b()
	{
    	echo "saxena";
	}
}
$obj = new xyz();
$obj->a();
?>
```