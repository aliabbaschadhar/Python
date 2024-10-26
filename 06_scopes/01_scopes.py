# Scopes
# A scope defines the visibility and lifetime of a variable in your code. There are four types of scopes in Python:

# Local Scope: Variables created inside a function are local to that function and cannot be accessed from outside it.

def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Outputs: 10
# print(x)  # Raises NameError: name 'x' is not defined


# Enclosing Scope: This refers to the scope of enclosing functions. If you have a nested function, the inner function can access variables from its enclosing function.

def outer_function():
    y = 20  # Enclosing variable
    def inner_function():
        print(y)  # Accessing enclosing variable
    inner_function()  # Outputs: 20

outer_function()

# Global Scope: Variables defined at the top level of a script or module are global. They can be accessed from any function within the same module.

x = 10  # Global variable

def my_function():
    print(x)  # Accessing global variable

my_function()

#! Overwriting the golbal variable is not recommended.

x = 10  # Global variable

def my_function():
    global x
    x = 20  # golbal variable overwritten
    print(x)  # Outputs: 20

my_function()

print(x)  # Outputs: 20

# Built-in Scope: This includes names that are pre-defined in Python, such as print(), len(), etc. These are available in any scope.

print(len("Hello, World!"))  # Outputs: 13


#! Closures
# A closure is a feature in Python where a nested function remembers the values of its enclosing lexical scope even when the outer function has finished executing. Closures are useful for maintaining state in a function without using global variables.

def outer_function(x):
    def inner_function(y):
        return x + y  # inner_function uses x from outer_function
    return inner_function  # Return the inner function

closure_instance = outer_function(10)  # x is now 10
print(closure_instance(5))  # Outputs: 15 (10 + 5)

closure_instance = outer_function(20)  # x is now 20
print(closure_instance(10))  # Outputs: 30 (20 + 10)

# Understanding the Closure: In the example above, inner_function forms a closure that retains access to x from outer_function, even after outer_function has finished executing.

