from tkinter import *
from PIL import Image, ImageTk

root = Tk()

w = 800
h = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(bg='bisque')

frame = Frame(root,height=h-60, width=w,background='black')
frame.place(x=0, y=0)

img1 = Image.open(r'trail codes\vishnu\play-button-arrowhead.png')
resized_image1= img1.resize((40,40), Image.ANTIALIAS)
play_image= ImageTk.PhotoImage(resized_image1)

img2 = Image.open(r'trail codes\vishnu\pause-button.png')
resized_image2= img2.resize((40,40), Image.ANTIALIAS)
pause_image= ImageTk.PhotoImage(resized_image2)

img3 = Image.open(r'trail codes\vishnu\stop-button.png')
resized_image3= img3.resize((40,40), Image.ANTIALIAS)
stop_image= ImageTk.PhotoImage(resized_image3)


playbutton = Button(root, text='Play', image=play_image)
playbutton.place(x=0, y=400)

playbutton = Button(root, text='Pause', image=pause_image)
playbutton.place(x=50, y=400)

playbutton = Button(root, text='Stop', image=stop_image)
playbutton.place(x=100, y=400)

root.mainloop()