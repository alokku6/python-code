# Create youtube downloader using python gui module tkinter
# pip install pytube
# pip install pillow 

import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pytube
import time

root = tk.Tk()
root.title("Youtude Downloader")
root.iconbitmap("Youtube.ico")
root.geometry("700x800")
root.maxsize(400,600)
root.minsize(700,300)

def Download():
    link = text.get("1.0","end-1c")

    if link == '':
        messagebox.showerror("YouTube Downloader","Please paste a link here")
    else:
        yt = pytude.YouTube(link)
        stream  = yt.streams.first()
        time.sleep(2)
        text.delete(1.0,'end')
        text.insert('end','wait Downloading.........')
        time.sleep(5)
        stream.download()
        messagebox.showinfo("YouTube Downloader",'Video has been download successfully')


header = Label(root,bg="black",width = "400",height = "4")
header.place(x=10,y=0)

yt_logo = ImageTk.PhotoImage(Image.open('Youtube.png'))
logo = Label(root, image = yt_logo,borderwidth =100)
logo.place(x=0,y=0)

caption = Label(root, text = "Youtube Downloader",font = ('verdana',10,'bold'))
caption.place(x=10,y=10)

yt1_logo = ImageTk.PhotoImage(Image.open('youtu.ico'))
logo2 = Label(root,image = yt1_logo,borderwidth=None)
logo2.place(x=260,y=150)

text = Text (root,width=60,height=2,font = ('verdana',10,'bold'))
text.place(x=100,y=280)
text.insert('end','Paste your video link here')

button = Button(root,text="Download",relief=RIDGE,font =('verdana',10,'bold'),bg="red",fg="white",command=Download)
button.place(x=280,y=350)

root.mainloop()
