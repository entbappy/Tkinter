# Packing Buttons In Tkinter
from tkinter import *

def hello():
    print("Hello world!")

def name():
    print("My name is Tkinter")

def bye():
    print("Good bye!")

root = Tk()
root.geometry("600x400")
frame = Frame(root, borderwidth=2, bg="grey",relief = SUNKEN)
frame.pack(side=LEFT,anchor="nw")
# Button series
bt1 = Button(frame,fg = "red",text="Hit me",command= hello)
bt1.pack(side=LEFT,padx=2)

bt2 = Button(frame,fg = "red",text="Name",command=name)
bt2.pack(side=LEFT,padx=2)

bt3 = Button(frame,fg = "red",text="bye",command=bye)
bt3.pack(side=LEFT,padx=2)

root.mainloop()