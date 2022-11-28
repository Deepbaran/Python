# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Deep'
age = 25

# triple quotes for multiline strings
my_string = """Hello
World"""

# escaping backslash
my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)

# backslash if you want to continue in the next line
my_string = "Hello \
World"

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
print(s.find('r'))  # index of 1st occurance. returns -1 if character is not there

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())  # False because of the space

# Is all numeric
print(s.isnumeric())


# Access characters and substrings
my_string = "Hello World"

# get character by referring to index
b = my_string[0]
print(b)

# Substrings with slicing
b = my_string[1:3] # Note that the last index is not included
print(b)
b = my_string[:5] # from beginning
print(b)
b = my_string[6:] # until the end
print(b)
b = my_string[::2] # start to end with every second item
print(b)
b = my_string[::-1] # reverse the string with a negative step:
print(b)


# Concatenate two or more strings
# concat strings with +
greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
print(sentence)


# replace a substring with another string (only if the substring is found)
# Note: The original string stays the same
message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)


# Format - New style is with .format() and old style is with % operator
# use braces as placeholders
a = "Hello {0} and {1}".format("Bob", "Tom")
print(a)

# the positions are optional for the default order
a = "Hello {} and {}".format("Bob", "Tom")
print(a)

a = "The integer value is {}".format(2)
print(a)

# some special format rules for numbers
a = "The float value is {0:.3f}".format(2.1234)
print(a)
a = "The float value is {0:e}".format(2.1234)
print(a)
a = "The binary value is {0:b}".format(2)
print(a)

# old style formatting by using % operator
print("Hello %s and %s" % ("Bob", "Tom")) # must be a tuple for multiple arguments
val =  3.14159265359
print("The decimal value is %d" % val)
print("The float value is %f" % val)
print("The float value is %.2f" % val)


# f-Strings - New since Python 3.6. Use the variables directly inside the braces.
name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)


# More on immutability and concatenation
# since a string is immutable, adding strings with +,  or += always creates a new string, and therefore is expensive for multiple operations --> join method is much faster
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i

# good
start = timer()
a = "".join(my_list)