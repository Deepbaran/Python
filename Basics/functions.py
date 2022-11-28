# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces.

# We can specifiy to which argument the value belongs to when passing it to the function if we do not want to pass arguments in order or if we are not passing all the arguments.

# In python parameters are passed by reference

'''
- Parameters are the variables that are defined or used inside parentheses while defining a function
- Arguments are the value passed for these parameters while calling a function
'''

"""
- We can pass arguments as positional or keyword arguments. 
- Some benefits of keyword arguments can be: 
    - We can call arguments by their names to make it more clear what they represent 
    - We can rearrange arguments in a way that makes them most readable
"""

"""
- Functions can have default arguments with a predefined value. 
- This argument can be left out and the default value is then passed to the function, or the argument can be used with a different value. 
- Note that default arguments must be defined as the last parameters in a function.
"""

"""
def fun(a, b=3, c, d): <-- This is wrong
    pass

fun(3, 4, d=5, c=8) <-- 3 is assigned to a and 4 is assigned to b. c and d should also be default arguments, otherwise if we do not pass the values of c and d then only a and b is passed.
Even if b is defined, the 2nd argument will get assigned to b
"""

# Create function
def sayHello(name, last_name='Kar'): # name is the parameter
    print(f"Hello {name} {last_name}")

sayHello('Deep') # 'Deep' is the argument
sayHello(name='Gopal')

# Return Values
def getSum(num1, num2):
    global total # global keyword marks a variable as global variable and the variable is put in the global scope. 
    total = num1 + num2
    return total

num = getSum(3, 4)
print(num)
print(total)


"""
Variable-length arguments (*args and **kwargs):
- If you mark a parameter with one asterisk (*), you can pass any number of positional arguments to your function (Typically called *args)
- If you mark a parameter with two asterisks (**), you can pass any number of keyword arguments to this function (Typically called **kwargs).
"""
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)
print()

# omitting of args or kwargs is also possible
foo(1, 2, three=3)


# Forced keyword arguments - Sometimes you want to have keyword-only arguments. You can enforce that with: - If you write '*,' in your function parameter list, all parameters after that must be passed as keyword arguments. - Arguments after variable-length arguments must be keyword arguments.
def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4)
# not allowed:
# foo(1, 2, 3, 4)

# arguments after variable-length arguments must be keyword arguments
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(8, 9, 10, last=50)


"""
Unpacking into agruments:
- Lists or tuples can be unpacked into arguments with one asterisk (*) if the length of the container matches the number of function parameters.
- Dictionaries can be unpacked into arguments with two asterisks (**) the the length and the keys match the function parameters.
"""
def foo(a, b, c):
    print(a, b, c)

# list/tuple unpacking, length must match
my_list = [4, 5, 6] # or tuple
foo(*my_list)

# dict unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible since wrong keyword


# Local vs global variables - Global variables can be accessed within a function body, but to modify them, we first must state global var_name in order to change the global variable.
# If we do not write global var_name and asign a new value to a variable with the same name as the global variable, this will create a local variable within the function. The global variable remains unchanged.
def foo1():
    x = number # global variable can only be accessed here
    print('number in function:', x)

number = 0
foo1()

# modifying the global variable
def foo2():
    global number # global variable can now be accessed and modified
    number = 3

print('number before foo2(): ', number)
foo2() # modifies the global variable
print('number after foo2(): ', number)


"""
Parameter passing:
- Python uses a mechanism, which is known as "Call-by-Object" or "Call-by-Object-Reference. The following rules must be considered: - The parameter passed in is actually a reference to an object (but the reference is passed by value) - Difference between mutable and immutable data types

This means that:
- Mutable objects (e.g. lists,dict) can be changed within a method.
- But if you rebind the reference in the method, the outer reference will still point at the original object.
- Immutable objects (e.g. int, string) cannot be changed within a method.
- But immutable object CONTAINED WITHIN a mutable object can be re-assigned within a method.
"""
# immutable objects -> no change
def foo(x):
    x = 5 # x += 5 also no effect since x is immutable and a new variable must be created

var = 10
print('var before foo():', var)
foo(var)
print('var after foo():', var)

# mutable objects -> change
def foo(a_list):
    a_list.append(4)

my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

# immutable objects within a mutable object -> change
def foo(a_list):
    a_list[0] = -100
    a_list[2] = "Paul"

my_list = [1, 2, "Max"]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

# Rebind a mutable reference -> no change
def foo(a_list):
    a_list = [50, 60, 70] # a_list is now a new local variable within the function
    a_list.append(50)

my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

# Be careful with += and = operations for mutable types. The first operation has an effect on the passed argument while the latter has not:
# another example with rebinding references:
def foo(a_list):
    a_list += [4, 5] # this chanches the outer variable

def bar(a_list):
    a_list = a_list + [4, 5] # this rebinds the reference to a new local variable

my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

my_list = [1, 2, 3]
print('my_list before bar():', my_list)
bar(my_list)
print('my_list after bar():', my_list)
