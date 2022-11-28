# JSON is commonly used with data APIs. Here how we can parse JSON into a Python dictionary
# JSON (JavaScript Object Notation) is a leightweight data format for data exchange
import json

# Sample JSON
userJSON = '''
{
    "first_name": "John", 
    "last_name": "Doe", 
    "age": 30
}
'''

# Parse to dict
user = json.loads(userJSON)
print(user)

# Parse to JSON
userJson = json.dumps(user)
print(type(userJson))


# load data from a file and convert it to a Python object with the json.load() method
with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)