from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
import pymysql
from PIL import ImageTk

def connect_database():
    if eventEntry.get() == '' or activityEntry.get() == '' or part_Combobox.get() == '':
        messagebox.showerror('Error','  Please Fill the necessary details!!')
    else:
        try:
            con=pymysql.connect(host='157.0.0.1',user='root',password='Harshita@030715')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not Established')
            return
        try:
            query = 'use cv_generator'
            mycursor.execute(query)
            query='CREATE TABLE `extra_curricular`(`email_id`VARCHAR(255) , `event_name` VARCHAR(255) NOT NULL, `activity_name` VARCHAR(255) NOT NULL, `participation_level` VARCHAR(255) NOT NULL, `rank` VARCHAR(255) NOT NULL, `description` VARCHAR(255) ) ENGINE=InnoDB;'

            mycursor.execute(query)

        except:
            query = '''insert into 'extra_curricular'('event_name','activity_name','participation_level','rank','description') values (%s,%s,%s,%s,%s))'''
            mycursor.execute(query, (eventEntry.get(), activityEntry.get(), part_Combobox.get(),rankEntry.get()))
            con.commit()
            con.close()




extracurricular=Tk()    #700x400+300+200
extracurricular.title("Extra Curricular")
#extracurricular.geometry('700x400+300+200')
extracurricular.geometry("{0}x{1}+0+0".format(extracurricular.winfo_screenwidth(), extracurricular.winfo_screenheight()))
extracurricular.resizable(False,False)
extracurricular.configure(bg='light grey')
icon_image=PhotoImage(file="extra.png")
extracurricular.iconphoto(False,icon_image)
eventLabel=Label(extracurricular,text='Event Name',font=('sifon',15,'bold'),bg='light grey',fg='black')
eventLabel.place(x=80,y=150)

eventEntry=Entry(extracurricular,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
eventEntry.place(x=200,y=150)
background=ImageTk.PhotoImage(file='excurricularform.png')

bgLabel=Label(extracurricular,image=background)
bgLabel.config(width=700, height=700)
bgLabel.place(x=750,y=40)
Label(extracurricular,text='Unleash your creativity with extracurricular activities!',font=("arial 13",16,'bold'),bg="light grey",fg="black").place(x=100,y=50)


activityLabel=Label(extracurricular,text='Activities',font=('sifon',15,'bold'),bg='light grey',fg='black')
activityLabel.place(x=70,y=250)
activityEntry=Entry(extracurricular,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
activityEntry.place(x=200,y=250)
participationLabel=Label(extracurricular,text='Participation Level',font=('sifon',15,'bold'),bg='light grey',fg='black')
participationLabel.place(x=30,y=350)
part_Combobox=Combobox(extracurricular,values=['Volunteer','Participant'],font=('sifon',15,'bold'),state='r',width=14)
part_Combobox.place(x=210,y=350)
part_Combobox.set('Participant')
rankLabel=Label(extracurricular,text='Rank',font=('sifon',15,'bold'),bg='light grey',fg='black')
rankLabel.place(x=470,y=350)
rankEntry=Entry(extracurricular,width=14,font=('sifon',15,'bold'),fg='black',bg='white')
rankEntry.place(x=540,y=350)
#descLabel=Label(extracurricular,text='Description',font=('sifon',15,'bold'),bg='light grey',fg='black')
#descLabel.place(x=50,y=250)
#descEntry = Text(extracurricular,width=50,height=4,bd=4)
#descEntry.place(x=200,y=250)
signupButton=Button(extracurricular,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='blue',activeforeground='white',width=10, command=connect_database)

signupButton.place(x=300,y=500)

nameValue = StringVar()
activityValue=StringVar()

extracurricular.mainloop()


