from tkinter import *
from PIL import ImageTk, Image 


root = Tk()
root.title("Learn how to Create new Windows GUI with Tkinter")
# root.iconbitmap("path")


def open():
	global my_img 
	top = Toplevel()
	top.title("The new Window Title")
	# top.iconbitmap("path")
	# label = Label(top, text="hello World").pack()
	my_img = ImageTk.PhotoImage(Image.open("pic1.jpg"))
	my_label = Label(top, image=my_img).pack()

	btn2 = Button(top, text="close window", command=top.destroy)

btn = Button(root, text="Open Second Window", command=open)
btn.pack()


mainloop()