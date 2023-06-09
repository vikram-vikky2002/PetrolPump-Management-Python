from tkinter import Label, messagebox
from customtkinter import *
from PIL import ImageTk, Image
import dataHandling, adminPage

set_appearance_mode('system')
set_default_color_theme('green')

'''
    goBack()
    This function is used to go back to the admin page.
    It will destroy the current window and open the admin page.

'''

def goBack(costWindow):
    costWindow.destroy()
    adminPage.admin()

'''
    updatePrice()
    This function is used to update the price of petrol and diesel.
    It will take the new price of petrol and diesel as input from the user.
    It will store the new price in the petrolPrice.pkl and dieselPrice.pkl files.
    It will also show a message box to confirm that the price has been updated.
    It will destroy the current window and open the admin page.
    
'''

def updatePrice(entry1, entry2, costWindow):
    if(entry1.get() or entry2.get()):
        e1 = float(entry1.get())
        dataHandling.storeData(r'data\petrolPrice.pkl', e1)
        messagebox.showinfo(message='Petrol Price Updated')
        
    if(entry2.get()):
        e2 = float(entry2.get())
        dataHandling.storeData(r'data\dieselPrice.pkl', e2)
        messagebox.showinfo(message='Diesel Price Updated')
        
    costWindow.destroy()
    adminPage.admin()

'''
    updateRate()
    This function is used to create the update rate page.
    It will show the current price of petrol and diesel.
    It will also have a back button to go back to the admin page.
    It will also have a button to update the price of petrol and diesel.
    It will also have a entry to enter the new price of petrol and diesel.
    It will also have a button to confirm the update.
    It will destroy the current window and open the update rate page.

'''

def updateRate():
    try:
        costWindow = CTkToplevel()
        costWindow.resizable(width= False, height= False)
        WW = 732
        WH = 450
        SW = costWindow.winfo_screenwidth()
        SH = costWindow.winfo_screenheight()
        x = SW/2 - WW/2
        y = SH/2 - WH/2
        costWindow.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
        costWindow.title('Petrol Pump Management')

        ic = Image.open('assets/background3.jpg')
        res_img = ic.resize((910,605))
        bg = ImageTk.PhotoImage(res_img)
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
        
        button = CTkButton(master=frame, text='Update Price', command= lambda: updatePrice(entry1, entry2, costWindow))
        button.pack(pady=25, padx=10)
        
        backButton = CTkButton(master=costWindow, text='<- Back', font=('Arial Rounded MT Bold', 16), width=18, height=2, command= lambda: goBack(costWindow))
        backButton.place(x= 5, y=5)
        
        costWindow.mainloop()
    
    except Exception as e:
        messagebox.showerror(f'Python Error', 'Error: {e}')