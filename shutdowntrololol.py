import os
import time
from tkinter import *
root = Tk()
root.title("SAY GOODBYE")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")
text = Label(root, text="TROLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOl")
text.pack()
text2 = Label(root, text="COMPUTER SAY BYE BYE")
text2.pack()
root.mainloop()
print ("BYE BYE")
os.system('shutdown /s')
time.sleep(1)