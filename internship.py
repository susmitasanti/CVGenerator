from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
from tkcalendar import DateEntry

def on_date_change():
    date = cal.get_date()
    print(f"Selected date: {date}")



internship=Tk()    #700x400+300+200
internship.title("Internship")
internship.geometry('700x400+300+200')
internship.resizable(False,False)
internship.configure(bg='#FF3030')
icon_image=PhotoImage(file="co.png")
internship.iconphoto(False,icon_image)
nameLabel=Label(internship,text='Intership Name',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
nameLabel.place(x=50,y=100)
nameEntry=Entry(internship,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
nameEntry.place(x=200,y=100)




Label(internship,text='Skills for the real world!!',font=('arial 13',16,'bold'),bg="#FF3030",fg="#fff").place(x=200,y=20)


domainLabel=Label(internship,text='Domain',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
domainLabel.place(x=50,y=150)
domainEntry=Entry(internship,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
domainEntry.place(x=200,y=150)
fromLabel=Label(internship,text='From',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
fromLabel.place(x=50,y=200)
cal = DateEntry(internship, width=12, background='darkblue',foreground='white', borderwidth=2, year=2023)
cal.place(x=200,y=200)
cal.bind("<<DateEntrySelected>>", on_date_change)
toLabel=Label(internship,text='To',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
toLabel.place(x=350,y=200)
cal1 = DateEntry(internship, width=12, background='darkblue',foreground='white', borderwidth=2, year=2023)
cal1.place(x=450,y=200)
cal1.bind("<<DateEntrySelected>>", on_date_change)

descLabel=Label(internship,text='Description',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
descLabel.place(x=50,y=250)
descEntry = Text(internship,width=50,height=4,bd=4)
descEntry.place(x=200,y=250)

nameValue = StringVar()
activityValue=StringVar()

internship.mainloop()


