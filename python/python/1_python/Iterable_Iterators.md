### **Ques. What is an Iterable?**
* Lists, tuples, dictionaries, Strings, and sets are all **iterable objects**. They are iterable containers which you can get an iterator from.
* An Iterable is an object that implements the __iter__() method and returns an iterator object or an object that implements __getitem__() method (and should raise an IndexError when indices are exhausted). 

### What is Iterators?
* iterator is an object, its print the value one by one.
* An iterator is an object that contains a countable number of values.
* An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
* Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
```python
# Example1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

Output:-
apple
banana
cherry

# Example 2
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

Output:- 
b
a
n
a
n
a

# Looping Through an Iterator
# The for loop actually creates an iterator object and executes the next() method for each loop
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

Output:-
apple
banana
cherry
```
<div style="page-break-before: always;"></div>

### **Ques. Difference between Iterators and iterable?**
* Every iterator is also an iterable, but not every iterable is an iterator.

| Iterable                                                                  | Iterator                                                                                                                |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| An Iterable is basically an object that any user can iterate over.        | An Iterator is also an object that helps a user in iterating over another object (that is iterable).                    |
| We can generate an iterator when we pass the object to the iter() method. | We use the __next__() method for iterating. This method helps iterators return the next item available from the object. |
| Every iterator is basically iterable.                                     | Not every iterable is an iterator.                                                                                      |

### **Ques. Difference between generator and iterators in python?**
| Iterator                                                                                            | Generator                                                                                                                                       |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Class is used to implement an iterator                                                              | Function is used to implement a generator.                                                                                                      |
| Local Variables aren’t used here.                                                                   | All the local variables before the yield function are stored.                                                                                   |
| Iterators are used mostly to iterate or convert other objects to an iterator using iter() function. | Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop |
| Iterator uses iter() and next() functions                                                           | Generator uses yield keyword                                                                                                                    |
| Every iterator is not a generator                                                                   | Every generator is an iterator                                                                                                                  |
