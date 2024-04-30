import os
import time
print ("WARNING")
time.sleep(0.5)
print("THIS SOFTWARE CAN DO DAMAGE TO UNSAVED SOFTWARE")
time.sleep(0.5)
print("THE CREATOR IS IN NO WAY LIABLE FOR ANY DAMAGES CAUSED BY THIS SOFTWARE")
time.sleep(0.5)
print("BY CONTINUING YOU ARE UNDERSTANDING THE RISKS INVOLVED")
time.sleep(0.5)
start = input ("Do you wish to continue? (Y/N)")
def mainStart():
    if start == ("Y"):
        print("Starting")
        os.system('cls')
        os.system('shutdown /s')
        time.sleep(1)
    elif start == ("N"):
        print("Canceled")
        time.sleep(1)
        os.system('exit')
    elif start == ("y"):
        print("Starting")
        os.system('cls')
        os.system('shutdown /s')
        time.sleep(1)
    elif start == ("n"):
        print("Canceled")
        time.sleep(1)
        os.system('exit')
    else:
        print ("Incorrect Command")
        mainStart()