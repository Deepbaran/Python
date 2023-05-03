"""
Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over.
Unlike lsts, they are lazy and thus produce items one at a time and only when asked.
So, they are much more memory efficient when dealing with large datasets
A generator is defined like a normal function but with the yield statement instead of return.

def my_generator():
    yield 1
    yield 2
    yield 3
"""

# Execution of a generator function
"""
Calling the function does not execute it. Instead, the functin returns a generator object which is used to control execution.
Generator objects execute when next() is called. Wehn calling next() the first time, execution begins at the start of the function and continues until the first yield statement where the value to the right of the statement is returned.
Subsequent calls to next() continue from yield statement (and loop around) until another yield is reached.
If yield is not called because of a condition in the end is reached, a StopIteration exception is raised.
"""

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not pring 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd)) # as generators are also itertors, so we have the next() function

# this will print the next values
print(next(cd))
print(next(cd))

# this will raise a StopIteration just like for a iterator
# print(next(cd))

# Starting
# 3
# 2
# 1
# Traceback (most recent call last):
#   File "D:\Upskilling\01 - Existing Skills\08 - Python\Advanced\Generators.py", line 38, in <module>
#     print(next(cd))
# StopIteration

# Iterating over a generator using for loop
cd = countdown(3)
for x in cd:
    print(x)
# 3
# 2
# 1

# We can use it for functions that take iterables as input
cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)
# Starting
# 6

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)
# Starting
# [1, 2, 3]

# Big advantage: Generators save memory
"""
Since the values are generated lazily, i.e. only when needed, it saves a lot of memory, especially when working with large data.
Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
"""

def firstn(n):
    num, nums = 0, [] # this is a tuple
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")
# 499999500000
# 8448728 bytes

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")
# 499999500000
# 104 bytes

# Another example: Fibonacci numbers
def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib)) # [0, 1, 1, 2, 3, 5, 8, 13, 21]


# Generator Expression
"""
Just like list comprehensions, generators can be written in the same syntax except with parenthesis instead of square brackets.
Generator expressions are often slower than list comprehensions because of the overhead of function calls.
"""
# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator), "bytes") # 104 bytes

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist), "bytes") # 4216 bytes


# Concept behind a generator
"""
This class implements our generator as an iterable object. It has to implement __iter__ and __next__ to make it iterable, keep track of the current state (the current number in this case), and take care of a StopIteration. It can be used to understand the concept behind generators. However, there is a lot of boilerplate code, and the logic is not as clear as with a simple function using the yield keyword.
"""
class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()

firstn_object = firstn(1000000)
print(sum(firstn_object)) # 499999500000


"""
 Recursively converting nested generators to list or lists.
"""

def nestedGenerator():
    def gen1():
        nums = [[1,2,3],[3,4]]
        for num in nums:
            yield num
    def gen2():
        nums = [gen1(),gen1()]
        for num in nums:
            yield num
    g = gen2()
    for v in gen2():
        yield v

def get_res():
    import types
    def generatorToList( res ):
        if isinstance(res, types.GeneratorType):
            for r in res:
                if isinstance(r, types.GeneratorType): result.append(generatorToList(r))
                else: result.append(r)
        else: result.append(res)
        return result
    result = []
    res = nestedGenerator()
    return generatorToList(res)


"""
yield vs return:

The yield statement suspends a function's execution and sends a value back to the caller, but retains enough state to enable the function to resume where it left off. When the function resumes, it continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don't want to store the entire sequence in memory. Yield is used in Python generators. A generator function is defined just like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. 
"""