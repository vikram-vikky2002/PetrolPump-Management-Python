from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import dataHandling
import customerPetrol, customerDiesel
import adminPage

set_appearance_mode('system')
set_default_color_theme('green')

class fillPage:     
    def __init__(self):
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

        bg = ImageTk.PhotoImage(file='assets/background.jpg')
        label1 = Label(fillWindow, image = bg)
        label1.place(x = 0, y = 0)

        frame = CTkFrame(master = fillWindow, height=200, width=600)
        frame.pack(pady=60, padx=60, expand=True)
        
        label = CTkLabel(master=frame, text='Choose Fuel Type', font=('Impact', 28))
        label.pack(pady=25, padx=70)
        
        Petrol = CTkButton(master=frame, text='Petrol', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: self.petrol(fillWindow))
        Petrol.pack(pady=20, padx=30, side= LEFT)

        Diesel = CTkButton(master=frame, text='Diesel', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: self.diesel(fillWindow))
        Diesel.pack(pady=20, padx=30, side= RIGHT)
        
        fillWindow.mainloop()


    def goBack(self, fillWindow):
        fillWindow.destroy()
        adminPage.admin()

    def petrol(self, fillWindow):
        fillWindow.destroy()
        customerPetrol.PetrolPage()
        
    def diesel(self, fillWindow):
        fillWindow.destroy()
        customerDiesel.dieselPage()