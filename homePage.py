from tkinter import Label
from customtkinter import *
from PIL import ImageTk

def Homepage():
    hWin = CTk()
    hWin.resizable(width= False, height= False)
    hWin.geometry('732x488')
    
    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(hWin, image = bg)
    label1.place(x = 0, y = 0)
    
    hWin.mainloop()
    