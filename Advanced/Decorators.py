# A decorator is a function that takes another function and extends the behavior of this function without explicitly modifying it.
# It allows to add new functionality to an existing function.
# There are 2 kinds of decorators:
# Function decorators
# Class decorators

"""
@my_decorator
def my_function():
    pass
"""

# Function decorators
"""
In Python, functions are first class objects, which means that - like any object - they can be defined inside another function, passed as argument to another funtion, or retirned from other functions.

A decorator is a function is a function that takes another function as argument, wraps its behavior inside an inner function, and returns the wrapped function. As a consequence, the decorated function now has extended functionality.
"""

# A decorator function takes another function as argument, wraps its behavior inside an inner finction, and returns the erapped funtion.
def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')

print_name()

print()

# Now wrap the function by passing it as argument to the decorator function
# and assign it to itself -> Our function has extended behavior!
print_name = start_end_decorator(print_name)
print_name()

# The decorator Syntax - Instead of wrapping our function and assign to itself, we can achieve the same thing simply by decorating our function with an @.
@start_end_decorator
def print_name():
    print('Alex')

print_name()

# Function Arguments - If the function has arguments and we try to wrap it with our decorator above, it will raise a TypeError since we have to call our function inside the erapper with this arguments, too. We can fix it using *args, **kwargs
def start_end_decorator_2(func):

    def wrapper(*args, **kwargs):
        print('start')
        func(*args, ** kwargs)
        print('End')
    return wrapper

@start_end_decorator_2
def add_5(x):
    return x+5

result = add_5(10)
print(result) # None

# Return values - In the above example, we do not get the result back, so as next step we also have to return the value from our inner function.
def start_end_decorator_3(func):

    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, ** kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_3
def add_5(x):
    return x+5

result = add_5(10)
print(result)
# start
# End
# 15

# Function identity - Using decorator, changes the __name__ of the function to the decorator. To fix this we need to use functools.wraps decorator, which will preserve the information about the original function. This is helpful for introspection purposes, i.e. the ability of an object to know about its own attributes at runtime
print(add_5.__name__)
help(add_5)
 # wrapper
# Help on function wrapper in module __main__:

# wrapper(*args, **kwargs)

import functools
def start_end_decorator_3(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, ** kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_3
def add_5(x):
    return x+5

result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)
# start
# End
# 15
# add_5
# Help on function add_5 in module __main__:

# add_5(x)

# FINAL TEMPLATE
"""
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
"""

# Decorator function arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Alex')
# Hello Alex
# Hello Alex
# Hello Alex


# Nested Decorators - The decorators are executed in the order they are listed.
def italic(func):
    
    def wrapper(*args, **kwargs):
        return '<i>' + func() + '</i>'
    
    return wrapper

def strong(func):

    def wrapper(*args, **kwargs):
        return '<strong>' + func() + '</strong>'

    return wrapper

@italic
@strong
def introduction():
    return 'This is a basic program'

print(introduction()) # <i><strong>This is a basic program</strong></i>


# Class Decorators
"""
We can also use a class as a decorator. Therefore, we have to implement the __call__() method to make our object callable.
Class decorators are typically used to maintain a state, e.g. here we keep track of the number of times our funciton is executed. 
The __call__ method does essentially the same thing as the wrapper() method. It adds some finctionality, executes the function, and returns its result.
Here we use functools.update_wrapper() instead of functools.wraps() to preserve the information about our function.
"""
class CountCalls:
    # the init needs to have the func as argument and store it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Call {self.num_calls} or {self.func.__name__!r}')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print('Hello!')
    
say_hello(5)
say_hello(5)
# Call 1 or 'say_hello'
# Hello!
# Call 2 or 'say_hello'
# Hello!