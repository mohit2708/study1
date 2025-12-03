### What is GIL?
- GIL standas for **Global Interpreter Lock**
- The GIL is a lock that allows only one thread to execute at a time in Python, making CPU-bound multithreading slow but I/O-bound tasks fast.

#### Why GIL Exists
- GIL is mainly used because of:
1. Memory Management (Reference Counting)
2. Performance Simplicity
3. Thread Safety for Built-in Objects


#### How to Bypass GIL
1. Use Multiprocessing
2. Use C Extensions / NumPy


#### Common Interview Questions with Answers
##### Ques. Why Python is slow in multithreading?
- Because of GIL, only one thread executes at a time.

##### Q2. Does Python support multithreading?
- Yes, but true parallelism is not achieved for CPU-bound tasks.

##### Q3. When should we use multithreading in Python?
- For I/O-bound tasks (API calls, file handling, web scraping).

##### Q4. When should we use multiprocessing?
- For CPU-bound tasks (ML, image processing, heavy calculations).