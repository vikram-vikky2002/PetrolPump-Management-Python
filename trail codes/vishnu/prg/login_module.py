from tkinter import *
from PIL import ImageTk,Image
# from tkinter import filedialog
# import os
# import time
# from functools import partial

un = 'vishnu'
pw = '1234'


def show():
    hide_button = Button(root, image=hide_image, command=hide, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=350, y=275)
    password_entry.config(show='')

def hide():
    show_button = Button(root, image=show_image, command=show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=350, y=275)
    password_entry.config(show='*')


def signin():
    inputUn = username_entry.get()
    inputPw = password_entry.get()
    if(un == inputUn):
        if(pw == inputPw):
            print('Login Successfull')
        else:
            print('Wrong Password')
    else:
        print('Incorrect Username')

root=Tk()
root.title("𝔽𝕖𝕖𝕝𝕫𝕪 ♩♪♫♬🎶")
WW = 400
WH = 600
SW = root.winfo_screenwidth()
SH = root.winfo_screenheight()
x = SW/2 - WW/2
y = SH/2 - WH/2
root.geometry('%dx%d+%d+%d' %(WW,WH,x,y))
root.resizable(False,False)

##frame##
frame = Frame(root,bg='#040405',width=400,height=700)
frame.place(x=0,y=0)



image_icon=PhotoImage(file="assets/logo1.png")
root.iconphoto(False,image_icon)
icon= Image.open("assets/icon.png")
resize_image = icon.resize((200, 150))
img = ImageTk.PhotoImage(resize_image)
label1=Label(image=img, bg='#040405')
label1.place(x=0,y=0)
label1.pack()
##Login label##
login_label=Label(frame,text="Login",fg="#15b7b9",font=("yu gothic ui", 18, "bold"),bg="#040405")
login_label.place(x=167,y=155)

##user name label###
Name_label=Label(frame,text="Username :",fg="#15b7b9",font=("yu gothic ui", 15, "bold"),bg="#040405")
Name_label.place(x=20,y=205)

##user name entry ##
username_entry = Entry(frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#15b7b9",font=("yu gothic ui ", 12, "bold"), insertbackground = '#75d0d2')
username_entry.place(x=130,y=214,width=200)

##user name  line##
username_line = Canvas(frame, width=250, height=2.0, bg="#15b7b9", highlightthickness=0)
username_line.place(x=130,y=240)

# ========================================================================
# ============================password====================================
# ========================================================================
password_label = Label(frame, text="Password :", bg="#040405", fg="#15b7b9",font=("yu gothic ui", 15, "bold"))
password_label.place(x=20, y=270)

password_entry = Entry(frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#15b7b9",
                            font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#15b7b9')
password_entry.place(x=130, y=270, width=200)

password_line = Canvas(frame, width=250, height=2.0, bg="#15b7b9", highlightthickness=0)
password_line.place(x=130, y=295)


# ========= show/hide password ==================================================================
show_image = ImageTk.PhotoImage \
    (file='trail codes\\images\\show.png')

hide_image = ImageTk.PhotoImage \
    (file='trail codes\\images\\hide.png')

show_button = Button(frame, image=show_image, command=show, relief=FLAT,
                            activebackground="white"
                            , borderwidth=0, background="white", cursor="hand2")
show_button.place(x=350, y=275)


lgn_button = Image.open('trail codes\\images\\btn1.png')
photo = ImageTk.PhotoImage(lgn_button)
lgn_button_label = Label(frame, image=photo, bg='#040405')
lgn_button_label.image = photo
lgn_button_label.place(x=55, y=350)
login = Button(frame, text='LOGIN', font=("yu gothic ui", 13, "bold"), 
               width=25, bd=0,bg='#3047ff', cursor='hand2', 
               activebackground='#3047ff', fg='white', command= signin)
login.place(x=80, y=365)


root.mainloop()




