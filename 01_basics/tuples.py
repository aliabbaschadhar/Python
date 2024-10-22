# Why do we need tuples?
# Because tuples are immutable and lists are mutable in memory
# Tuples are faster than lists
# Tuples are used to store data that cannot change  

tea_types = ('Black', 'Green', 'Oolong', 'White')
print(tea_types) # ('Black', 'Green', 'Oolong', 'White')

print(tea_types[0]) # 'Black'

print(tea_types[-1]) # 'White'

# Same slicing can happen in tuples also
print(tea_types[1:]) # ('Green', 'Oolong', 'White')

# tea_types[0] = "Lemon" ; # TypeError bcz tuples are immutable

print(len(tea_types)) # 4

# Tuples can be concatenated

more_tea = ('Ginger', 'Mint') ;
all_tee = tea_types + more_tea
print(all_tee) # ('Black', 'Green', 'Oolong', 'White', 'Ginger', 'Mint')

if 'Black' in all_tee:
    print("I have Black")
else: 
    print("I don't have Black")


more_tea = ('Ginger', 'Mint' , "Ginger") ;
print(more_tea.count("Ginger")) # 2

#Unwraping a tuple
tea_types = ('Black', 'Green', 'Oolong', 'White')

# No of variables must be same to number of values in tuple for unwrapping of tuple

(black , green , oolong , white) = tea_types
print(black) # Black
print(green) # Green
print(oolong) # Oolong
print(white) # White

print(type(tea_types)) # <class 'tuple'>