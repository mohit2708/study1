
### Ques. What is Polymorphism?

* When one task is performed by different ways i.e known as polymorphism.
* Polymorphism is ability to use function & method in different ways.

#### Types of Polymorphism?
Polymorphism could be static and dynamic both. Overloading is static polymorphism while, overriding is dynamic polymorphism.

1. Compile time polymorphism (Static) - Method Overloading

2. Runtime time polymorphism (Dynamic) - Method Overriding

__Overloading__ is defining functions/methods that have same signatures with different parameters in the same class.

__Overriding__ is redefining parent class functions/methods in child class with same signature. So, basically the purpose of overriding is to change the behavior of your parent class method.

 The overloading methods are invoked when interacting with properties or methods that have not been declared or are not visible in the current scope. The rest of this section will use the terms "inaccessible properties" and "inaccessible methods" to refer to this combination of declaration and visibility.


### Ques. What is Inheritance?

* Acquiring the property from parent class to child class is called the inheritance.
* An inherited class is defined by using the extends keyword.

__Single Inheritance:-__
```php
class abc
{
	public function a()		//agar function private ho to or call karna ho to 
	{
		echo "mohit";
	}

	public function b()
	{
		//self::a();		// to self laga kar call  karenge
		echo "saxena";
	}
}
class xyz extends abc
{
	public function c()
	{
		echo "mohit saxena";
	}
}
$obj = New xyz();
$obj -> b(); //saxena
$obj -> a(); //mohit
$obj -> c(); //mohit saxena
```
```php
class BaseClass{
	function add(){
		$x=1000;
		$y=500;
		$add=$x+$y;
		echo "Addition=".$add."<br/>";
}}

class chld extends BaseClass{
	function sub(){
		$x=1000;
		$y=500;
		$sub=$x-$y;
		echo "subtraction=".$sub."<br/>";
}}
class Nestedchld extends chld{
	function mult(){
		$x=1000;
		$y=500;
		$mult=$x*$y;
		echo "multiplication=".$mult."<br/>";
}}
class show extends Nestedchld{
	function __construct(){
	parent::add();
	parent::sub();
	parent::mult();
}}
$obj= new show();
Output:- Addition=1500 subtraction=500 multiplication=500000

$obj= new Nestedchld();
$obj->sub(); //subtraction=500
$obj->add(); //Addition=1500
```


### Ques. What is Static class?
Static class ka hame object nahi banna padta hai, scope resolution se call kar lete hai.
```php
<?php
class a
{
	static public function xyz()
        	{
                    	echo "mohit";
        	}
        	public function mno()
        	{
                    	echo "saxena";
        	}
}
class b extends a
{
        	public static function xy()
        	{
                    	echo "mohi saxena";
        	}
        	
}
b ::xyz();      	
?>
```
**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Constructor?

* Constructors are special function/method which is automatically called when an object is created.
* the construct function starts with two underscores (__)!
* PHP Constructor, If a class name and function name will be similar in that case function is known as constructor.
* agar private karte hai to hum obj nahi bana sakte, agar banate hai to fetal error aati hai
* ek class mai ek hi constract hota hai.
```php
class Tree 
{ 
    function Tree() 
    { 
        echo "Its a User-defined Constructor of the class Tree"; 
    } 
  
    function __construct() 
    { 
        echo "Its a Pre-defined Constructor of the class Tree"; 
    } 
} 
  
$obj= new Tree();	//Its a Pre-defined Constructor of the class Tree
```

#### Types of  Constructor?

__Default Constructor:__ A constructor without any parameters is called a default constructor.

__Parameterized Constructor:__ A constructor with at least one parameter is called a parametrized constructor.

__Copy Constructor:__

__Static Constructor:__

__Private Constructor:__

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Destructor?
A Destructor is special functions which are automatically called when an object is destroyed.

Tip: As constructors and destructors helps reducing the amount of code, they are very useful!




### **Ques:- What is the key difference between concrete class and abstract class?**

Concrete classes are those classes which has to declare body of abstract methods which extends or implements from abstract class or interface

OR

Abstract classes usually have partial or no implementation. On the other hand, Concrete classes always have full implementation of its behavior. Unlike Concrete classes, Abstract classes cannot be instantiated.

### Ques. Is Multiple inheritance support in php ?
PHP supports only single inheritance; it means that a class can be extended from only one single class using the keyword 'extended'.

### Ques. What is the meaning of a final class and final method ?
Final class means that this class cannot be extended and a final method cannot be overridden.