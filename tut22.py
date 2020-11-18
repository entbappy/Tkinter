# ScrollBar In Tkinter GUI
from tkinter import *

root = Tk()
root.title("ScrollBar")
root.geometry("600x400")
#For connecting scrollbar to a widget
# 1.widger(yscrollcommand) = Scrollbar.set()
#2.scrollbar.config(command=widget.yview)

#Initializing scrollbar
scrollbar  = Scrollbar()
scrollbar.pack(side=RIGHT,fill=Y)

#Listbox widget
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Added {i}")
listbox.pack(fill=BOTH,padx=23,pady=10)
scrollbar.config(command=listbox.yview)

root.mainloop()