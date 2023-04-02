from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
from tkcalendar import DateEntry
from PIL import ImageTk

def on_date_change():
    date = cal.get_date()
    print(f"Selected date: {date}")



internship=Tk()    #700x400+300+200
internship.title("Internship")
#internship.geometry('700x400+300+200')
internship.geometry("{0}x{1}+0+0".format(internship.winfo_screenwidth(), internship.winfo_screenheight()))
background=ImageTk.PhotoImage(file='intershipform.png')

bgLabel=Label(internship,image=background)
bgLabel.config(width=700, height=700)
bgLabel.place(x=750,y=40)
internship.resizable(False,False)
internship.configure(bg='light grey')
icon_image=PhotoImage(file="co.png")
internship.iconphoto(False,icon_image)
nameLabel=Label(internship,text='Intership Name',font=('sifon',15,'bold'),bg='light grey',fg='black')
nameLabel.place(x=180,y=190)
nameEntry=Entry(internship,width=35,font=('sifon',15,'bold'),fg='black',bg='white')
nameEntry.place(x=330,y=190)




Label(internship,text='Skills for the real world!!',font=('arial 13',16,'bold'),bg="light grey",fg="black").place(x=400,y=50)


domainLabel=Label(internship,text='Domain',font=('sifon',15,'bold'),bg='light grey',fg='black')
domainLabel.place(x=200,y=250)
domainEntry=Entry(internship,width=35,font=('sifon',15,'bold'),fg='black',bg='white')
domainEntry.place(x=330,y=250)
fromLabel=Label(internship,text='From',font=('sifon',15,'bold'),bg='light grey',fg='black')
fromLabel.place(x=200,y=300)
cal = DateEntry(internship, width=10, background='darkblue',foreground='white', borderwidth=2, year=2023,font=('sifon',15,'bold'))
cal.place(x=330,y=300)
cal.bind("<<DateEntrySelected>>", on_date_change)
toLabel=Label(internship,text='To',font=('sifon',15,'bold'),bg='light grey',fg='black')
toLabel.place(x=510,y=300)
cal1 = DateEntry(internship, width=10, background='darkblue',foreground='white', borderwidth=2, year=2023,font=('sifon',15,'bold'))
cal1.place(x=590,y=300)
cal1.bind("<<DateEntrySelected>>", on_date_change)

descLabel=Label(internship,text='Description',font=('sifon',15,'bold'),bg='light grey',fg='black')
descLabel.place(x=200,y=350)
descEntry = Text(internship,width=50,height=4,bd=4)
descEntry.place(x=330,y=350)
signupButton=Button(internship,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='blue',activeforeground='white',width=10)

signupButton.place(x=300,y=500)


nameValue = StringVar()
activityValue=StringVar()

internship.mainloop()


