# chai = "alpha"
# chai[0] = "b";
# print(chai) # Error bcz string is immuteable

chai = "Lemon Chai"
print(chai);

first_char = chai[0];
print(first_char);

slice_chai = chai[0:6]
print(slice_chai)

# string[start:stop:step]

# start: The index where the slice begins (inclusive).
# stop: The index where the slice ends (exclusive).
# step: The number of indices to skip between each character in the slice (optional, defaults to 1).

# Extra Keypoints

# If you omit the start, it defaults to 0.
# If you omit the stop, it defaults to the length of the string.
# If you omit the step, it defaults to 1.
# Negative indices can be used to slice from the end of the string.


number_list = "0123456789"
print(number_list[:]) # "0123456789"
print(number_list[3:]) # "3456789"
print(number_list[:7]) # "0123456"
print(number_list[0:7:2]) # "0246"
print(number_list[0:7:3]) # "036"
print(number_list[0:7:-1]) # empty string

#Step in slice string defines how the iteration will move in string if it is positive then it will move from start to end of the string 
# If it is -ve then it will move from end to forward 

print(number_list[9:0:-1]) # "987654321"
print(number_list[9:0:-3]) # 963

#String Methods
print(chai.lower())
print(chai.upper())

new_chai = "    Masala Chai     "
print(new_chai.strip()) #  Remove spaces from front and back of string

Original_Chai = "Ginger Tea"
print(Original_Chai.replace("Ginger", "Lemon")) # Lemon Tea

chai = "Lemon, Ginger, Masala, Mint";
print(chai.split(", ")) # Conver the string into list on the basis of ", "(comma and a space after that)

chai = "Masala Chai";
# To find the starting index of string
print(chai.find("Chai")) #7
print(chai.find('chai')) #-1 --> Which means that chai is not in the string

chai = "Masala Chai Chai Chai"
print(chai.count("Chai")); #3

# ---> Order formating in Python in strings
name = 'Ali Abbas'
age = 22;
string = "My name is {} and my age is {} "
print(string.format(name,age));

# --->Using F-Strings 

# F-Strings ( formatted string literals) provide a more concise and readable way to format strings. You simply prefix the string with an f 
#* f"string{variable}"

string = f"My name is {name} and my age is {age}"
print(string)

#---> Converting list into string

chai_variety = ["Lemon", "Masala", "Ginger"]
print(", ".join(chai_variety)) # Convert the whole list into string with ", "(comma and a space format)

print(len(string)) # For length of string or list or anyother data type i think so

#! --> Raw String 

# chai = "He said, "Masala chai is awesome" "
# If we want to print string like this then we have to use back  by using it the first string is considered as it is it is not considered as a string so

chai = r"He said, \"Masala chai is awesome\" "
print(chai)

chai = "Masala\nChai"
print(chai)

chai = r"Masala\nChai"
print(chai)

chai = "c:\\usr\\pwd"
print(chai)
chai = r"c:\usr\pwd" #both syntaxes are same

chai = "Masala chai"
print("Masala" in chai) #True