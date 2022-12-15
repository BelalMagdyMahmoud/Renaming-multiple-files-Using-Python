import os

# Declaring variables
i = 0
j = 1
path="D:/Belal/Test/"

for filename in os.listdir(path):       
# Path of a files with exception numbers
        old_name = path + filename
        if j in [5,10,15,20,25,30,35]:
            j += 1
        new_name = path + "URRC054_RC005348"+str(j)+"_"+str(i)+"m-"+str(i+1)+"m.jpg"
 
# Excuting the rename and increamintation
        try:
            os.rename(old_name, new_name)
            i += 1
            j += 1

        except WindowsError:
            print ("error renaming "+filename)

print ("@BelalMagdyMahmoud")
