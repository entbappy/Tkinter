"""
Date: 10-11-2020
Project :Creating A Calculator Using Tkinter
Author : Bappy Ahmed
Email : bappymalik4161@gmail.com
"""
 
from tkinter import *

#Button function
def click(event):

    global str_var

    text = event.widget.cget("text") #Getting button value
    print(text)

    if text == "=":
        if str_var.get().isdigit():
            value = int(str_var.get())
            print(type(value))
        else:
            try:
                value = eval(str_var.get())
            except Exception as e:
                print(e)
                value = "Syntax Error!"


        str_var.set(value)
        screen.update()    

    
    elif text == "C":
        str_var.set("")
        screen.update()
    
    else:
        str_var.set(str_var.get() + text)
        screen.update()

#Initializing tkinter
root = Tk()
root.geometry("300x592")
root.title("Calculator by Bappy")
root.wm_iconbitmap("cal.ico")

#String variable
str_var = StringVar()
str_var.set("")

#Entry widget
screen = Entry(root,textvar=str_var,font="lucica 33 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

#Frame and button 1
f = Frame(root,bg='grey')
#button
b = Button(f,text="9",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="7",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

#Frame and button 2 
f = Frame(root,bg='grey')
#button
b = Button(f,text="6",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="4",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

#Frame and button 3
f = Frame(root,bg='grey')
#button
b = Button(f,text="3",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="1",padx=10,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

#Frame and button 4
f = Frame(root,bg='grey')
#button
b = Button(f,text="0",padx=12,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx=12,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="*",padx=12,pady=1,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

#Frame and button 5
f = Frame(root,bg='grey')
#button
b = Button(f,text="/",padx=14,pady=1,font="lucica 26 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="%",padx=8,pady=1,font="lucica 26 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="+",padx=10,pady=0,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

#Frame and button 6
f = Frame(root,bg='grey')
#button
b = Button(f,text="C",padx=9,pady=0,fg="red",font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx=10,pady=0,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text=".",padx=10,pady=0,font="lucica 28 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()
