# More Tkinter Tips, Tricks & Functions
from tkinter import *

root = Tk()
root.title("More tips")
root.geometry("600x300")
#To set a icon on my GUI
root.wm_iconbitmap("corona.ico")
root.configure(background="red")
#To know the screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"Width {width}\nHeight {height}")

Button(text="Exit",command=root.destroy).pack()



root.mainloop()