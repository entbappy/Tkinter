"""
Date: 12-11-2020
Project :Creating A Notepad Using Tkinter
Author : Bappy Ahmed
Email : bappymalik4161@gmail.com
"""
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global files
    root.title("Untitled - Notepad")
    files = None
    textArea.delete(1.0,END)

def openFile():

    global files
    files =  askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    print(files)
    
    if files == "":
       files = None

    else:
        root.title(os.path.basename(files + "- Notepad"))
        textArea.delete(1.0,END)
        f = open(files,"r")
        textArea.insert(1.0, f.read())
        f.close()



def saveFile():
    global files
    print(files)

    if files == None:
        files = asksaveasfilename(initialfile= "Untitled.txt",defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        print(files)
        
        if files =="":
            files = None
        
        else:
            #save as a new file
            f = open(files,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(files + "- Notepad"))
            print("File Saved")
    else:
        #save The  file
        f = open(files,"w")
        f.write(textArea.get(1.0,END))
        f.close()

        
def exitFile():
    root.destroy()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def helps():
    showinfo("Notepad","This notepad was developed in 2020 by Bappy Ahmed!!")



if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("note.ico")
    root.geometry("600x680")

    # Adding text area
    textArea = Text(root,font="luicida 13")
    textArea.pack(expand=True,fill=BOTH)
    files = None

    # Lets create a menubar
    menubar = Menu(root)

    #File menu starts

    fileMenu = Menu(menubar, tearoff=False)
    #To open a new file
    fileMenu.add_command(label="New",command=newFile)
    #To open already existing file
    fileMenu.add_command(label="Open",command=openFile)
    #To save the current file
    fileMenu.add_command(label="Save",command=saveFile)
    #To separate by a line
    fileMenu.add_separator()
    #To exit from notepad
    fileMenu.add_command(label="Exit",command=exitFile)
    #packing fileMenu
    menubar.add_cascade(label="File",menu=fileMenu)
    
    # file menu ends
# *******************************************>>>>>>>>
    #Edit menu starts

    editMenu = Menu(menubar,tearoff=False)
    #To give features of cut,copy & past
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy",command=copy)
    editMenu.add_command(label="Paste",command=paste)
    #Packing editMenu
    menubar.add_cascade(label="Edit",menu=editMenu)
    #Edit menu ends
# *******************************************>>>>>>>>
    # Help menu starts
    helpMenu = Menu(menubar,tearoff=False)
    helpMenu.add_command(label="About Notepad",command=helps)
    # Packing helpMenu
    menubar.add_cascade(label="Help",menu=helpMenu)
    #Help menu ends

    root.config(menu = menubar)
# *******************************************>>>>>>>>
    #Adding Scrollbar
    scrollbar = Scrollbar(textArea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollbar.set)


    root.mainloop()

 



