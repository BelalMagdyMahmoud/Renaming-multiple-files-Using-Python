import os

for i in range(2,500):
# Absolute path of a file
    old_name = r"D:\Belal\ITI\Python\New folder\New Text Document - Copy ("+str(i)+").txt"
    new_name = r"D:\Belal\ITI\Python\New folder\huh "+str(i)+".txt"

# Renaming the file
    try:
        os.rename(old_name, new_name)
    except WindowsError:
        print (old_name)
