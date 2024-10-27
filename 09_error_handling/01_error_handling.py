# Exception handling in Python is the process of managing runtime errors to keep the program from crashing unexpectedly.
# Python provides a structured approach using try, except, else, and finally blocks to handle exceptions gracefully.

# Basic Structure of Exception Handling
# The general structure of handling exceptions is:

#? try:
    # Code that may raise an exception
#? except SomeException as e:
    # Code to handle the exception
#? else:
    # Code to execute if no exceptions were raised
#? finally:
    # Code that will always execute, whether an exception was raised or not

# Example: Handling Different Types of Exceptions

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Operation completed successfully.")
finally:
    print("End of operation.")

# Explanation that might raise an exception is placed here.
# except: Catches specific exceptions and allows you to handle them separately.
# Here, ValueError and ZeroDivisionError are handled.
# else: Executes only if no exceptions were raised in the try block.
# finally: Runs regardless of whether an exception occurred or not.
# It's useful for cleanup actions like closing files.

# Handling Multiple Exceptions in One Block
# If you want to handle multiple exceptions with the same response, you can specify them in a single except statement:

try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")

# Raising Exceptions
# You can raise exceptions intentionally using the raise keyword.
# This can be useful for validating inputs or enforcing rules.

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "Access granted."

try:
    print(check_age(16))
except ValueError as e:
    print(e)

# Custom Exceptions
# Python allows you to define custom exceptions by creating a new class that inherits from Exception.

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)

# Common Exception Types
# Here are some frequently encountered exceptions in Python:

# ValueError: Raised when a function gets an argument of the right type but inappropriate value.
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# FileNotFoundError: Raised when trying to open a file that doesn't exist.
# ZeroDivisionError: Raised when dividing by zero.
# KeyError: Raised when accessing a dictionary with a key that doesn't exist.

# Example: Cleanup with finally

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()  # Ensures the file is closed

# Combining else and finally Blocks

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"Result is {result}")
    finally:
        print("Execution complete.")

divide(10, 2)
divide(10, 0)

# With try, except, else, and finally, you can handle exceptions effectively and ensure your program manages errors gracefully.
# Let me know if you have more questions or specific use cases!