# single Inheritance In Python
"""accessing parent class attributes"""


class mom:
    kitchen_size = None
    pocket_money = 500

    def momsclass(self):
        print("This Is Mom Class")


class son(mom):

    def sonsclass(self):
        print("this is sons")


mummy = mom()
mummy.kitchen_size = 100
mummy.pocket_money = 3000

manya = son()
print(manya.pocket_money)
print(mummy.pocket_money)
