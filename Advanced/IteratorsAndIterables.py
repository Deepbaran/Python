"""
Iteration is a processof using a loop to access all the elements of a sequence. Most of the time, we use for loop to iterate over a sequence.
But there are some times when we need to iterate over a sequence using different approach. In those cases, we need to use an iterator.

In Python, both the terms iterators and iterables are sometimes used interchangeably but they have different meanings.

We can say that an iterable is an object which can be iterated upon, and an iterator is an object which keeps a state and produces the next value each time.

NOTE: Every iterator is an iterable, but not every iterable is an iterator.
"""

# Iterator in Python
# Iterable is a sequence that can be iterated over, i.e., you can use a for loop to iterate over the elements in the squence.
for value in ['a','b','c','d']:
    print(value)

# Examples are:
# Lists, Tuples, Strings, Dictionaries, Sets, Generators

# Iterable objects are also known as iterable containers.

"""
NOTE: We can create an iterator object from iterable by using the iter() function since the iter() function returns an iterator from an iterable object.
But when using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself.
The for statement does that automatically, creating a temporary unnamed variable to hold the iterator for the duration of the loop.
"""


# Iterator in Python
"""
An iterator is an object which must implement the iterator protocol consisting of the two methods __iter__() and __next__().
An iterator contains a countable number of values and can return the next element in the sequence, on element at a time.
Implementing __iter__() is required to allow both containers and iterators to be used with the for and in statements.
Implementing __next__() specifies how to return the next item from the iterator. If there are no further items, a StopIteration exception should be raised.
After implementing __iter__() and __next__(), we can also explicitly call iter() and next().
"""

# iter()
# The iter() function returns an iterator object. It takes any collection object as an argument and returns an iterator object.
# We can use the iter() function to convert an iterable into an iterator.

# iterator = iter(object)
colors = ['Black', 'Purple', 'Green']
iterator = iter(colors)
print(iterator) # Returns a itertor object

# Convert to concrete type
colors = list(iterator)
print(colors)


# next()
# The next() function is used to get the next item from the iterator. If there are no further items, it raises a StopIteration exception.
# The __next__() method is called automatically when the for statement tries to get the next item from the iterator.

colors = ['Black', 'Purple', 'Green']
iterator = iter(colors)
print(next(iterator))  # Output: Black
print(next(iterator))  # Output: Purple
print(next(iterator))  # Output: Green
# print(next(iterator))    
# Output:
# Traceback (most recent call last):
#   File "iterator-and-iterable-in-python.py", line 31, in <module>
#     print(next(iterator))
# StopIteration


# Why not ecery iterale is an iterator
# Every iterable is an iterator. This is for example because we cannot use next() with every iterable, so it does not follow the iterator protocol

a = [1,2,3]
# next(a)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'list' object is not an iterator