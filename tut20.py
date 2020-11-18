# Creating RadioButtons In Tkinter 
from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.title("Radio Button")
root.geometry("400x200")

def order():
    print(f"Got it {var.get()}")
    tmsg.showinfo("Your order is confirmed!",f"Thanks! We have recieved your order of {var.get()}")

# var = IntVar()
var = StringVar()
var.set("radio")
# var.set(1)
Label(root,text="What do you want to have sir?",font="luicida 19 bold",justify=LEFT,pady=15).pack()
radio = Radiobutton(root,text="Pizza",padx=15,variable=var,value="Pizza").pack(anchor="w")

radio = Radiobutton(root,text="Paratha",padx=15,variable=var,value="Paratha").pack(anchor="w")

radio = Radiobutton(root,text="Samosa",padx=15,variable=var,value="Samosa").pack(anchor="w")

radio = Radiobutton(root,text="Chicken",padx=15,variable=var,value="Chicken").pack(anchor="w")

Button(root,text="Order Now!",command=order).pack()
root.mainloop()