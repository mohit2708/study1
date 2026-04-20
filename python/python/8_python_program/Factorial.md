### **Ques. Find the Factorial of a Number?**
* factorial of 6 is 6*5*4*3*2*1 which is 720.
```python
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

Output:- 
Enter a number: 6
The factorial of 6 is 720
```