import math

def circle_stat(radius):
    # area = math.floor(math.pi * radius **2)
    # circumference = math.floor(2 * math.pi * radius)

    area = round(math.pi * radius **2 , 2)
    circumference = round(2 * math.pi * radius,2)

    # rounded_area = round(area,2)

    return area, circumference;

area, circumference = circle_stat(3)

# print("Area is:",area , "Circumference is: ",circumference) # floor--> 28 , 18

print("Area is:",area , "Circumference is: ",circumference) #round ---> 28.27  & 18.85
