from customtkinter import *
from tkinter import Label, ttk
from tkinter import *
from PIL import ImageTk
import csv
import adminPage

set_appearance_mode('system')
set_default_color_theme('green')

'''
    goBack()
    This function is used to go back to the admin page.
    It will destroy the current window and open the admin page.
    
'''
def goBack(transactionWindow):
    transactionWindow.destroy()
    adminPage.admin()

'''
    transactionPage()
    This function is used to show the transaction page.
    It will show the transaction page and the buttons to go to the other pages.

'''
def transactionPage():
    transactionWindow = CTkToplevel()
    transactionWindow.resizable(width= False, height= False)
    WW = 732
    WH = 450
    SW = transactionWindow.winfo_screenwidth()
    SH = transactionWindow.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    transactionWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    transactionWindow.title('Petrol Pump Management')

    bg = ImageTk.PhotoImage(file='assets/background2_small.jpeg')
    label1 = Label(transactionWindow, image = bg)
    label1.place(x = 0, y = 0)
    
    mainFrame = Frame(transactionWindow, bg='darkgray')
    mainFrame.pack(side=LEFT, padx=20)
    
    label = CTkLabel(master=mainFrame, text='Transaction History', font=('Impact', 35, 'bold'))
    label.pack(pady=10, padx=40)
    
    frm = Frame(mainFrame)
    frm.pack(side=LEFT, padx=20, pady=10)
    
    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show='headings', height='20')
    tv.pack()
    
    backButton = CTkButton(master=transactionWindow, text='<- Back', font=('Arial Rounded MT Bold', 16), width=18, height=2, command= lambda: goBack(transactionWindow))
    backButton.place(x= 5, y=5)
    
    file = open(r'data\transactions.csv')
    csvreader = csv.reader(file)
    r_set = [row for row in csvreader]
    
    tv.heading(1, text='ID', anchor=CENTER)
    tv.heading(2, text='Transaction Detail', anchor=W)
    tv.heading(3, text='Debit')
    tv.heading(4, text='Credit')
    
    for dat in r_set:
        v = [r for r in dat]
        tv.insert('', 'end', iid=v[0], values=v)
    
    transactionWindow.mainloop()
