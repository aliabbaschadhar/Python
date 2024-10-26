class Car:
    total_car = 0 # claas variable
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1 # Another way to access class variables

    def full_name(self):
        return f"{self.brand}, {self.model}"
    
    # Function Overriding to achieve Polymorphism
    def fuel_type(self):
        return "Petrol & diesel"
    # Static methods : Static methods are the methods which can only be acccessed by the class not by it's instances/ objects
    #! To make a method static in python we use @staticmethod decorator
    # Decorators are the enhance the power of the method or other things

    #If we write the simple function whcih can an object access
    #? def general_description(self):
    #?     return "Cars are means of transport"

    @staticmethod 
    def general_description():
        return "Cars are means of transport"
        # Now only class can access this function

    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size

    def get_battery_size(self):
        return self.__battery_size
    
    # Function Overriding to achieve Polymorphism
    def fuel_type(self):
        return "Electric Charger"

    def full_name(self):
        return super().full_name() + f", {self.__battery_size}"

my_car = Car("BMW", "X5")
print(my_car.fuel_type()) # Function Overriding
my_tesla = ElectricCar("Tesla", "Model_S", "100kWh")
print(my_tesla.fuel_type()) # Function Overriding
print(my_tesla.full_name())
print(my_tesla.get_battery_size())

print(Car.total_car) # 2

print(Car.general_description()) # Cars are the means of transport
print(my_car.general_description()) # Causes error