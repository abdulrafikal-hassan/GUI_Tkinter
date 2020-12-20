from tkinter import * 
from PIL import ImageTk, Image 



""" 
This uses the slider property 
to resize the window of the program.

Without the arg in the slide function it wont resize auto, 
and will give an error.
the click button will work error free if there is no par in the slide function

"""


root = Tk()
root.title('Making Sliders with Python Tkinter')
# root.iconbitmap('path')
root.geometry("400x400")

def slide():
	my_label = Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x"+ str(vertical.get()))


vertical = Scale(root, from_=0, to=500, command=slide)
vertical.pack()

horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL, command=slide)
horizontal.pack()

# new_label = Label(root, text=horizontal.get()).pack()


my_btn = Button(root, text="Resize!", command=slide).pack()


root.mainloop()