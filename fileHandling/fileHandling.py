# file handling is used to read and write files in python.
#  It is a very important skill to have as a programmer. In this tutorial, we will learn how to handle files in python.
# To handle files in python, we use the built-in open() function. 
# The open() function takes two arguments: the name of the file and the mode in which we want to open the file.
#  The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'x' for creating a new file.

# handleing files in python is a very important skill to have as a programmer.
#  It allows you to read and write files, which is essential for many applications.
# In this tutorial, we have learned how to handle files in python using the open() function and the with statement.
#import pathlib  

import pathlib
# creating a new file and writing to it
print('Creating a new file and writing to it:')

check_file = pathlib.Path('newfile.txt')
if not check_file.exists():
    with open('example.txt', 'w') as file:
        file.write('This is a new file created using python.\n')
else:    print('The file already exists.')



# check if a file exists before opening it
print('Checking if the file exists before opening it:')
file_path = pathlib.Path('example.txt')
if file_path.exists():
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
else:
    print('The file does not exist.')  


# updating a file by appending new content to it
print('Updating a file by appending new content to it:')

file_path = pathlib.Path('example.txt')
if file_path.exists():  
    with open('example.txt', 'a') as file:
        file.write('This is an additional line added to the file.\n')   
else:    print('The file does not exist.')  

#deleting a file
print('Deleting a file:')

file_path = pathlib.Path('example.txt')
if file_path.exists():
    file_path.unlink()  
    print('The file has been deleted.') 
else:    print('The file does not exist.')


