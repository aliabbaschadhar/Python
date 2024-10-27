#! File Handling in python

#! Opening a File
# The open() function is used to open files in Python. The syntax is:


file = open("filename", "mode")

# !Modes:

# 'r' : Read (default mode) – Opens a file for reading.
# 'w' : Write – Opens a file for writing. If the file exists, it will be overwritten. If it doesn’t exist, a new file will be created.
# 'a' : Append – Opens a file for appending data. Creates a new file if it doesn’t exist.
# 'r+': Read and Write – Opens a file for both reading and writing.

#* Example of Basic Operations

#! Reading a File

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

#! Writing to a File

file = open("example.txt", "w")
file.write("Hello, world!")
file.close()

# Appending to a File

file = open("example.txt", "a")
file.write("\nAppended text.")
file.close()

#! Using with for Better File Handling

# Using with ensures the file is properly closed after operations, even if an error occurs.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


#! Reading Line by Line

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

#! Working with Binary Files
# To handle binary files, like images or executable files, use the 'rb', 'wb', or 'ab' modes.


with open("image.jpg", "rb") as file:
    binary_data = file.read()


#! File Methods Summary:

# read(size): Reads the file’s content up to the specified size.
# readline(): Reads a single line from the file.
# readlines(): Reads all lines and returns them as a list.
# write(content): Writes content to the file.
# writelines(list_of_strings): Writes a list of strings to the file.

#! Checking if a File Exists

# To check if a file exists before attempting to open it, you can use os.path.exists():


import os

if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist.")