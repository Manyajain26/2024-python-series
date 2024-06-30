class Vechiles:
    def calculate_average(self,fuel:int,ride:int):
        return f'Average ={ride/fuel}km per litre'


mustang = Vechiles()
print(mustang.calculate_average(50,100))
