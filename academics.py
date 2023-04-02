from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib
import pymysql
from PIL import ImageTk


def connect_database():
    if part_Combobox.get() == '' or semEntry.get() == '' or CGPIEntry.get() == '':
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
            query='CREATE TABLE `academics`(`email_id` VARCHAR(255) NULL,`year_of_study` VARCHAR(255) NOT NULL,`sem` VARCHAR(255) NOT NULL,`cgpi` VARCHAR(255) NOT NULL,UNIQUE INDEX `year_of_study_UNIQUE`(`year_of_study`ASC) VISIBLE,UNIQUE INDEX `sem_UNIQUE`(`sem` ASC) VISIBLE);'

            mycursor.execute(query)

        except:

            query = '''insert into 'academics'('year_of_study','sem','cgpi') values (%s,%s,%s))'''
            mycursor.execute(query, (part_Combobox.get(), semEntry.get(), CGPIEntry.get()))
            con.commit()
            con.close()




academics=Tk()    #700x400+300+200
academics.title("Academics")
#academics.geometry('700x400+300+200')
academics.geometry("{0}x{1}+0+0".format(academics.winfo_screenwidth(), academics.winfo_screenheight()))
academics.resizable(False,False)
academics.configure(bg='light grey')
background=ImageTk.PhotoImage(file='acedemicsform.png')

bgLabel=Label(academics,image=background)
bgLabel.config(width=700, height=700)
bgLabel.place(x=750,y=40)
icon_image=PhotoImage(file="extra.png")
academics.iconphoto(False,icon_image)
yearofstudyLabel=Label(academics,text='Year of Study',font=('sifon',15,'bold'),bg='light grey',fg='black')
yearofstudyLabel.place(x=200,y=150)
part_Combobox=Combobox(academics,values=['First year','Second year','Third year','Fourth year'],font=('sifon',15,'bold'),state='r',width=14)
part_Combobox.place(x=380,y=150)
part_Combobox.set('First year')

# yearofstudyEntry=Entry(academics,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
# yearofstudyEntry.place(x=200,y=100)
Label(academics,text='Value your academics !!',font=("arial 13",16,'bold'),bg="light grey",fg="black").place(x=300,y=50)

# x=200,y=150
CGPILabel=Label(academics,text='CGPI',font=('sifon',15,'bold'),bg='light grey',fg='black')
CGPILabel.place(x=280,y=250)
CGPIEntry=Entry(academics,width=13,font=('sifon',15,'bold'),fg='black',bg='white')
CGPIEntry.place(x=380,y=250)
semLabel=Label(academics,text='Sem',font=('sifon',15,'bold'),bg='light grey',fg='black')
semLabel.place(x=280,y=350)
semEntry=Combobox(academics,values=['Sem I','Sem II','Sem III','Sem IV','Sem V','Sem VI','Sem VII','Sem VIII'],font=('sifon',15,'bold'),state='r',width=14)
semEntry.place(x=380,y=350)
semEntry.set('Sem I')
# rankLabel=Label(academics,text='Rank',font=('sifon',15,'bold'),bg='light grey',fg='black')
# rankLabel.place(x=400,y=200)
# rankEntry=Entry(academics,width=14,font=('sifon',15,'bold'),fg='black',bg='white')
# rankEntry.place(x=450,y=200)
# descLabel=Label(academics,text='Description',font=('sifon',15,'bold'),bg='light grey',fg='black')
# descLabel.place(x=50,y=250)
# descEntry = Text(academics,width=50,height=4,bd=4)
# descEntry.place(x=200,y=250)
signupButton=Button(academics,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                    fg='white',activebackground='blue',activeforeground='white',width=10, command=connect_database)

signupButton.place(x=300,y=500)

nameValue = StringVar()
activityValue=StringVar()

academics.mainloop()


