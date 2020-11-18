# Canvas Widget In Python Tkinter
from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Bappy ka GUI!")
canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

#The line goes from the point x1,y1 to x2,y2 (like coordinate geometry)
canvas_widget.create_line(0,0, 800,400 ,fill="red")
canvas_widget.create_line(0,400, 800,0 ,fill="red")

#To create a ractangle specify parameter ->> coordinate of top left and coordinate of bottom right
canvas_widget.create_rectangle(200,100 ,400,200 ,fill="blue")

#text
canvas_widget.create_text(400,200,text="Machine Learning")

#oval
canvas_widget.create_oval(10, 10, 200, 100)
root.mainloop()