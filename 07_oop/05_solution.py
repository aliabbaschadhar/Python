class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand}, {self.__model}"

    def fuel_type(self):
        return "Petrol & diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
    # the @property decorator is used to define a method as a property, allowing it to be accessed like an attribute instead of calling it like a method & make sure that variable is read only and can't be modified again after initialization

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size

    def get_battery_size(self):
        return self.__battery_size

    def fuel_type(self):
        return "Electric Charger"

    def full_name(self):
        return super().full_name() + f", {self.__battery_size}"
    

my_car = Car("BMW", "X5")
# my_car.model = "X6" # Causes error bcz due to @property decorator my_car.model is read only property and cannot be modified

# print(my_car.__model)


my_tesla = ElectricCar("Tesla", "Model_S", "100kWh")

print(isinstance(my_tesla, Car)) # True
print( isinstance(my_tesla, ElectricCar)) # True

class Batttery:
    def battery_info(self):
        return "this is a battery"

class Engine:
    def engine_info(self):
        return "this is an engine"

class ElectricCarTwo(Car, Batttery, Engine):
    pass # pass is used as placeholder which says "do nothing" allowing you to define code blocks where logic is yet to be implemented, without causing syntax errors

my_new_tesla = ElectricCarTwo("Tesla", "Model_S")
print(my_new_tesla.battery_info()) # this is a battery
print(my_new_tesla.engine_info()) # this is an engine

