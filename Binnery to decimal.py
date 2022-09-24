def i(event):
        r.after(100,execute)
def clear_screen(event):
        global d
        d=Entry(r)
        d.place(x=210,y=100)
        x.set("* No value *")
        
def omgponnu():
        global b
        x.set(b)
def y(event):
        if event.char=="C" or event.char=="":
              cc()
        #print(event.char)
        global b
        if event.char=="1" or  event.char=="0":
              execute()

def execute():
        global b
        try:
                global x;f=0;j=10
                Value=d.get();c=len(Value)
                for i in range(c):
                	ya=int(Value[i])
                	if ya>=2 or ya<=-1:
                		x.set("* Invalid Binnery code *")
                		j=100
                if j==10:
                        for i in range(c):
                                a=(int(Value[i]))*(2**(c-(i+1)));f+=a       
                                b=int(f)
                                x.set(b)
                                F.write('Binnery '+d.get()+' Equal :'+str(b)+'\n')
        except:
                q=d.get()
                if q=="":
                      x.set(" No Value Found...")
                else:
                      x.set(" - Invalid Entry -") 

	
from tkinter import *
import tkinter as tk
ans=5
b="-----"
def cc():
	 global ii
	 ii+=1
	 if ii==lc:
	 	ii=0
	 r.configure(background=list[ii])
	 W.config(background=list[ii])
	 J.config(background=list[ii])
	 U.config(background=list[ii])
	 
list=['gray8','purple','magenta','pink','red','aqua','brown','lime','orange','green',
'lightblue','lightgreen','silver','white','gray',
'navy',]
ii=0;lc=len(list);f='yellow'
F=open('files/Covert to Decimal.txt','a')
r=Tk()
r.resizable(0,0)
r.bind('<Key>',y)
r.bind('<space>',clear_screen)
r.bind('<BackSpace>',i)
r.bind('<Return>',i)
x=StringVar()

r.title('Convert to binnery...')
r.geometry("650x400")
r.configure(background="gray8")

Label(r,text='              - Binnery to Decimal Converter -                ',fg="white",font=("arial",17,"bold"),bg='black',height='2').pack(fill=BOTH,side=TOP)

U=Label(r,text='Enter Binnery code : ',bg=list[ii],height='1',font=("arial",14,"bold"),fg="yellow");U.pack()
U.place(y=100,x=10)
d=Entry(r);
d.pack();
d.bind("<Return>",i);
d.bind("<BackSpace>",i)
d.place(x=210,y=100)
#d.bind('<Return>',y)
W=Label(r,text='The Decimal Value : ',bd='4',bg=list[ii],height='1',font=("arial",15,"bold"),fg="red");W.pack()
W.place(x=90,y=230)


J=Label(r,textvariable=x,height='1',bd='5',bg=list[ii],fg='brown',font=("arial",20,"bold"))
J.pack()
J.place(y=225,x=280)
q=Label(r,text='Create By Sajithmym',bg='black',fg='white',height="2")
q.pack(side=BOTTOM,fill=BOTH)

r.mainloop()
F.close()
