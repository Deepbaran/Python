# The async/await Syntax and Native Coroutines
"""
At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function.

A coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.
"""

# Asynchronous
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
"""
One
One
One
Two
Two
AsyncIO02.py executed in 0.00 seconds.
"""

"""
Talking to each of the calls to count() is a single event loop, or coordinator. When each task reaches await asyncio.sleep(1), the function yells up to the event loop and gives control back to it, saying, “I’m going to be sleeping for 1 second. Go ahead and let something else meaningful be done in the meantime.”
"""

# Synchronous
# import time

# def count():
#     print("One")
#     time.sleep(1)
#     print("Two")

# def main():
#     for _ in range(3):
#         count()

# if __name__ == "__main__":
#     s = time.perf_counter()
#     main()
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")
"""
One
Two
One
Two
One
Two
AsyncIO02.py executed in 3.03 seconds.
"""

"""
While using time.sleep() and asyncio.sleep() may seem banal, they are used as stand-ins for any time-intensive processes that involve wait time. (The most mundane thing you can wait on is a sleep() call that does basically nothing.) That is, time.sleep() can represent any time-consuming blocking function call, while asyncio.sleep() is used to stand in for a non-blocking call (but one that also takes some time to complete).

The benefit of awaiting something, including asyncio.sleep(), is that the surrounding function can temporarily cede control to another function that’s more readily able to do something immediately. In contrast, time.sleep() or any other blocking call is incompatible with asynchronous Python code, because it will stop everything in its tracks for the duration of the sleep time.
"""