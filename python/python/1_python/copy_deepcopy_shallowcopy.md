|  No.  | [Questions](../0.0_python_questions.md)                                                                              |
| :---: | -------------------------------------------------------------------------------------------------------------------- |
|       | [Copy Object](#copy-of-object)                                                                                       |
|       | [Using Equal(=) Oprater](#copy-object-using-equal-oprater)                                                           |
|       | [Using Deep Copy](#copy-object-using-deep-copy)                                                                      |
|       | [Using shallow Copy](#copy-object-using-shallow-copy)                                                                |

# Copy Of Object
### **Copy Object Using Equal(=) Oprater**
* In Python, we use **= operator** to create a copy of an object. It only creates a new variable that shares the reference of the original object.
* When we make any **changes** to a copy **of** an **object**, those changes **do reflect** in the original object **because** it creates a new object that **stores** the **references** of the **original** elements.
```python
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list) # output:- Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('New List:', new_list) # Output:- New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

```python
original = [2, 5, [1, 2]]
copy_list = original

copy_list.append(100)
copy_list[2].append(200)

print(original) # output:- [2, 5, [1, 2, 200], 100]
print(copy_list) # output:- [2, 5, [1, 2, 200], 100]
```

### **Copy object Using Deep Copy**
* In deep copy, when we make any changes to the copied object, those changes **do not reflect in the original object**.
* Deep copy **creates a completely independent** copy of the object, including its nested objects, so there are no shared references between them.
* In Python, we **use copy.deepcopy()** for deep copying.

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

new_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)

Output:- 
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
```
```python
import copy

original = [2, 5, [1, 2]]
deep = copy.deepcopy(original)

deep[0] = 4
deep[2][0] = 10
deep[2].append(101)

print(original) # Output:- [2, 5, [1, 2]]
print(deep)     # Output:- [4, 5, [10, 2, 101]]
```
<div style="page-break-before: always;"></div>

### **Copy object Using Shallow copy**
* A shallow copy creates a new object which **stores** the **reference** of the **original elements**.
* When we make any changes to a copy of an object, those **changes** do reflect in the **original object** because it creates a new object that **stores** the **references** of the **original elements.**
```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

Output:- 
Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
```

#### More details of shallow copy
* A shallow copy creates a new outer object, but it copies the references of the elements inside it. Therefore, nested mutable objects are shared between the original and copied object.
* **HINDI:-** Shallow copy mein outer object naya banta hai, lekin uske andar ke objects ke references copy hote hain. Isliye nested mutable objects original aur copied object ke beech shared hote hain.
* Shallow copy mein outer list alag hoti hai, lekin nested mutable object shared hota hai. Isliye nested mutable object mein kiya gaya change original mein bhi reflect hota hai.
* Kyuki shallow copy mein outer object khud ka naya object ban jata hai.

```python
import copy

original = [2, 5, [1, 2]]
shallow = copy.copy(original)

shallow[0] = 100
shallow.append(102)
shallow[2].append(101)
shallow[2][0] = 3

print(original) # Output [2, 5, [3, 2, 101]]
print(shallow) # Output [100, 5, [3, 2, 101], 102]
```