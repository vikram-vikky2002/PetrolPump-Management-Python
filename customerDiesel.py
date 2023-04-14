from tkinter import Label, messagebox
from customtkinter import *
from PIL import ImageTk
import dataHandling
import homePage
import uuid

set_appearance_mode('system')
set_default_color_theme('green')

'''
    goBack()
    This function is used to go back to the home page.
    It will destroy the current window and open the home page.

'''

def goBack(dieselWindow):
    dieselWindow.destroy()
    homePage.HomePage()
    
'''
    fillLitreFunction()
    This function is used to fill the diesel.
    It will check if the quantity of diesel entered by the user is less than the available quantity.
    If the quantity is less than the available quantity, it will show a message box.
    If the quantity is more than the available quantity, it will show a message box.
    
'''
    
def fillLitreFunction(entry1, dieselWindow):
    availdiesel = dataHandling.getData(r'data\dieselQty.pkl')
    rate = dataHandling.getData(r'data\dieselPrice.pkl')
    inputVal = int(entry1.get())
    qty = int(inputVal)
    id = uuid.uuid1()
    maxLimit = dataHandling.getData(r'data\dieselMax.pkl')
    
    if(qty< availdiesel):
        messagebox.showinfo(message='Filling...')
        availdiesel = availdiesel - qty
        price = round(qty*rate, 2)
        messagebox.showinfo(message=f'Pay : Rs.{price}\nQuantity Filled : {qty}Ltrs.')
        dataHandling.storeData(r'data\dieselQty.pkl', availdiesel)
        dataHandling.addTraction([[f'{id.hex}','Diesel Filled', '', f'{price}']])
        goBack(dieselWindow)
        
    else:
        messagebox.showinfo(message='Fuel Capacity Insufficient...')
        goBack(dieselWindow)

'''
    dieselPage()
    This class is used to create the diesel page.
    It will show the current price and quantity of diesel.
    It will also have a back button to go back to the homePage page.
    It will also have a button to fill the diesel.
    It will also have a entry to enter the quantity of diesel to be filled.

'''

def dieselPage():
    try:
        crPrice = dataHandling.getData(r'data\dieselPrice.pkl')
        crQty = dataHandling.getData(r'data\dieselQty.pkl')
        # print(availdiesel)
        
        
        dieselWindow = CTkToplevel()
        dieselWindow.resizable(width= False, height= False)
        WW = 732
        WH = 450
        SW = dieselWindow.winfo_screenwidth()
        SH = dieselWindow.winfo_screenheight()
        x = SW/2 - WW/2
        y = SH/2 - WH/2
        dieselWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
        dieselWindow.title('Petrol Pump Management')

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
    
    except Exception as e:
        messagebox.showerror(f'Python Error', 'Error: {e}')