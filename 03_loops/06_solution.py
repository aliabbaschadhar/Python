number = 5 ;
factorial = 1

# while loop only works if the condition is true 
# while true --> will work 
# while false--> not work

while number>0 :
    factorial = factorial * number;
    number -=1

print("Factorial of number is",factorial)