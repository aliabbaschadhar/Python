class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        #Use self to give context of function to object
        return f"{self.brand} , {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        return super().full_name() + f" , {self.battery_size}"

my_tesla= ElectricCar("Tesla", "Model_S", "100kWh")

print(my_tesla.full_name())

print(my_tesla.brand)