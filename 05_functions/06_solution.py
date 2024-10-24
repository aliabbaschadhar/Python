# Syntax of lambda expression/function in python
# variable = lambda arguments: expression

lambda_cube = lambda x: x**3  # Creates a lambda function that returns x^3

print(lambda_cube(3))  # Prints 27

# Create anotherCube using lambda_cube
anotherCube = lambda_cube  # Correct way to assign lambda function

print(anotherCube(8))  # Prints 512

def simple_cube(x):
    return x ** 3  # Regular function definition

second_cube = simple_cube  # Works for both def and lambda functions

print(second_cube(9))  # Prints 729

# Explanation:
# Lambda functions are anonymous functions that return values implicitly.
# Regular functions defined using def keyword return values explicitly via return statement.
# Both lambda and def functions can be assigned to variables, storing a reference to the function.
# The function will execute only when invoked, not when its reference is stored.


