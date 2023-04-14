from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import customerFill, checkPrice, login

set_appearance_mode('system')
set_default_color_theme('green')

'''
    goBack()
    This function is used to go back to the login page.
    It will destroy the current window and open the login page.
    
'''
def goBack(hWin):
    hWin.destroy()
    login.LoginPage()

'''
    fillRedirect()
    This function is used to go to the fill page.
    It will destroy the current window and open the fill page.
    
'''
def fillRedirect(hWin):
    hWin.destroy()
    cf = customerFill.fillPage()

'''
    priceCheck()
    This function is used to go to the price check page.
    It will destroy the current window and open the price check page.

'''
def priceCheck(hWin):
    hWin.destroy()
    checkPrice.CheckPrice()

'''
    HomePage()
    This function is used to show the home page.
    It will show the home page and the buttons to go to the other pages.
    It will also have a logout button to go back to the login page.

'''    
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
    hWin.title('Petrol Pump Management')

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(hWin, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = hWin)
    frame.pack(pady=60, padx=60, expand=True)

    label = CTkLabel(master=frame, text='User Menu', font=('Impact', 28))
    label.pack(pady=25, padx=70)

    filling = CTkButton(master=frame, text='Fill Fuel', font=('Arial Rounded MT Bold', 18), width=162, height=30, command=lambda : fillRedirect(hWin))
    filling.pack(pady=6, padx=10)

    checkPrice = CTkButton(master=frame, text='Check Price', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: priceCheck(hWin))
    checkPrice.pack(pady=6, padx=10)

    label = CTkLabel(master=frame, text='', font=('Impact', 26))
    label.pack(pady=2, padx=40)
    
    logoutButton = CTkButton(master=hWin, text='Logout', font=('Arial Rounded MT Bold', 16), width=18, height=2, command= lambda: goBack(hWin))
    logoutButton.place(x= 650, y=10)

    hWin.mainloop()
