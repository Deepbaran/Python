# https://realpython.com/async-io-python/#odds-and-ends
"""
Asynchronous IO (async IO): a language-agnostic paradigm (model) that has implementations across a host of programming languages

async/await: two new Python keywords that are used to define coroutines.

asyncio: the Python package that provides a foundation and API for running and managing coroutines

Coroutines (specialized generator functions) are the heart of async IO in Python, and we’ll dive into them later on.
"""

"""
Where Does Async IO Fit In?

Concurrency and parallelism are expansive subjects that are not easy to wade into. While this article focuses on async IO and its implementation in Python, it’s worth taking a minute to compare async IO to its counterparts in order to have context about how async IO fits into the larger, sometimes dizzying puzzle.

Parallelism consists of performing multiple operations at the same time.

Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL.

What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.

To recap the above, concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.

Now it’s time to bring a new member to the mix. Over the last few years, a separate design has been more comprehensively built into CPython: asynchronous IO, enabled through the standard library’s asyncio package and the new async and await language keywords. To be clear, async IO is not a newly invented concept, and it has existed or is being built into other languages and runtime environments, such as Go, C#, or Scala.

The asyncio package is billed by the Python documentation as a library to write concurrent code. However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.

In fact, async IO is a single-threaded, single-process design: it uses cooperative multitasking, a term that you’ll flesh out by the end of this tutorial. It has been said in other words that async IO gives a feeling of concurrency despite using a single thread in a single process. Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent.

To reiterate, async IO is a style of concurrent programming, but it is not parallelism. It’s more closely aligned with threading than with multiprocessing but is very much distinct from both of these and is a standalone member in concurrency’s bag of tricks.

That leaves one more term. What does it mean for something to be asynchronous? This isn’t a rigorous definition, but for our purposes here, I can think of two properties:
    - Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
    - Asynchronous code, through the mechanism above, facilitates concurrent execution. To put it differently, asynchronous code gives the look and feel of concurrency.

Async IO takes long waiting periods in which functions would otherwise be blocking and allows other functions to run during that downtime. (A function that blocks effectively forbids others from running from the time that it starts until the time that it returns.)

Python’s async model is built around concepts such as callbacks, events, transports, protocols, and futures.
"""