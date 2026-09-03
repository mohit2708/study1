### Difference between abstract class and interface in python?
- Python **does not have** a separate interface keyword like Java.
- Interfaces are implemented using Abstract Base Classes (ABC) from the abc module.
- जब कई classes में कुछ common functionality share करनी हो, तब Abstract Class का उपयोग करते हैं।


```python
Feature	Abstract Class	Interface (Using ABC)
Purpose	Provides partial implementation + rules	Defines only contract/rules
Methods	Can have abstract and concrete methods	Usually contains only abstract methods
Variables	Can have instance/class variables	Usually only constants
Constructor (__init__)	Allowed	Generally avoided
Implementation	Child class can use inherited code	Child class must implement all methods
Use Case	When classes share common functionality	When classes need same behavior contract
Abstract Class Example
from abc import ABC, abstractmethod

class Animal(ABC):

    def eat(self):
        print("Animal is eating")

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.eat()
d.sound()

Output:

Animal is eating
Bark

👉 Here eat() is already implemented, while sound() must be implemented by child classes.

Interface Example (Python Style)

Python doesn't have a separate interface keyword like Java. We create an interface using an abstract class containing only abstract methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

👉 Car must implement both start() and stop().

Interview Answer (Short)

Abstract Class is used when we want to provide some common implementation along with abstract methods.

Interface is used when we only want to define a contract that child classes must follow.

In Python, interfaces are usually implemented using Abstract Base Classes (ABC) with only abstract methods. ✅

explain in hindi
Abstract Class vs Interface (Hindi)
🔹 Abstract Class क्या होती है?

Abstract Class एक base class होती है जिसमें:

Abstract methods (जिनकी body नहीं होती) हो सकती हैं।
Normal methods (जिनकी body होती है) भी हो सकती हैं।
Variables और Constructor (__init__) भी हो सकते हैं।

जब कई classes में कुछ common functionality share करनी हो, तब Abstract Class का उपयोग करते हैं।

Example:

from abc import ABC, abstractmethod

class Animal(ABC):

    def eat(self):
        print("Animal is eating")

    @abstractmethod
    def sound(self):
        pass

यहाँ eat() की implementation पहले से दी गई है, जबकि sound() को child class में implement करना पड़ेगा।

🔹 Interface क्या होती है?

Interface केवल एक contract (नियम) होती है।

यह बताती है कि child class में कौन-कौन से methods होने चाहिए, लेकिन उनकी implementation नहीं देती।

Python में अलग से interface keyword नहीं है, इसलिए Interface को ABC (Abstract Base Class) से बनाया जाता है।

Example:

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

जो भी class Vehicle को inherit करेगी, उसे start() और stop() implement करना ही होगा।

🎯 Interview Answer
Abstract Class	Interface
Common implementation दे सकती है	केवल contract define करती है
Abstract + Normal methods दोनों हो सकते हैं	सामान्यतः केवल abstract methods होते हैं
Variables और constructor हो सकते हैं	सामान्यतः नहीं होते
Code reuse के लिए उपयोग होती है	Rules enforce करने के लिए उपयोग होती है
आसान उदाहरण

🚗 Abstract Class = "Vehicle" जिसमें पहले से fuel() method बना हुआ है और start() implement करना बाकी है।

📜 Interface = एक नियम-पुस्तक जो कहती है कि हर Vehicle में start() और stop() होना चाहिए, लेकिन कैसे होगा यह नहीं बताती।

याद रखने की Trick:

Abstract Class = What + How (कुछ implementation भी)
Interface = What Only (सिर्फ नियम) ✅
```