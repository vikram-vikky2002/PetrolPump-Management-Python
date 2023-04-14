import tkinter as ttk
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
import dataHandling
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
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,width=20,
                           yscrollcommand=vscrollbar.set)
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

class Homepage:
    def __init__(self,p):
        self.playlst=dataHandling.getData(r'data\Playlist.pkl')
        self.mainfra=Frame(p)
        self.mainfra.pack()
        self.titlab=Label(self.mainfra,text='Playlist')
        self.titlab.pack(side='top',anchor=CENTER)
        self.addfra=Frame(self.mainfra)
        self.addfra.pack(side='top')
        self.addbut=Button(self.addfra,text='add',command=self.addplay)
        self.addbut.pack(side='left')
        sf=VerticalScrolledFrame(self.mainfra)
        sf.pack(side='top')
        self.innerframe=sf.interior
        for i in self.playlst:
            fra=Frame(self.innerframe)
            playbut=Button(fra,text=i)
            playbut.pack(side='left')
            delbut=Button(fra,text='X', command=lambda k=i, f=fra: self.delfun(f,k))
            delbut.pack(side='left')
            fra.pack(side='top')
        

    def addplay(self):
        try:
            e=Entry(self.addfra,width=10)
            e.pack(side='right')
            self.addbut.config(text='save',command=lambda:self.saveplay(e))
            self.addbut.pack(side='right')
        except Exception as e:
            print(e)
            
    def openPlaylst(self, name):
        self.titlab.destroy()
        self.addbut.destroy()
        self.addfra.destroy()
        Playlist(name, root)
        
    def delfun(self,f,n):
        f.destroy()
        self.playlst.remove(n)
        dataHandling.storeData(r'data\Playlist.pkl', self.playlst)
        
    def saveplay(self,e):
        if(len(e.get())!=0):
            name=e.get()
        else:
            return
        e.destroy()
        self.addbut.config(text='add',command=self.addplay)
        fra=Frame(self.innerframe)
        playbut=Button(fra,text=name)
        playbut.pack(side='left')
        delbut=Button(fra,text='X')
        delbut.pack(side='left')
        self.playlst.append(name)
        dataHandling.storeData(r'data\Playlist.pkl', self.playlst)
        fra.pack(side='top')
        delbut.config(command=lambda:self.delfun(fra,name))
        

root=Tk()
cur=Homepage(root)
root.mainloop()