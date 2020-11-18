# Using Classes And Objects To Create GUIs (oops)
from tkinter import *

class GUI(Tk):
    """
    This is a GUI class using opps 
    """
    def __init__(self): #Here self is the Tk()
        super().__init__() #Have to use the super()
        self.geometry("400x200")
        self.title("GUI using oops")

    #Creating a statusBar
    def statusbar(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.sbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor=W)
        self.sbar.pack(side=BOTTOM,fill=X)

    #Button
    def createbutton(self):
        Button(self,text="Click me",command=self.hello).pack()

    def hello(self):
        print("Hello there!")

if __name__ == "__main__":
    #Objects
    root = GUI()
    root.statusbar()
    root.createbutton()
    root.mainloop()        

