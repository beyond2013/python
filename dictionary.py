# Dictionaries are used to store data values in key: value pairs
# Dictionary is a collection which is ordered, changeable and do not allow duplicates

# Dictionaries are written with curly brackets 

mycar = {
        "make": "Suzuki",
        "name": "Alto",
        "color": "white",
        "Engine Capacity": 1000,
        "model": 2010
        }

print("Using print to display dictionary mycar\n", mycar)

print("\n")
# Use square brackets to refer to dictionary items
print("Use square brackets to refer to dictionary items")
print("mycar[\"color\"]: ", mycar["color"])
print("\n")

print("Dictionaries cannot have two items with the same key")
print("\n")

# Use len() to find how many items a dictionary has
print("Use len() to find how many items a dictionary has")
print("len(mycar): ", len(mycar))
print("\n")

# The values in dictionary items can be of any data type, even lists
print("""The values in dictionary items can be of any data type, even tuple, sets, lists, e.g. \n
Mehran = {
        "make": "Suzuki",
        "variants": ("VX", "VXR"), #tuple
        "year": {1990,1991,1992}, # set
        "color": ["white", "silver", "golden"] # list
        } \n 
        """)

Mehran = {
        "make": "Suzuki",
        "variants": ("VX", "VXR"), #tuple
        "year": {1990,1991,1992}, # set
        "color": ["white", "silver", "golden"] # list
        } 
print(Mehran)

print("==========================================\n")
print("""Dictionaries can even be nested
Suzuki = {
        "800cc": {
          "name": "Mehran",
          "variants": ("VX", "VXR")
          },
        "1000cc": {
            "name": "Alto",
            "variants": ("VX","VXR", "VXL")
            }
        }
""")
Suzuki = {
        "800cc": {
          "name": "Mehran",
          "variants": ("VX", "VXR")
          },
        "1000cc": {
            "name": "Alto",
            "variants": ("VX","VXR", "VXL")
            }
        }
print(Suzuki)


print("==========================================\n")
print("""
        Use dict() constructor to make a dictionary as follows:

        Mehran2 = dict( make= "Suzuki",
        variants= ("VX", "VXR"), #tuple
        year= {1990,1991,1992}, # set
        color= ["white", "silver", "golden"] # list
        ) 
""")
Mehran2 = dict(make = "Suzuki",
        variants = ("VX", "VXR"), #tuple
        year = {1990,1991,1992}, # set
        color = ["white", "silver", "golden"] # list
        )
print(Mehran2)

print("==========================================\n")

# Accessing Items: use key name in square brackets

print("Mehran2['make']= ", Mehran2["make"])

print("Mehran2.get('make')=", Mehran2.get('make'))

print("==========================================\n")
# keys() method returns a list of all the keys in the dictionary
print("keys() method returns a list of all the keys in the dictionary ")
print("Mehran2.keys(): ", Mehran2.keys())

print("==========================================\n")
x = Mehran2.keys()
print("x = Mehran2.keys()")
print("x before modifying dictionary", x)
Mehran2['transmission']='manual'
print("Mehran2['transmission']='manual' ")
print("x after modifying dictionary ", x) 

print("==========================================\n")
print("The values() method returns a list of all the values in the dictionary")
x = Mehran2.values()
print("x = Mehran2.values()")
print("x= ", x)
print("Any change in dictionary will also be reflected in x")

print("==========================================\n")
print("The items() method returns each item in a dictionary, as tuples in a list")
x = Mehran2.items()
print("x = Mehran2.items()")
print("x = ", x)
print("Any change in dictionary will also be reflected in x")

print("==========================================\n")
print("Use the in keyword to check if a key exists in dictionary")
print("\"color\" in Mehran2 = ", "color" in Mehran2)

print("==========================================\n")
print("change values of a specific item by referring to its key")
print(mycar)
print("mycar[\"model\"] = 2011 to change model of my car to 2011")
mycar["model"] = 2011
print(mycar)

print("==========================================\n")
print("use the update(dict) method to update dictionary") 
print("for adding transmission: manual and assembly: local to mycar")
print("mycar.update({\"transmission\": \"manual\", \"assembly\": \"local\"})") 
mycar.update({"transmission": "manual", "assembly": "local"})
print(mycar)

print("==========================================\n")
print("Remove items using the pop(key) method")
print("mycar.pop(\"assembly\")")
mycar.pop("assembly")
print(mycar)


print("==========================================\n")
print("popitem() removes the last inserted item")
mycar.popitem()
print("mycar after calling popitem()", mycar)


print("==========================================\n")
print("the del keyword removes the item with the specified key name")
print("del mycar[\"make\"]")
del mycar["make"]
print(mycar)

print("==========================================\n")
print("the del keyword can also delete the dictionary completely")
print("del mycar")
del mycar
#print("trying to refer to mycar after del mycar", mycar)

print("==========================================\n")
print("clear() method empties the dictionary")
print("Suzuki dictionary before calling clear()", Suzuki)
print("printing Suzuki after calling Suzuki.clear()", Suzuki.clear(), Suzuki)


print("==========================================\n")
print("Loop through a dictionary")
print("When looping through dictionary the return value are the keys")
print("Mehran:", Mehran)
print("Looping through mehran using for loop")
print("""
        for x in Mehran:
          print(x)
     """)
for x in Mehran:
    print(x)

print("==========================================\n")
print("using loop to print values of a dictionary one by one")
print("""
        for x in Mehran:
          print(Mehran[x])
     """)

for x in Mehran:
    print(Mehran[x])

print("\nanother way to loop through dictionary values")
print("""
        for x in Mehran.values():
          print(x)
     """)

for x in Mehran.values():
    print(x)
