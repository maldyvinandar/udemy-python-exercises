# Sample of I/O Operations

myfile = open('myfile.txt')

myfile.read()

# Resets the cursor back to the starting point
myfile.seek(0)

myfile.readlines()

myfile.close()

# No need to close with this way
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
