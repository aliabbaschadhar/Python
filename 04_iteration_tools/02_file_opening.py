file = open("01_behind_the_secene.py")

print(file.readline())

# After reaching at the end of the file it will give a empty string internally it is using __next__() to move forward but file.readline() is a wraper of __next__() to handle it with very much care and make code more readable

# print(file.readlines()) # This is method is not used in production bcz it is not very memory efficient

# We can also use for loop to read the file

for line in file:
    print(line, end="")

# Solution of above problem

# # for, while, comprehensions are iteration tools in python


# # lists, file, strings, dictionaries, sets, tuples, generators are iterateable objects in python

# # Iteration tools make query to iterable object that i want to iterate over you and sends a iter() method to iterable object then it gives permission to iterate and reponds you with the refrence of first element/item in the list/dictionary and a __next__() method which helps to move to next refrence in the list.

# eg_list = [1,2,3,4]

# # list is an iterable object and it will be iterated from iter() provided by iterable tools and then iter() will receive the refrence of first ele and iterate through it then as we know that __next__() holds the refrence of next ele in list so,
# # It will move forward and when it reaches the last ele of list it will give a exception that we have reached at the end of list 

# # Using file as a iterateable object

# import time

# print("Chai is here");
# username = "Ali Abbas Chadhar"
# print(username)

# Using while loop
while True:
    line = file.readline()
    if not line:
        break
    print(line, end="") 

file.close()

# Understanding iter() and __next__() using list

mylist = [1,2,3,4,5,6,7,8,9,10]
I = iter(mylist)
#Gives refrence of fist element in the list
print(I) # <list_iterator object at 0x7a6017230a00>

print(I.__next__()) #1

#__next__() will say, i will be keeping memory refrence of fist ele of the list and i will point to it only but i will be keep a pointer to next ele in the list

print(I) # <list_iterator object at 0x7a6017230a00>

print(I.__next__()) # 2

print(I) # <list_iterator object at 0x7a6017230a00>

# I will always point to the first ele of the list always 

print(I.__next__()) # 3
print(I.__next__()) # 4
print(I.__next__()) # 5

# File has its own iter() method by default and list doesn't have its own iter() object


file = open("01_behind_the_secene.py")

print(file is iter(file))# True
#Are file and iter(file) are same? # Yes

mylist = [1,2,3,4,5,6,7,8,9,10]

print(mylist is iter(mylist)) # False
#Are mylist and iter(mylist) are same? # No

#! This proves that when we take a refrence of file inside a variable, the variable is an iterable object while on other hand when we take refrence of list inside a variable ,it is not iterable object , it's refrence is iterateable object

