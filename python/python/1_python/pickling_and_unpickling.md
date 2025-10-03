### **Ques. What are pickling and unpickling in Python?**
* pickling and unpickling  should be done using binary files since they support byte steam.
* Python pickle module is used for serializing and de-serializing python object structures. The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called pickling or serialization or flattening or marshalling. We can converts the byte stream (generated through pickling) back into python objects by a process called as unpickling.
**Pickling:**
* pickling is a process of converting a class **object** into a **byte** stream so that it can be stored into a file. this is also **called** as **object serialization**.
* Pickling is the name of the serialization process in Python. Any object in Python can be serialized into a byte stream and dumped as a file in the memory.
* The function used for the above process is **pickle.dump()** or **pickle.dumps()**.

**unpickling:**
* unpickling is a process whereby **byte** stream is converted back into a class **object**. it is inverse operation of pickling. this is also called as de-serialization.
* The function used for the above process is **pickle.load()**.
```python
import pickle
class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address
    
    def display(self):
        print(f"name {self.name} roll is {self.roll} address {self.address}")

with open('student.dat', mode='wb') as f:
    stu1 = Student('mohit', 001, 'mainpuri')
    stu2 = Student('rohit', 001, 'agra')
    pickle.dump(stu1, f)
    pickle.dump(stu2, f)
    print('pickling Done')
    
with open('student.dat', mode='rb') as f:
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
    print('unpikling Done!!!')
    obj1.display()
    obj2.display()
```

```python
import pickle

# Sample data to be pickled
data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science', 'History']
}

# Pickling: Serialize the Python object (data) and save it to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
    print("Data has been pickled and saved to data.pkl.")

# Unpickling: Load the pickled data back into a Python object
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print("Data has been unpickled:")
    print(loaded_data)

```