import random

# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
a= random.uniform(1,10)
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1,10)
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0,1)
print(a)

# choose a random element from a sequence
a = random.choice(list('ABCDEFGHI'))
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"), k=3)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)


# The seed generator
# With random.seed(), we can ,ake results reproducible, and the chain of calls after random.seed() will produce the same trail of data.
random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

random.seed(42) # Re-seed
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

random.seed(1) # Re-seed
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

random.seed(42) # Re-seed
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))
