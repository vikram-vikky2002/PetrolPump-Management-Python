from tkinter import Frame, Label, Scrollbar
from customtkinter import *
from PIL import ImageTk

def CheckPrice():
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
    
    canvas = CTkCanvas(fillWindow)
    scrollbar = CTkScrollbar(fillWindow, command=canvas.yview)
    scrollable_frame = CTkFrame(canvas)
    
    scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

# Add some widgets to the scrollable frame
    for i in range(50):
        Label(scrollable_frame, text=f"Label {i}").pack()

    
    # for i in range(5):
    #     frame = CTkFrame(master = fillWindow)
    #     frame.pack(pady=60, padx=60, expand=True)
    
    fillWindow.mainloop()


CheckPrice()
