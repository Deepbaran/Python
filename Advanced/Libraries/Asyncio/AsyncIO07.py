# Async IO’s Roots in Generators
# Other Features: async for and Async Generators + Comprehensions

import asyncio

"""
Along with plain async/await, Python also enables async for to iterate over an asynchronous iterator. The purpose of an asynchronous iterator is for it to be able to call asynchronous code at each stage when it is iterated over.

A natural extension of this concept is an asynchronous generator. Recall that you can use await, return, or yield in a native coroutine. Using yield within a coroutine became possible in Python 3.6 (via PEP 525), which introduced asynchronous generators with the purpose of allowing await and yield to be used in the same coroutine function body.
"""
async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)

# Last but not least, Python enables asynchronous comprehension with async for. Like its synchronous cousin, this is largely syntactic sugar:
async def main():
    # This does *not* introduce concurrent execution
    # It is meant to show syntax only
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f
g, f = asyncio.run(main())
print(g) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(f) # [1, 2, 16, 32, 256, 512]

"""
This is a crucial distinction: neither asynchronous generators nor comprehensions make the iteration concurrent. All that they do is provide the look-and-feel of their synchronous counterparts, but with the ability for the loop in question to give up control to the event loop for some other coroutine to run.

In other words, asynchronous iterators and asynchronous generators are not designed to concurrently map some function over a sequence or iterator. They’re merely designed to let the enclosing coroutine allow other tasks to take their turn. The async for and async with statements are only needed to the extent that using plain for or with would “break” the nature of await in the coroutine. This distinction between asynchronicity and concurrency is a key one to grasp.
"""