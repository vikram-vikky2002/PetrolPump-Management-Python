from customtkinter import *
from tkinter import Label, messagebox, ttk
from tkinter import *
from PIL import ImageTk
import uuid

set_appearance_mode('system')
set_default_color_theme('green')

def addTransaction():
    id = uuid.uuid1()
    print(id.hex)
    detail = 'Fuel Added'
    print(detail)
    credits = ''
    debit = 100
    
    dict = {id.hex, detail, credits, debit}
    print(dict)

addTransaction()

def transactionPage():
    transactionWindow = CTk()
    transactionWindow.resizable(width= False, height= False)
    WW = 732
    WH = 450
    SW = transactionWindow.winfo_screenwidth()
    SH = transactionWindow.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    transactionWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))

    bg = ImageTk.PhotoImage(file='assets/background2_small.jpeg')
    label1 = Label(transactionWindow, image = bg)
    label1.place(x = 0, y = 0)
    
    mainFrame = Frame(transactionWindow, bg='darkgray')
    mainFrame.pack(side=LEFT, padx=20)
    
    label = CTkLabel(master=mainFrame, text='Transaction History', font=('Impact', 35, 'bold'))
    label.pack(pady=10, padx=40)
    
    frm = Frame(mainFrame)
    frm.pack(side=LEFT, padx=20, pady=10)
    
    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show='headings', height='5')
    tv.pack()
    
    tv.heading(1, text='ID', anchor=CENTER)
    tv.heading(2, text='Transaction Detail', anchor=W)
    tv.heading(3, text='Debit')
    tv.heading(4, text='Credit')
    
    transactionWindow.mainloop()
