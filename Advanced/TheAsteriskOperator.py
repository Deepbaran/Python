# As operator
# * -> multiplication
# ** -> power


# Creating list, tuple, or string with repeatable elements

# list
zeros = [0] * 10
onetwos = [1,2] * 5
print(zeros)
print(onetwos)

# tuple
zeros = (0,) * 10
onetwos = (1,2) * 5
print(zeros)
print(onetwos)

# string
A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)


# *args and **kwargs annd * - already noted in the Basics


# Unpacking for function arguments
def foo(a, b, c):
    print(a, b, c)

# length must match
my_list = [1,2,3]
foo(*my_list)

my_string = "ABC"
foo(*my_string)

# length and keys must match
my_dict = {'a' : 4, 'b' : 5, 'c' : 6}
foo(**my_dict) # ** for key-value pairs


# Unpacking containers
numbers = (1,2,3,4,5,6,7,8)

*beginning, last = numbers
print(beginning)
print(last)

print()

first, *end = numbers
print(first)
print(end)

print()

first, *middle, last = numbers
print(first)
print(middle)
print(last)