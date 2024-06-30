class areacalculator:
    def __init__(self, length, breadth, radius):
        self.choice = choice
        self.length = length
        self.breadth = breadth
        self.radius = radius

    def ractangle(self):
        print("area of ractangle is= ", self.length * self.breadth)

    def square(self):
        print("area of square is =", (self.length) ** 2)

    def triangle(self):
        print("area of triangle= ", 1 / 2 * (self.length * self.breadth))

    def circle(self):
        print("area of circle= ", 3.14 * (self.radius * self.radius))


choice = int(input("enter your choice"))

obj1 = areacalculator(2, 7, 4)
if choice == 1:
    obj1.ractangle()
elif choice == 2:
    obj1.square()
elif choice == 3:
    obj1.triangle()
elif choice == 4:
    obj1.circle()
else:
    print("Enter Your Choice Between 1 and 4")
