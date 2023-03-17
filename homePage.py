from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import fill, checkPrice

set_appearance_mode('system')
set_default_color_theme('green')

def fillRedirect(hWin):
    hWin.destroy()
    fill.fillPage()
    
def priceCheck(hWin):
    hWin.destroy()
    checkPrice.CheckPrice()
    
def HomePage():
    hWin = CTkToplevel()
    hWin.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = hWin.winfo_screenwidth()
    SH = hWin.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    hWin.geometry('%dx%d+%d+%d' %(WW, WH, x, y))

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(hWin, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = hWin)
    frame.pack(pady=60, padx=60, expand=True)

    label = CTkLabel(master=frame, text='User Menu', font=('Impact', 28))
    label.pack(pady=25, padx=70)

    filling = CTkButton(master=frame, text='Fill Fuel', font=('Arial Rounded MT Bold', 18), width=162, height=30, command=lambda : fillRedirect(hWin))
    filling.pack(pady=6, padx=10)

    checkPrice = CTkButton(master=frame, text='Check Price', font=('Arial Rounded MT Bold', 18), width=162, height=30, command=priceCheck)
    checkPrice.pack(pady=6, padx=10)

    label = CTkLabel(master=frame, text='', font=('Impact', 26))
    label.pack(pady=2, padx=40)


    hWin.mainloop()
