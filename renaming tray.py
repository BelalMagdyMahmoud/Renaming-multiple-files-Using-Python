import os

# Declaring variables
i = 0
j = 1
path="D:/Belal/Test/"

for filename in os.listdir(path):       
# Path of a files with exception numbers
        old_name = path + filename
        new_name = path + "URRC054_Tray_No."+str(j)+"_"+str(i)+"m-"+str(i+20)+"m.jpg"
 
# Excuting the rename and increamintation
        try:
            os.rename(old_name, new_name)
            i += 20
            j += 1
        except WindowsError:
            print ("error renaming "+filename)

print ("@BelalMagdyMahmoud")
