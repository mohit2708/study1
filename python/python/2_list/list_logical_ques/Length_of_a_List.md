### **Find the Length of a List?**
* Using **len() Function** or **length_hint** function
```python
# Using lentgh function
li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)
Output:- The length of list is:  3

# Using length_hint Function
from operator import length_hint
test_list = [1, 4, 5, 7, 8]
list_len_hint = length_hint(test_list)
print("Length of list using length_hint() is : " + str(list_len_hint))
Output:- Length of list using length_hint() is : 5

# using for loop
test_list = [1, 4, 5, 7, 8]
counter = 0
for i in test_list:
	counter = counter + 1
print("Length of list using naive method is : " + str(counter))
Output:- Length of list using naive method is : 5
```