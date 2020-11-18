# Frame In Tkinter
from tkinter import *

root = Tk()
root.geometry("655x322")
#Frame 1
f1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
l = Label(f1,text="Hello Bappy Sir.py")
l.pack(pady=142)

#Frame 2
f2 = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l2 = Label(f2,text="Welcome to - PyCharm",font="Helvetica 16 bold",fg="red")
l2.pack()






root.mainloop()