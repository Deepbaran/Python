# Async IO’s Roots in Generators

import asyncio
from itertools import cycle

@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine"""
    # No need to build these yourself, but be aware of what they are
    s = yield from stuff()
    return s

async def py35_coro():
    """Native coroutine, modern syntax"""
    s = await stuff()
    return s

async def stuff():
    return 0x10, 0x20, 0x30

# Calling a coroutine in isolation returns a awaitable coroutine object
# > py35_coro()
# <coroutine object py35_coro at 0x10126dcc8>

# Coroutines are enhanced generators under the hood.
# The behavior is similar in this regard:
def gen():
    yield 0x10, 0x20, 0x30
g = gen()
print(g)  # Nothing much happens - need to iterate with `.__next__()`
# <generator object gen at 0x1012705e8>
next(g)
# (16, 32, 48)

"""
Generator functions are, as it so happens, the foundation of async IO (regardless of whether you declare coroutines with async def rather than the older @asyncio.coroutine wrapper). Technically, await is more closely analogous to yield from than it is to yield. (But remember that yield from x() is just syntactic sugar to replace for i in x(): yield i.)

One critical feature of generators as it pertains to async IO is that they can effectively be stopped and restarted at will. For example, you can break out of iterating over a generator object and then resume iteration on the remaining values later. When a generator function reaches yield, it yields that value, but then it sits idle until it is told to yield its subsequent value.
"""
# This can be fleshed out through an example:

def endless():
    """Yields 9, 8, 7, 6, 9, 8, 7, 6, ... forever"""
    yield from cycle((9, 8, 7, 6))
e = endless()
total = 0
for i in e:
    if total < 30:
        print(i, end=" ")
        total += i
    else:
        print()
        # Pause execution. We can resume later.
        break
# 9 8 7 6 9 8 7 6 9 8 7 6 9 8
# Resume
print(next(e), next(e), next(e))
# (6, 9, 8)

"""
The await keyword behaves similarly, marking a break point at which the coroutine suspends itself and lets other coroutines work. “Suspended,” in this case, means a coroutine that has temporarily ceded control but not totally exited or finished. Keep in mind that yield, and by extension yield from and await, mark a break point in a generator’s execution.

This is the fundamental difference between functions and generators. A function is all-or-nothing. Once it starts, it won’t stop until it hits a return, then pushes that value to the caller (the function that calls it). A generator, on the other hand, pauses each time it hits a yield and goes no further. Not only can it push this value to calling stack, but it can keep a hold of its local variables when you resume it by calling next() on it.

There’s a second and lesser-known feature of generators that also matters. You can send a value into a generator as well through its .send() method. This allows generators (and coroutines) to call (await) each other without blocking.

Let’s try to condense all of the above articles into a few sentences: there is a particularly unconventional mechanism by which these coroutines actually get run. Their result is an attribute of the exception object that gets thrown when their .send() method is called.
"""

"""
key points on the topic of coroutines as generators:
    1. Coroutines are repurposed generators that take advantage of the peculiarities of generator methods.

    2. Old generator-based coroutines use yield from to wait for a coroutine result. Modern Python syntax in native coroutines simply replaces yield from with await as the means of waiting on a coroutine result. The await is analogous to yield from, and it often helps to think of it as such.

    3. The use of await is a signal that marks a break point. It lets a coroutine temporarily suspend execution and permits the program to come back to it later.
"""