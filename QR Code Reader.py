import cv2
from tkinter import *
import os
from tkinter import filedialog as Sajith

def geting():
    global lbl
    InItial =os.path.join(os.getcwd(),'QR Code')
    try:
        p=Sajith.askopenfilename(initialdir=InItial,title="Choose a QR Code",filetypes=(("png files",".png"),("all files","*.*")))
        img = cv2.imread(p)
        Detector = cv2.QRCodeDetector()
        msg,b,c = Detector.detectAndDecode(img)
        lbl.place(x=100,y=130)
        lbl.config(text="Message is :-  "+msg)
    except Exception as f:
        print('------>',f,'<------------')

a = Tk()
a.configure(bg='gray8')
a.geometry('730x230')
a.resizable(0,0)

Label(a,text="   ` ` ` ` QR Code Reader ` ` ` ` ",font=('arial',20,'bold'),bg='black',fg='white').pack(fill=BOTH)

btn = Button(a,text="Get QR Code",font=('arial',20,'bold'),bg='black',fg='gray',command=geting)
btn.pack()
btn.place(x=270,y=60)

lbl = Label(a,font=('arial',18,'bold'),bg='gray8',fg='red')
lbl.pack()
lbl.place(x=100,y=1200)

a.mainloop()