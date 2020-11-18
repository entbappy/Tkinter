# Handling Events In Tkinter GUI 
from tkinter import *

def bappy(event):
    print(f"You clicked on the button at {event.x} {event.y}")

root = Tk()
root.title("Event in Tkinter")
root.geometry("600x300")

widget = Button(root,text="Click me please")
widget.pack()
widget.bind('<Button-1>',bappy)
widget.bind('<Double-1>',quit)

root.mainloop()