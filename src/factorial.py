def factorial(n):
    result = 1
    for j in range(1, n+1):
        result = result * j 
    return result

num = int(input("enter a value to calculate factorial\t"))
print("factorial of ", num, " is ", factorial(num))
