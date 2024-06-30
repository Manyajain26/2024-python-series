# __init__ method in python
'''
__init__ method in Python is used to initialize objects of a class.
It is also called a constructor.

To completely understand the concept of __init__ method,
 you should be familiar with:
 Prerequisites – Python Class and Objects, Self
'''


class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.fullname = name + '_kumar_' + lastname


std1 = Student("garv", "mehra")
print(std1.fullname)
