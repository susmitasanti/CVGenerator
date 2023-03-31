from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib

cocurricular=Tk()    #700x400+300+200
cocurricular.title("Co-Curricular")
cocurricular.geometry('700x400+300+200')
cocurricular.resizable(False,False)
cocurricular.configure(bg='#FF3030')
icon_image=PhotoImage(file="co.png")
cocurricular.iconphoto(False,icon_image)
activityLabel=Label(cocurricular,text='Activity',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
activityLabel.place(x=50,y=100)
activity_Combobox=Combobox(cocurricular,values=['Workshop','Hackathon'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
activity_Combobox.place(x=200,y=100)
activity_Combobox.set('Workshop')


Label(cocurricular,text='Co-curricular – discovering what’s possible....',font=('arial 13',16,'bold'),bg="#FF3030",fg="#fff").place(x=150,y=20)


conductLabel=Label(cocurricular,text='Conduced By ',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
conductLabel.place(x=50,y=150)
conductEntry=Entry(cocurricular,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
conductEntry.place(x=200,y=150)
participationLabel=Label(cocurricular,text='Participation Level',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
participationLabel.place(x=40,y=200)
part_Combobox=Combobox(cocurricular,values=['Volunteer','Participant'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
part_Combobox.place(x=210,y=200)
part_Combobox.set('Participant')
descLabel=Label(cocurricular,text='Description',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
descLabel.place(x=50,y=250)
descEntry = Text(cocurricular,width=50,height=4,bd=4)
descEntry.place(x=200,y=250)

nameValue = StringVar()
activityValue=StringVar()

cocurricular.mainloop()


