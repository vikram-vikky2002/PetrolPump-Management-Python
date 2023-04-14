from tkinter import Label
from customtkinter import *
from PIL import ImageTk
import fillPetrol, fillDiesel
import adminPage

set_appearance_mode('system')
set_default_color_theme('green')

'''
    goBack()
    This function is used to go back to the admin page.
    It will destroy the current window and open the admin page.
    
'''

def goBack(fillWindow):
    fillWindow.destroy()
    adminPage.admin()
'''
    petrol()
    This function is used to go to the petrol page.
    It will destroy the current window and open the petrol page.
    
'''
def petrol(fillWindow):
    fillWindow.destroy()
    fillPetrol.PetrolPage()

'''
    diesel()
    This function is used to go to the diesel page.
    It will destroy the current window and open the diesel page.
    
'''
def diesel(fillWindow):
    fillWindow.destroy()
    fillDiesel.dieselPage()

'''
    fillPage()
    This function is used to show the fill page.
    It will show the fill page and the buttons to go to the other pages.
    
'''
def fillPage():

    fillWindow = CTkToplevel()
    fillWindow.resizable(width= False, height= False)
    WW = 732
    WH = 488
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
    
    Petrol = CTkButton(master=frame, text='Petrol', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: petrol(fillWindow))
    Petrol.pack(pady=20, padx=30, side= LEFT)

    Diesel = CTkButton(master=frame, text='Diesel', font=('Arial Rounded MT Bold', 18), width=162, height=30, command= lambda: diesel(fillWindow))
    Diesel.pack(pady=20, padx=30, side= RIGHT)
    
    backButton = CTkButton(master=fillWindow, text='<- Back', font=('Arial Rounded MT Bold', 16), width=18, height=2, command= lambda: goBack(fillWindow))
    backButton.place(x= 5, y=5)
    
    fillWindow.mainloop()
