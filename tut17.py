# Menus & Submenus In Tkinter Python 
from tkinter import *
root =Tk()
root.title("VS Code")
root.geometry("600x300")

def func1():
    print("Hello I am an Function")

#Menu widget
#Use them to create a non drop down menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=func1)
# mymenu.add_command(label="Exit",command=quit)
# #Packing method of menu
# root.config(menu=mymenu)

# To create a drop down menubar
dropmenu = Menu(root)
m1 = Menu(dropmenu,tearoff=0)
m1.add_command(label="Open",command=func1)
m1.add_command(label="Save",command=func1)
#To draw a separator line
m1.add_separator()
m1.add_command(label="Save as",command=func1)
m1.add_command(label="Print",command=func1)

root.config(menu=dropmenu)
dropmenu.add_cascade(label="File",menu=m1)

#Edit menu
m2 = Menu(dropmenu,tearoff=0)
m2.add_command(label="Undo",command=func1)
m2.add_command(label="Redo",command=func1)
m2.add_command(label="Copy",command=func1)
m2.add_command(label="Past",command=func1)

root.config(menu=dropmenu)
dropmenu.add_cascade(label="Edit",menu=m2)



root.mainloop()

