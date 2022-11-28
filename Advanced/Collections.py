# Collections: Counter, OrderedDict, defaultDict, deque, namedtuple, ChainMap, UserDict, UserList, UserString

from collections import Counter, OrderedDict, defaultdict, deque

# Counter - dict subclass for counting hashable objects
# It is a container that stores elements as dictionary keys, and their counts are sorted as dictionary values.
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

print(my_counter.items()) # dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c', 'd', 'e'])
print(my_counter.values()) # dict_values([5, 4, 3, 2, 1])

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter) # Counter({1: 4, 2: 3, 0: 2, 3: 2, 4: 1})

# Most Common items
print(my_counter.most_common(1)) # [(1, 4)]
print(my_counter.most_common(3)) # [(1, 4), (2, 3), (0, 2)]

# Return an iterator over elements repeating each as many times as its count.
# Elements are returned in arbitrary order.
print(list(my_counter.elements())) # [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]]


# OrderedDict - dict subclass that remembers the order entries were added
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
for k, v in ordered_dict.items():
    print(k, v)


# defaultdict - dict subclass that calls a factory function to supply missing values.
# If a key is not present in defaultdict then a default value will be assigned to it.
d = defaultdict(int) # we need to define the default value type that will be assigned if key-value is not present
d['a'] = 1
d['b'] = 2
print(d.items()) # dict_items([('a', 1), ('b', 2)])
print(d['c']) # 0

d = defaultdict(list)
s = [('a', 1), ('b', 2), ('c', 3)]
for k, v in s:
    d[k].append(v)
print(d.items()) # dict_items([('a', [1]), ('b', [2]), ('c', [3])])
print(d['d']) # []


# deque - list-like container with fast appends and pops on either side.
# This is a double-ended queue.
# Adding and removing data from either side of the queue will take O(1) time.
d = deque()

# append
d.append('a')
d.append('b')
print(d)

# appendLeft
d.appendleft('c')
print(d)

# pop: removes element from right
print(d.pop())
print(d)

# popleft
print(d.popleft())
print(d)

# clear
d.clear()
print(d)

d = deque(['a','b','c','d'])

# extend at right or left side
d.extend(['e','f','g'])
d.extendleft(['h', 'i', 'j']) # 'j' is not the left most positon
print(d)

# count(x)
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)












