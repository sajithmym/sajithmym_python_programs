from tkinter import *
from tkcalendar import *
import datetime

a = Tk()

NOW = datetime.datetime.now()

#print(NOW.strftime('{%Y} -- : {%m} -- : {%d}---'))
yyyy = int(NOW.strftime('%Y'))
mm =  int(NOW.strftime('%m'))
dd = int(NOW.strftime('%d'))

a.title("- Calender -")
a.geometry('600x410')
a.configure(bg='gray')
a.resizable(0,0)

Widget = Calendar(a,year=yyyy,month=mm,day=dd,font=("Arial 14",25,'bold'))
Widget.pack(pady=20)

a.mainloop()