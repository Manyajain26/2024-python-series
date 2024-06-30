#Method Of Overloading In Python
'''Two or more methods have the same name but
different numbers of parameters or different types of parameters

Like other languages (for example, method overloading in C++) do,
 python does not support method overloading by default.
 But there are different ways to achieve method overloading in Python.

The problem with method overloading in Python
 is that we may overload the methods but can only use the latest defined method.
'''
class Numss:


    def product(self,a:int,b:int):
        print("product is= ",a*b)

    def product(self,a:int,b:int,c:int):
        print("product is= ",a*b*c)

obj1=Numss()
obj1.product(3,3)
#Python Me Overloading Nhi Hoti....
#isme jo latest method hoti hai bo hi run hota hai ...


