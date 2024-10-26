class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        #Use self to give context of function to object
        return f"{self.brand} , {self.model}"
    
# Inheritence in python 
class ElectricCar(Car):

    # Constructor of child class
    def __init__(self, brand, model, battery_size):

        # Call __init__ of parent class        
        super().__init__(brand, model)
        # Private variable : To make a variable in python private is to add __(double underscore) before variable name
        self.__battery_size = battery_size

    # Getter: To access the prive variable
    def get_battery_size(self):
        return self.__battery_size

    # Overriding the parent class function
    def full_name(self):
        return super().full_name() + f" , {self.__battery_size}"

my_tesla= ElectricCar("Tesla", "Model_S", "100kWh")

print(my_tesla.full_name())

# print(my_tesla.__battery_size) # Error bcz __battery_size is private
print(my_tesla.get_battery_size()) # This is the only way to access private variable is to make a getter function
