# Async IO in Context
# When and Why Is Async IO the Right Choice?

"""
putting async before every function is a bad idea if all of the functions use blocking calls. (This can actually slow down your code.) There are places where async IO and multiprocessing can live in harmony.

Threading tends to scale less elegantly than async IO, because threads are a system resource with a finite availability. Creating thousands of threads will fail on many machines, and trying it in the first place is not recommended. Creating thousands of async IO tasks is completely feasible.

Async IO shines when you have multiple IO-bound tasks where the tasks would otherwise be dominated by blocking IO-bound wait time, such as:
    1. Network IO, whether your program is the server or the client side

    2. Serverless designs, such as a peer-to-peer, multi-user network like a group chatroom

    3. Read/write operations where you want to mimic a “fire-and-forget” style but worry less about holding a lock on whatever you’re reading and writing to

The biggest reason not to use it is that await only supports a specific set of objects that define a specific set of methods. If you want to do async read operations with a certain DBMS, you’ll need to find not just a Python wrapper for that DBMS, but one that supports the async/await syntax. Coroutines that contain synchronous calls block other coroutines and tasks from running.

Libraries That Work With async/await: https://realpython.com/async-io-python/#libraries-that-work-with-asyncawait
"""