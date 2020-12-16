from tkinter import * 
from PIL import ImageTk,Image 

root = Tk()
root.title("Frame Design using Python")

frame = LabelFrame(root, text="This is my Frame....", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Dont Click Me!")
b2 = Button(frame, text=".... or here!")

b.grid(row=0, column=0)
b2.grid(row=1, column=1)



root.mainloop()