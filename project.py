from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib




project=Tk()    #700x400+300+200
project.title("project")
project.geometry('700x400+300+200')
project.resizable(False,False)
project.configure(bg='#FF3030')
icon_image=PhotoImage(file="co.png")
project.iconphoto(False,icon_image)
nameLabel=Label(project,text='Project Name',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
nameLabel.place(x=50,y=100)
nameEntry=Entry(project,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
nameEntry.place(x=200,y=100)




Label(project,text='Skills for the real world!!',font=('arial 13',16,'bold'),bg="#FF3030",fg="#fff").place(x=200,y=20)


domainLabel=Label(project,text='Domain',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
domainLabel.place(x=50,y=150)
domainEntry=Entry(project,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
domainEntry.place(x=200,y=150)
fromLabel=Label(project,text='From',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
fromLabel.place(x=50,y=200)

toLabel=Label(project,text='To',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
toLabel.place(x=350,y=200)


descLabel=Label(project,text='Description',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
descLabel.place(x=50,y=250)
descEntry = Text(project,width=50,height=4,bd=4)
descEntry.place(x=200,y=250)

nameValue = StringVar()
activityValue=StringVar()

project.mainloop()


