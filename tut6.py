# Attributes Of Label & Pack 
from tkinter import *

root = Tk()
root.geometry("550x200")
root.title("Elon Musk")
# important label option

# text -> Add text
# bd -> Backgroung
# fg -> foreground
# font -> set the font
# padx -> x padding
# pady -> y padding
# relief -> Border style - SUNKEN,RAISED,GROOVE,RIDGE

title_label = Label(text='''Elon Reeve Musk FRS is a business magnate, 
 industrial designer,
 engineer, and philanthropist. He is the founder, CEO, CTO 
 and chief designer of SpaceX; early investor, CEO and product 
 architect of Tesla, Inc.; founder of The Boring Company; co-founder 
 of Neuralink; and co-founder and initial 
 co-chairman of OpenAI.''', bg='red',fg='white',
 padx = 23,pady=22,font=('comicsansms',12,"bold"),borderwidth=5,relief=SUNKEN)

 #Important pack Options

#  anchor -> nw,ne
# side -> top,bottom,left, right
# fill 
# padx
# pady

# title_label.pack(side=BOTTOM ,anchor ="nw",fill=X)
title_label.pack(side=LEFT ,fill=Y,padx=21,pady=22)
root.mainloop()
