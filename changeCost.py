from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import dataHandling

set_appearance_mode('system')
set_default_color_theme('green')

def updatePrice(entry1, entry2):
    e1 = entry1.get()
    e2 = entry2.get()
    if(e1!=''):
        dataHandling.storeData(r'data\petrolPrice.pkl', e1)
    if(e2!=''):
        dataHandling.storeData(r'data\dieselPrice.pkl', e2)
    
    print(e1, e2)
    

def updateRate():
    costWindow = CTkToplevel()
    costWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = costWindow.winfo_screenwidth()
    SH = costWindow.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    costWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))

    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(costWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = costWindow, height=500, width=60)
    frame.pack(pady=60, padx=60, expand=True)
    
    currentPetrolPrice = dataHandling.getData(r'data\petrolPrice.pkl')
    currentDieselPrice = dataHandling.getData(r'data\dieselPrice.pkl')
    
    label1 = CTkLabel(master=frame, text='Current Price Details', font=('Arial Rounded MT Bold', 24), width=162, height=30)
    label1.pack(pady=8, padx=70)
    
    label2 = CTkLabel(master=frame, text=f'Petrol : {currentPetrolPrice}', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    label2.pack(pady=5, padx=70)
    
    label3 = CTkLabel(master=frame, text=f'Diesel : {currentDieselPrice}', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    label3.pack(pady=5, padx=70)
    
    sizeBox = CTkLabel(master=frame, text=f' ', font=('Arial Rounded MT Bold', 50), width=162, height=30)
    sizeBox.pack(pady=20, padx=10)
    
    label4 = CTkLabel(master=frame, text=f'Enter New Petrol Rate', font=('Arial Rounded MT Bold', 15), width=100, height=30)
    label4.place(x=20, y=160)
    entry1 = CTkEntry(master=frame, placeholder_text='Update Petrol Price')
    entry1.place(x=216, y=160)

    label5 = CTkLabel(master=frame, text=f'Enter New Diesel Rate', font=('Arial Rounded MT Bold', 15), width=162, height=30)
    label5.place(x=20, y=200)
    entry2 = CTkEntry(master=frame, placeholder_text='Update Diesel Price')
    entry2.place(x=216, y=200)
    
    button = CTkButton(master=frame, text='Update Price', command= lambda: updatePrice(entry1, entry2))
    button.pack(pady=25, padx=10)
    
    costWindow.mainloop()
    
updateRate()