# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set , or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop - We can iterate through lists, Sets, tuples, strings, keys of dictionaries [dirtionary.keys()]
for person in people:
    print(f'Current Person: {person}')

# Break
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')


# Continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

for i in range(0, 11, 2):
    print(f'Number: {i}')

for i in range(11, 0, -1):
    print(f'Number: {i}')


# While loops execute a set of statements as long as condition is true
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1 # without this we will get infinite loops