# In Python, decorators are a way to modify or extend the behavior of functions or methods without permanently changing their code. They are commonly used for adding functionality, like logging, access control, or even modifying return values.

# We can understand it by using toolbath analogy like every vehical has to go throught tool both whether it is big car or small car.
# If it is a big then we shall get some charges from them and if it is small then we shall get some charges/no charges from them.
# But all of them go through the tool box

# How Decorators Work
# A decorator is essentially a function that takes another function as an argument, wraps some additional functionality around it,
# And then returns a new function with the added functionality. In Python, you use the @ symbol above a function to apply a decorator to it.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() # Output:
# Something is happening before the function is called.
# Hello! 
# Something is happening after the function is called.

# Here’s what’s happening:

# my_decorator is defined to add code before and after the func function.
# Using @my_decorator before say_hello() tells Python to pass say_hello through my_decorator, modifying its behavior.


# Find time taken by a function to execute using decorators

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time() # start time fo function
        result = func(*args,**kwargs)
        end = time.time() # End time of function
        print(f"{func.__name__} ran in {round(end-start,2)} seconds time")
        return result
    # Closure
    return wrapper

@timer # now example will go throught the toolboth
def example_function(n):
    time.sleep(n) # Pauses the execution of program for given time/specifc time

example_function(2)