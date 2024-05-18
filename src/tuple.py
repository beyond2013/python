# Tuple is a collection which is 
# i. ordered,
# ii. unchangeable,
# iii. and allow duplicate values

students = ("Fahad", "Furqan", "Hamdullah")
print("Tuple students:" , students)
students.add("Imran")

# changing students to a list
list_student = list(students)

print("Type of list_student: ", type(list_student))
# to get the length of a tuple use len function

print("Lenght of students tuple", len(students))

# Creating tuple with one item

Instructor = ("Imran", )
print(Instructor)

# Tuple Items can be of any type and one tuple can store multiple types

student = ("Furqan", "BSIT", 2020, 3.9)
print(student)
print(type(student))

# possible to create tuple using constructor

learners = tuple( ("Imran", "Furqan", "Fahad", "Hamdullah") )
print(learners)

# Access tuple Items using index number inside square brackets

print(learners[2])

# Negative indexing is supported
print(learners[-1])

# A range can be used to get items of tuple
print("Accessing tuples using range: ", learners[1:4])

# to check if an item exists
if "Imran" in learners:
    print("Imran is also among learners")

# unpack a tuple

(w, x, y, z) = learners
print(w)
print(z)

# Asterisk can be used to assign values as a list when unpacking

(ustad, *shagird) = learners
print("Ustad: ", ustad)
print("Shagird: ", shagird)
print("Type of shagird= " , type(shagird))
# Loop through a tuple
for x in learners:
    print(x)

# Using index number to loop through tuple

for i in range(len(learners)):
    print(i,"\t", learners[i])

# Using while loop 
i=0
while i < len(learners):
    print(i+1, learners[i])
    i+=1

# To get the count of a specific value in a tuple
print("Fahad occurs ", learners.count("Fahad"), " times in learners")

# To get the index of a specific value in a tuple
print("Fahad occurs at index ", learners.index("Fahad"))
