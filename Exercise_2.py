#Create a GUI which takes an input of width and height from user
# and according to the input it changes the size of GUI

from tkinter import *


def getval():
    s_width = sizeOf_width.get()
    s_height = sizeOf_height.get()
    root.geometry(f"{s_width}x{s_height}")

root = Tk()
root.title("Window Changer")
root.geometry("300x200")

# Label
Label(root,text="Window Resizer!",font="comicsansms 13 bold",pady=3).grid(row=0,column=3)
W = Label(root,text="Enter The Width")
H = Label(root,text="Enter The Height")

# Label grid
W.grid(row=1,column=2)
H.grid(row=2,column=2)

#Variable Classes
sizeOf_width = StringVar()
sizeOf_height = StringVar()

#Entry Widget
width = Entry(root,textvariable=sizeOf_width)
height = Entry(root,textvariable=sizeOf_height)

#packing Entry
width.grid(row=1,column=3)
height.grid(row=2,column=3)

#Button and packing
Button(text="Apply",fg="red",command=getval).grid(row=3,column=3)
root.mainloop()