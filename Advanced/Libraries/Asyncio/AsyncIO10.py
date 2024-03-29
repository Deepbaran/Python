# Odds and Ends
# Other Top-Level asyncio Functions

"""
In addition to asyncio.run(), you’ve seen a few other package-level functions such as asyncio.create_task() and asyncio.gather().

You can use create_task() to schedule the execution of a coroutine object, followed by asyncio.run():

>>> import asyncio

>>> async def coro(seq) -> list:
...     \"""'IO' wait time is proportional to the max element.\"""
...     await asyncio.sleep(max(seq))
...     return list(reversed(seq))
...
>>> async def main():
...     # This is a bit redundant in the case of one task
...     # We could use `await coro([3, 2, 1])` on its own
...     t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
...     await t
...     print(f't: type {type(t)}')
...     print(f't done: {t.done()}')
...
>>> t = asyncio.run(main())
t: type <class '_asyncio.Task'>
t done: True

There’s a subtlety to this pattern: if you don’t await t within main(), it may finish before main() itself signals that it is complete. Because asyncio.run(main()) calls loop.run_until_complete(main()), the event loop is only concerned (without await t present) that main() is done, not that the tasks that get created within main() are done. Without await t, the loop’s other tasks will be cancelled, possibly before they are completed. If you need to get a list of currently pending tasks, you can use asyncio.Task.all_tasks().

Note: asyncio.create_task() was introduced in Python 3.7. In Python 3.6 or lower, use asyncio.ensure_future() in place of create_task().
"""

"""
Separately, there’s asyncio.gather(). While it doesn’t do anything tremendously special, gather() is meant to neatly put a collection of coroutines (futures) into a single future. As a result, it returns a single future object, and, if you await asyncio.gather() and specify multiple tasks or coroutines, you’re waiting for all of them to be completed. (This somewhat parallels queue.join() from our earlier example.) The result of gather() will be a list of the results across the inputs:

>>> import time
>>> async def main():
...     t = asyncio.create_task(coro([3, 2, 1]))
...     t2 = asyncio.create_task(coro([10, 5, 0]))  # Python 3.7+
...     print('Start:', time.strftime('%X'))
...     a = await asyncio.gather(t, t2)
...     print('End:', time.strftime('%X'))  # Should be 10 seconds
...     print(f'Both tasks done: {all((t.done(), t2.done()))}')
...     return a
...
>>> a = asyncio.run(main())
Start: 16:20:11
End: 16:20:21
Both tasks done: True
>>> a
[[1, 2, 3], [0, 5, 10]]

You probably noticed that gather() waits on the entire result set of the Futures or coroutines that you pass it. Alternatively, you can loop over asyncio.as_completed() to get tasks as they are completed, in the order of completion. The function returns an iterator that yields tasks as they finish. Below, the result of coro([3, 2, 1]) will be available before coro([10, 5, 0]) is complete, which is not the case with gather():

>>> async def main():
...     t = asyncio.create_task(coro([3, 2, 1]))
...     t2 = asyncio.create_task(coro([10, 5, 0]))
...     print('Start:', time.strftime('%X'))
...     for res in asyncio.as_completed((t, t2)):
...         compl = await res
...         print(f'res: {compl} completed at {time.strftime("%X")}')
...     print('End:', time.strftime('%X'))
...     print(f'Both tasks done: {all((t.done(), t2.done()))}')
...
>>> a = asyncio.run(main())
Start: 09:49:07
res: [1, 2, 3] completed at 09:49:10
res: [0, 5, 10] completed at 09:49:17
End: 09:49:17
Both tasks done: True
"""

"""
Lastly, you may also see asyncio.ensure_future(). You should rarely need it, because it’s a lower-level plumbing API and largely replaced by create_task(), which was introduced later.
"""

"""
The Precedence of await:

While they behave somewhat similarly, the await keyword has significantly higher precedence than yield. This means that, because it is more tightly bound, there are a number of instances where you’d need parentheses in a yield from statement that are not required in an analogous await statement. 

Examples of “await” expressions: https://peps.python.org/pep-0492/#examples-of-await-expressions
"""

# Conclusion
"""
Here’s a recap of what we’ve covered:

    1. Asynchronous IO as a language-agnostic model and a way to effect concurrency by letting coroutines indirectly communicate with each other

    2. The specifics of Python’s new async and await keywords, used to mark and define coroutines

    3. asyncio, the Python package that provides the API to run and manage coroutines
"""

# Python Version Specifics
"""
Async IO in Python has evolved swiftly, and it can be hard to keep track of what came when. Here’s a list of Python minor-version changes and introductions related to asyncio:

    - 3.3: The yield from expression allows for generator delegation.

    - 3.4: asyncio was introduced in the Python standard library with provisional API status.

    - 3.5: async and await became a part of the Python grammar, used to signify and wait on coroutines. They were not yet reserved keywords. (You could still define functions or variables named async and await.)

    - 3.6: Asynchronous generators and asynchronous comprehensions were introduced. The API of asyncio was declared stable rather than provisional.

    - 3.7: async and await became reserved keywords. (They cannot be used as identifiers.) They are intended to replace the asyncio.coroutine() decorator. asyncio.run() was introduced to the asyncio package, among a bunch of other features.

If you want to be safe (and be able to use asyncio.run()), go with Python 3.7 or above to get the full set of features.
"""