### Ques. What is Oops(Object-oriented programming System)?
Oops provide a way of programming language that organizes with objects rather than data.

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Advantage of Oops(Object-oriented programming System)?

* __Code Reusability:__ it can be achieved through inheritance and traits. 
* __Modularity:__ it can be achieved through breaking large code into small modules, Modularity reduces complexity.
* __Flexibility:__ it can be achieved through polymorphism
* __Maintainability:__ it is to maintain code which follow Object Oriented Programming Concepts.
* __Security:__ it can be achieved through Encapsulation
* __Testability:__ it is easy to test.

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Class?

* A class/method is a blueprint or a prototype that defines the variables and methods.
* A class is a collection of objects of similar type.  
* Class represent all properties and behaviors of an object.

__Example:-__
```php
<?php
class abc
{   public function add()
   {
    echo "mohit";
   }
}
$obj = new abc(); //object create
$obj->add();    //call function
?>
```
```php
class Person{
   public $name;
   public $age;
   function __construct($name, $age){
       $this->name = $name;
       $this->age = $age;
   }
   function getUserDetails(){
       return "Hi, My Name is ".$this->name." and I'm ". $this->age ." old <br>";
   }
}
//To create php object we have to use a new operator. 
$obj = new Person("Ajay", 23);
echo $obj->getUserDetails();
//Output:
Hi, My Name is Ajay and I'm 23 old
```
**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Object?
Any entity that has state and behaviours is known as object. Ex- Chair, Pen, table etc
```php
//Create an object of MyClass 
$obj = new MyClass();
OR
$obj = new MyClass;
```

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Encapsulation?
Binding(or wrapping) code and data together into a single unit is known as encapsulation.
One object is encapsulated from another object.
```php
class Person {
	private $name;
	public function setName($name) {
		$this->name = $name;
	}
	public function getName($name) {
		return $this->name;
	}
}
$personObj = new Person();
$personObj->setName('Full Stack Tutorials');
$personObj->getName();
```

**[⬆ Back to Top](#table-of-contents)**
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

**[⬆ Back to Top](#table-of-contents)**
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
**[⬆ Back to Top](#table-of-contents)**
### Ques. What is the difference between Abstract class Interface?
|                                                                                     Abstract Class                                                                                     |                                            Interface                                            |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: |
|                                                                         abstract class ko hum extend karte hai                                                                         |                              interface ko hum implement karte hai                               |
|                                                                  abstarct class ko hum acess modifier bana sakte hai                                                                   |                                       not acess modifier                                        |
|                                                             abstart class mai kam sa kam 1 abstarct method hona jaruri hai                                                             |                         interface mai sare abstarct method hona chaiye                          |
|                                       In abstract class a method must be declared as abstract. Abstract methods doesn’t have any implementation.                                       |                      In interface all the methods by default are abstract.                      |
|                                                    Abstract class can also contain member variables and concrete functions/methods.                                                    | Interfaces cannot contain any member variables and concrete functions/methods except constants. |
| An Abstract methods can be declare with access modifiers like public, protected etc. Concrete Class which is extending the abstract class must be defined with the same or visibility. |                      All methods declared in an interface must be public.                       |
|                                       A class can Inherits only one Abstract class and Multiple inheritance is not possible for Abstract class.                                        |      A class can implement many interfaces and Multiple interface inheritance is possible.      |
|                                                                 Only complete member of abstract class can be static.                                                                  |                             Members of Interface can not be static.                             |
|                                                                 Abstract class does nor support multiple inheritance.                                                                  |                             Interface Supports multiple inheritance                             |
|                                                                          Abstract class contains Data Member.                                                                          |                            Interface does not Contains Data member.                             |
|                                                                         Abstract class contains Constructors.                                                                          |                            Interface does not contains Constructors                             |
|                                                      An Abstract class  can contain both incomplete(abstract) and complete member                                                      |               An interface contains only incomplete member (signature of member)                |

**[⬆ Back to Top](#table-of-contents)**
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