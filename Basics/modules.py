# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

"""
Circular Imports/Circular Dependency:
Python Circular Imports is a type of Circular dependency. It occurs in python when two or more models import each other and it repeats the importing connection into an infinite circular call. With Circular Imports, the python script gives an error.

How to fix circular import error?
- If the error occurs due to a circular dependency, it can be resolved by moving the imported classes to a third file and importing them from this file. 
- If the error occurs due to a misspelled name, the name of the class in the Python file should be verified and corrected.
"""

# pip install <module_name>
# Using this will install the module globally

# We should use pipenv to install modules inside that environment only and not globally

# import datetime
# import datetime as dt
from datetime import date
# import time
from time import time

from validator import validate_email

# today = datetime.date.today()
# today = dt.date.today()
today = date.today()

# timestamp =  time.time()
timestamp =  time()

print(today, timestamp)

email = 'test@test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')
