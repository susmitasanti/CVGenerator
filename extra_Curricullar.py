from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
import pymysql

def connect_database():
    if eventEntry.get() == '' or activityEntry.get() == '' or part_Combobox.get() == '':
        messagebox.showerror('Error','  Please Fill the necessary details!!')
    else:
        try:
            con=pymysql.connect(host='127.0.0.1',user='root',password='Harshita@030712')
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
            mycursor.execute(query, (eventEntry.get(), activityEntry.get(), part_Combobox.get(),rankEntry.get(),descEntry.get("1.0", "end-1c")))
            con.commit()
            con.close()




extracurricular=Tk()    #700x400+300+200
extracurricular.title("Extra Curricular")
extracurricular.geometry('700x400+300+200')
extracurricular.resizable(False,False)
extracurricular.configure(bg='#FF3030')
icon_image=PhotoImage(file="extra.png")
extracurricular.iconphoto(False,icon_image)
eventLabel=Label(extracurricular,text='Event Name',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
eventLabel.place(x=50,y=100)

eventEntry=Entry(extracurricular,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
eventEntry.place(x=200,y=100)
Label(extracurricular,text='Unleash your creativity with extracurricular activities!',font=("arial 13",16,'bold'),bg="#FF3030",fg="#fff").place(x=100,y=20)


activityLabel=Label(extracurricular,text='Activities',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
activityLabel.place(x=50,y=150)
activityEntry=Entry(extracurricular,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
activityEntry.place(x=200,y=150)
participationLabel=Label(extracurricular,text='Participation Level',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
participationLabel.place(x=40,y=200)
part_Combobox=Combobox(extracurricular,values=['Volunteer','Participant'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
part_Combobox.place(x=210,y=200)
part_Combobox.set('Participant')
rankLabel=Label(extracurricular,text='Rank',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
rankLabel.place(x=400,y=200)
rankEntry=Entry(extracurricular,width=14,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
rankEntry.place(x=450,y=200)
descLabel=Label(extracurricular,text='Description',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
descLabel.place(x=50,y=250)
descEntry = Text(extracurricular,width=50,height=4,bd=4)
descEntry.place(x=200,y=250)
signupButton=Button(extracurricular,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='blue',activeforeground='white',width=10, command=connect_database)

signupButton.place(x=300,y=350)

nameValue = StringVar()
activityValue=StringVar()

extracurricular.mainloop()


