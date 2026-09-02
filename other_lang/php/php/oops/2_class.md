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