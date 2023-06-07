# The Rules of Async IO
import asyncio
import random

"""
- The syntax async def introduces either a native coroutine or an asynchronous generator. The expressions async with and async for are also valid, and you’ll see them later on.

- The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”
"""
# In code, that second bullet point looks roughly like this:
# async def g():
#     # Pause here and come back to g() when f() is ready
#     r = await f()
#     return r

"""
There’s also a strict set of rules around when and how you can and cannot use async/await. These can be handy whether you are still picking up the syntax or already have exposure to using async/await:
    - A function that you introduce with async def is a coroutine. It may use await, return, or yield, but all of these are optional. Declaring async def noop(): pass is valid:
        - Using await and/or return creates a coroutine function. To call a coroutine function, you must await it to get its results.
        - It is less common (and only recently legal in Python) to use yield in an async def block. This creates an asynchronous generator, which you iterate over with async for.
        - Anything defined with async def may not use yield from, which will raise a SyntaxError.
    - Just like it’s a SyntaxError to use yield outside of a def function, it is a SyntaxError to use await outside of an async def coroutine. You can only use await in the body of coroutines.
"""
# Here are some terse examples meant to summarize the above few rules:
# async def f(x):
#     y = await z(x)  # OK - `await` and `return` allowed in coroutines
#     return y

# async def g(x):
#     yield x  # OK - this is an async generator

# async def m(x):
#     yield from gen(x)  # No - SyntaxError

# def m(x):
#     y = await z(x)  # Still no - SyntaxError (no `async def` here)
#     return y

"""
Finally, when you use await f(), it’s required that f() be an object that is awaitable. Well, that’s not very helpful, is it? For now, just know that an awaitable object is either (1) another coroutine or (2) an object defining an .__await__() dunder method that returns an iterator. If you’re writing a program, for the large majority of purposes, you should only need to worry about case #1.

That brings us to one more technical distinction that you may see pop up: an older way of marking a function as a coroutine is to decorate a normal def function with @asyncio.coroutine. The result is a generator-based coroutine. This construction has been outdated since the async/await syntax was put in place in Python 3.5.
"""
# These two coroutines are essentially equivalent (both are awaitable), but the first is generator-based, while the second is a native coroutine:
# @asyncio.coroutine
# def py34_coro():
#     """Generator-based coroutine, older syntax"""
#     yield from stuff()

# async def py35_coro():
#     """Native coroutine, modern syntax"""
#     await stuff()

"""
If you’re writing any code yourself, prefer native coroutines for the sake of being explicit rather than implicit. Generator-based coroutines will be removed in Python 3.10.

The reason that async/await were introduced is to make coroutines a standalone feature of Python that can be easily differentiated from a normal generator function, thus reducing ambiguity.

Don’t get bogged down in generator-based coroutines, which have been deliberately outdated by async/await. They have their own small set of rules (for instance, await cannot be used in a generator-based coroutine) that are largely irrelevant if you stick to the async/await syntax.

Here’s one example of how async IO cuts down on wait time: given a coroutine makerandom() that keeps producing random integers in the range [0, 10], until one of them exceeds a threshold, you want to let multiple calls of this coroutine not need to wait for each other to complete in succession. You can largely follow the patterns from the two scripts above, with slight changes:
"""
# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

"""
This program uses one main coroutine, makerandom(), and runs it concurrently across 3 different inputs. Most programs will contain small, modular coroutines and one wrapper function that serves to chain each of the smaller coroutines together. main() is then used to gather tasks (futures) by mapping the central coroutine across some iterable or pool.

In this miniature example, the pool is range(3).
"""