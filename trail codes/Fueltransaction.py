from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import ImageTk

win = Tk()

frm = LabelFrame(win)

myCanva = Canvas(frm)
myCanva.pack(side=LEFT)

yscrollBar = Scrollbar(frm, command=myCanva.yview)
yscrollBar.pack(side=RIGHT, fill='y')

myCanva.configure(yscrollcommand=yscrollBar.set)
myCanva.bind('<configure>', lambda e: myCanva.configure(scrollregion = myCanva.bbox('all')))

myFrame = Frame(myCanva)
myCanva.create_window((0,0), window=myFrame, anchor='nw')

frm.pack(fill=BOTH, expand=True, padx=10, pady=10)

for i in range(100):
    CTkButton(myFrame, text=f'My Button {i}').pack()

win.resizable(width= False, height= False)
WW = 732
WH = 488
SW = win.winfo_screenwidth()
SH = win.winfo_screenheight()
x = SW/2 - WW/2
y = SH/2 - WH/2
win.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
win.mainloop()