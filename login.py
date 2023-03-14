from customtkinter import *
from tkinter import Label, messagebox
from tkinter import *
from PIL import ImageTk
import homePage

set_appearance_mode('system')
set_default_color_theme('green')
cUn = 'vikram'
cPw = '12345'
adUn = 'Admin'
adPw = 'Admin'


def login():
    username = entry1.get()
    password = entry2.get()
    if(username == cUn):
        if(password == cPw):
            messagebox.showinfo(message='Login Successfull')
            root.destroy()
            homePage.Homepage()
        else:
            messagebox.showinfo(message='Wrong Password')
            
    elif(username == adUn):
        if(password == adPw):
            messagebox.showinfo(message='Admin Login Successfull')
            root.destroy()
            homePage.Homepage()
        else:
            messagebox.showinfo(message='Wrong Admin Password')
    
    else:
        messagebox.showinfo(message='Username Not Found')
        

root = CTk()
root.resizable(width= False, height= False)
WW = 732
WH = 488
SW = root.winfo_screenwidth()
SH = root.winfo_screenheight()
x = SW/2 - WW/2
y = SH/2 - WH/2
root.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
# root.geometry('732x488+470+150')

bg = ImageTk.PhotoImage(file='assets/background.jpg')
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

button = CTkButton(master=frame, text='Login', command=login)
button.pack(pady=25, padx=10)

root.mainloop()