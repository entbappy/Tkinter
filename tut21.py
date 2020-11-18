# ListBox In Tkinter
from tkinter import *
import tkinter.messagebox as tmsg


def addItem():
    global i
    L_box.insert(ACTIVE ,f"Added {i}")
    i += 1

i = 0
root = Tk()
root.title("Box List")
root.geometry("400x200")

L_box = Listbox(root)
L_box.pack()
L_box.insert(END,"First item in the list")
Button(root,text="Add Item",command=addItem).pack()
root.mainloop()
