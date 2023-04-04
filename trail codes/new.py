from tkinter import *
from customtkinter import *
from PIL import ImageTk

set_appearance_mode('system')
set_default_color_theme('green')

# def goBack(fillWindow):
#     fillWindow.destroy()
#     homePage.HomePage()


def CheckPrice():
    fillWindow = CTkToplevel()
    fillWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = fillWindow.winfo_screenwidth()
    SH = fillWindow.winfo_screenheight()
    x = SW/2 + 200
    y = SH/2 - WH/2
    fillWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    # fillWindow.geometry('732x488+470+150')

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(fillWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = fillWindow, height=200, width=6000)
    frame.pack(pady=60, padx=60, expand=True)
    
    currentPetrolPrice = 80
    currentDieselPrice = 78
    
    label1 = CTkLabel(master=frame, text='Current Price Details', font=('Arial Rounded MT Bold', 24), width=162, height=30)
    label1.pack(pady=8, padx=70)
    
    label2 = CTkLabel(master=frame, text=f'Petrol : {currentPetrolPrice}', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    label2.pack(pady=5, padx=70)
    
    label3 = CTkLabel(master=frame, text=f'Diesel : {currentDieselPrice}', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    label3.pack(pady=5, padx=70)
    
    sizeBox = CTkLabel(master=frame, text=f' ', font=('Arial Rounded MT Bold', 2), width=162, height=10)
    sizeBox.pack(pady=20, padx=10)
    
    backButton = CTkButton(master=fillWindow, text='Logout', font=('Arial Rounded MT Bold', 16), width=18, height=2)
    backButton.place(x= 650, y=10)
    
    fillWindow.mainloop()

CheckPrice()