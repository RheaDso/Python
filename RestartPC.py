import os
choice = input("Restart your computer? (y or n): ")
if choice == "y" or choice =="Y":
    os.system("shutdown /r /t 1")
else:
    exit()    