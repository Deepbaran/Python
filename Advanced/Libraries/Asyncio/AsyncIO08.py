# Async IO’s Roots in Generators
# The Event Loop and asyncio.run()

import asyncio

"""
You can think of an event loop as something like a while True loop that monitors coroutines, taking feedback on what’s idle, and looking around for things that can be executed in the meantime. It is able to wake up an idle coroutine when whatever that coroutine is waiting on becomes available.
"""
# Thus far, the entire management of the event loop has been implicitly handled by one function call:
# asyncio.run(main())  # Python 3.7+

"""
asyncio.run(), introduced in Python 3.7, is responsible for getting the event loop, running tasks until they are marked as complete, and then closing the event loop.
"""
# There’s a more long-winded way of managing the asyncio event loop, with get_event_loop(). The typical pattern looks like this:
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()

"""
You’ll probably see loop.get_event_loop() floating around in older examples, but unless you have a specific need to fine-tune control over the event loop management, asyncio.run() should be sufficient for most programs.

If you do need to interact with the event loop within a Python program, loop is a good-old-fashioned Python object that supports introspection with loop.is_running() and loop.is_closed(). You can manipulate it if you need to get more fine-tuned control, such as in scheduling a callback by passing the loop as an argument.

What is more crucial is understanding a bit beneath the surface about the mechanics of the event loop. Here are a few points worth stressing about the event loop.
"""

"""
#1: Coroutines don’t do much on their own until they are tied to the event loop.

If you have a main coroutine that awaits others, simply calling it in isolation has little effect:

>>> import asyncio
>>> async def main():
...     print("Hello ...")
...     await asyncio.sleep(1)
...     print("World!")

>>> routine = main()
>>> routine
<coroutine object main at 0x1027a6150>

Remember to use asyncio.run() to actually force execution by scheduling the main() coroutine (future object) for execution on the event loop:

>>> asyncio.run(routine)
Hello ...
World!

(Other coroutines can be executed with await. It is typical to wrap just main() in asyncio.run(), and chained coroutines with await will be called from there.)
"""

"""
#2: By default, an async IO event loop runs in a single thread and on a single CPU core. Usually, running one single-threaded event loop in one CPU core is more than sufficient. It is also possible to run event loops across multiple cores.
"""

"""
#3. Event loops are pluggable. That is, you could, if you really wanted, write your own event loop implementation and have it run tasks just the same. This is wonderfully demonstrated in the uvloop package, which is an implementation of the event loop in Cython.

That is what is meant by the term “pluggable event loop”: you can use any working implementation of an event loop, unrelated to the structure of the coroutines themselves. The asyncio package itself ships with two different event loop implementations, with the default being based on the selectors module. (The second implementation is built for Windows only.)
"""