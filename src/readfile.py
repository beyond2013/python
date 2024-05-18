"""
Following code assume that a text file "sample.txt" exists
in the same folder as this file.

The code shows how to read a file 
"""

try:
    f = open("sample.txt", "r") # to specify file located elsewhere use 
                                # path of the file with its name
    # print(f.read())             # read also take arguments of type int

    # print(f.read(10))           # try f.read(10)
    print(f.readline())          # use readline() to read a complete line
except:
    print("Could not find file")
finally:
    f.close()




"""
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
