# itertools module is a collection of tools for handling iterators.
# Simply put, iterators are data types that can be used in a for loop.
# The most common iterator in Python is the list.

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

# product() - This tool computes the cartesian product of input itertools.
# It is equivalent to nested for-loops. For example, product(A, B) returns the same as ((x,y) for x in A for y in B)
prod = product([1,2], [3,4])
# converting the iterator to list for printing
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

# to allow the product of an iterable with itself, specify the number of repetitions
prod = product([1,2], [3], repeat=2)
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]


# permutations() - This tool returns successive length permutations of elements in an iterable, with all possible orderings, and no repeated elements.
perm = permutations([1,2,3])
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# optional: the length of the permuatation tuples
perm = permutations([1,2,3], 2)
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# combinations() and combinations_with_replacement()
# combination() does not allow repeated elements
# but combinations_with_replacement() allows

# the secondary argument is mandatory and specifies the length of the output tuples.
comb = combinations([1,2,3,4], 2)
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
 
comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


# accumulate() - Make an iterator that returns accumulated sums, or accumulated results of their binary functions.

# return accumulated sums
acc = accumulate([1,2,3,4])
print(list(acc)) # [1, 3, 6, 10]

# other possible functions are possible
import operator
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc)) # [1, 2, 6, 24]

acc = accumulate([1,5,2,6,3,4], func=max)
print(list(acc)) # [1, 5, 5, 6, 6, 6]


# groupby() - Make an iterator that returns consecutive keys and groups form the iterable.
# The key is a function computing key value for each element.
# If not specified or is None, key defaults to an identity function and returns the element unchanged.
# Generally, the iterable needs to already be sorted on the same key function.

# use a function as key
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1,2,3,4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))
# True [1, 2]
# False [3, 4]

# use a lambda expression
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x : "i" in x)
for key, group in group_obj:
    print(key, list(group))
# True ['hi', 'nice']
# False ['hello', 'cool']

persons = [{'name':'Tim', 'age':25},{'name':'Dan', 'age':25},{'name':'Lisa', 'age':27},{'name':'Claire', 'age':28}]
for key, group in groupby(persons, key=lambda x : x['age']):
    print(key, list(group))
# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]


# Infinite iterators: count(), cycle(), repeat()

# count(x) - count from x: x, x+1, x+2, x+3, ...
for i in count(10):
    print(i)
    if i >= 13:
        break

# cycle(iterable) - cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1,2,3]):
    print(i)
    sum += i
    if sum >= 12:
        break

# repeat(x) - repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i)