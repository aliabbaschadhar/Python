class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        #Use self to give context of function to object
        return f"{self.brand} , {self.model}"
    
my_car = Car("Toyota" , "Corolla")

print(my_car.brand , " " , my_car.model)
print(my_car.full_name())