from tkinter import *

root = Tk()
root.title("ScrollBar")
root.geometry("600x400")

scrollbar  = Scrollbar()
scrollbar.pack(side=RIGHT,fill=Y)

g = Text(root,yscrollcommand=scrollbar.set)
g.pack(fill= BOTH)
scrollbar.config(command=g.yview)

root.mainloop()