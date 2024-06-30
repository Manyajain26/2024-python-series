# single Inheritance In Python
"""accessing parent class attributes"""


class mom:
    def __init__(self, kitchen_size, pocket_money):
        self.kitchen_size = kitchen_size
        self.pocket_money = pocket_money

    def momsclass(self):
        print("This Is Mom Class ", self.kitchen_size)


class son(mom):

    def __init__(self, kitchen_size, pocket_money):
        self.kitchen_size = kitchen_size
        self.pocket_money = pocket_money

        # invoking the __init__ of the parent class
        mom.__init__(self, kitchen_size, pocket_money)

    def sonsclass(self):
        print("this is sons")


manya = son(200, 3000)
manya.momsclass()
print(manya.pocket_money)
