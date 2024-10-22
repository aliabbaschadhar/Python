number = int(input("Enter number: "))

# desired_number = range(number)

# To find the range of numbers
desired_number = range(1,number+1);

sum = 0 

for num in desired_number:
    if num % 2 ==0:
        sum = sum + num
print("The sum of even number is: ", sum);