# A variable is a container for a value, which can be of various types

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
