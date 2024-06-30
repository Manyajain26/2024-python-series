class Tableprinting:
    number=None

    def table(self):
        for i in range(1,11):
            print(self.number,"*",i,"=",self.number*i)

            
obj1=Tableprinting()
obj1.number=2
obj1.table()