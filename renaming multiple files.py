import os

for i in range(0,200,1):
# Absolute path of a file
    old_name = r"D:\Belal\ITI\Python\New folder\gaag "+str(i)+".txt"
    new_name = r"D:\Belal\ITI\Python\New folder\gag "+str(i)+".txt"

# Renaming the file
    try:
        os.rename(old_name, new_name)
    except WindowsError:
        print (old_name)

print ("@BelalMagdyMahmoud")
