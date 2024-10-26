class Car:
    def __init__(self, brand, model):

        # __init__ is the constructor of the class in python 
        #self keyword works same as this key word in cpp or js
        #self keyword is used to give context of variables of class to objects

        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla") # Creating an object of the class in python
print(my_car.brand, ": " , my_car.model) # Accessing the attributes of the object

my_new_car = Car("BMW", "X5")
print(my_new_car.brand, ": " , my_new_car.model) 