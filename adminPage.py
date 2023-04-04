from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import fill, changeCost, login
import tranactionModule

set_appearance_mode('system')
set_default_color_theme('green')


def goBack(adminWindow):
    adminWindow.destroy()
    login.LoginPage()

def updateQty(adminWindow):
    adminWindow.destroy()
    fill.fillPage()
    
    
def updatePrice(adminWindow):
    adminWindow.destroy()
    changeCost.updateRate()
    

def transactions(adminWindow):
    adminWindow.destroy()
    tranactionModule.transactionPage()


def admin():
    adminWindow = CTkToplevel()
    adminWindow.resizable(width= False, height= False)
    WW = 732
    WH = 450
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

    checkPrice = CTkButton(master=frame, text='Transactions', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: transactions(adminWindow))
    checkPrice.pack(pady=6, padx=10)

    label = CTkLabel(master=frame, text='', font=('Impact', 26))
    label.pack(pady=2, padx=40)
    
    logoutButton = CTkButton(master=adminWindow, text='Logout', font=('Arial Rounded MT Bold', 16), width=18, height=2, command= lambda: goBack(adminWindow))
    logoutButton.place(x= 650, y=10)
    
    adminWindow.mainloop()