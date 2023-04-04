from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import dataHandling
import fillPetrol, fillDiesel
import adminPage

set_appearance_mode('system')
set_default_color_theme('green')

def goBack(fillWindow):
    fillWindow.destroy()
    adminPage.admin()

def petrol(fillWindow):
    fillWindow.destroy()
    fillPetrol.PetrolPage()
    
def diesel(fillWindow):
    fillWindow.destroy()
    fillDiesel.dieselPage()
    
def fillPage():

    fillWindow = CTkToplevel()
    fillWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
    SW = fillWindow.winfo_screenwidth()
    SH = fillWindow.winfo_screenheight()
    x = SW/2 + 200
    y = SH/2 - WH/2
    fillWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))


    bg = ImageTk.PhotoImage(file='assets/background.jpg')
    label1 = Label(fillWindow, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = fillWindow, height=200, width=600)
    frame.pack(pady=60, padx=60, expand=True)
    
    label = CTkLabel(master=frame, text='Choose Fuel Type', font=('Impact', 28))
    label.pack(pady=25, padx=70)
    
    Petrol = CTkButton(master=frame, text='Petrol', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: petrol(fillWindow))
    Petrol.pack(pady=20, padx=30, side= LEFT)

    Diesel = CTkButton(master=frame, text='Diesel', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: diesel(fillWindow))
    Diesel.pack(pady=20, padx=30, side= RIGHT)
    
    fillWindow.mainloop()
