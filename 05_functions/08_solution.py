def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        # print(key, " ", value)
        print(f"{key} : {value}") # called formated literal string method

# Inside the funtion *args is treated as a tuple of arguments
# Inside the funtion **kwargs is treated as a dictionary of arguments
# Use *args when you need to pass a list or tuple of values without needing to specify parameters names.
# Use **kwargs when you need to pass a dictionary of values with specfic names.

#! The * in *args unpacks a variable-length list or tuple of positional arguments.
# It tells Python to take all the positional arguments provided and pack them into a single tuple called args.

#* Purpose of * in args and ** in kwargs

#! The ** in **kwargs unpacks a variable-length dictionary of keyword arguments.
# It tells Python to take all the keyword arguments provided and pack them into a single dictionary called kwargs.

print_kwargs(name="Hitesh", age=20)
print_kwargs(name="Ali", age=20, country="India")