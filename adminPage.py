from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import fill, changeCost

set_appearance_mode('system')
set_default_color_theme('green')

def updateQty(adminWindow):
    adminWindow.destroy()
    fill.fillPage()
    

def updatePrice(adminWindow):
    adminWindow.destroy()
    changeCost.updateRate()


def admin():
    adminWindow = CTkToplevel()
    adminWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = adminWindow.winfo_screenwidth()
    SH = adminWindow.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    adminWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(adminWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = adminWindow, height=200, width=6000)
    frame.pack(pady=60, padx=60, expand=True)
    
    label = CTkLabel(master=frame, text='Admin Menu', font=('Impact', 28))
    label.pack(pady=25, padx=70)

    filling = CTkButton(master=frame, text='Update  Price', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: updatePrice(adminWindow))
    filling.pack(pady=6, padx=10)
    
    filling = CTkButton(master=frame, text='Update  Quantity', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: updateQty(adminWindow))
    filling.pack(pady=6, padx=10)

    checkPrice = CTkButton(master=frame, text='Transactions', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    checkPrice.pack(pady=6, padx=10)

    label = CTkLabel(master=frame, text='', font=('Impact', 26))
    label.pack(pady=2, padx=40)
    
    adminWindow.mainloop()