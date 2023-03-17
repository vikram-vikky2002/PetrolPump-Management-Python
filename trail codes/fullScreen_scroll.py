from tkinter import *
from tkinter import ttk
from customtkinter import *

root = CTk()
root.title('Scroll')
root.geometry('500x400')



for thing in range(100):
    CTkButton(root, text=f'Button {thing} Yo!').grid(row=thing, column=0)
    
root.mainloop()