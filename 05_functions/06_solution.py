# Syntax  of lambda expression/function in python
#! variable = lambda arguments: expression

# lambda: The keyword that signifies the creation of a lambda function.
# arguments: A comma-separated list of parameters (can be zero or more).
# expression: A single expression that is evaluated and returned.

lambda_cube = lambda x:x**3

print(lambda_cube(3))

#! anotherCube = lambda_cube # causes error

# print(anotherCube(8))

def simple_cube (x):
    return x **3

second_cube =simple_cube # This can only happend with def function but not with lambda function

print(second_cube(9))

# In Python, lambda functions are anonymous functions that return values implicitly, meaning the result of their expression is automatically returned without the need for a return keyword. 
# They can only contain a single expression and are often used for short, simple tasks. On the other hand, regular functions defined using the def keyword return values explicitly when executed via the return statement. 
# If no return is provided, the function returns None by default. Both lambda and def functions can be assigned to variables, but this assignment stores a reference to the function rather than calling it.
#  The function will only execute when it is explicitly invoked, not when its reference is stored.