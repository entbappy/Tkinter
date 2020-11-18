# Entry Widget & Grid Layout In Tkinter
from tkinter import *

def getval():
    print(uservalue.get())
    print(passvalue.get())

root = Tk()
root.geometry("600x400")
user  =  Label(root,text="Username:")
password = Label(root,text="Password:")
user.grid()
password.grid(row=1)

# Variable Classes in tkinter
# BooleanVar,
# DoubleVar,
# IntVar,
# StringVar

#Entry Widget
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text = "Submit",command = getval).grid()

root.mainloop()