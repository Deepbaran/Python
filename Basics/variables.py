# A variable is a container for a value, which can be of various types

"""
PEP - Python Enhancement Proposals

PEP 8 - Style Guides:
- Use 4 spaces per indentation level
- Spaces are preferred over Tabs for indentation
    - Tabs should be used to remain consistent with code that is already indented with tabs.
    - Python disallows mixing tabs and spaces for indentation
- Limit all lines to a maximum of 79 characters
    - For flowing long block of text with fewer structural restrictions (decstring or comments), the line length should be limited to 72
- Surround top-level function and class definitions with two blank lines.
    - Method definitions inside a class are surrounded by a single blank line.
    - Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners
    - Use blank lines in functions, sparingly, to indicate logical sections.
- Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration.
- imports should be done at the top of the file.
"""

'''
This is a
multiple comment
or docstring (used to define a function purpose)
can be single or double quotes
'''

"""
VARAIBLE RULES:
    - Variable names are case sensitive (name and NAME are different variables)
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

"""
Data Types:
- Numeric:
    - Integer
    - Complex Number [2+4j]
    - Float
- Ditionary
- Boolean [True/False]
- Set
- Sequence Type:
    - Strings (Immutable)
    - List (Mutable)
    - Tuple (Immutable)
"""

"""
Operators:
+, -, *, /, //, %, =, +=, -=, and, not, or, in, not in, is, is not, >>, <<

- For and operator the 2nd statemnet is evaluated only if the 1st statment is True
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str
is_cool = True  # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic Math
a = x + y

print(x, y, name, is_cool, a)  # 1 2.5 John True 3.5

# Casting
X = str(x)
Y = int(y)
Z = float(y)

print(type(X), X)  # <class 'str'> 1
print(type(Y), Y)  # <class 'int'> 2
print(type(Z), Z)  # <class 'float'> 2.5

# Take user input
a = input()
b = input("Insert the value of b")
print(a, b)