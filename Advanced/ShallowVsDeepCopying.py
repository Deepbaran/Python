import copy

# Using the assignment operator (=) will only create a new variable with same reference.
# Modifying one will affect the other.

# Shallow Copy
# One level deep. Modifying on level 1 does not affect the otehr list. Use copy.copy(), or object specific copy funciton/copy constructor

list_a = [1,2,3,4,5]
list_b = copy.copy(list_a) 
# list_b = list(list_a)
# list_b = list_a[:]
# list_b = list_a.copy()

# not affect the other list
list_b[0] = -10
print(list_a)
print(list_b)

# But with nested objects, modifying on level 2 or deeper does affect the other.
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.copy(list_a)

# affect the other
list_a[0][0] = -10
print(list_a)
print(list_b)


# Deep copy
# Full independent clones. Use copy.deepcopy()
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.deepcopy(list_a)

# not affect the other
list_a[0][0] = -10
print(list_a)
print(list_b)