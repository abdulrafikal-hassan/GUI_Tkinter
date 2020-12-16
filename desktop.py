from tkinter import * 

root = Tk()


#1. Creating a label Widget 
myLabek1 = Label(root, text="Hello From TKinter")
myLabek2 = Label(root, text="My name is Abdul Rafik")
myLabel3 = Label(root, text="")



# 2.Showing it onto screen 
myLabek1.grid(row=0, column=0)
myLabek2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()