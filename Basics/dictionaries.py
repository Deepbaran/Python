# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Possible key types - Any immutable type, like strings or numbers can be used as a key. Also, a tuple can be used if it contains only immutable elements.
# Rather than Key-Value, it's Index-Value

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')

# Get a value
print(person['first_name'])
# .get() will not throw error if the key is not present in the dict and rather return None
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict [Deep Copy]
person2 = person.copy() # All iterables can be copied using .copy()
person2['city'] = 'Boston'

# Remove item
del person['age']
person.pop('phone') # This returns and removes the item
person.popitem() # returns and removes the last inserted key-value pair

# check for key
'first_name' in person

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
print(person, type(person))
print(person2, type(person2))


# Merge two dictionaries
# Use the update() method to merge 2 dicts
# existing keys are overwritten, new keys are added
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

# Nested dictionaries - The values can also be container types (e.g. lists, tuples, dictionaries).
my_dict_1 = {"name": "Max", "age": 28}
my_dict_2 = {"name": "Alex", "age": 25}
nested_dict = {"dictA": my_dict_1,
               "dictB": my_dict_2}
print(nested_dict)