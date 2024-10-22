age = int(input("Enter age :"))

#Used int() here because every value received from user always come in string

if age<13:
    print("Child")
elif age >=13 and age <=18:
    print("Teenager");
elif 20 <= age <=59: 
    print("Adult")
else:
    print("Senior")