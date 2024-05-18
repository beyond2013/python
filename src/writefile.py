try:
    f = open("sample.txt", "a")
    f.write("this line has been added to the file by writefile.py\n")
except:
    print("Could not open file sample.txt")
finally:
    f.close()

