# A variable is a container for a value, which can be of various types

"""
PEP - Python Enhancement Proposals

PEP 8 - Style Guides:
- Use 4 spaces per indentation level
- Spaces are preferred over Tabs for indentation
    - Tabs should be used to remain consistent with code that is already indented with tabs.
    - Python disallows mixing tabs and spaces for indentation
- Limit all lines to a maximum of 79 characters
    - For flowing long block of text with fewer structural restrictions (decstring or comments), the line length should be limited to 72
- Surround top-level function and class definitions with two blank lines.
    - Method definitions inside a class are surrounded by a single blank line.
    - Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners
    - Use blank lines in functions, sparingly, to indicate logical sections.
- Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration.
- imports should be done at the top of the file.
"""

'''
This is a
multiple comment
or docstring (used to define a function purpose)
can be single or double quotes
'''

"""
VARAIBLE RULES:
    - Variable names are case sensitive (name and NAME are different variables)
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

"""
Data Types:
- Numeric:
    - Integer
    - Complex Number [2+4j]
    - Float
- Ditionary
- Boolean [True/False]
- Set
- Sequence Type:
    - Strings (Immutable)
    - List (Mutable)
    - Tuple (Immutable)
"""

"""
Stack Memory:

It is called stack memory allocation as the allocation happens in the function call stack. At the time of allocation, the memory size is known to the compiler and when there is a function call that happens, then its variable gets memory allocated on the stack.

It is the memory that is needed inside a particular function. When the function is called, it will be added to the program call's stack. Variable initialization inside the function is temporarily stored in the function call stack, where it will be deleted after the completion of the function. This memory allocation onto a contiguous memory is handled by the compiler, developers do not have to worry about it.
"""

"""
Heap Memory:

Heap memory allocation is done when memory is allocated at the time of execution of a program written by the programmer. As there is a pile of memory space available in the process of allocation and de-allocation, that's why it is known as heap memory. The variable which is required globally in the program is stored in heap memory.
"""

"""
Garbage Collection:

It is a process in which memory is deallocated when it is not in use to make the space available for other objects. In case, when no one is referencing the object in memory then in the virtual machine, the garbage collector comes to work to automatically delete the object in the heap memory.

Reference Counting:

It is a procedure that works by counting the number of times an object is referenced by other objects in the computer. This count for an object is decremented when reference to an object is removed. And when this count becomes zero, then that object is deallocated.
For example, in the case of two variables having the same value. Then the virtual machine instead of making two different objects, it makes two pointers pointing at the same object created in the private heap.
"""

"""
Python Interpretor:

The execution of the Python program involves 2 Steps:
1. Compilation
2. Interpreter

Compilation: 
The program is converted into byte code. It can run on any operating system and hardware. The byte code instructions are created in the .pyc file. The .pyc file is not explicitly created, as Python handles it internally.

Interpreter:
The next step involves converting the byte code (.pyc file) into machine code. This step is necessary as the computer can understand only machine code (binary code). Python Virtual Machine (PVM) first understands the operating system and processor in the computer and then converts it into machine code. Further, these machine code instructions are executed by processor and the results are displayed.

Source Code (.py) -Compiled-> Byte Code (.pyc) [INTERNAL] -Interpreted-> Machine Code -> Computer Execution

So, when we run a python code, it is first compiled and then interpreted line by line. The compilation part is mostly hidden from the user. While running the code, Python generates a byte code internally, this byte code is then converted using a python virtual machine (p.v.m) to generate the output.

However, the interpreter inside the PVM translates the program line by line thereby consuming a lot of time. To overcome this, a compiler known as Just In Time (JIT) is added to PVM. JIT compiler improves the execution speed of the Python program. This compiler is not used in all Python environments like CPython which is standard Python software.

---------------------------------------------
Why Interpreted?
One popular advantage of interpreted languages is that they are platform-independent. As long as the Python bytecode and the Virtual Machine have the same version, Python bytecode can be executed on any platform (Windows, MacOS, etc).

Dynamic typing is another advantage. In static-typed languages like C++, you have to declare the variable type and any discrepancy like adding a string and an integer is checked during compile time. In strongly typed languages like Python, it is the job of the interpreter to check the validity of the variable types and operations performed.

----------------------------------------------
Disadvantages of Interpreted languages:
Dynamic typing provides a lot of freedom, but simultaneously it makes your code risky and sometimes difficult to debug.

Python is often accused of being 'slow'. Now while the term is relative and argued a lot, the reason for being slow is because the interpreter has to do extra work to have the bytecode instruction translated into a form that can be executed on the machine.
"""

"""
Operators:
+, -, *, /, //, %, =, +=, -=, and, not, or, in, not in, is, is not, >>, <<

- For and operator the 2nd statemnet is evaluated only if the 1st statment is True
"""

"""
The isinstance() function returns True if the specified object is of the specified type, otherwise False.

isinstance(object, type)
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str
is_cool = True  # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic Math
a = x + y

print(x, y, name, is_cool, a)  # 1 2.5 John True 3.5

# Casting
X = str(x)
Y = int(y)
Z = float(y)

print(type(X), X)  # <class 'str'> 1
print(type(Y), Y)  # <class 'int'> 2
print(type(Z), Z)  # <class 'float'> 2.5

# Take user input
a = input()
b = input("Insert the value of b")
print(a, b)