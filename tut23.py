# Status Bar In Tkinter
from tkinter import *
import time

def upload():
    statusvar.set("Please wait...")
    sbar.update()
    time.sleep(2)
    statusvar.set("Uploaded done!!")
    sbar.update()
    time.sleep(2)
    statusvar.set("Python 3.7")

root =Tk()
root.title("StatusBar")
root.geometry("600x300")

statusvar = StringVar()
statusvar.set("Python 3.7")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(side= BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()

root.mainloop()
