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

