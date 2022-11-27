# JSON is commonly used with data APIs. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON)
print(user)

# Parse to JSON
userJson = json.dumps(user)
print(type(userJson))