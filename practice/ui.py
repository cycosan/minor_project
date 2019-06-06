from tkinter import *
import os
root=Tk()
root.configure(background="white")
def dataset():
	os.system("py data_set.py")

def trainer1():
	os.system("py trainer.py")	
	
def reconize():
	os.system("py reconize.py")
	
def exit():
	root.destroy()


root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=dataset).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=trainer1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Recognizer",font=("times new roman",20),bg="#0D47A1",fg='white',command=reconize).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Exit",font=("times new roman",20),bg="green",fg='black',command=exit).grid(row=6,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
root.mainloop()