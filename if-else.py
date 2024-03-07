cnic = input("Enter CNIC: \t")
a = len(cnic) == 15
b = cnic[5] == '-'
c = cnic[13] == '-'

if(a and b and c):
	print("Valid cnic")
else :
	print("Invalid cnic")
