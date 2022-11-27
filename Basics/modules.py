# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

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
