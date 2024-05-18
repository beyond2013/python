# Set is a collection used to store multiple items. 
# Set type is unordered, unchangeable, unindexed, duplicates not allowed

names = {"imran", "fahad", "furqan", "hamdullah"}
print("names set : ",  names)

# Set items type
# Set items can be of any type string, int, bool, 
# and a set can contain items of different data types

set1 = {"Imran", 45, 78.5, True}
print("set1: ", set1)

# Create set using set constructor
print("\n=========================================\n")
set2 = set( ("Fahad", 28, 60.0, True) )
print("set2: ", set2)

# Access set items: cannot use index
print("\n=========================================\n")
print("Use 'in' to check set membership")
print("imran in names = ", "imran" in names)

# Add items to a set
print("Use set.add('member') to add items to the set")
names.add("Siraj")

# Remove set items
# 1. remove() will raise an error if the item is not in the set
# 2. discard() will not raise error 

print("\n=========================================\n")
#names.remove("Ghulam")
names.discard("Ghulam")
names.remove("hamdullah")
print("After removing hamdullah names = ", names)

# Loop sets
print("\n=========================================\n")
print("Using for loop to print set")
for x in names:
    print(x)

# Join sets
print("\n=========================================\n")
Furqan = {"Islamic History", "English Literature", "Sociology"}
Fahad = {"Islamic History", "International Relations", "Persian"}

FahadUnionFurqan = Fahad.union(Furqan)
print("Fahad = ", Fahad)
print("Furqan= ", Furqan)
print("Joining Furqan and Fahad sets = ", FahadUnionFurqan)

# Update
print("\n=========================================\n")
print("A.update(B) inserts the items of the set B into set A excluding duplicates- A will be modified")
Furqan = {"Islamic History", "English Literature", "Sociology"}
Fahad = {"Islamic History", "International Relations", "Persian"}
print("Fahad: ", Fahad)
print("Furqan: ", Furqan)
Fahad.update(Furqan)
print("Fahad: ", Fahad)
print("Furqan: ", Furqan)

# intersection_update()
print("\n=========================================\n")
print("To get the duplicate items of sets A and B,  use A.intersection_update(B)")
Fahad = {"Islamic History", "International Relations", "Persian"}
print("Fahad = ", Fahad)
print("Furqan= ", Furqan)
Fahad.intersection_update(Furqan)
print("Fahad.intersection_update(Furqan) results in changing Fahad to ", Fahad)


# intersection()
print("\n=========================================\n")
Fahad = {"Islamic History", "International Relations", "Persian"}
print("Fahad = ", Fahad)
print("Furqan= ", Furqan)
CommonCourses = Fahad.intersection(Furqan)
print("using Fahad.intersection(Furqan) returns new set having CommonCourses: ", CommonCourses)

# To keep all items except the duplicates 

print("\n=========================================\n")
Furqan = {"Islamic History", "English Literature", "Sociology"}
Fahad = {"Islamic History", "International Relations", "Persian"}
print("Fahad = ", Fahad)
print("Furqan= ", Furqan)
Fahad.symmetric_difference_update(Furqan)
print("After calling Fahad.symmetric_difference_update(Furqan)")
print("Fahad = ", Fahad)
print("Furqan= ", Furqan)

# symmetric_difference
print("\n=========================================\n")
Furqan = {"Islamic History", "English Literature", "Sociology"}
Fahad = {"Islamic History", "International Relations", "Persian"}
print("Fahad = ", Fahad)
print("Furqan= ", Furqan)
DistinctCourses= Furqan.symmetric_difference(Fahad)
print("Furqan.symmetric_difference(Fahad)= ", DistinctCourses)

# copy()
print("\n=========================================\n")
print("Use A.copy() to get a copy of set A")
copyFurqan = Furqan.copy() 
print("Furqan.copy() returns:", copyFurqan)

# issubset and issuperset
print("\n=========================================\n")
print("Using issubset an issuperset ")
A = {1,2,3}
B = {1,2,3,4}
print("A: ", A)
print("B: ", B)

print("A is the subset of B", A.issubset(B))
print("B is the subset of A", B.issubset(A))

print("A is the superset of B", A.issuperset(B))
print("B is the superset of A", B.issuperset(A))

# isdisjoint
print("\n=========================================\n")
print("Use isdisjoint to find if two sets do not overlap")
C = {4, 5,6,7}
print("A: ", A)
print("B: ", B)
print("C: ", C)
print("A and C are disjoint sets: ", A.isdisjoint(C))
print("B and C are disjoint sets: ", B.isdisjoint(C))
