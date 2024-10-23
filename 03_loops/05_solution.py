# Find the first non repeated char in string

input_str = "teetr"

for char in input_str:
    if input_str.count(char) ==1 :
        print("The non repeated char is: ", char)

    