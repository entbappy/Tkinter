from tkinter import *
from PIL import Image,ImageTk

#This function will make every sentences of 100 character
def make_100(news):
    final_text = ""
    for i in range(0,len(news)):
        final_text += news[i]
        if i%100 == 0 and i!=0:
            final_text += "\n"
    return final_text
    

root = Tk()
root.title("News For Today!!")
root.geometry("1000x800")

news = []
photos = []

for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        texts = f.read()
        news.append(make_100(texts))
    
    images = Image.open(f"{i+1}.jpg")
    #TODO: Resizing images
    images = images.resize((235,235), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(images))

#This is Frame 1
f0 = Frame(root,width =800, height=70)
Label(f0,text="Today's Hottest News!!",font='lucida 33 bold').pack()
Label(f0,text="23 Octobor 2020",font='lucida 15 bold').pack()
f0.pack()

#This is Frame 2
f1 = Frame(root,width=900,height=200,pady=2)
Label(f1,text=news[0],padx=50,pady=52).pack(side="left")
Label(f1,image=photos[0],anchor='e').pack()
f1.pack(anchor="w")

#This is Frame 2
f2 = Frame(root,width=900,height=200,padx=50)
Label(f2,text=news[1],padx=50,pady=52).pack(side="right")
Label(f2,image=photos[1],anchor='e').pack()
f2.pack(anchor="w")

#This is Frame 2
f3 = Frame(root,width=900,height=200)
Label(f3,text=news[2],padx=50,pady=52).pack(side="left")
Label(f3,image=photos[2],anchor='e').pack()
f3.pack(anchor="w")
    
# print(news)
# print(photos)
       

root.mainloop()