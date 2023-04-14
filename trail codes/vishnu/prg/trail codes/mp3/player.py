import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

#hello 
root=Tk()
root.title("Feelzy")
root.geometry("485x700+290+10")
root.configure(background="#333333")
root.resizable(False,False)

def Addmusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END,song)
def Playmusic():
    Music_Name=Playlist.get(ACTIVE)
    print(Music_Name(ACTIVE))
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

lower_frame=Frame(root,background="#FFFFFF",
                  width=485,height=180)
lower_frame.place(x=0,y=400)

image_icon=PhotoImage(file="logo1.png")
root.iconphoto(False,image_icon)

Menu=PhotoImage(file="menu.png")
Label(root,image=Menu).place(x=0,y=580,width=485,height=100)

frame_music=Frame(root,bd=2,relief=RIDGE)
frame_music.place(x=0,y=585,width=485,height=100)


ButtonPlay=PhotoImage(file="play1.png")
Button(root,image=ButtonPlay,bg="#FFFFFF",bd=0,height=60,width=60,command=Playmusic).place(x=215,y=487)

Button(root,text="Browse music",width=50,height=3,
       font=("calibri",12,"bold"),fg="Black",
       bg="#FFFFFF",command=Addmusic).place(x=0,y=550)

Scroll=Scrollbar(frame_music)
Playlist=Listbox(frame_music,width=100,font=("Times new roman",10),
                 bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,
                 yscrollcommand=Scroll.set)

Scroll.config(command= Playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
Playlist.pack(side=RIGHT,fill=BOTH)

root.mainloop()