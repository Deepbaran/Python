# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces.

# Create function
def sayHello(name, last_name='Kar'):
    print(f"Hello {name} {last_name}")

sayHello('Deep')
sayHello(name='Gopal')

# Return Values
def getSum(num1, num2):
    global total # global keyword marks a variable as global variable and the variable is put in the global scope. 
    total = num1 + num2
    return total

num = getSum(3, 4)
print(num)
print(total)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))
