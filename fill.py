from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import dataHandling
import fillPetrol
set_appearance_mode('system')
set_default_color_theme('green')

def petrol(fillWindow):
    fillWindow.destroy()
    fillPetrol.PetrolPage()

def fillPage():
    # availPetrol = dataHandling.getData('petrolQty.pkl')
    # print(availPetrol)
    # if(availPetrol >= qty):
    #     print('Filling...')
    #     avPetrol = avPetrol - qty
    #     price = qty*rate
    # else:
    #     print('Fuel Not there...')
    
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

    frame = CTkFrame(master = fillWindow, height=200, width=600)
    frame.pack(pady=60, padx=60, expand=True)
    
    label = CTkLabel(master=frame, text='Choose Fuel Type', font=('Impact', 28))
    label.pack(pady=25, padx=70)
    
    Petrol = CTkButton(master=frame, text='Petrol', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: petrol(fillWindow))
    Petrol.pack(pady=20, padx=30, side= LEFT)

    diesel = CTkButton(master=frame, text='Diesel', font=('Arial Rounded MT Bold', 18), width=162, height=30)
    diesel.pack(pady=20, padx=30, side= RIGHT)
    
    fillWindow.mainloop()

