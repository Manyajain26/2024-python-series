class calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self):
        print("the sum of a and b is = ", self.a + self.b)

    def substract(self):
        print("the substraction of a and b is = ", self.a - self.b)

    def multiply(self):
        print("the multiplication of a and b is = ", self.a * self.b)

    def division(self):
        print("the division of a and b is = ", self.a / self.b)


obj = calculator(2, 4)
obj.sum()
obj.substract()
obj.multiply()
obj.division()
