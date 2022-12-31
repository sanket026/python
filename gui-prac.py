"""# tkinter with widgets

from tkinter import *

window=Tk()
window.title("My APP")
window.geometry("250x250")
b= Button(window,text="First Button")
b.pack()
window.mainloop()"""

# Tkinter with widget 
"""
from tkinter import *

window=Tk()
window.title("My APP")
window.geometry("250x250")

b1=Button(window,text="one",activeforeground="white",activebackground="black",pady=10,padx=50)
b1.pack(side=TOP)
b2=Button(window,text="two",activeforeground="white",activebackground="black",pady=10)
b2.pack(side=RIGHT)
b3=Button(window,text="three",activeforeground="white",activebackground="black",pady=10)
b3.pack(side=BOTTOM)
b4=Button(window,text="four",activeforeground="white",activebackground="black",pady=10)
b4.pack(side=LEFT)                      

window.mainloop()"""

# using of messagebox

from tkinter import * 
from tkinter import messagebox

window = Tk() 
window.geometry("200x100") 
def fun(): 
   messagebox.showinfo("Hello", "WELCOME TO TKINTER") 
b1 = Button(window,text = "SUBMIT ",command = fun)
b1.pack() 
window.mainloop() 
