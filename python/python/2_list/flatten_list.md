### **flatten list**
* Flattening a list in Python refers to the process of **converting a nested list** (a list containing other lists as elements) **into a single, one-dimensional list**. This operation removes the nested structure and combines all elements into a single sequence.
* Several methods can achieve this, including list comprehensions, loops, and recursion.
```python
# ex1
def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList
 
 
lis = [1, [11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
print('List', lis)
print('Flat List', flat(lis))
Output:- 
List [1, [11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
Flat List [1, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
----------------------------------------------------------------------
listnum = [[5,6,7,'C#'], ['C++',2,3]]
flatten_list = [ele for sublist in listnum for ele in sublist]
print('flatten list =',flatten_list)


#ex2:-
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [1, [2, 3], [4, [5, 6]]]
flattened_list = flatten_list(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
```