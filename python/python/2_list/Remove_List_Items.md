### **Ques. Remove List Items?**
```python
# * Remove **Specified Item** from the List using remove() method.
# remove() method the first instance of a matching object.
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)     # Output:- ['apple', 'cherry', "banana"]


# If item not exist in remove method then show the error
thislist.remove("banana1")
print(thislist) # Output:- error item not in the list


# using **pop() method:-** The pop() method **removes the specified index**.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)     # Output:- ['apple', 'cherry']


# pop() method without index:- if we do not specify the index, the pop() method **removes the last item**.
thislist.pop()
print(thislist)     # Output:- ['apple', 'banana']


# **del() method:-** The del keyword also **removes the specified index.**
del thislist[0]
print(thislist)     # Output:- ['banana', 'cherry']


# The **del** keyword can also **delete the list completely.**
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".


#  **clear() method:-** The clear() method **empties the list.**
thislist.clear()
print(thislist)     # Output:- []
```