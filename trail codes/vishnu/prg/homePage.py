import tkinter as ttk
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
import dataHandling
import pickle as pk

from playlist import Playlist


class VerticalScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,width=20, yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

def savePl(a, e, p):
    name = e.get()
    lst.append(name)
    dataHandling.storeData(r'data\Playlist.pkl', lst)
    a['text'] = 'New Playlist'
    e.destroy()
    but=Button(p,text=f'{name}', width=40, height=3)
    but.pack(side=BOTTOM)
    a.configure(command= lambda: addfun(innerframe, addbut))


def addfun(p, a):
    # name = askstring('Name', 'Enter playlist name : ')
    # showinfo('Hello!', 'Hi, {}'.format(name))
    en=Entry(p, width=40,font=(15))
    en.pack(side=BOTTOM)
    a['text'] = 'Save'
    a.configure(command= lambda: savePl(a,en, p))
    # name = en.get()
    # lst.append(name)
    # dataHandling.storeData(r'data\Playlist.pkl', lst)
    
def openPlaylst(name):
    lab1.destroy()
    addbut.destroy()
    sframe.destroy()
    Playlist(name, root)
    
    

lst = dataHandling.getData(r'data\Playlist.pkl')
root=Tk()

WW = 732
WH = 450
SW = root.winfo_screenwidth()
SH = root.winfo_screenheight()
x = SW/2 - WW/2
y = SH/2 - WH/2
root.geometry('%dx%d+%d+%d' %(WW, WH, x, y))

lab1 = Label(root, text='Playlist')
lab1.pack()

addbut=Button(root,text='New Playlist',width=5, height=2,command=lambda:addfun(innerframe, addbut))
addbut.place(x=600, y=30)
sframe=VerticalScrolledFrame(root)
sframe.pack()

innerframe=sframe.interior
for i in lst:
    but=Button(innerframe,text=f'{i}', width=40, height=3, command= lambda k=i: openPlaylst(k))
    but.pack(side=BOTTOM)


root.mainloop()