# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}
# fruits_set = set(['Apples', 'Oranges', 'Mango'])
# fruits_set = set(('Apples', 'Oranges', 'Mango'))

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add("Grape")

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
# fruits_set.clear()

# Delete
# del fruits_set

# Copy set
fruits_copy = fruits_set.copy()

print(fruits_set, fruits_copy)

# Union and Intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
u = odds.union(evens)
print(u)

# intersection(): take elements that are in both sets
i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)


# Difference of sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference() : returns a set with all the elements from the setA that are not in setB.
diff_set = setA.difference(setB)
# diff_set = setA - setB
print(diff_set)

# A.difference(B) is not the same as B.difference(A)
diff_set = setB.difference(setA)
# diff_set = setB - setA
print(diff_set)

# symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
diff_set = setA.symmetric_difference(setB)
print(diff_set)

# A.symmetric_difference(B) = B.symmetric_difference(A)
diff_set = setB.symmetric_difference(setA)
print(diff_set)


# Updating sets
etA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# update() : Update the set by adding elements from another set.
setA.update(setB)
print(setA)

# intersection_update() : Update the set by keeping only the elements found in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)

# difference_update() : Update the set by removing elements found in another set.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)

# symmetric_difference_update() : Update the set by only keeping the elements found in either set, but not in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)

# Note: all update methods also work with other iterables as argument, e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])


# Subset, Superset, and Disjoint
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(setA.issubset(setB))
print(setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))


# Frozenset
# Frozen set is just an immutable version of normal set. While elements of a set can be modified at any time, elements of frozen set remains the same after creation. Creation with: my_frozenset = frozenset(iterable)

a = frozenset([0, 1, 2, 3, 4])

# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()

# Also no update methods are allowed:
# a.update([1,2,3])

# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))