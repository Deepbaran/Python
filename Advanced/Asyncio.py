# https://youtu.be/t5Bo1Je9EmE
import asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    # Creating tasks
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # task1 will return a future initially which will be populated after task1 is fully executed
    value = await task1
    print(value)
    await task2

# Creating an event loop onject to run the main coroutine
asyncio.run(main()) 

"""
start fetching
0
1
2
3
done fetching
4
{'data': 1}
5
6
7
8
9
"""

"""
async - async keyword is used to create coroutines. adding it before any function definition turns that function into a coroutine.
await - stops the execution of the coroutine till the completion of a task.
event loop - We need an event loop object to run coroutines asynchronously.
task - to execute time comsuming operations asynchronously, we need to create tasks.
future - a task returns future which is a placeholder for the value that will be returned once the task is completed.
"""