# A list is a collection which is ordered and changeable. Allows duplicate members. Can store multiple data types.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into postion
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list - Sort in-place
fruits.sort()

# Sort list - Returns a sorted list
# sorted() works on any iterable type, not just lists
fruits_sorted = sorted(fruits, reverse=False) # reverse is False by default

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)


# create list with repeated elements
list_with_zeros = [0] * 5
print(list_with_zeros)


# concatenation
list_concat = list_with_zeros + fruits
print(list_concat)


# convert string to list
string_to_list = list('Hello')
print(string_to_list)


# Slicing - Only lists, tuples and strings support slicing as they are ordered. Dictionaries and Sets do not support slicing as they are unordered.
# a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here -This is only support in lists, not in tuples and strings as both of them are immutable
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)


# List Comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)


# Nested Lists
a = [[1, 2], [3, 4]]
print(a)
print(a[0])

# Extend a list
list1 = [1,2,3]
list2 = [2,3,4]
list1.extend(list2)
print(list1) # [1,2,3,2,3,4]

# Find element in a list
a = [1,2,3,4,5]
print(6 in a) # False
print(3 in a) # True
try:
    # If element 3 and 7 are present in the list, then their indexes will be returned. Otherwise ValueError Exception will be thrown
    ix1 = a.index(3)
    print(ix1) # 2 
    ix2 = a.index(7) # ValueError Exception will be thrown
except ValueError as e:
    print(f"The element {e} is not present in the array {a}. Hence {ValueError} error is thrown")
    # The element 7 is not in list is not present in the array [1, 2, 3, 4, 5]. Hence <class 'ValueError'> error is thrown

# Count number of zeros in a list
nums = [1,0,2,3,0]
print(nums.count(0)) # 2