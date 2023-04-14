import time
from customtkinter import *
from tkinter import Label, messagebox
from tkinter import *
from PIL import ImageTk
import homePage, adminPage

'''
    These two lines are used to set the theme of the application.
    The theme is set to green.
    
'''

set_appearance_mode('system')
set_default_color_theme('green')

cUn = 'vikram'
cPw = '12345'
adUn = 'Admin'
adPw = 'Admin'

'''
    login()
    This function is used to check the username and password entered by the user.
    If the username and password is correct, it will open the home page.
    If the username is correct but the password is wrong, it will show a message box.
    If the username is wrong, it will show a message box.
    
'''

def login(entry1, entry2, root):
    username = entry1.get()
    password = entry2.get()
    if(username == cUn):
        if(password == cPw):
            messagebox.showinfo(message='Login Successfull')
            root.destroy()
            homePage.HomePage()
        else:
            messagebox.showinfo(message='Wrong Password')
            
    elif(username == adUn):
        if(password == adPw):
            messagebox.showinfo(message='Admin Login Successfull')
            root.destroy()
            adminPage.admin()
        else:
            messagebox.showinfo(message='Wrong Admin Password')
    
    else:
        messagebox.showinfo(message='Username Not Found')

'''
    splashScreen()
    This function is used to show the splash screen of the application.
    It will show the application name and a loading message.
    
'''
class splashScreen:
    def __init__(self):
        root=Tk()
        width_of_window = 450
        height_of_window = 260
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        root.geometry("%dx%d+%d+%d" %(screen_width,screen_height,x_coordinate,y_coordinate))
        root.overrideredirect(1)

        Frame(root, width=570, height=250, bg='#272727').place(x=0,y=0)

        label1=Label(root, text='PETROL PUMP MANAGEMENT', fg='white', bg='#272727')
        label1.configure(font=("Berlin Sans FB Demi", 22))  
        label1.place(x=50,y=90)

        label2=Label(root, text='Loading...', fg='white', bg='#272727')
        label2.configure(font=("Calibri", 14, 'bold'))
        label2.place(x=10,y=215)

        image_a=ImageTk.PhotoImage(file='assets/c2.png')
        image_b=ImageTk.PhotoImage(file='assets/c1.png')


        for i in range(3):
            l1=Label(root, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
            l2=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
            l3=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
            l4=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
            root.update_idletasks()
            time.sleep(0.2)

            l1=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
            l2=Label(root, image=image_a, border=0, relief=SUNKEN).place(x=260, y=145)
            l3=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
            l4=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
            root.update_idletasks()
            time.sleep(0.2)

            l1=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
            l2=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
            l3=Label(root, image=image_a, border=0, relief=SUNKEN).place(x=280, y=145)
            l4=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
            root.update_idletasks()
            time.sleep(0.2)

            l1=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
            l2=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
            l3=Label(root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
            l4=Label(root, image=image_a, border=0, relief=SUNKEN).place(x=300, y=145)
            root.update_idletasks()
            time.sleep(0.2)


        root.destroy()
        LoginPage()
        root.mainloop()

'''
    LoginPage()
    This function is used to create the login page of the application.
    It will show the username and password entry boxes.
    It will also show the login button.

'''
def LoginPage():
    root1 = Tk()
    root1.withdraw()
    root = CTkToplevel()
    root.resizable(width= False, height= False)
    WW = 732
    WH = 450
    SW = root.winfo_screenwidth()
    SH = root.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    root.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    root.title('Petrol Pump Management')

    bg = ImageTk.PhotoImage(file='assets/background2_small.jpeg')
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)

    frame = CTkFrame(master = root, height=200, width=6000)
    frame.pack(pady=60, padx=60, expand=True)

    label = CTkLabel(master=frame, text='User Login', font=('Impact', 35, 'bold'))
    label.pack(pady=25, padx=40)

    entry1 = CTkEntry(master=frame, placeholder_text='Username')
    entry1.pack(pady=12, padx=10)

    entry2 = CTkEntry(master=frame, placeholder_text='Password', show='*')
    entry2.pack(pady=12, padx=10)

    button = CTkButton(master=frame, text='Login', command= lambda: login(entry1, entry2, root))
    button.pack(pady=25, padx=10)

    root.mainloop()