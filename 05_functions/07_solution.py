# *args key word in python

# *args is used to get multiple parameters/arguments in function 

# def sum_all(args): # this causes error and shows that by using args it will take only one argument

def sum_all(*args):
    # print(*args) # 1,2,3,4,5
    print(args) # (1,2,3,4,5) # this will give us a tuple
    # As it is a tuple so we can iterate over it
    for i in args:
        print(i*2 ,end=" ")
    print()

    return  sum(args) # 15

print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5 , 7 ,8 ,9))