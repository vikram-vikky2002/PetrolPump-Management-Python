from tkinter import Label, messagebox
from customtkinter import *
from PIL import ImageTk
import dataHandling
import homePage
import uuid

set_appearance_mode('system')
set_default_color_theme('green')

def goBack(petrolWindow):
    petrolWindow.destroy()
    homePage.HomePage()
    

def fillLitreFunction(entry1, petrolWindow):
    availPetrol = dataHandling.getData(r'data\petrolQty.pkl')
    rate = dataHandling.getData(r'data\petrolPrice.pkl')
    inputVal = int(entry1.get())
    qty = int(inputVal)
    maxLimit = dataHandling.getData(r'data\petrolMax.pkl')
    id = uuid.uuid1()
    if((availPetrol+qty) <= maxLimit):
        messagebox.showinfo(message='Filling...')
        availPetrol = availPetrol + qty
        price = round(qty*rate, 2)
        messagebox.showinfo(message=f'Pay : Rs.{price}\nQuantity Filled : {qty}Ltrs.')
        dataHandling.storeData(r'data\petrolQty.pkl', availPetrol)
        dataHandling.addTraction([[f'{id.hex}','Petrol Filled', '', f'{price}']])
        goBack(petrolWindow)
        
    else:
        messagebox.showinfo(message='Fuel Capacity Overflow...')
        goBack(petrolWindow)


def PetrolPage():
    crPrice = dataHandling.getData(r'data\petrolPrice.pkl')
    crQty = dataHandling.getData(r'data\petrolQty.pkl')
    # print(availPetrol)
    
    
    petrolWindow = CTkToplevel()
    petrolWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = petrolWindow.winfo_screenwidth()
    SH = petrolWindow.winfo_screenheight()
    x = SW/2 + 200
    y = SH/2 - WH/2
    petrolWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    # petrolWindow.geometry('732x488+470+150')

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(petrolWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = petrolWindow, height=200, width=600)
    frame.pack(pady=60, padx=60, expand=True)
    
    label = CTkLabel(master=frame, text='Petrol', font=('Impact', 28))
    label.pack(pady=9, padx=70)
    
    label = CTkLabel(master=frame, text=f'Current Petrol Price : {crPrice}', font=('Impact', 16))
    label.pack(pady=5, padx=70)
    
    label = CTkLabel(master=frame, text=f'Petrol Quantity : {crQty}', font=('Impact', 16))
    label.pack(pady=5, padx=70)
    
    entry1 = CTkEntry(master=frame, placeholder_text='Enter Quantity')
    entry1.pack(pady=8, padx=10)
    
    filling = CTkButton(master=frame, text='Fill', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: fillLitreFunction(entry1, petrolWindow))
    filling.pack(pady=15, padx=30)

    petrolWindow.mainloop()
