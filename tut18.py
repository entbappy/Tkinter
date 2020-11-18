# Message Box In Tkinter Python

from tkinter import *
import tkinter.messagebox as tmsg

root =Tk()
root.title("VS Code")
root.geometry("600x300")

def func1():
    print("Hello I am an Function")
   
# Message Box
def helps():
    print("I will help you")
    tmsg.showinfo("Help!","Bappy will help you with this GUI")

# Message Box
def rate():
    print("Rate us")
    val = tmsg.askquestion("How was your experience?","Did you enjoy using this GUI?")
    print(val)
    if val == "yes":
        msg = "Great!! Rate us on playstore app please. "
    else:
        msg = "Please tell us what went wrong! we will fix it soon."
    tmsg.showinfo("feedback!",msg)

def ellen():
    con = tmsg.askretrycancel("Be friend with Ellen","Ellen is not gonna be your friend") 
    print(con)
    if con:
        print("Nope!! She doesn't want to be your friend")
    else:
        print("Well done! You refused")



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

# for m3
m3 = Menu(dropmenu,tearoff=0)
m3.add_command(label="Help",command=helps)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Ellen",command=ellen)
root.config(menu=dropmenu)
dropmenu.add_cascade(label="Help",menu=m3)



root.mainloop()

