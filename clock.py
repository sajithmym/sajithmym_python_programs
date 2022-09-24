from tkinter import *
from time import *

def timeof():
    tm = strftime('%I : %M : %S %p')
    Show.config(text=tm)
    Show.after(1000,timeof)

q= Tk()
q.resizable(0,0)
q.title('Gui Clock')
Show = Button(q,font=('Copperplate Gothic Bold',40,'bold'),bg='gray8',fg='lightgreen',borderwidth=35,
activebackground='lightblue', activeforeground='blue')
Show.pack()
timeof()

q.mainloop()