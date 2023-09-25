fileptr = open("newfile.txt", "x")
print(fileptr)
if fileptr:
    print("File created successfully")

fileptr.close()