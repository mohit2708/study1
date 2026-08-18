### **Context Manager?**
* A context manager is an object used with Python's with statement. Its job is to properly open and close resources — such as files, network connections, or locks — so that the program does not leak or misuse resources.
* (Context Manager एक ऐसा ऑब्जेक्ट होता है जो Python के with स्टेटमेंट के साथ इस्तेमाल होता है। इसका काम होता है कोई रिसोर्स (resource) — जैसे फ़ाइल, नेटवर्क कनेक्शन, या लॉक — को सही तरीके से खोलना (setup) और बंद करना (cleanup) ताकि प्रोग्राम में रिसोर्स लीक (resource leak) या गलत उपयोग न हो।)
* A context manager is typically implemented using __enter__() and __exit__() methods.

* Example:-
  * Most commonly, you see context managers used with the with statement. The best-known example is opening a file:
```python
with open('file.txt', 'r') as f:
    data = f.read()
# The file is automatically closed here, even if an error occurred inside the block.
```


#### How does with it work?
* The with statement is used to execute a block of code inside a managed context.
* Internally, A context manager implements two special methods:
  * __enter__(self): Code that runs when entering the with block. It usually sets up the resource and returns it.
  * __exit__(self, exc_type, exc_val, exc_tb): Code that runs when exiting the with block. It cleans up resources and handles exceptions if any.

#### What are the parameters of __exit__()?
```python
def __exit__(self, exc_type, exc_value, traceback):
    ...
```
* **exc_type:-** Exception ka type. -> ValueError
* exc_value:- Actual exception object.
* traceback:- Exception ka traceback information.

#### खुद का Context Manager बनाना
```python
class MyContext:
    def __enter__(self):
        print("Context में प्रवेश हुआ")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Context से बाहर निकला")
        if exc_type:
            print(f"Exception आया: {exc_val}")
        # False मतलब exception को suppress नहीं करेगा

with MyContext():
    print("Context के अंदर काम हो रहा है")

Output:-
ntext में प्रवेश हुआ
Context के अंदर काम हो रहा है
Context से बाहर निकला
```