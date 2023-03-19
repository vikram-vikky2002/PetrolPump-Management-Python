from tkinter import Label, messagebox
from customtkinter import *
from PIL import ImageTk
import dataHandling
import homePage

set_appearance_mode('system')
set_default_color_theme('green')

def goBack(dieselWindow):
    dieselWindow.destroy()
    homePage.HomePage()
    

def fillLitreFunction(entry1, dieselWindow):
    availdiesel = dataHandling.getData(r'data\dieselQty.pkl')
    rate = dataHandling.getData(r'data\dieselPrice.pkl')
    inputVal = int(entry1.get())
    qty = int(inputVal)
    maxLimit = dataHandling.getData(r'data\dieselMax.pkl')
    
    if((availdiesel+qty) <= maxLimit):
        messagebox.showinfo(message='Filling...')
        availdiesel = availdiesel + qty
        price = qty*rate
        messagebox.showinfo(message=f'Pay : Rs.{price}\nQuantity Filled : {qty}Ltrs.')
        dataHandling.storeData(r'data\dieselQty.pkl', availdiesel)
        goBack(dieselWindow)
        
    else:
        messagebox.showinfo(message='Fuel Capacity Overflow...')
        goBack(dieselWindow)


def dieselPage():
    crPrice = dataHandling.getData(r'data\dieselPrice.pkl')
    crQty = dataHandling.getData(r'data\dieselQty.pkl')
    # print(availdiesel)
    
    
    dieselWindow = CTkToplevel()
    dieselWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = dieselWindow.winfo_screenwidth()
    SH = dieselWindow.winfo_screenheight()
    x = SW/2 + 200
    y = SH/2 - WH/2
    dieselWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    # dieselWindow.geometry('732x488+470+150')

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(dieselWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = dieselWindow, height=200, width=600)
    frame.pack(pady=60, padx=60, expand=True)
    
    label = CTkLabel(master=frame, text='Diesel', font=('Impact', 28))
    label.pack(pady=9, padx=70)
    
    label = CTkLabel(master=frame, text=f'Current Diesel Price : {crPrice}', font=('Impact', 16))
    label.pack(pady=5, padx=70)
    
    label = CTkLabel(master=frame, text=f'Diesel Quantity Available : {crQty}', font=('Impact', 16))
    label.pack(pady=5, padx=70)
    
    entry1 = CTkEntry(master=frame, placeholder_text='Enter Quantity')
    entry1.pack(pady=8, padx=10)
    
    filling = CTkButton(master=frame, text='Fill', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: fillLitreFunction(entry1, dieselWindow))
    filling.pack(pady=15, padx=30)

    dieselWindow.mainloop()
