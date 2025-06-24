tea_varieties = ["Black", "Green", "Oolong",  "White"]
print(tea_varieties)
print(tea_varieties[1])#Green
print(tea_varieties[-1]) #White

#As we were using string as a list and we were able to do slicing dicing so we can also do slicing in normal list

print(tea_varieties[:2]) #["black", "Green"]
print(tea_varieties[1:]) # ["Green", "Oolong",  "White"]
print(tea_varieties[0:2:1]) # ["black", "Green"]

#! ------->List is mutable datatype
tea_varieties[3] = "Herbal"
print(tea_varieties) # ["Black", "Green", "Oolong",  "Herbal"]

print(tea_varieties[1:2]) # ["Green"]

tea_varieties[1:2] = "Lemon"
print(tea_varieties) # ["Black", 'L', 'e', 'm', o', 'n', "Oolong",  "Herbal"]

#? Why has it behaved like that?

# Python treats the string "Lemon" as an iterable list, replacing the sliced element with each character individually. To replace "Green" with "Lemon" as a single element, use tea_varieties[1:2] = ["Lemon"].

# But in the above case python returns a sublist of slice of the original list. Which is also iterable but with index of one but here the who list is taken as a list that's why python inserted the whole string as a single single character. 

# To avoid this we will use: 

tea_varieties = ["Black", "Green", "Oolong",  "White"]

tea_varieties[1:2] = ["Lemon"]
print(tea_varieties) # ["Black", "Lemon", "Oolong",  "White"]

print(tea_varieties[1:3]) # ["Lemon", "Oolong"]
tea_varieties[1:3] = ["Ginger", "Mint"]
print(tea_varieties) # ["Black", "Ginger", "Mint",  "White"]

print(tea_varieties[1:1]) # []
tea_varieties[1:1] = ["Test", "Test"]
print(tea_varieties) # ["Black", "Test", "Test", "Ginger", "Mint",  "White"]

tea_varieties[1:3]= []
print(tea_varieties) # ["Black", "Ginger", "Mint",  "White"]

# Loops
for tea in tea_varieties:
    print(tea)

# Black
# Ginger
# Mint
# White

for tea in tea_varieties:
    print(tea, end="-")

# Black-Ginger-Mint-White
print("\n")
# Conditionals

if "Oolong" in tea_varieties:
    print("I have Oolong")
else:
    print("I don't have Oolong")

# I don't have Oolong

tea_varieties.append("Oolong") # To add value at the end of list

if "Oolong" in tea_varieties:
    print("I have Oolong")
else:
    print("I don't have Oolong")

# I have Oolong

# To remove the last value from the list
# pop() returns the value 

print(tea_varieties.pop()) 
print(tea_varieties) # ["Black", "Ginger", "Mint",  "White"]

# To remove the first value from the list

print(tea_varieties.pop(0))
print(tea_varieties) # ["Ginger", "Mint",  "White"]

# To remove a value from list
# remove() doesn't return the removed value but pop returns the value

tea_varieties.remove("Mint")
print(tea_varieties) # ["Ginger", "White"]

# To clear the list
tea_varieties.clear()
print(tea_varieties) # []

# To insert value in list
tea_varieties.insert(0, "Lemon")
print(tea_varieties) # ["Lemon"]

tea_varieties = ["Lemon", "Ginger", "White", "Oolong"]

tea_varieties_copy = tea_varieties; # This has not made a copy of list but a reference to the same list
print(tea_varieties_copy) # ["Lemon", "Ginger", "White", "Oolong"]

# To make a copy of list    

tea_varieties_copy_ref = tea_varieties.copy() #This has made copy of the list with same values but different reference, the main list and the copy has different reference
print(tea_varieties_copy_ref) # ["Lemon", "Ginger", "White", "Oolong"]

#Making a change in the main list will affect the tea_varieties_copy but not the tea_varieties_copy_ref

tea_varieties[0] = "Black"
print(tea_varieties) # ["Black", "Ginger", "White", "Oolong"]
print(tea_varieties_copy) # ["Black", "Ginger", "White", "Oolong"]
print(tea_varieties_copy_ref) # ["Lemon", "Ginger", "White", "Oolong"]

# ! -----List Comprehension----- ! #

squared_numbers = [x**2 for x in range(10)]
print(squared_numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cubed_numbers = [x **3 for x in range(10)] # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(cubed_numbers)

fourth_number = [x **4 for x in range(30)]
print(fourth_number) # [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, 14641, 20736, 28561, 38416, 43008, 47825, 53256, 59049, 65024, 71329, 77884, 84741, 91872, 99201, 106276, 113906, 121876, 130281, 139008]

squared_numbers = [x**2 for x in range(10) if x % 2 == 0]
print(squared_numbers) # [0, 4, 16, 36, 64, 100]