"""
  binarySearch(A, target)
  mid = floor((hi + lo)/2)
  while(mid != lo or mid != hi):
     if(A[mid] < target):
       lo = mid + 1
     elif(A[mid] > target):
       hi = mid - 1
     else:
       print("item found")
       break
     mid = floor((hi + lo)/2)
"""
import math

Alist = [4,6,8,10,12,14,16,18,20]

def binarySearch(A, target):
 hi = len(A) 
 lo = 0
 mid = math.floor(( hi + lo )/2)
 while(hi >= lo  ):
   # print("hi = ", hi, " lo = ", lo, " mid = ", mid)
   if(A[mid] < target):
       lo = mid + 1
   #    print("inside if", "hi = ", hi, " lo = ", lo)
   elif(A[mid] > target):
       hi = mid - 1
   #    print("inside elif", "hi = ", hi, " lo = ", lo)
   elif(A[mid]==target):
       print(target, " found ", " at location " , mid)
       break
   mid = math.floor((hi + lo)/2)
 if(hi < lo):
   print(target, " not present in list: ", A)

choice = 1
while(choice == 1): 
  print("Alist contains: ", Alist)
  search = int( input("Enter a number to search\t") )
  binarySearch(Alist, search)
  choice = int( input("Press 1 to run the search again\t") )

