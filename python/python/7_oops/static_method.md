### **What is static method?**
* static method don't use the self parameter.
* Does not use cls (class)
* Does not depend on object or class data
* static method ko hum object ke sath bhi call kar sakte hai or class ke stah bhi.
```python
class Student:
    
    @staticmethod
    def hello():
        print("hello")
    
stu1 = Student()
stu1.hello()        # output:- Hello

# Call direct class
Student.hello()     # output:- Hello
```

- Example 2: Payment Calculation (E-commerce)
```python
class PaymentCalculator:
    @staticmethod
    def calculate_gst(amount):
        return amount * 0.18

    @staticmethod
    def total_amount(amount):
        return amount + PaymentCalculator.calculate_gst(amount)


print(PaymentCalculator.total_amount(1000)) # Output:- 
```

### Why used static class?
- Hum static method isliye banate hain jab function class se logically related ho, lekin usse object ya class ke data ki zarurat na ho.
- Logic ko ek jagah organize karne ke liye
- Jab kuch functions same kaam se related hote hain, to unhe ek class ke andar rakh dete hain.
- Object banane ki zarurat nahi hoti
- Project structure professional lagta hai