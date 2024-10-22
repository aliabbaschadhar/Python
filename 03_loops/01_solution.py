numbers = [1, -2, 3 ,-4 , 5 , -6 , -7 , -8,9,10]
count = 0 

for num in numbers:
    if num>0:
        count+=1
    else:
        continue

print("Number of positive numbers in list are:",count)