# Inheritance In Python
'''
Inheritance allows us to define a class
that inherits all the methods and properties from another class.
Parent class is the class being inherited from
, also called base class.
Child class is the class that inherits from another class,
 also called derived class.
'''


class mom:
    def momsclass(self):
        print("This Is Mom Class")


class son(mom):
    def sonsclass(self):
        print("this is sons")


m1 = mom()
s1 = son()
m1.momsclass()
s1.momsclass()
