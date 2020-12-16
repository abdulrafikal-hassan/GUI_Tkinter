from tkinter import * 
from tkinter import messagebox 
from PIL import ImageTk, Image 

root = Tk()
root.title('Learn To Build GUI in Python with TK()')
# root.iconbitmap('path')
# types of mssgbox showinfo, showerror, askquestion, askokcancel, askyesno 
def popup():
	# 1st type mssg box
	messagebox.showinfo("This is my Popup", "Hello World!")
	messagebox.showwarning("This type is for warning", "warning message")
	messagebox.showerror("This is an error mssgbox", "error box python")
	messagebox.askyesno("This is Yes/No mssgbox", "yes or no")
	messagebox.askokcancel("This is Ok cancle prompt", "Ok or cancle option")

def prompt():
	response = messagebox.askyesno("This is my popup", "here i come!")
	# Label(root, text=response).pack() This shows the result in Bool
	if response == 1:
		Label(root, text="You clicked Yes").pack()
	else:
		Label(root, text="You clicked No").pack()


Button(root, text="Prompt", command=prompt).pack()

Button(root, text="Popup", command=popup).pack()



mainloop()