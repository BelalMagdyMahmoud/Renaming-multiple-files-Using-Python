import os

for i in range(0,201,1):
# Absolute path of a file
    old_name = r"D:\Belal\ITI\Python\New folder\gag "+str(i)+".txt"
    new_name = r"D:\Belal\ITI\Python\New folder\gaag "+str(i)+".txt"

# Renaming the file
    try:
        os.rename(old_name, new_name)
    except WindowsError:
        print (new_name)

print ("@BelalMagdyMahmoud")
