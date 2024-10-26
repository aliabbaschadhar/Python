# Generator function with yeild even numbers upto a specified limit

def  even_generator(limit ):
    # we can also use list as a bucket to store all the numbers:
    li = []
    for i in range(2, limit+1, 2):

        # print(i) # 2,4 ,6 ,8 ,10
        # return i # As we known function only return once so it will give us only 2
    #     li.append(i)
    # return li # this will return us a list [2, 4 ,6, 8, 10]
    # # But we didn't needed a list we needed just numbers.
        return i



# even_generator(10) 

# In industry generators are used in that way 

#? for num in even_generator(10):
    #? print(num)
    # but this will cause error bcz the even_generator() is returning int which is not iterable so here comes the cocept of yield

#? Concept of yield

# ?def even_generator1(limit):
# ?    for i in range(2,limit+1 , 2):
# ?        return i;

# ?for num in even_generator1(10):
#?     print(num) # Not iteratable

# Explaining the secenario
# Now what happens here we make a loop on even_generator() function and even_generator() is returning the value and what we need right now is that:
# It runs the even_generator function, it doesn't return the value it generates the value and remembers that where was I in the memory this is called yielding/yield
# I mean that when func() runs first time it will give us 2 but when it again runs it wil also give us 2 we want that it should give us 4 then 6 and so on...
# I am trying to say that when i called the function you give us the result & when i again call the function you should remember that where were you previously in the memory 
# This all happens with the help of "yield" keyowrd using instead of return in the function.

def even_generator1(limit):
    for i in range(2,limit+1 , 2):
        yield i;

for num in even_generator1(10):
    print(num) # 2,4,6,8,10(after "\n")