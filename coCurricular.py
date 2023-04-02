from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
from PIL import ImageTk

cocurricular=Tk()    #700x400+300+200
cocurricular.title("Co-Curricular")
#cocurricular.geometry('700x400+300+200')
cocurricular.geometry("{0}x{1}+0+0".format(cocurricular.winfo_screenwidth(), cocurricular.winfo_screenheight()))
cocurricular.resizable(False,False)
cocurricular.configure(bg='light grey')
background=ImageTk.PhotoImage(file='cocurricularfimg.png')

bgLabel=Label(cocurricular,image=background)
bgLabel.config(width=700, height=700)
bgLabel.place(x=750,y=40)
icon_image=PhotoImage(file="co.png")
cocurricular.iconphoto(False,icon_image)
activityLabel=Label(cocurricular,text='Activity',font=('sifon',15,'bold'),bg='light grey',fg='black')
activityLabel.place(x=80,y=150)
activity_Combobox=Combobox(cocurricular,values=['Workshop','Hackathon'],font=('sifon',15,'bold'),state='r',width=14)
activity_Combobox.place(x=200,y=150)
activity_Combobox.set('Workshop')


Label(cocurricular,text='Co-curricular – discovering what’s possible....',font=('sifon',20,'bold'),bg="light grey",fg="black").place(x=90,y=40)


conductLabel=Label(cocurricular,text='Conduced By ',font=('sifon',15,'bold'),bg='light grey',fg='black')
conductLabel.place(x=50,y=250)
conductEntry=Entry(cocurricular,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
conductEntry.place(x=200,y=250)
participationLabel=Label(cocurricular,text='Participation Level',font=('sifon',15,'bold'),bg='light grey',fg='black')
participationLabel.place(x=30,y=350)
part_Combobox=Combobox(cocurricular,values=['Volunteer','Participant'],font=('sifon',15,'bold'),state='r',width=14)
part_Combobox.place(x=210,y=350)
part_Combobox.set('Participant')
#descLabel=Label(cocurricular,text='Description',font=('Sifon',15,'bold'),bg='light grey',fg='black')
#descLabel.place(x=80,y=450)
#descEntry = Text(cocurricular,width=50,height=6,bd=4)
#descEntry.place(x=200,y=450)
signupButton=Button(cocurricular,text='Submit',font=('sifon',15,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='light grey',activeforeground='white',width=10, )
#command=connect_database
signupButton.place(x=300,y=500)


nameValue = StringVar()
activityValue=StringVar()

cocurricular.mainloop()


