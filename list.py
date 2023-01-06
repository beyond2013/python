# lists are one of the four built-in data types used to store
# collections of data

shopping = ["shampoo", "conditioner", "toothpaste"]
print(shopping)

# looping through the list
for item in shopping:
    print(item)

# using list constructor to create list
shopping2 = list( ("tea", "milk", "sugar", "sugar") )

# New items inserted at the end of the list

shopping.append("soap")
print(shopping)

# lists allow duplicate items
shopping.append("soap")
print(shopping)

# one list can store multiple type of data

student = [1, "Hamdullah", 3.5]
print(student)

# list methods
shopping.clear() # removes all the elements from the list

shopping = shopping2.copy() # returns a copy of the list

print("Number of times 'Sugar' appears in the list= ", shopping.count("sugar")) # returns the count of the item

shopping.extend(["shampoo", "conditioner", "toothpaste"]) # adds the list to the end of the current list
print(shopping)

print("index of conditioner = ", shopping.index("conditioner")) # returns the index of the item. index base = 0

shopping.insert(0, "Rice") # insert an element at specified position
print(shopping)

item = shopping.pop(3) # default argument is -1, which removes the last item
print(item, "Removed from shopping")
print(shopping)

shopping.reverse() # Reverses the order of the list
print(shopping)

shopping.sort() # sort the list
print(shopping)
