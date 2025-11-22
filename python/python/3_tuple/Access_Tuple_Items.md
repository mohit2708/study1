### **Ques. Access Tuple Items?**
```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Access Tuple Items 
print(thistuple[1])   #Output:- banana
print(thistuple[2:])  #Output:- ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[:4])  #Output:- ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:5]) #Output:- ('cherry', 'orange', 'kiwi')
# Negative Indexing
print(thistuple[-1])    #Output:- mango
print(thistuple[-4:-1]) #Output:- ('orange', 'kiwi', 'melon')
print(thistuple[:-4])   #output:- ('apple', 'banana', 'cherry'))
```

* Get the Items at Specified Intervals

```python
print(thistuple[::2])    # Output:- ('apple', 'cherry', 'kiwi', 'mango')
print(thistuple[::-2])   # Output:- ('mango', 'kiwi', 'cherry', 'apple')
print(thistuple[::-1])   # Output:- ('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple')  #reverse the tuple using slice
```

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", ["mango","xyz"]]
print(thislist[6][0][1]) # output:- a
```