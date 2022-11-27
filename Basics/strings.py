# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Deep'
age = 25

# Concatenate
print("Hello, I am " + name + ' and I am ' + str(age) +
      ' years old')  # We can only concatenate strings

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, I am {name} and I am {age}')

# String Methods
s = "Deepbaran Kar"

# Capitalizing string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('Deepbaran', 'Gopal'))

# Count
sub = 'a'
print(s.count(sub))

# Starts with
print(s.startswith('Deep'))

# Ends with
print(s.endswith('r'))

# Split into list
print(s.split())
# To join a list into a string --> "".join()

# Find Postion
print(s.find('r'))  # index of 1st occurance

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())  # False because of the space

# Is all numeric
print(s.isnumeric())
