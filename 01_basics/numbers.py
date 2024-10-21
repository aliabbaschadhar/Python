#! Your intention must be clear in the code

# --> to raise power in python we use ** like 2**3 = 8

a = 40 
b = 2.34
print(a+b) # We should avoid that kind of operation always use the same data type in operation.
#Becz there is a chance that next time we can do operation is in different datatypes and which can cause errors like :
name = "hitesh"
# print(name + a) #This kind of errors can happen

# To convert a number into another data type we will use like this

alpha = int(b); #This will covert the b into a int datatype
print(alpha)

#Same thing goes with "a" int to float
beta = float(a); #Will convert the number into the into float
print(beta);


newStr = "chai" + "code" # concatinate string
print(newStr) #chaicode

# str1 = "chai" * "code" # Not possible causes error
# print(str1) 

x=2
y=3
z=4
print(x,y,z)

result = 1 / 3.0
print(result) # 0.33333333333333 which we don't want the user to see so we round off it in python

print(x<y<z) #True

# print(1 ==2 < 3) is equal to print(1==2 and 2<3) #False

# In python when we write 1 it is interpretated by compiler as True

print(True == 2 and 2 <3) # It is not a good syntax

import math #! Imorting math library

# math.floor() gives us closest int number below the provided number
print(math.floor(3.4)) #3

# math.ceil() gives us closest int number above the provided number 
print(math.ceil(3.5)) #4

# math.trunc() gives us closes number toward zero on realnumber line 
print(math.trunc(2.8)) #2
print(math.trunc(-2.8)) #-2


#!                Octal, Binary , Hexadecimals

# Binary --> 0b11(binary number starts from 0b )
# Octal --> 0o34 (octal starts from 0o)
# Hexadecimals--> 0x34(hexa starts from 0x34)

# To convert a number into octal binary hexa use those methods like : 
print(oct(45)) # 0o55

print(bin(34)) # 0b100010

print(hex(1003)) # 0x3eb

