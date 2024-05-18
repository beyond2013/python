"""
Strings in Python are array
"""

str = "My name is Imran"
print(str)
print("Imran is present in str = ", "Imran" in str)
print("Ali is not in str =", "Ali" not in str)

# looping through a string
for x in str:
    print(x.upper())

# String length
print("length of str = ", len(str))

# String slicing
print(str[len(str)-5:len(str)+5])
print(str[len(str)-5:])
print(str[-5:])

# modifying strings
print("return upper case str", str.upper(), str)
print("return lower case str", str.lower(), str)

# strip leading and trailing whitespace
str="   3 spaces before and 3 after   "
print(str)
print(str.strip())

# replace string
print(str.replace("3", "0"))

# split string
print(str.split("and"))

# concat
print(str + "use + to concatenate two strings")

# format string
age = 45
str = "My name is Imran, and I am {}"
print(str.format(age))

# escape characters 
"""
\'    single quote
\\    backslash
\n    new line
\r    carriage return # see the url below for discussion on the difference between \r and \n
https://stackoverflow.com/questions/1761051/difference-between-n-and-r
\t    tab
\b    backspace
\f    form feed
\ooo  octal value  backslash followed by 3 digits will result in octal value
\xhh  hex value

