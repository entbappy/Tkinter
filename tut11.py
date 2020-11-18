# Registation Form Using Checkbuttons & Entry Widget 
from tkinter import *

# Data Collector function
def getval():
    # print(nameval.get())
    # print(professionval.get())
    # print(sexval.get())
    # print(phoneval.get())
    # print(paymentval.get())
    # print(agreeval.get())
    data = {
        "Name":nameval.get(),
        "Profession":professionval.get(),
        "Sex":sexval.get(),
        "Phone":phoneval.get(),
        "Payment":paymentval.get(),
        "Agree":agreeval.get()}

    with open("tkinterData.txt","a") as f:
        for item,value in data.items():
            f.write(f"{item}:{value}\n")
        f.write("\n")
    print("ok")



root = Tk()
root.geometry("600x300")

#Title Label
Label(root,text="Welcome to Machine Learning!",font="comicsansms 13 bold",pady=15).grid(row=0, column=3)

#Label
name = Label(root,text="Name")
profession = Label(root,text="Profession")
sex = Label(root,text="Sex")
phone = Label(root,text="Phone")
payment = Label(root,text="Payment Mode")

#Label Grid
name.grid(row=1 , column=2)
profession.grid(row=2 , column=2)
sex.grid(row=3 , column=2)
phone.grid(row=4, column=2)
payment.grid(row=5 , column=2)

# Variable Classes
nameval = StringVar()
professionval = StringVar()
sexval = StringVar()
phoneval = StringVar()
paymentval = StringVar()
agreeval = IntVar()

#Entry Widget
nameentry = Entry(root,textvariable=nameval)
professionentry = Entry(root,textvariable=professionval)
sexentry = Entry(root,textvariable=sexval)
phoneentry = Entry(root,textvariable=phoneval)
paymententry = Entry(root,textvariable=paymentval)

# Entry grid
nameentry.grid(row=1 , column=3)
professionentry.grid(row=2 , column=3)
sexentry.grid(row= 3, column=3)
phoneentry.grid(row= 4, column=3)
paymententry.grid(row=5 , column=3)

# Checkbutton/Checkbox
agree = Checkbutton(text = "Are you agree?",variable=agreeval)
agree.grid(row=6, column=3)

#Button and packing it
Button(text ="Submit",fg="red",command=getval).grid(row=7,column=3)

root.mainloop()