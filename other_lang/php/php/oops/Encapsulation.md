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