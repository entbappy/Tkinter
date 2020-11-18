#Displaying Images Using Label

from tkinter import *
#JPG file photo doesn't support in  Tkinter so we use pillow to fix
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x368")
#For PNG photos
# photo = PhotoImage(file="welcome.png")

#For JPG photos
image = Image.open("pic.jpg")

photo = ImageTk.PhotoImage(image)


photo_label = Label(image=photo)
photo_label.pack()
root.mainloop()