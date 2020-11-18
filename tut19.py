# Sliders In Tkinter Using Scale() 
from tkinter import *
import tkinter.messagebox as tmsg

def get_dollars():
    print(f"You got {myslider.get()} dollars to your bank account!")
    tmsg.showinfo("Congratulation!",f"You got {myslider.get()} dollars to your bank account!")

root = Tk()
root.geometry("400x200")
root.title("Slider")
#Vertical Slider
# myslider = Scale(root,from_=0,to_=100)
# myslider.pack()

#Horizontal Slider
Label(root,text="How much dollars do you want?").pack()
myslider = Scale(root,from_=0,to_=100,orient=HORIZONTAL,tickinterval=50)
# myslider.set(10)
myslider.pack()
Button(root,text="Get dollars!",fg="red",command=get_dollars).pack()


root.mainloop()