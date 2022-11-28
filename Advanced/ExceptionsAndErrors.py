# A Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception.

# Raising exception:
# raise Exception('Raising an exception')

# Raising AssertionException:
# x = -5
# assert (x >= 0), 'x is not positive.'

# Handling Exceptions:
# try:
    #statement
# except Exception as e:
#     print(e)

# try:
    #statement
# except ZeroDivisionError as e:
#     pritn(e)
# except TypeError as e:
#     print(e)

# try:
    #statement
# except ZeroDivisionError as e:
#     pritn(e)
# else:
#     print('Everything is ok')

# try:
    #statement
# except ZeroDivisionError as e:
#     pritn(e)
# finally:
#     print('This will be executed even if there is a return statment in try or catch')
#     print('Clean up studd here...')

# Define personal Exceptions
class PersonalExcpetion(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test(a):
    if a > 1000:
        raise PersonalExcpetion('Value too high.', a)
    return a

try:
    test(5000)
except PersonalExcpetion as e:
    print(e.message, e.value)