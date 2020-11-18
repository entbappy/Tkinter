from tkinter import *
from PIL import Image, ImageTk
from glob import glob
from tkinter import filedialog

root = Tk()
root.geometry("576x432")

path = filedialog.askdirectory(title='Album') #get the directory path
location1  = glob(f'{path}//*.png') #get the path of all png image

location2 = glob(f'{path}//*.jpg') #get the path of all jpg image
final_loc = location1 + location2 #combine those list to a final main list
print(final_loc) #check the list

i = 0 #set the index value to 0
def show():
    global i #so that the value of i changes on global scope
    try: 
        image1 = Image.open(final_loc[i]) #open the index-th image
        photo1 = ImageTk.PhotoImage(image1)
        photo_label1.config(image=photo1) #using config so the image doesnt overlap
        photo_label1.img = photo1 #keeping a reference
        i += 1 #increasing the index number
    except IndexError: #if no more items in the list to index
        i = 0 #set index back to 0
    finally:
        root.after(2000,show) #keep repeating the function every 2 sec or 2000 ms

photo_label1 = Label(root) #create a label, later to be editeed
photo_label1.pack()

show() #call the function

root.mainloop()
