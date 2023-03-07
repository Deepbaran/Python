# A class is like a blueprint for creating objects. An object has properties and methods (functions) assocaited with it. Almost everything in python is an object

# Every class is a child class of Object class

# Instance, Class and Static Methods - https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=Class%20methods%20don't%20need,access%20to%20cls%20or%20self%20.

"""
- A class method takes cls as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can't access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
- We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
- We generally use static methods to create utility functions.
- Both staticmethod and classmethod can be inherited and overridden.
"""

"""
- Variable set outside __init__ belong to the class. They're shared by all instances.
- Variables created inside __init__ (and all other method functions) and prefaced with self. belong to the object instance.
"""

"""
There is no methor overloading in Python. We simply use the default parameters to handle it.
"""

from abc import ABC, abstractmethod

# Abstract class
class AbstractClass(ABC):
    @abstractmethod
    def define_this(self):
        pass

# Create class
class User(AbstractClass):
    # Class state
    user = "Deep"

    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

    def define_this(self):
        print("Defined")

    # private method - python does not have a private keyword. so simply add a underscore (_) to mark the method as private
    def _privat_method(self):
        print("Private method")

    # classmethod
    @classmethod
    def class_method(cls):
        print(f"This is class method by {cls.user}")

    # staticmethod
    @staticmethod
    def static_method():
        print("This is a static method")

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        # super - calling the constructor of the parent class
        # If there is a multiple inheritance, then super will call the constructors of each parent class in the order that they are mentioned.
        super(Customer, self).__init__(name, email, age)
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # Method overwriting
    def greeting(self):
        print(super(Customer, self).greeting()) # calling the overridden method in the super class
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}' 

# Init user object
deep = User("Deep", "deep@gmail.com", 24)

print(type(deep))
print(deep.age)
deep.has_birthday()
print(deep.greeting())
print(User.class_method())
print(User.static_method())

# Init Customer object
janet = Customer('janet', 'j@ymail.com', 25)

janet.set_balance(500)
print(janet.greeting())
print(Customer.class_method())
print(Customer.static_method())