# Learning Objective : Label, Geometry, Maxsize & Minsize

from tkinter import *

#Tkinter Object
root = Tk()

# GUI logic
#Height X Width
root.geometry("733x433")

#Width,Height
root.minsize(200,100)
#Width,Height
root.maxsize(1200,800)

#Label
bappy = Label(text="Hello I am Bappy.")
bappy.pack()


#Event loop
root.mainloop()