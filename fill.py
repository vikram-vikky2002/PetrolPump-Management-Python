from tkinter import Label
from customtkinter import *
from PIL import ImageTk

set_appearance_mode('system')
set_default_color_theme('green')


def fill_Petrol():
    # if(avPetrol >= qty):
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

    frame = CTkFrame(master = fillWindow, height=200, width=6000)
    frame.pack(pady=60, padx=60, expand=True)
    
    fillWindow.mainloop()

