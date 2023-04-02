from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
import pymysql


def connect_database():
    if part_Combobox.get() == '' or semEntry.get() == '' or CGPIEntry.get() == '':
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
            query='CREATE TABLE `academics`(`email_id` VARCHAR(255) NULL,`year_of_study` VARCHAR(255) NOT NULL,`sem` VARCHAR(255) NOT NULL,`cgpi` VARCHAR(255) NOT NULL,UNIQUE INDEX `year_of_study_UNIQUE`(`year_of_study`ASC) VISIBLE,UNIQUE INDEX `sem_UNIQUE`(`sem` ASC) VISIBLE);'

            mycursor.execute(query)

        except:

            query = '''insert into 'academics'('year_of_study','sem','cgpi') values (%s,%s,%s))'''
            mycursor.execute(query, (part_Combobox.get(), semEntry.get(), CGPIEntry.get()))
            con.commit()
            con.close()




academics=Tk()    #700x400+300+200
academics.title("Academics")
academics.geometry('700x400+300+200')
academics.resizable(False,False)
academics.configure(bg='#00BFFF')
icon_image=PhotoImage(file="extra.png")
academics.iconphoto(False,icon_image)
yearofstudyLabel=Label(academics,text='Year of Study',font=('Microsoft Yahei UI Light',12,'bold'),bg='#00BFFF',fg='#fff')
yearofstudyLabel.place(x=50,y=100)
part_Combobox=Combobox(academics,values=['First year','Second year','Third year','Fourth year'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
part_Combobox.place(x=200,y=100)
part_Combobox.set('First year')

# yearofstudyEntry=Entry(academics,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
# yearofstudyEntry.place(x=200,y=100)
Label(academics,text='Value your academics !!',font=("arial 13",16,'bold'),bg="#00BFFF",fg="#fff").place(x=100,y=20)

# x=200,y=150
CGPILabel=Label(academics,text='CGPI',font=('Microsoft Yahei UI Light',12,'bold'),bg='#00BFFF',fg='#fff')
CGPILabel.place(x=50,y=200)
CGPIEntry=Entry(academics,width=13,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
CGPIEntry.place(x=200,y=200)
semLabel=Label(academics,text='Sem',font=('Microsoft Yahei UI Light',12,'bold'),bg='#00BFFF',fg='#fff')
semLabel.place(x=50,y=150)
semEntry=Combobox(academics,values=['Sem I','Sem II','Sem III','Sem IV','Sem V','Sem VI','Sem VII','Sem VIII'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
semEntry.place(x=200,y=150)
semEntry.set('Sem I')
# rankLabel=Label(academics,text='Rank',font=('Microsoft Yahei UI Light',12,'bold'),bg='#00BFFF',fg='#fff')
# rankLabel.place(x=400,y=200)
# rankEntry=Entry(academics,width=14,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
# rankEntry.place(x=450,y=200)
# descLabel=Label(academics,text='Description',font=('Microsoft Yahei UI Light',12,'bold'),bg='#00BFFF',fg='#fff')
# descLabel.place(x=50,y=250)
# descEntry = Text(academics,width=50,height=4,bd=4)
# descEntry.place(x=200,y=250)
signupButton=Button(academics,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='blue',activeforeground='white',width=10, command=connect_database)

signupButton.place(x=300,y=350)

nameValue = StringVar()
activityValue=StringVar()

academics.mainloop()


