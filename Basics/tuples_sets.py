# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'oranges', 'Grapes')
fruits2 = tuple(('Apple', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits3 = ('Apple',)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears' # ERROR

# Delete tuple
del fruits2

# Length of tuple
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add("Grape")

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
# fruits_set.clear()

# Delete
# del fruits_set

print(fruits_set)
