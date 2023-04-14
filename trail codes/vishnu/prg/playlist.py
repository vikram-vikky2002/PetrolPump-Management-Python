import tkinter as ttk
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
import dataHandling
import pickle as pk
from tkinter import filedialog

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




class Playlist:
    def __init__(self,name,p):
        try:
            self.playlst=dataHandling.getData(f'data/{name}.pkl')
        except:
            lst = []
            dataHandling.storeData(f'data/{name}.pkl', lst)
            self.playlst = dataHandling.getData(f'data/{name}.pkl')
            
        self.mainfra=Frame(p)
        self.mainfra.pack()
        titlab=Label(self.mainfra,text=name)
        titlab.pack(side='top',anchor=CENTER)
        addbut=Button(self.mainfra,text='add',command= lambda: self.addfile(name))
        addbut.pack()
        sf=VerticalScrolledFrame(self.mainfra)
        sf.pack(side='top')
        self.innerframe=sf.interior
        for i in self.playlst:
            fr = Frame(self.innerframe)
            fr.pack(side='top')
            but = Button(fr, text=i)
            but.pack(side='left')
            dele=Button(fr, text='X', command=lambda k=i:self.delfun(fr, k, name))
            dele.pack(side='left')
        
        
    def addfile(self, name):
        filepath=filedialog.askopenfilename()
        playfra=Frame(self.innerframe)
        playfra.pack()
        namebut=Button(playfra,text=filepath)
        namebut.pack(side='left')
        delbut=Button(playfra,text='X',command=lambda:self.delfun(playfra,filepath,name))
        delbut.pack(side='left')
        self.playlst.append(filepath)
        dataHandling.storeData(f'data/{name}.pkl', self.playlst)
        
    def delfun(self,fra,name,playlist):
        if(isinstance(fra,Frame)):
            fra.destroy()
        self.playlst.remove(name)
        dataHandling.storeData(f'data/{playlist}.pkl', self.playlst)


# root = Tk()
# p = Playlist('Mallu', root)
# root.mainloop()
    
