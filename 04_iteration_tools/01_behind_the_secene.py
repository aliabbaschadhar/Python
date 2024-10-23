# for, while, comprehensions are iteration tools in python

# lists, file, strings, dictionaries, sets, tuples, generators are iterateable objects in python

# Iteration tools make query to iterable object that i want to iterate over you and sends a iter() method to iterable object then it gives permission to iterate and reponds you with the refrence of first element/item in the list/dictionary and a __next__() method which helps to move to next refrence in the list.

eg_list = [1,2,3,4]

# list is an iterable object and it will be iterated from iter() provided by iterable tools and then iter() will receive the refrence of first ele and iterate through it then as we know that __next__() holds the refrence of next ele in list so,
# It will move forward and when it reaches the last ele of list it will give a exception that we have reached at the end of list 

# Using file as a iterateable object

import time

print("Chai is here");
username = "Ali Abbas Chadhar"
print(username)

