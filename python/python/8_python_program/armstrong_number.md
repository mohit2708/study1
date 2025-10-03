### **Ques. Check number is an Armstrong number or not?**
* 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3) = 153
* 1634 = (1 * 1 * 1 * 1) + (6 * 6 * 6 * 6) + (3 * 3 * 3 * 3) + (4 * 4 * 4 * 4) = 1634
```python
num = int(input("Enter a number: "))
len = len(str(num))
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum = sum + digit ** len
   temp = temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

Output:- 
Enter a number: 1634
1634 is an Armstrong number
```