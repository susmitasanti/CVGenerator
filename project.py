from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
from PIL import ImageTk



project=Tk()    #700x400+300+200
project.title("project")
#project.geometry('700x400+300+200')
project.geometry("{0}x{1}+0+0".format(project.winfo_screenwidth(), project.winfo_screenheight()))
background=ImageTk.PhotoImage(file='projectform.png')

bgLabel=Label(project,image=background)
bgLabel.config(width=700, height=700)
bgLabel.place(x=750,y=40)
project.resizable(False,False)
project.configure(bg='light grey')
icon_image=PhotoImage(file="co.png")
project.iconphoto(False,icon_image)
nameLabel=Label(project,text='Project Name',font=('sifon',15,'bold'),bg='light grey',fg='black')
nameLabel.place(x=50,y=100)
nameEntry=Entry(project,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
nameEntry.place(x=200,y=100)




Label(project,text='Skills for the real world!!',font=('arial 13',16,'bold'),bg="light grey",fg="black").place(x=200,y=20)


domainLabel=Label(project,text='Domain',font=('sifon',15,'bold'),bg='light grey',fg='black')
domainLabel.place(x=50,y=150)
domainEntry=Entry(project,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
domainEntry.place(x=200,y=150)
#fromLabel=Label(project,text='From',font=('sifon',12,'bold'),bg='light grey',fg='black')
#fromLabel.place(x=50,y=200)

#toLabel=Label(project,text='To',font=('sifon',12,'bold'),bg='light grey',fg='black')
#toLabel.place(x=350,y=200)


descLabel=Label(project,text='Description',font=('sifon',15,'bold'),bg='light grey',fg='black')
descLabel.place(x=50,y=250)
descEntry = Text(project,width=50,height=4,bd=4)
descEntry.place(x=200,y=250)
signupButton=Button(project,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='blue',activeforeground='white',width=10)

signupButton.place(x=300,y=500)


nameValue = StringVar()
activityValue=StringVar()

project.mainloop()


