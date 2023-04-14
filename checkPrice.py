from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import dataHandling
import homePage

set_appearance_mode('system')
set_default_color_theme('green')

'''
    goBack()
    This function is used to go back to the home page.
    It will destroy the current window and open the home page.

'''

def goBack(fillWindow):
    fillWindow.destroy()
    homePage.HomePage()

'''
    CheckPrice()
    This function is used to show the current price of petrol and diesel.
    It will show the current price of petrol and diesel.
    It will also have a back button to go back to the home page.
    It will also have a button to update the price of petrol and diesel.
    It will also have a entry to enter the new price of petrol and diesel.
    It will also have a button to confirm the update.
    It will destroy the current window and open the update rate page.
        
'''

def CheckPrice():
    fillWindow = CTkToplevel()
    fillWindow.resizable(width= False, height= False)
    WW = 732
    WH = 450
    SW = fillWindow.winfo_screenwidth()
    SH = fillWindow.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    fillWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    fillWindow.title('Petrol Pump Management')

    ic = Image.open('assets/background3.jpg')
    res_img = ic.resize((910,605))
    bg = ImageTk.PhotoImage(res_img)
    label1 = Label(fillWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = fillWindow, height=200, width=6000)
    frame.pack(pady=60, padx=60, expand=True)
    
    currentPetrolPrice = dataHandling.getData(r'data\petrolPrice.pkl')
    currentDieselPrice = dataHandling.getData(r'data\dieselPrice.pkl')
    
    label1 = CTkLabel(master=frame, text='Current Price Details', font=('Arial Rounded MT Bold', 24), width=162, height=30)
    label1.pack(pady=8, padx=70)
    
    label2 = CTkLabel(master=frame, text=f'Petrol : {currentPetrolPrice}', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    label2.pack(pady=5, padx=70)
    
    label3 = CTkLabel(master=frame, text=f'Diesel : {currentDieselPrice}', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    label3.pack(pady=5, padx=70)
    
    sizeBox = CTkLabel(master=frame, text=f' ', font=('Arial Rounded MT Bold', 2), width=162, height=10)
    sizeBox.pack(pady=20, padx=10)
    
    backButton = CTkButton(master=fillWindow, text='<- Back', font=('Arial Rounded MT Bold', 16), width=18, height=2, command= lambda: goBack(fillWindow))
    backButton.place(x= 5, y=5)
    
    fillWindow.mainloop()

