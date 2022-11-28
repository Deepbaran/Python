# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# The immutability of tuples enables Python to make internal optimizations. Thus, tuples can be more efficient when working with large data.

# Create tuple
fruits = ('Apples', 'oranges', 'Grapes')
# fruits2 = tuple(('Apple', 'Oranges', 'Grapes'))
# fruits2 = tuple(['Apple', 'Oranges', 'Grapes'])

# Single value needs trailing comma
fruits3 = ('Apple',)

# Get value
print(fruits[1])
# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
print(fruits[-1])

# Can't change value
# fruits[0] = 'Pears' # ERROR

# Delete tuple
del fruits2

# Length of tuple
print(len(fruits))

my_tuple = ('a','p','p','l','e',)
# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple = ('a', 'b') * 5
print(my_tuple)

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)

# Similar to Lists, slicing can be done in tuples too.
# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)


# Unpacking Tuples
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name ,age, city)

# Nested tuples
a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])