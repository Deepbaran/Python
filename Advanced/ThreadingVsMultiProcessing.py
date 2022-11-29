# We have two common approaches to run code in parallel (achieve multitasking and speed up your program) : via threads or via multiple processes

"""
Process - A Process is an instance of a program, e.g. a Python interpreter. 
They are independent from each other and do not share the same memory.

Key facts - A new process is started independently from the first process.
Takes advantage of multiple CPUs and cores - Separate memory space - Memory is not shared between processes - 
One GIL (Global Interpreter Lock) for each process, i.e. avoids GIL limitation - Great for CPU bound processing - Child processes
are interruptable/killable.

- Starting a process is slower than starting a thread
- Larger memory footprint
- IPC (Inter-Process Communication) is more complicated
"""

"""
Threads - A thread is an entity within a process that can be scheduled for execution (Also known as "lightweight process").
A process can spawn multiple threads. The main difference is that all threads within a process share the same memory.

Key facts - Multiple threads can be spawned within one process - Memory is shared between all threads - Starting a thread is faster than
process - Great for I/O-bound tasks - Lightweight - low memory footprint.

- One GIL for all threads, i.e. threads are limited by GIL
- Multithreading has no effect for CPU-bound tasks due to the GIL
- Not interrupetible/killable -> be careful with memory leaks
- increased potential for race conditions
"""

# Threading in Python
from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads and assign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

"""
When is Threading useful:
Despite the GIL it is useful for I/O-bound tasks when your program has to talk to slow devices, like a hard drive or a network connection.
With threading the program can use the time waiting for these devices and intelligently do other tasks in the meantime.

Example: Download website information for multiple sites. Use a thread for each site.
"""


# Multiprocessing
from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        result = i * i

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and assign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        thread.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        thread.join()

"""
When is Multiprocessing useful:
It is useful for CPU-bund tasks that have to do a lot of CPU operations for a large amount of data and require a lot of computation time.
With multiprocessing you can split the data into equal parts and do parallel computing on different CPUs.

Example: Claculate the square numbers for all numbers from 1 to 1000000. Divide the numbers into equal sized parts and use a process for each subset.
"""


# GIL - Global Interpreted Lock
"""
This is a mutex (or a lock) that allows only one thread to hold control of the Python interpreter. This means that the GIL allows only one thread
to execute at a time even in a multi-threaded architecture.

Why is it needed?
It is needed because CPython's (reference implementation of Python) memory management is not thread-safe. Python uses reference counteing
for memory management. It means that objects created in Python have reference count variable that keeps track of the number of references
that point to the object. When this count reached zero, the memory occupied by the object is released. The problem was that this reference
count variable needed protection from race conditions where two threads increase or decrease its value simultaneously. If this happens, it
can cause either leaked memory that is never released or incorrectly release the memory while a reference to that object still exists.

How to avoid the GIL?
The GIL is very controversial in the Python community. The main way to avoid the GIL is by using multiprocessing instead of threading.
Another (however uncomfortable) solution would be to avoid the CPython implementation and use a free-threaded Python implementation like
Jython or IronPython. A third option is to move parts of the application out into binary extension modules, i.e. use Python as a wrapper
for third party libraries (e.g. in C/C++). This is the path taken by numpy and scipy.
"""