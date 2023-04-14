from tkinter import *
import pygame

root=Tk()
root.title("Vishnu")
root.iconbitmap("D:\Study\sem 4\CS206-PYTHON\media player\Create-mp3-player\codemy audio\icon.ico")
root.geometry("500x300")

pygame.mixer.init()

song_box=Listbox(root,bg="black",fg="green",width=60)
song_box.pack(padx=20,pady=50)

root.mainloop()