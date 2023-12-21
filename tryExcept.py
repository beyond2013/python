# Code that causes exception without try block
# for x in range(10, -1, -2):
#     print(7/x)

# place a block of code in try if it has potential to cause an exception / error
for x in range(10, -1, -2):
    try:
        print(7/x)
    except:
        print("Division by zero")


