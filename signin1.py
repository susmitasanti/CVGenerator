# signin.py

from tkinter import *
from tkinter import Tk

import pymysql
from PIL import ImageTk #pip install pillow
# import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.ttk import Combobox

username_ = ""
openeye=""
passwordEntry=""
eyeButton=""
usernameEntry=""
tree=""
connection=""
cursor=""
data=""

login_page=""
login_window=""

dashboard_page=""

internship_page=""
internship_window=""

academics_page=""
academics_window=""

cocurricular_page=""
cocurricular_window=""
cocurricular=""

extracurricular_page=""
extracurricular_window=""

projects_page=""
projects_window=""

academics_part_Combobox=""
academics_CGPIEntry=""
academics_semEntry=""

eventEntry=""
activity_Combobox=""
conductEntry=""
part_Combobox=""
rankEntry=""

extra_eventEntry=""
extra_activityEntry=""
extra_part_Combobox=""
extra_rankLabel=""
extra_rankEntry=""

titleEntry=""
describeEntry=""
addressEntry=""
gitEntry=""
linkedInEntry=""
skill1_Entry=""
skill2_Entry=""
skill3_Entry=""
skill4_Entry=""
skill5_Entry=""
skill6_Entry=""
resume_nameEntry=""

signup_window=""
signup_nameEntry=""
signup_ageEntry=""
signup_emailEntry=""
signup_phoneEntry=""
signup_genEntry=""
signup_degreeEntry=""
signup_branchEntry=""
signup_start_year=""
signup_end_year=""
signup_passwordEntry=""
signup_confirm_PasswordEntry=""
check=""
clear=""

add_info=""
add_information=""

name=""
age =""
phone_no=""
gender=""
branch=""
degree=""
from_date=""
to_date=""

project_1_name=""
project_1_desc=""
project_2_name=""
project_2_desc=""
project_3_name=""
project_4_name=""

internship_1_name=""
internship_1_desc=""
internship_1_from=""
internship_1_to=""
internship_2_name=""
internship_2_desc=""
internship_2_from=""
internship_2_to=""
internship_3_name=""
internship_3_desc=""
internship_3_from=""
internship_3_to=""

internship=""
internship_nameEntry=""
internship_domainEntry=""
internship_fromEntry=""
internship_toEntry=""
internship_descEntry=""

project=""
project_nameEntry=""
project_techstackEntry=""
project_descEntry=""
 
def set_username(name):
    global signin
    global username
    username = name
    print(name)

def signup_page():
        global login_window
        global signup
        login_window.destroy()
        signup()   

def hide():
        global openeye
        global passwordEntry
        global eyeButton
        openeye.config(file='closeye.png')
        passwordEntry.config(show='*')
        eyeButton.config(command=show)

def show():
        global openeye
        global passwordEntry
        global eyeButton
        openeye.config(file='openeye.png')
        passwordEntry.config(show='')
        eyeButton.config(command=hide)

def user_enter(event):
        global usernameEntry
        if usernameEntry.get()=='Email-id':
            usernameEntry.delete(0,END)

def password_enter(event):
        global passwordEntry
        if passwordEntry.get()=='Password':
            passwordEntry.delete(0,END)    

def handle_click(page):
        global dashboard_window
        global dash_page
        global academics_page
        global cocurricular_page
        global extracurricular_page
        global internship_page
        global projects_page

        if (page == "internship_page"):           
            dashboard_window.destroy()
            internship_page()
        elif (page == "academics_page"):
            dashboard_window.destroy()
            academics_page()
        elif (page == "cocurricular_page"):
            dashboard_window.destroy()
            cocurricular_page()
        elif (page == "extracurricular_page"):
            dashboard_window.destroy()
            extracurricular_page()
        elif (page == "projects_page"):
            dashboard_window.destroy()
            projects_page()
        elif (page=="dashboard_page"):
             dashboard_window.destroy()
             dashboard_page()

def handle_click1(page):
            global academics_window
            global dashboard_page
            global academics_page
            global cocurricular_page
            global extracurricular_page
            global internship_page
            global projects_page

            if (page == "internship_page"):
                academics_window.destroy()
                internship_page()
            elif (page == "academics_page"):
                academics_window.destroy()
                academics_page()
            elif (page == "cocurricular_page"):
                academics_window.destroy()
                cocurricular_page()
            elif (page == "extracurricular_page"):
                academics_window.destroy()
                extracurricular_page()
            elif (page == "projects_page"):
                academics_window.destroy()
                projects_page()
            elif (page == "dashboard_page"):
                 academics_window.destroy()
                 dashboard_page()

def handle_click2(page):
            global cocurricular_window
            global dashboard_page
            global academics_page
            global cocurricular_page
            global extracurricular_page
            global internship_page
            global projects_page

            if (page == "internship_page"):
                cocurricular_window.destroy()
                internship_page()
            elif (page == "academics_page"):
                cocurricular_window.destroy()
                academics_page()
            elif (page == "cocurricular_page"):
                cocurricular_window.destroy()
                cocurricular_page()
            elif (page == "extracurricular_page"):
                cocurricular_window.destroy()
                extracurricular_page()
            elif (page == "projects_page"):
                cocurricular_window.destroy()
                projects_page()
            elif (page == "dashboard_page"):
                 cocurricular_window.destroy()
                 dashboard_page()

def handle_click3(page):
    global extracurricular_window
    global dashboard_page
    global academics_page
    global cocurricular_page
    global extracurricular_page
    global internship_page
    global projects_page

    if (page == "internship_page"):
        extracurricular_window.destroy()
        internship_page()
    elif (page == "academics_page"):
        extracurricular_window.destroy()
        academics_page()
    elif (page == "cocurricular_page"):
        extracurricular_window.destroy()
        cocurricular_page()
    elif (page == "extracurricular_page"):
        extracurricular_window.destroy()
        extracurricular_page()
    elif (page == "projects_page"):
        extracurricular_window.destroy()
        projects_page()
    elif (page == "dashboard_page"):
         extracurricular_window.destroy()
         dashboard_page()

def handle_click4(page):
    global internship_window
    global dashboard_page
    global academics_page
    global cocurricular_page
    global extracurricular_page
    global internship_page
    global projects_page

    if (page == "internship_page"):
        internship_window.destroy()
        internship_page()
    elif (page == "academics_page"):
        internship_window.destroy()
        academics_page()
    elif (page == "cocurricular_page"):
        internship_window.destroy()
        cocurricular_page()
    elif (page == "extracurricular_page"):
        internship_window.destroy()
        extracurricular_page()
    elif (page == "projects_page"):
        internship_window.destroy()
        projects_page()
    elif (page == "dashboard_page"):
         internship_window.destroy()
         dashboard_page()

def handle_click5(page):
    global projects_window
    global dashboard_page
    global academics_page
    global cocurricular_page
    global extracurricular_page
    global internship_page
    global projects_page

    if (page == "internship_page"):
        projects_window.destroy()
        internship_page()
    elif (page == "academics_page"):
        projects_window.destroy()
        academics_page()
    elif (page == "cocurricular_page"):
        projects_window.destroy()
        cocurricular_page()
    elif (page == "extracurricular_page"):
        projects_window.destroy()
        extracurricular_page()
    elif (page == "projects_page"):
        projects_window.destroy()
        projects_page()
    elif (page == "dashboard_page"):
         projects_window.destroy()
         dashboard_page()


def academics_execute():
    global academics_part_Combobox
    global academics_CGPIEntry
    global academics_semEntry

    cursor = connection.cursor()

    cursor.execute('''INSERT INTO `academics`(`email_id`, `year_of_study`, `sem`, `cgpi`) VALUES (%s,%s,%s,%s)''', ((username_), academics_part_Combobox.get(), academics_semEntry.get(), academics_CGPIEntry.get()))

    connection.commit() 

def plus_academics():
    global academics_part_Combobox
    global academics_CGPIEntry
    global academics_semEntry

    academics=Tk()    #700x400+300+200
    academics.title("Academics")
    academics.geometry('700x400+300+200')
    academics.resizable(False,False)
    academics.configure(bg='light blue')
    # icon_image=PhotoImage(file="extra.png")
    # academics.iconphoto(False,icon_image)
    yearofstudyLabel=Label(academics,text='Year of Study',font=('sifon',12,'bold'),bg='light blue',fg='black')
    yearofstudyLabel.place(x=50,y=100)
    academics_part_Combobox=Combobox(academics,values=['First year','Second year','Third year','Fourth year'],font=('sifon',10,'bold'),state='r',width=14)
    academics_part_Combobox.place(x=200,y=100)
    academics_part_Combobox.set('First year')

    # yearofstudyEntry=Entry(academics,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    # yearofstudyEntry.place(x=200,y=100)
    Label(academics,text='Value your academics !!',font=("arial 13",16,'bold'),bg="light blue",fg="black").place(x=100,y=20)

    # x=200,y=150
    CGPILabel=Label(academics,text='CGPI',font=('sifon',12,'bold'),bg='light blue',fg='black')
    CGPILabel.place(x=50,y=200)
    academics_CGPIEntry=Entry(academics,width=13,font=('sifon',12,'bold'),fg='black',bg='white')
    academics_CGPIEntry.place(x=200,y=200)
    semLabel=Label(academics,text='Sem',font=('sifon',12,'bold'),bg='light blue',fg='black')
    semLabel.place(x=50,y=150)
    academics_semEntry=Combobox(academics,values=['Sem I','Sem II','Sem III','Sem IV','Sem V','Sem VI','Sem VII','Sem VIII'],font=('sifon',10,'bold'),state='r',width=14)
    academics_semEntry.place(x=200,y=150)
    academics_semEntry.set('Sem I')
    signupButton=Button(academics,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                        fg='white',activebackground='blue',activeforeground='white',width=10, command=academics_execute)

    signupButton.place(x=300,y=350)

    academics.mainloop()

def cocurricular_execute():
    global username_
    global activity_Combobox
    global eventEntry
    global conductEntry
    global part_Combobox
    global rankEntry
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO `cocurricular`(`email_id`, `event_name`, `activity_name`, `conducted_by`, `participation_level`, `rank`) VALUES (%s,%s,%s,%s,%s,%s)''', ((username_), eventEntry.get(), activity_Combobox.get(), conductEntry.get(), part_Combobox.get(), rankEntry.get()))

    connection.commit()  
    # connection.close()
     
def plus_cocurricular():
        global activity_Combobox
        global eventEntry
        global conductEntry
        global part_Combobox
        global rankEntry

        cocurricular=Tk()    #700x400+300+200
        cocurricular.title("Co-Curricular")
        cocurricular.geometry('700x400+300+200')
        cocurricular.resizable(False,False)
        cocurricular.configure(bg='light blue')
        # icon_image=PhotoImage(file="co.png")
        # cocurricular.iconphoto(False,icon_image)
        eventLabel=Label(cocurricular,text='Event Name ',font=('sifon',12,'bold'),bg='light blue',fg='black')
        eventLabel.place(x=50,y=100)
        eventEntry=Entry(cocurricular,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        eventEntry.place(x=200,y=100)

        activityLabel=Label(cocurricular,text='Activity',font=('sifon',12,'bold'),bg='light blue',fg='black')
        activityLabel.place(x=50,y=150)
        activity_Combobox=Combobox(cocurricular,values=['Workshop','Hackathon'],font=('sifon',10,'bold'),state='r',width=14)
        activity_Combobox.place(x=200,y=150)
        activity_Combobox.set('Workshop')
        Label(cocurricular,text='Co-curricular – discovering what’s possible....',font=('arial 13',16,'bold'),bg="light blue",fg="black").place(x=150,y=20)
        
        conductLabel=Label(cocurricular,text='Conducted By ',font=('sifon',12,'bold'),bg='light blue',fg='black')
        conductLabel.place(x=50,y=200)
        conductEntry=Entry(cocurricular,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        conductEntry.place(x=200,y=200)
        participationLabel=Label(cocurricular,text='Participation Level',font=('sifon',12,'bold'),bg='light blue',fg='black')
        participationLabel.place(x=50,y=250)
        part_Combobox=Combobox(cocurricular,values=['Volunteer','Participant'],font=('sifon',10,'bold'),state='r',width=14)
        part_Combobox.place(x=210,y=250)
        part_Combobox.set('Participant')
        rankLabel=Label(cocurricular,text='Rank',font=('sifon',12,'bold'),bg='light blue',fg='black')
        rankLabel.place(x=50,y=300)
        rankEntry=Entry(cocurricular,width=10,font=('sifon',12,'bold'),fg='black',bg='white')
        rankEntry.place(x=200,y=300)

        signupButton=Button(cocurricular,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',fg='white',activebackground='blue',activeforeground='white',width=10, command=cocurricular_execute)
        signupButton.place(x=300,y=350)

        cocurricular.mainloop()

def extracurricular_execute():
    global username_
    global extra_eventEntry
    global extra_activityEntry
    global extra_part_Combobox
    global extra_rankEntry
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO `extra_curricular`(`email_id`, `event_name`, `activity_name`, `participation_level`, `rank`) VALUES (%s,%s,%s,%s,%s)''', ((username_), extra_eventEntry.get(), extra_activityEntry.get(), extra_part_Combobox.get(), extra_rankEntry.get()) )

    connection.commit()  
    # connection.close()
     
def plus_extracurricular():
        global extracurricular
        global username_
        global extra_eventEntry
        global extra_activityEntry
        global extra_part_Combobox
        global extra_rankEntry
        extracurricular=Tk()    #700x400+300+200
        extracurricular.title("Extra Curricular")
        extracurricular.geometry('700x400+300+200')
        extracurricular.resizable(False,False)
        extracurricular.configure(bg='light blue')
        # icon_image=PhotoImage(file="extra.png")
        # extracurricular.iconphoto(False,icon_image)

        extra_eventLabel=Label(extracurricular,text='Event Name',font=('sifon',12,'bold'),bg='light blue',fg='black')
        extra_eventLabel.place(x=50,y=100)

        extra_eventEntry=Entry(extracurricular,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        extra_eventEntry.place(x=200,y=100)
        Label(extracurricular,text='Unleash your creativity with extracurricular activities!',font=("arial 13",16,'bold'),bg="light blue",fg="black").place(x=100,y=20)


        extra_activityLabel=Label(extracurricular,text='Activity Name',font=('sifon',12,'bold'),bg='light blue',fg='black')
        extra_activityLabel.place(x=50,y=150)

        extra_activityEntry=Entry(extracurricular,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        extra_activityEntry.place(x=200,y=150)

        extra_participationLabel=Label(extracurricular,text='Participation Level',font=('sifon',12,'bold'),bg='light blue',fg='black')
        extra_participationLabel.place(x=40,y=200)

        extra_part_Combobox=Combobox(extracurricular,values=['Volunteer','Participant'],font=('sifon',10,'bold'),state='r',width=14)
        extra_part_Combobox.place(x=210,y=200)
        extra_part_Combobox.set('Participant')

        extra_rankLabel=Label(extracurricular,text='Rank',font=('sifon',12,'bold'),bg='light blue',fg='black')
        extra_rankLabel.place(x=400,y=200)

        extra_rankEntry=Entry(extracurricular,width=14,font=('sifon',12,'bold'),fg='black',bg='white')
        extra_rankEntry.place(x=450,y=200)

        signupButton=Button(extracurricular,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                            fg='white',activebackground='blue',activeforeground='white',width=10, command=extracurricular_execute)

        signupButton.place(x=300,y=350)

        extracurricular.mainloop()

def internship_execute():
    global internship
    global username_
    global internship_nameEntry
    global internship_domainEntry
    global internship_fromEntry
    global internship_toEntry
    global internship_descEntry

    cursor = connection.cursor()

    cursor.execute('''INSERT INTO `internship`(`email_id`, `name`, `domain`, `description`, `from_date`, `to_date`) VALUES (%s,%s,%s,%s,%s,%s)''', ((username_), internship_nameEntry.get(), internship_domainEntry.get(), internship_descEntry.get("1.0", "end-1c"), internship_fromEntry.get(), internship_toEntry.get() ) )

    connection.commit()  
    # connection.close()

def plus_internship():
    global internship
    global username_
    global internship_nameEntry
    global internship_domainEntry
    global internship_fromEntry
    global internship_toEntry
    global internship_descEntry

    internship=Tk()    #700x400+300+200
    internship.title("Internship")
    internship.geometry('700x400+300+200')
    internship.resizable(False,False)
    internship.configure(bg='light blue')
    # icon_image=PhotoImage(file="co.png")
    # internship.iconphoto(False,icon_image)
    nameLabel=Label(internship,text='Intership Name',font=('sifon',12,'bold'),bg='light blue',fg='black')
    nameLabel.place(x=50,y=100)
    internship_nameEntry=Entry(internship,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    internship_nameEntry.place(x=200,y=100)

    Label(internship,text='Skills for the real world!!',font=('arial 13',16,'bold'),bg="light blue",fg="black").place(x=200,y=20)

    domainLabel=Label(internship,text='Domain',font=('sifon',12,'bold'),bg='light blue',fg='black')
    domainLabel.place(x=50,y=150)
    internship_domainEntry=Entry(internship,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    internship_domainEntry.place(x=200,y=150)
    fromLabel=Label(internship,text='From',font=('sifon',12,'bold'),bg='light blue',fg='black')
    fromLabel.place(x=50,y=200)
    internship_fromEntry = Entry(internship, width=12,font=('sifon',12,'bold'),fg='black',bg='white')
    internship_fromEntry.place(x=200,y=200)
    # cal.bind("<<DateEntrySelected>>", on_date_change)
    toLabel=Label(internship,text='To',font=('sifon',12,'bold'),bg='light blue',fg='black')
    toLabel.place(x=350,y=200)
    internship_toEntry = Entry(internship, width=12,font=('sifon',12,'bold'),fg='black',bg='white')
    internship_toEntry.place(x=450,y=200)
    # cal1.bind("<<DateEntrySelected>>", on_date_change)

    descLabel=Label(internship,text='Description',font=('sifon',12,'bold'),bg='light blue',fg='black')
    descLabel.place(x=50,y=250)
    internship_descEntry = Text(internship, height=3,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    internship_descEntry.place(x=200,y=250)

    internship_Button=Button(internship,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                            fg='white',activebackground='blue',activeforeground='white',width=10, command=internship_execute)

    internship_Button.place(x=300,y=350)

    internship.mainloop()

def project_execute():
    global project
    global username_
    global project_nameEntry
    global project_techstackEntry
    global project_descEntry
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO `projects`(`email_id`, `project_name`, `tech_stack`, `project_description`) VALUES (%s,%s,%s,%s)''', ((username_), project_nameEntry.get(), project_techstackEntry.get(), project_descEntry.get("1.0", "end-1c")) )

    connection.commit()  
    # connection.close()

def plus_project():
    global project
    global username_
    global project_nameEntry
    global project_techstackEntry
    global project_descEntry

    project=Tk()    #700x400+300+200
    project.title("project")
    project.geometry('700x400+300+200')
    project.resizable(False,False)
    project.configure(bg='light blue')
    # icon_image=PhotoImage(file="co.png")
    # project.iconphoto(False,icon_image)
    nameLabel=Label(project,text='Project Name',font=('sifon',12,'bold'),bg='light blue',fg='black')
    nameLabel.place(x=50,y=100)
    project_nameEntry=Entry(project,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    project_nameEntry.place(x=200,y=100)
    Label(project,text='Skills for the real world!!',font=('arial 13',16,'bold'),bg="light blue",fg="black").place(x=200,y=20)
    techstackLabel=Label(project,text='Tech Stack',font=('sifon',12,'bold'),bg='light blue',fg='black')
    techstackLabel.place(x=50,y=150)
    project_techstackEntry=Entry(project,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    project_techstackEntry.place(x=200,y=150)
    descLabel=Label(project,text='Description',font=('sifon',12,'bold'),bg='light blue',fg='black')
    descLabel.place(x=50,y=200)
    project_descEntry = Text(project, height=3,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
    project_descEntry.place(x=200,y=200)

    signupButton=Button(project,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                                fg='white',activebackground='blue',activeforeground='white',width=10, command=project_execute)

    signupButton.place(x=300,y=350)

    project.mainloop()


def fetch_variables():
    global project_1_name
    global project_1_desc
    global project_2_name
    global project_2_desc
    global project_3_name
    global project_3_desc

    global internship_1_name
    global internship_1_desc
    global internship_1_from
    global internship_1_to

    global internship_2_name
    global internship_2_desc
    global internship_2_from
    global internship_2_to

    global internship_3_name
    global internship_3_desc
    global internship_3_from
    global internship_3_to



    cursor1=connection.cursor()
    cursor1.execute('''SELECT `project_name`,`project_description` FROM `projects` WHERE email_id=%s''', (username_))
    result1=cursor1.fetchall()

    project_1_name=result1[0][0]
    project_1_desc=result1[0][1]

    project_2_name=result1[1][0]
    project_2_desc=result1[1][1]

    project_3_name=result1[2][0]
    project_3_desc=result1[2][1]

    cursor2=connection.cursor()
    cursor2.execute('''SELECT  `name`, `description`, `from_date`, `to_date` FROM `internship` WHERE email_id=%s''',(username_))
    result2=cursor2.fetchall()

    internship_1_name=result2[0][0]
    internship_1_desc=result2[0][1]
    internship_1_from=result2[0][2]
    internship_1_to=result2[0][3]

    internship_2_name=result2[1][0]
    internship_2_desc=result2[1][1]
    internship_2_from=result2[1][2]
    internship_2_to=result2[1][3]

    internship_3_name=result2[2][0]
    internship_3_desc=result2[2][1]
    internship_3_from=result2[2][2]
    internship_3_to=result2[2][3]

    
def login_user():
        global login_window
        global dashboard_page
        global passwordEntry
        global usernameEntry
        global username_

        if usernameEntry.get()=='' or passwordEntry.get()=='':
            messagebox.showerror('Error','All fields Are Required')

        else:
            try:
                con=pymysql.connect(host='127.0.0.1',user='root',password='Harshita@030712')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Connection is not Established')
                return

            query = 'use cv_generator'
            mycursor.execute(query)
            query='select * from registration13 where email_id=%s and password=%s'
            mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid username or password')

            else:
                messagebox.showinfo('Success','Login is successful')
                username_=usernameEntry.get()
                print(username_)
                login_window.destroy()
                dashboard_page()

def clear():
    signup_emailEntry.delete(0,END)

    signup_passwordEntry.delete(0,END)
    signup_confirm_PasswordEntry.delete(0,END)
    check.set(0)

def signup_connect():
    global signup_nameEntry
    global signup_ageEntry
    global signup_emailEntry
    global signup_phoneEntry
    global signup_genEntry
    global signup_degreeEntry
    global signup_branchEntry
    global signup_start_year
    global signup_end_year
    global signup_passwordEntry
    global signup_confirm_PasswordEntry
    global check
    global signup_window
    global login_page

    if signup_emailEntry.get("1.0", "end-1c") == '' or signup_nameEntry.get("1.0", "end-1c") == '' or signup_ageEntry.get("1.0", "end-1c") == '' or signup_phoneEntry.get("1.0", "end-1c") == '' or signup_genEntry.get("1.0", "end-1c") == '' or signup_branchEntry.get("1.0", "end-1c")=='' or signup_degreeEntry.get("1.0", "end-1c")=='' or signup_start_year.get() == '' or signup_end_year.get() == '' or signup_passwordEntry.get("1.0", "end-1c")=='' or signup_confirm_PasswordEntry.get("1.0", "end-1c")=='':
        messagebox.showerror('Error','All fields are Required')
    elif signup_passwordEntry.get("1.0", "end-1c") !=signup_confirm_PasswordEntry.get("1.0", "end-1c"):
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please accept Terms and Conditions')
    else:
        try:
            con=pymysql.connect(host='127.0.0.1',user='root',password='Harshita@030712')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity issue')
            return
        try:

            query='create database cv_generator'
            mycursor.execute(query)
            query='use cv_generator'
            mycursor.execute(query)
            query='CREATE TABLE `registration13`(`email_id`VARCHAR(255) NOT NULL, `name` VARCHAR(255) NOT NULL, `age` VARCHAR(255) NOT NULL, `phone_no` VARCHAR(255) NOT NULL, `password` VARCHAR(255) NOT NULL, `gender` VARCHAR(255) NOT NULL, `branch` VARCHAR(255) NOT NULL, `degree` VARCHAR(255) NOT NULL, `from_date` VARCHAR(255)NOT NULL, `to_date` VARCHAR(255) NOT NULL, PRIMARY KEY(`email_id`)) ENGINE=InnoDB;'
            mycursor.execute(query)



        except:
            mycursor.execute('use cv_generator')
        query='select * from registration13 where email_id=%s'
        mycursor.execute(query,(signup_emailEntry.get("1.0", "end-1c")))

        row=mycursor.fetchone()

        if row !=None:
            messagebox.showerror('Error', 'Email Already exists')
        else:

            query='insert into registration13(email_id,name,age,phone_no,password,gender,branch,degree,from_date,to_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            mycursor.execute(query,(signup_emailEntry.get("1.0", "end-1c"),signup_nameEntry.get("1.0", "end-1c"),signup_ageEntry.get("1.0", "end-1c"),signup_phoneEntry.get("1.0", "end-1c"),signup_passwordEntry.get("1.0", "end-1c"),signup_genEntry.get("1.0", "end-1c"),signup_branchEntry.get("1.0", "end-1c"),signup_degreeEntry.get("1.0", "end-1c"),signup_start_year.get(),signup_end_year.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registration is successful")
            clear()
            signup_window.destroy()
            login_page()

def login_page1():
    global login_page
    global signup_window
    signup_window.destroy()
    login_page()
            
def signup():
        global signup_nameEntry
        global signup_ageEntry
        global signup_emailEntry
        global signup_phoneEntry
        global signup_genEntry
        global signup_degreeEntry
        global signup_branchEntry
        global signup_start_year
        global signup_end_year
        global signup_passwordEntry
        global signup_confirm_PasswordEntry
        global check
        global signup_window
        global login_page
        global signup_nameEntry_get

        signup_window=Tk()
        signup_window.title('Signup Page')
        signup_window.geometry("{0}x{1}+0+0".format(signup_window.winfo_screenwidth(), signup_window.winfo_screenheight()))
        signup_window.resizable(False,False)
        background=ImageTk.PhotoImage(file='reg_bg.png')

        bgLabel=Label(signup_window,image=background)
        bgLabel.config(width=800, height=800)
        bgLabel.place(x=0,y=0)
        #bgLabel.grid()
        frame=Frame(signup_window,bg='light blue')

        frame.config(width=760, height=800)
        frame.place(x=760,y=10)
        heading=Label(frame,text='CREATE AN ACCOUNT',font=('Open Sans',20,'bold'),bg='light blue',fg='black')
        #heading.grid(row=0,column=5,padx=10,pady=10)
        heading.config(width=25,height=1)
        heading.place(x=180,y=80)


        nameLabel=Label(frame,text='Name',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #nameLabel.grid(row=0,column=6,sticky='w',padx=25,pady=(10,0))
        nameLabel.config(width=25,height=1)
        nameLabel.place(x=80,y=170)
        signup_nameEntry=Entry(frame,font=('sifon',10,'bold'),fg='white',bg='firebrick1')
        signup_nameEntry= Text(frame, height=1, width=25, wrap='word')
        signup_nameEntry.place(x=80,y=200)

        #nameEntry.grid(row=2,column=6,sticky='w',padx=25)
        ageLabel=Label(frame,text='Age',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #ageLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
        ageLabel.config(width=25,height=1)
        ageLabel.place(x=500,y=170)
        signup_ageEntry=Spinbox(frame,width=10,font=('sifon',10,'bold'),fg='white',bg='firebrick1',from_=12 ,to=30)
        #ageEntry.grid(row=4,column=0,sticky='w',padx=25)
        signup_ageEntry = Text(frame, height=1, width=25, wrap='word')
        signup_ageEntry.place(x=500,y=200)

        emailLabel=Label(frame,text='Email',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #emailLabel.grid(row=0,column=0,sticky='w',padx=25,pady=(10,0))
        emailLabel.config(width=25,height=1)
        emailLabel.place(x=500,y=294)
        signup_emailEntry=Entry(frame,width=30,font=('sifon',10,'bold'),fg='white',bg='firebrick1')
        #emailEntry.grid(row=2,column=0,sticky='w',padx=25)
        signup_emailEntry = Text(frame, height=1, width=25, wrap='word')
        signup_emailEntry.place(x=500,y=325)

        phoneLabel=Label(frame,text='Phone No.',font=('Open Sans',15,'bold'),bg='Light blue',fg='black')
        #phoneLabel.grid(row=3,column=5,sticky='w',padx=25,pady=(10,0))
        phoneLabel.config(width=25,height=1)
        phoneLabel.place(x=80,y=230)
        signup_phoneEntry=Entry(frame,width=20,font=('sifon',10,'bold'),fg='black',bg='white')
        #phoneEntry.grid(row=4,column=5,sticky='w',padx=25)
        signup_phoneEntry = Text(frame, height=1, width=25, wrap='word')
        signup_phoneEntry.place(x=80,y=260)

        genLabel=Label(frame,text='Gender',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #genLabel.grid(row=3,column=6,sticky='w',padx=25,pady=(10,0))
        genLabel.config(width=25,height=1)
        genLabel.place(x=480,y=230)
        signup_genEntry=Entry(frame,width=20,font=('sifon',10,'bold'),fg='black',bg='white')
        #genEntry.grid(row=4,column=6,sticky='w',padx=25)
        signup_genEntry = Text(frame, height=1, width=25, wrap='word')
        signup_genEntry.place(x=500,y=260)

        degreeLabel=Label(frame,text='Degree',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #degreeLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
        degreeLabel.config(width=25,height=1)
        degreeLabel.place(x=80,y=285)
        signup_degreeEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),fg='black',bg='white')
        #degreeEntry.grid(row=6,column=0,sticky='w',padx=25)
        signup_degreeEntry = Text(frame, height=1, width=25, wrap='word')
        signup_degreeEntry.place(x=80,y=325)

        branchLabel=Label(frame,text='Branch',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #branchLabel.grid(row=5,column=5,sticky='w',padx=25,pady=(10,0))
        branchLabel.config(width=25,height=1)
        branchLabel.place(x=80,y=355)
        signup_branchEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),fg='black',bg='white')
        #branchEntry.grid(row=6,column=5,sticky='w',padx=25)
        signup_branchEntry = Text(frame, height=1, width=25, wrap='word')
        signup_branchEntry.place(x=80,y=380)

       
        signup_start_year = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
        #start_year.grid(row=8,column=0,sticky='w',padx=25)
        signup_start_year.config(width=9)
        signup_start_year.place(x=490,y=380)


        # Create a Spinbox widget for the ending year
        toLabel=Label(frame,text='To',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
        toLabel.config(width=5,height=1)
        toLabel.place(x=570,y=370)
        signup_end_year = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
        #end_year.grid(row=8,column=5,sticky='w',padx=25)
        signup_end_year.config(width=9)
        signup_end_year.place(x=630,y=380)

        # start_year1 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
        # #start_year.grid(row=8,column=0,sticky='w',padx=25)
        # start_year1.config(width=9)
        # start_year1.place(x=490,y=510)


        # Create a Spinbox widget for the ending year
        # toLabel1=Label(frame,text='To',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        # #toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
        # toLabel1.config(width=5,height=1)
        # toLabel1.place(x=570,y=510)
        # end_year1 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
        # #end_year.grid(row=8,column=5,sticky='w',padx=25)
        # end_year1.config(width=9)
        # end_year1.place(x=630,y=510)

        # start_year2 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
        # #start_year.grid(row=8,column=0,sticky='w',padx=25)
        # start_year2.config(width=9)
        # start_year2.place(x=490,y=570)


        # Create a Spinbox widget for the ending year
        # toLabel2=Label(frame,text='To',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        # #toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
        # toLabel2.config(width=5,height=1)
        # toLabel2.place(x=570,y=570)
        # end_year2 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
        # #end_year.grid(row=8,column=5,sticky='w',padx=25)
        # end_year2.config(width=9)
        # end_year2.place(x=630,y=570)

        # usernameLabel=Label(frame,text='Username',font=('sifon',10,'bold'),bg='white',fg='firebrick1')
        # usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
        #
        # usernameEntry=Entry(frame,width=30,font=('sifon',10,'bold'),fg='white',bg='firebrick1')
        # usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

        passwordLabel=Label(frame,text='Password',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #passwordLabel.grid(row=9,column=6,sticky='w',padx=25,pady=(10,0))
        passwordLabel.config(width=25,height=1)
        passwordLabel.place(x=80,y=420)
        signup_passwordEntry=Entry(frame,width=25,font=('Open Sans',11,'bold'),fg='black',bg='white')
        #passwordEntry.grid(row=10,column=6,sticky='w',padx=25)
        signup_passwordEntry = Text(frame, height=1, width=25, wrap='word')
        signup_passwordEntry.place(x=80,y=450)

        confirm_PasswordLabel=Label(frame,text='Confirm Password',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #confirm_PasswordLabel.grid(row=40,column=6,sticky='w',padx=25,pady=(10,0))
        confirm_PasswordLabel.config(width=20,height=1)
        confirm_PasswordLabel.place(x=480,y=420)
        signup_confirm_PasswordEntry=Entry(frame,width=25,font=('Open Sans',10,'bold'),fg='black',bg='light blue')
        #confirm_PasswordEntry.grid(row=45,column=6,sticky='w',padx=25)
        signup_confirm_PasswordEntry = Text(frame, height=1, width=25, wrap='word')
        signup_confirm_PasswordEntry.place(x=500,y=450)

        # school_nameLabel=Label(frame,text='School Name',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        # #confirm_PasswordLabel.grid(row=40,column=6,sticky='w',padx=25,pady=(10,0))
        # school_nameLabel.config(width=20,height=1)
        # school_nameLabel.place(x=85,y=480)
        # school_nameEntry=Entry(frame,width=25,font=('Open Sans',10,'bold'),fg='black',bg='light blue')
        # #confirm_PasswordEntry.grid(row=45,column=6,sticky='w',padx=25)
        # school_nameEntry = tk.Text(frame, height=1, width=25, wrap='word')
        # school_nameEntry.place(x=80,y=510)

        # college_nameLabel=Label(frame,text='College Name',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        # #confirm_PasswordLabel.grid(row=40,column=6,sticky='w',padx=25,pady=(10,0))
        # college_nameLabel.config(width=20,height=1)
        # college_nameLabel.place(x=85,y=540)
        # college_nameEntry=Entry(frame,width=25,font=('Open Sans',10,'bold'),fg='black',bg='light blue')
        # #confirm_PasswordEntry.grid(row=45,column=6,sticky='w',padx=25)
        # college_nameEntry = tk.Text(frame, height=1, width=25, wrap='word')
        # college_nameEntry.place(x=80,y=570)



        #confirm_PasswordEntry.place(x=250,y=30)
        check=IntVar()
        termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Open Sans',12,'bold'),fg='black',bg='light blue',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
        #termsandconditions.grid(row=51,column=5,pady=0,padx=5)
        termsandconditions.place(x=230,y=600)
        signupButton=Button(frame,text='Sign up',font=('Open Sans',15,'bold'),bd=0,bg='white',
                            fg='black',activebackground='light blue',activeforeground='black',width=17,
                            command=signup_connect)
        signupButton.place(x=300,y=650)
        signupButton.config(height=1,width=10)

        #signupButton.grid(row=50,column=5,pady=(90,30))

        alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans',15,'bold'),bg='light blue',fg='black')
        #alreadyaccount.grid(row=60,column=5,sticky='w',padx=10,pady=65)
        alreadyaccount.config(height=1,width=20)
        alreadyaccount.place(x=270,y=700)
        loginButton=Button(frame,text='Log in',font=('Open Sans',15,'bold underline'),bg='light blue',fg='black',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page1)
        loginButton.place(x=330,y=740)

        signup_window.mainloop()

def login_page():
        global usernameEntry
        global login_window
        global openeye
        global passwordEntry
        global eyeButton
        
        
        
        login_window=Tk()
        #login_window.geometry('990x660+50+50')
        login_window.geometry("{0}x{1}+0+0".format(login_window.winfo_screenwidth(), login_window.winfo_screenheight()))
        #cocurricular_window.resizable(0,0)
        #cocurricular_window.configure(bg="light blue")

        login_window.resizable(0,0)
        bgImage=ImageTk.PhotoImage(file='loginbg.png')
        # login_window.state("zoom")

        bgLabel=Label(login_window,image=bgImage)
        bgLabel.place(x=100,y=50)
        heading=Label(login_window,text='USER LOGIN',font=('sifon',23,'bold'),bg='light blue',fg='black')
        heading.place(x=200,y=120)
        usernameEntry=Entry(login_window,width=25,font=('sifon',15,'bold'),bd=0,fg='black')
        usernameEntry.place(x=250,y=200)
        usernameEntry.insert(0,'Email-id')
        usernameEntry.bind('<FocusIn>',user_enter)

        #frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
        #frame1.place(x=580,y=222)

        passwordEntry=Entry(login_window,width=25,font=('sifon',15,'bold'),bd=0,fg='black', show="*")
        passwordEntry.place(x=250,y=250)
        passwordEntry.insert(0,'Password')
        passwordEntry.bind('<FocusIn>',password_enter)
        #frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
        #frame2.place(x=580,y=282)

        openeye=PhotoImage(file='closeye.png')
        eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2', command=hide) #,command=hide
        eyeButton.place(x=500,y=250)

        forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('sifon',9,'bold'),fg='black',activeforeground='light blue')

        forgetButton.place(x=250,y=295)

        loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='black',bg='light blue',activeforeground='white',activebackground='light blue',cursor='hand2',bd=0,width=19, command=login_user) #,command=login_user
        loginButton.place(x=178,y=350)

        #orlabel=Label(login_window,text="----------------OR---------------",font=('Open Sans',16),fg='firebrick1',bg='white')
        #orlabel.place(x=583,y=400)

        #facebook_logo=PhotoImage(file='facebook.png')
        #fblabel=Label(login_window,image=facebook_logo,bg='white')
        #fblabel.place(x=640,y=440)
        #google_logo=PhotoImage(file='google.png')
        #googlelabel=Label(login_window,image=google_logo,bg='white')
        #googlelabel.place(x=690,y=440)
        #twitter_logo=PhotoImage(file='twitter.png')
        #twitterlabel=Label(login_window,image=twitter_logo,bg='white')
        #twitterlabel.place(x=740,y=440)

        signuplabel=Label(login_window,text="Dont have an account?",font=('Open Sans',9,'bold'),fg='black',bg='light blue')
        signuplabel.place(x=250,y=400)
        loginlabel=Label(login_window,text="E-mail",font=('Open Sans',13,'bold'),fg='black',bg='light blue')
        loginlabel.place(x=150,y=200)
        passwordlabel=Label(login_window,text="Password",font=('Open Sans',13,'bold'),fg='black',bg='light blue')
        passwordlabel.place(x=150,y=250)
        newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',10,'bold underline'),fg='black',bg='light blue',activeforeground='white',activebackground='light blue',cursor='hand2',bd=0, command=signup_page) #,command=signup_page
        newaccountButton.place(x=250,y=450)

        login_window.mainloop()


def dashboard_page():
        global connection
        global cursor
        global data
        global username_
        global dashboard_window
        global tree
        global name 
        global age 
        global phone_no 
        global gender 
        global branch 
        global degree
        global from_date
        global to_date

        dashboard_window = Tk()

        #dashboard_window.geometry('990x660+50+50')
        dashboard_window.geometry("{0}x{1}+0+0".format(dashboard_window.winfo_screenwidth(), dashboard_window.winfo_screenheight()))
        dashboard_window.resizable(0,0)
        dashboard_window.configure(bg='light grey')

        img = Image.open("plus_sign.jpg")

        img_tk = ImageTk.PhotoImage(img)


        # Create a frame to hold the navbar buttons
        navbar_frame = Frame(dashboard_window, padx=15, pady=15)

    # Create a button for each page
        dashboard_button=  Button(navbar_frame, text="Dashboard",width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click("dashboard_page")) #, command=lambda: handle_click("dashboard_page")
        academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click("academics_page")) #, command=lambda: handle_click("academics_page")
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click("cocurricular_page")) #, command=lambda: handle_click("cocurricular_page")
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click("extracurricular_page")) #, command=lambda: handle_click("extracurricular_page")
        internships_button = Button(navbar_frame, text="Internships",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click("internship_page")) # , command=lambda: handle_click("internship_page")
        projects_button = Button(navbar_frame, text="Projects", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click("projects_page")) # , command=lambda: handle_click("projects_page")
        button = Button(navbar_frame, text="Create", compound="left", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=add_info) #, command=add_info
        # button = Button(navbar_frame, compound="left", width=5, height=5)



    # Pack the navbar buttons horizontally
        dashboard_button.pack(side="left")
        academics_button.pack(side="left")
        cocurricular_button.pack(side="left")
        extracurricular_button.pack(side="left")
        internships_button.pack(side="left")
        projects_button.pack(side="left")
        button.pack(side="right")


    # Pack the navbar frame at the top of the window
        navbar_frame.pack(side="top", fill="x")
           # Create a connection object
        connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="Harshita@030712",
        database="cv_generator"    
            )
    # Create a cursor object
        cursor = connection.cursor()

    # Execute a SELECT statement to fetch data
        cursor.execute('''SELECT  `name`, `age`, `phone_no`, `gender`, `branch`, `degree`, `from_date`, `to_date` FROM `registration13` WHERE email_id=%s''', (username_))

    # Fetch all the rows using fetchall() method
        result = cursor.fetchone()

         # Create a frame for the main content of the window
        content_frame = Frame(dashboard_window,bg="light blue")
        content_frame.config(height=60,width=50)
        content_frame.place(x=100,y=200)

        name = result[0]
        age = result[1]
        phone_no = result[2]
        gender = result[3]
        branch = result[4]
        degree= result[5]
        from_date= result[6]
        to_date= result[7]


        name_label = Label(content_frame, text="Name: ",font="35",bg="light blue")
        name_label.place(x=200,y=150)
        age_label = Label(content_frame, text="Age: ",font="35",bg="light blue")
        age_label.place(x=200,y=200)
        phone_label = Label(content_frame, text="Phone No.: ",font="35",bg="light blue")
        phone_label.place(x=200,y=250)
        gender_label = Label(content_frame, text="Gender: ",font="35",bg="light blue")
        gender_label.place(x=200,y=300)
        branch_label= Label(content_frame, text="Branch: ",font="35",bg="light blue")
        branch_label.place(x=200,y=350)
        degree_label= Label(content_frame, text="Degree: ",font="35",bg="light blue")
        degree_label.place(x=200,y=400)
        from_label= Label(content_frame, text="From: ",font="35",bg="light blue")
        from_label.place(x=200,y=450)
        to_label= Label(content_frame, text="To: ",font="35",bg="light blue")
        to_label.place(x=200,y=500)



        name_value = Label(content_frame, text=name,font="35",bg="light blue")
        name_value.place(x=350,y=150)
        age_value = Label(content_frame, text=age,font="35",bg="light blue")
        age_value.place(x=350,y=200)
        phone_value = Label(content_frame, text=phone_no,font="35",bg="light blue")
        phone_value.place(x=350,y=250)
        gender_value = Label(content_frame, text=gender,font="35",bg="light blue")
        gender_value.place(x=350,y=300)
        branch_value = Label(content_frame, text=branch,font="35",bg="light blue")
        branch_value.place(x=350,y=350)
        degree_value = Label(content_frame, text=degree,font="35",bg="light blue")
        degree_value.place(x=350,y=400)
        from_value = Label(content_frame, text=from_date,font="35",bg="light blue")
        from_value.place(x=350,y=450)
        to_value = Label(content_frame, text=to_date,font="35",bg="light blue")
        to_value.place(x=350,y=500)

        
        

    # Pack the main content frame
        content_frame.pack(expand=True, fill="both")

    # Run the Tkinter event loop
        dashboard_window.mainloop()

def academics_page():
            global connection
            global cursor
            global data
            global username_
            global academics_window
            global tree

            academics_window = Tk()

            #academics_window.geometry('990x660+50+50')
            academics_window.geometry("{0}x{1}+0+0".format(academics_window.winfo_screenwidth(), academics_window.winfo_screenheight()))
            academics_window.resizable(0,0)
            academics_window.configure(bg="light blue")

            img = Image.open("plus.jpg")

            img_tk = ImageTk.PhotoImage(img)


            # Create a frame to hold the navbar buttons
            navbar_frame = Frame(academics_window, padx=15, pady=15,bg="light grey")


            # Create a button for each page
            dashboard_button=  Button(navbar_frame, text="Dashboard",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click1("dashboard_page")) #, command=lambda: handle_click1("dashboard_page")
            academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click1("academics_page")) # , command=lambda: handle_click1("academics_page")
            cocurricular_button = Button(navbar_frame, text="Co-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click1("cocurricular_page")) # , command=lambda: handle_click1("cocurricular_page")
            extracurricular_button = Button(navbar_frame, text="Extra-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click1("extracurricular_page")) # , command=lambda: handle_click1("extracurricular_page")
            internships_button = Button(navbar_frame, text="Internships",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click1("internship_page")) # , command=lambda: handle_click1("internship_page")
            projects_button = Button(navbar_frame, text="Projects",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click1("projects_page")) # , command=lambda: handle_click1("projects_page")
            button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, bg='white',fg='black',font=('Open Sans',10,'bold'), command=plus_academics) # , command=plus_academics

            # Pack the navbar buttons horizontally
            dashboard_button.pack(side="left")
            academics_button.pack(side="left")
            cocurricular_button.pack(side="left")
            extracurricular_button.pack(side="left")
            internships_button.pack(side="left")
            projects_button.pack(side="left")
            button.pack(side="right")

            # Pack the navbar frame at the top of the window
            navbar_frame.pack(side="top", fill="x")

            # Create a connection object
            # connection = pymysql.connect(
            #     host="127.0.0.1",
            #     user="academics_window",
            #     password="Harshita@030712",
            #     database="trials_cvgenerator"
            # )

            # Create a cursor object
            cursor = connection.cursor()

            # Execute a SELECT statement to fetch data
            cursor.execute('''SELECT `year_of_study`, `sem`, `cgpi` FROM `academics` WHERE email_id=%s''', (username_))
            # Fetch all the rows using fetchall() method
            data = cursor.fetchall()

            # Create a frame for the main content of the window
            content_frame = Frame(academics_window,bg="light blue")

            # Create a Treeview widget
            tree = ttk.Treeview(academics_window)

            # Define columns
            tree["columns"] = ("column1", "column2", "column3")

            # Format columns
            tree.column("#0", width=0, stretch=NO)
            tree.column("column1", width=195, anchor=CENTER)
            tree.column("column2", width=195, anchor=CENTER)
            tree.column("column3", width=195, anchor=CENTER)
            


            # Add headings
            tree.heading("#0", text="", anchor=CENTER)
            tree.heading("column1", text="Year of Study", anchor=CENTER)
            tree.heading("column2", text="Semester", anchor=CENTER)
            tree.heading("column3", text="CGPI", anchor=CENTER)
            


            # Add data to treeview
            for row in data:
                tree.insert("", END, text="", values=row)

            # Pack the Treeview widget
            tree.pack()

            # Pack the main content frame
            content_frame.pack(expand=True, fill="both")
            

            # Run the Tkinter event loop
            academics_window.mainloop()

def cocurricular_page():
        global connection
        global cursor
        global data
        global username_
        global cocurricular_window
        global tree
        

        cocurricular_window = Tk()

        #cocurricular_window.geometry('990x660+50+50')
        cocurricular_window.geometry("{0}x{1}+0+0".format(cocurricular_window.winfo_screenwidth(), cocurricular_window.winfo_screenheight()))
        cocurricular_window.resizable(0,0)
        cocurricular_window.configure(bg="light blue")


        img = Image.open("plus.jpg")

        img_tk = ImageTk.PhotoImage(img)


        # Create a frame to hold the navbar buttons
        navbar_frame = Frame(cocurricular_window, padx=15, pady=15)

        # Create a button for each page
        dashboard_button=  Button(navbar_frame, text="Dashboard", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click2("dashboard_page")) #, command=lambda: handle_click2("dashboard_page")
        academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click2("academics_page")) # command=lambda: handle_click2("academics_page")
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click2("cocurricular_page") ) #command=lambda: handle_click2("cocurricular_page")
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click2("extracurricular_page")) # command=lambda: handle_click2("extracurricular_page")
        internships_button = Button(navbar_frame, text="Internships", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click2("internship_page")) # command=lambda: handle_click2("internship_page")
        projects_button = Button(navbar_frame, text="Projects", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click2("projects_page")) # command=lambda: handle_click2("projects_page")
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, bg='white',fg='black',font=('Open Sans',10,'bold'), command=plus_cocurricular) #command=plus_cocurricular


        # Pack the navbar buttons horizontally
        dashboard_button.pack(side="left")
        academics_button.pack(side="left")
        cocurricular_button.pack(side="left")
        extracurricular_button.pack(side="left")
        internships_button.pack(side="left")
        projects_button.pack(side="left")
        button.pack(side="right")

        # Pack the navbar frame at the top of the window
        navbar_frame.pack(side="top", fill="x")

        # Create a connection object
        # connection = pymysql.connect(
        #     host="127.0.0.1",
        #     user="cocurricular",
        #     password="Harshita@030712",
        #     database="trials_cvgenerator"
        # )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a SELECT statement to fetch data
        cursor.execute('''SELECT  `event_name`, `activity_name`, `conducted_by`, `participation_level`, `rank` FROM `cocurricular` WHERE email_id=%s''', (username_))

        # Fetch all the rows using fetchall() method
        data = cursor.fetchall()

        # Create a frame for the main content of the window
        content_frame = Frame(cocurricular_window,bg="light blue")


        # Create a Treeview widget
        tree = ttk.Treeview(cocurricular_window)

        # Define columns
        tree["columns"] = ("column1", "column2", "column3", "column4", "column5")

        # Format columns
        tree.column("#0", width=0, stretch=NO)
        tree.column("column1", width=195, anchor=CENTER)
        tree.column("column2", width=195, anchor=CENTER)
        tree.column("column3", width=195, anchor=CENTER)
        tree.column("column4", width=195, anchor=CENTER)
        tree.column("column5", width=195, anchor=CENTER)


        # Add headings
        tree.heading("#0", text="", anchor=CENTER)
        tree.heading("column1", text="Event Name", anchor=CENTER)
        tree.heading("column2", text="Activity Name", anchor=CENTER)
        tree.heading("column3", text="Conducted by", anchor=CENTER)
        tree.heading("column4", text="Participation Level", anchor=CENTER)
        tree.heading("column5", text="Rank", anchor=CENTER)


        # Add data to treeview
        for row in data:
            tree.insert("", END, text="", values=row)

        # Pack the Treeview widget
        tree.pack()

        # Pack the main content frame
        content_frame.pack(expand=True, fill="both")
        
        # Run the Tkinter event loop
        cocurricular_window.mainloop()

def extracurricular_page():
        global connection
        global cursor
        global data
        global username_
        global extracurricular_window
        global tree

        extracurricular_window = Tk()

#extracurricular_window.geometry('990x660+50+50')
        extracurricular_window.geometry("{0}x{1}+0+0".format(extracurricular_window.winfo_screenwidth(), extracurricular_window.winfo_screenheight()))
        extracurricular_window.resizable(0,0)
        extracurricular_window.configure(bg='light blue')
        img = Image.open("plus.jpg")

        img_tk = ImageTk.PhotoImage(img)



        # Create a frame to hold the navbar buttons
        navbar_frame = Frame(extracurricular_window, padx=15, pady=15,bg="light grey")


        # Create a button for each page
        dashboard_button=  Button(navbar_frame, text="Dashboard", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click3("dashboard_page")) #, command=lambda: handle_click2("dashboard_page")
        academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click3("academics_page")) # command=lambda: handle_click2("academics_page")
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click3("cocurricular_page") ) #command=lambda: handle_click2("cocurricular_page")
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click3("extracurricular_page")) # command=lambda: handle_click2("extracurricular_page")
        internships_button = Button(navbar_frame, text="Internships", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click3("internship_page")) # command=lambda: handle_click2("internship_page")
        projects_button = Button(navbar_frame, text="Projects", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click3("projects_page")) # command=lambda: handle_click2("projects_page")
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, bg='white',fg='black',font=('Open Sans',10,'bold'), command=plus_extracurricular) #command=plus_cocurricular

        # Pack the navbar buttons horizontally
        dashboard_button.pack(side="left")
        academics_button.pack(side="left")
        cocurricular_button.pack(side="left")
        extracurricular_button.pack(side="left")
        internships_button.pack(side="left")
        projects_button.pack(side="left")
        button.pack(side="right")


        # Pack the navbar frame at the top of the window
        navbar_frame.pack(side="top", fill="x")

        # Create a connection object
        # connection = pymysql.connect(
        #     host="127.0.0.1",
        #     user="root",
        #     password="Harshita@030712",
        #     database="trials_cvgenerator"
        # )
       
        
        # Create a cursor object
        cursor = connection.cursor()

        # Execute a SELECT statement to fetch data
        cursor.execute("SELECT `event_name`, `activity_name`, `participation_level`, `rank` FROM `extra_curricular` WHERE email_id=%s", (username_))

        # Fetch all the rows using fetchall() method
        data = cursor.fetchall()

        # Create a frame for the main content of the window
        content_frame = Frame(extracurricular_window,bg="light blue")

        # Create a Treeview widget
        tree = ttk.Treeview(extracurricular_window)

        # Define columns
        tree["columns"] = ("column1", "column2", "column3", "column4")

        # Format columns
        tree.column("#0", width=0, stretch=NO)
        tree.column("column1", width=195, anchor=CENTER)
        tree.column("column2", width=195, anchor=CENTER)
        tree.column("column3", width=195, anchor=CENTER)
        tree.column("column4", width=195, anchor=CENTER)


        # Add headings
        tree.heading("#0", text="", anchor=CENTER)
        tree.heading("column1", text="Event Name", anchor=CENTER)
        tree.heading("column2", text="Activity Name", anchor=CENTER)
        tree.heading("column3", text="Participation Level", anchor=CENTER)
        tree.heading("column4", text="Rank", anchor=CENTER)


        # Add data to treeview
        for row in data:
            tree.insert("", END, text="", values=row)

        

        # Pack the Treeview widget
        tree.pack()
        
        # Pack the main content frame
        content_frame.pack(expand=True, fill="both")

        
        # Run the Tkinter event loop
        extracurricular_window.mainloop()

def internship_page():
        global connection
        global cursor
        global data
        global username_
        global internship_window
        global tree

        internship_window = Tk()

        #internship_window.geometry('990x660+50+50')
        internship_window.geometry("{0}x{1}+0+0".format(internship_window.winfo_screenwidth(), internship_window.winfo_screenheight()))
        internship_window.resizable(0,0)
        internship_window.configure(bg="light blue")
        img = Image.open("plus.jpg")

        img_tk = ImageTk.PhotoImage(img)


            # Create a frame to hold the navbar buttons
        navbar_frame = Frame(internship_window, padx=15, pady=15,bg="light grey")


            # Create a button for each page
        dashboard_button=  Button(navbar_frame, text="Dashboard", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click4("dashboard_page")) #, command=lambda: handle_click2("dashboard_page")
        academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click4("academics_page")) # command=lambda: handle_click2("academics_page")
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click4("cocurricular_page") ) #command=lambda: handle_click2("cocurricular_page")
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click4("extracurricular_page")) # command=lambda: handle_click2("extracurricular_page")
        internships_button = Button(navbar_frame, text="Internships", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click4("internship_page")) # command=lambda: handle_click2("internship_page")
        projects_button = Button(navbar_frame, text="Projects", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click4("projects_page")) # command=lambda: handle_click2("projects_page")
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, bg='white',fg='black',font=('Open Sans',10,'bold'), command=plus_internship) #command=plus_cocurricular



            # Pack the navbar buttons horizontally
        dashboard_button.pack(side="left")
        academics_button.pack(side="left")
        cocurricular_button.pack(side="left")
        extracurricular_button.pack(side="left")
        internships_button.pack(side="left")
        projects_button.pack(side="left")
        button.pack(side="right")

            # Pack the navbar frame at the top of the window
        navbar_frame.pack(side="top", fill="x")

            # Create a connection object
        # connection = pymysql.connect(
        # host="127.0.0.1",
        # user="root",
        # password="Harshita@030712",
        # database="trials_cvgenerator"
        # )

            # Create a cursor object
        cursor = connection.cursor()

            # Execute a SELECT statement to fetch data
        cursor.execute('''SELECT `name`, `domain`, `description`, `from_date`, `to_date` FROM `internship` WHERE email_id=%s''', (username_))
            

            # Fetch all the rows using fetchall() method
        data = cursor.fetchall()

            # Create a frame for the main content of the window
        content_frame = Frame(internship_window,bg="light blue")


            # Create a Treeview widget
        tree = ttk.Treeview(internship_window)

            # Define columns
        tree["columns"] = ("column1", "column2", "column3", "column4", "column5")

            # Format columns
        tree.column("#0", width=0, stretch=NO)
        tree.column("column1", width=195, anchor=CENTER)
        tree.column("column2", width=195, anchor=CENTER)
        tree.column("column3", width=195, anchor=CENTER)
        tree.column("column4", width=195, anchor=CENTER)
        tree.column("column5", width=195, anchor=CENTER)



            # Add headings
        tree.heading("#0", text="", anchor=CENTER)
        tree.heading("column1", text="Name", anchor=CENTER)
        tree.heading("column2", text="Domain", anchor=CENTER)
        tree.heading("column3", text="Description", anchor=CENTER)
        tree.heading("column4", text="From", anchor=CENTER)
        tree.heading("column5", text="To", anchor=CENTER)


            # Add data to treeview
        for row in data:
            tree.insert("", END, text="", values=row)

            # Pack the Treeview widget
        tree.pack()

            # Pack the main content frame
        content_frame.pack(expand=True, fill="both")
        
            # Run the Tkinter event loop
        internship_window.mainloop()

def projects_page():
    global connection
    global cursor
    global data
    global username_
    global projects_window
    global tree
    global projects_window

    projects_window=Tk()
    projects_window.geometry("{0}x{1}+0+0".format(projects_window.winfo_screenwidth(), projects_window.winfo_screenheight()))
    projects_window.resizable(0,0)
    projects_window.configure(bg="light blue")

    img = Image.open("plus.jpg")

    img_tk = ImageTk.PhotoImage(img)


    # Create a frame to hold the navbar buttons
    navbar_frame = Frame(projects_window, padx=15, pady=15,bg="light grey")

    # Create a button for each page
    dashboard_button=  Button(navbar_frame, text="Dashboard", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click5("dashboard_page")) #, command=lambda: handle_click2("dashboard_page")
    academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click5("academics_page")) # command=lambda: handle_click2("academics_page")
    cocurricular_button = Button(navbar_frame, text="Co-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click5("cocurricular_page") ) #command=lambda: handle_click2("cocurricular_page")
    extracurricular_button = Button(navbar_frame, text="Extra-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click5("extracurricular_page")) # command=lambda: handle_click2("extracurricular_page")
    internships_button = Button(navbar_frame, text="Internships", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click5("internship_page")) # command=lambda: handle_click2("internship_page")
    projects_button = Button(navbar_frame, text="Projects", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'), command=lambda: handle_click5("projects_page")) # command=lambda: handle_click2("projects_page")
    button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, bg='white',fg='black',font=('Open Sans',10,'bold'), command=plus_project) #command=plus_cocurricular

    # Pack the navbar buttons horizontally
    dashboard_button.pack(side="left")
    academics_button.pack(side="left")
    cocurricular_button.pack(side="left")
    extracurricular_button.pack(side="left")
    internships_button.pack(side="left")
    projects_button.pack(side="left")
    button.pack(side="right")

    # Pack the navbar frame at the top of the window
    navbar_frame.pack(side="top", fill="x")

    # Create a connection object
    # connection = pymysql.connect(
    #     host="127.0.0.1",
    #     user="projects_window",
    #     password="Harshita@030712",
    #     database="trials_cvgenerator"
    # )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SELECT statement to fetch data
    cursor.execute('''SELECT `project_name`, `tech_stack`, `project_description` FROM `projects` WHERE email_id=%s''', (username_))
    # Fetch all the rows using fetchall() method
    data = cursor.fetchall()

    # Create a frame for the main content of the window
    content_frame = Frame(projects_window,bg="light blue")

    # Create a Treeview widget
    tree = ttk.Treeview(projects_window)

    # Define columns
    tree["columns"] = ("column1", "column2", "column3")

    # Format columns
    tree.column("#0", width=0, stretch=NO)
    tree.column("column1", width=195, anchor=CENTER)
    tree.column("column2", width=195, anchor=CENTER)
    tree.column("column3", width=195, anchor=CENTER)


    # Add headings
    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("column1", text="Name", anchor=CENTER)
    tree.heading("column2", text="Tech Stack", anchor=CENTER)
    tree.heading("column3", text="Description", anchor=CENTER)


    # Add data to treeview
    for row in data:
        tree.insert("", END, text="", values=row)

    # Pack the Treeview widget
    tree.pack()

    # Pack the main content frame
    content_frame.pack(expand=True, fill="both")
    

    # Run the Tkinter event loop
    projects_window.mainloop()

def add_info():
        global titleEntry
        global describeEntry
        global addressEntry
        global linkedInEntry
        global gitEntry
        global skill1_Entry
        global skill2_Entry
        global skill3_Entry
        global skill4_Entry
        global skill5_Entry
        global skill6_Entry
        
        global resume_nameEntry
        global add_information

        add_information=Tk()    #700x400+300+200
        add_information.title("Extra Curricular")
        add_information.geometry('800x800+300+200')
        add_information.resizable(False,False)
        add_information.configure(bg='light blue')
        # icon_image=PhotoImage(file="extra.png")
        # add_information.iconphoto(False,icon_image)


        Label(add_information,text='Additional Information',font=("arial 13",16,'bold'),bg='light blue',fg="black").place(x=100,y=20)

        titleLabel=Label(add_information,text='Job Title',font=('sifon',12,'bold'),bg='light blue',fg='black')
        titleLabel.place(x=50,y=100)
        titleEntry=Entry(add_information,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        titleEntry.place(x=200,y=100)

        addressLabel=Label(add_information,text='Address',font=('sifon',12,'bold'),bg='light blue',fg='black')
        addressLabel.place(x=50,y=150)
        addressEntry=Entry(add_information,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        addressEntry.place(x=200,y=150)

        gitLabel=Label(add_information,text='Github Link',font=('sifon',12,'bold'),bg='light blue',fg='black')
        gitLabel.place(x=50,y=200)
        gitEntry=Entry(add_information,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        gitEntry.place(x=200,y=200)

        linkedInLabel=Label(add_information,text='LinkedIn Link',font=('sifon',12,'bold'),bg='light blue',fg='black')
        linkedInLabel.place(x=50,y=250)
        linkedInEntry=Entry(add_information,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        linkedInEntry.place(x=200,y=250)

        skill1_Label=Label(add_information,text='Skill 1',font=('sifon',12,'bold'),bg='light blue',fg='black')
        skill1_Label.place(x=100,y=300)
        skill1_Entry=Entry(add_information,width=15,font=('sifon',12,'bold'),fg='black',bg='white')
        skill1_Entry.place(x=200,y=300)

        skill2_Label=Label(add_information,text='Skill 2',font=('sifon',12,'bold'),bg='light blue',fg='black')
        skill2_Label.place(x=370,y=300)
        skill2_Entry=Entry(add_information,width=15,font=('sifon',12,'bold'),fg='black',bg='white')
        skill2_Entry.place(x=470,y=300)

        skill3_Label=Label(add_information,text='Skill 3',font=('sifon',12,'bold'),bg='light blue',fg='black')
        skill3_Label.place(x=100,y=350)
        skill3_Entry=Entry(add_information,width=15,font=('sifon',12,'bold'),fg='black',bg='white')
        skill3_Entry.place(x=200,y=350)

        skill4_Label=Label(add_information,text='Skill 4',font=('sifon',12,'bold'),bg='light blue',fg='black')
        skill4_Label.place(x=370,y=350)
        skill4_Entry=Entry(add_information,width=15,font=('sifon',12,'bold'),fg='black',bg='white')
        skill4_Entry.place(x=470,y=350)

        skill5_Label=Label(add_information,text='Skill 5',font=('sifon',12,'bold'),bg='light blue',fg='black')
        skill5_Label.place(x=100,y=400)
        skill5_Entry=Entry(add_information,width=15,font=('sifon',12,'bold'),fg='black',bg='white')
        skill5_Entry.place(x=200,y=400)

        skill6_Label=Label(add_information,text='Skill 6',font=('sifon',12,'bold'),bg='light blue',fg='black')
        skill6_Label.place(x=370,y=400)
        skill6_Entry=Entry(add_information,width=15,font=('sifon',12,'bold'),fg='black',bg='white')
        skill6_Entry.place(x=470,y=400)


        resume_nameLabel=Label(add_information,text='Resume Name',font=('sifon',12,'bold'),bg='light blue',fg='black')
        resume_nameLabel.place(x=50,y=450)
        resume_nameEntry=Entry(add_information,width=45,font=('sifon',12,'bold'),fg='black',bg='white')
        resume_nameEntry.place(x=200,y=450)

        addButton=Button(add_information,text='Add',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                            fg='white',activebackground='blue',activeforeground='white',width=10, command=fetch_variables)

        addButton.place(x=200,y=500)


        createButton=Button(add_information,text='Create',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                            fg='white',activebackground='blue',activeforeground='white',width=10, command=create)

        createButton.place(x=300,y=500)


        add_information.mainloop()

def create():
    global name 
    global age 
    global phone_no 
    global gender 
    global branch 
    global degree
    global from_date
    global to_date

    global titleEntry
    global describeEntry
    global addressEntry
    global linkedInEntry
    global gitEntry
    global skill1_Entry
    global skill2_Entry
    global skill3_Entry
    global skill4_Entry
    global skill5_Entry
    global skill6_Entry
    global resume_nameEntry

    global project_1_name
    global project_1_desc
    global project_2_name
    global project_2_desc
    global project_3_name
    global project_3_desc

    global internship_1_name
    global internship_1_desc
    global internship_1_from
    global internship_1_to

    global internship_2_name
    global internship_2_desc
    global internship_2_from
    global internship_2_to

    global internship_3_name
    global internship_3_desc
    global internship_3_from
    global internship_3_to

    Name = name
    Title = titleEntry.get()
    Contact = f"{addressEntry.get()}\n{username_}\n{linkedInEntry.get()}\n{gitEntry.get()}"
    ProjectsHeader = 'PROJECTS/PUBLICATIONS'
    ProjectOneTitle = project_1_name
    ProjectOneDesc = project_1_desc
    ProjectTwoTitle = project_2_name
    ProjectTwoDesc = project_2_desc
    ProjectThreeTitle = project_3_name
    ProjectThreeDesc = project_3_desc
    # Portfolio = 'Portfolio: rebrand.ly/ekirkland'
    WorkHeader = 'EXPERIENCE'
    WorkOneTitle = internship_1_name
    WorkOneTime = f"{internship_1_from} - {internship_1_to}"
    WorkOneDesc = internship_1_desc
    WorkTwoTitle = internship_2_name
    WorkTwoTime =  f"{internship_2_from} - {internship_2_to}"
    WorkTwoDesc = internship_2_desc
    WorkThreeTitle = internship_3_name
    WorkThreeTime =  f"{internship_3_from} - {internship_3_to}"
    WorkThreeDesc = internship_3_desc
    EduHeader = 'EDUCATION'
    EduOneTitle = 'Example University, Bachelor of Business Administration'
    EduOneTime = '2000-2004'
    # EduOneDesc = '- Major: Management, Minor: Statistics'
    EduTwoTitle = 'Example University, Master of Arts'
    EduTwoTime = '2013-2017'
    SkillsHeader = 'Skills'
    SkillsDesc = f"-{skill1_Entry.get()}\n-{skill2_Entry.get()}\n-{skill3_Entry.get()}\n-{skill4_Entry.get()}\n-{skill5_Entry.get()}\n-{skill6_Entry.get()}"
    # ExtrasTitle = 'DataQuest\nData Scientist Path'
    # ExtrasDesc = 'Learned popular data science\nlanguages, data cleaning and\nmanipulation, machine learning \nand statistical analysis'
    # CodeTitle = 'View Portfolio'
    # Setting style for bar graphs
    import matplotlib.pyplot as plt
    #%matplotlib inline
    # set font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'STIXGeneral'
    fig, ax = plt.subplots(figsize=(8.5, 11))
    # Decorative Lines
    ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
    plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
    plt.axhline(y=.88, xmin=0, xmax=1, color='black', linewidth=3)
    # set background color
    ax.set_facecolor('white')
    # remove axes
    plt.axis('off')
    # add text
    plt.annotate(EduHeader, (.02,.98), weight='regular', fontsize=8, alpha=.75)
    plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
    plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
    plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='black')
    plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='black')
    plt.annotate(ProjectOneTitle, (.02,.832), weight='bold', fontsize=10)
    plt.annotate(ProjectOneDesc, (.04,.78), weight='regular', fontsize=9)
    plt.annotate(ProjectTwoTitle, (.02,.745), weight='bold', fontsize=10)
    plt.annotate(ProjectTwoDesc, (.04,.693), weight='regular', fontsize=9)
    plt.annotate(ProjectThreeTitle, (.02,.672), weight='bold', fontsize=10)
    plt.annotate(ProjectThreeDesc, (.04,.62), weight='regular', fontsize=9)
    # plt.annotate(Portfolio, (.02,.6), weight='bold', fontsize=10)
    plt.annotate(WorkHeader, (.02,.54), weight='bold', fontsize=10, color='black')
    plt.annotate(WorkOneTitle, (.02,.508), weight='bold', fontsize=10)
    plt.annotate(WorkOneTime, (.02,.493), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkOneDesc, (.04,.445), weight='regular', fontsize=9)
    plt.annotate(WorkTwoTitle, (.02,.4), weight='bold', fontsize=10)
    plt.annotate(WorkTwoTime, (.02,.385), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkTwoDesc, (.04,.337), weight='regular', fontsize=9)
    plt.annotate(WorkThreeTitle, (.02,.295), weight='bold', fontsize=10)
    plt.annotate(WorkThreeTime, (.02,.28), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkThreeDesc, (.04,.232), weight='regular', fontsize=9)
    plt.annotate(EduHeader, (.02,.185), weight='bold', fontsize=10, color='black')
    plt.annotate(EduOneTitle, (.02,.155), weight='bold', fontsize=10)
    plt.annotate(EduOneTime, (.02,.14), weight='regular', fontsize=9, alpha=.6)
    # plt.annotate(EduOneDesc, (.04,.125), weight='regular', fontsize=9)
    plt.annotate(EduTwoTitle, (.02,.08), weight='bold', fontsize=10)
    plt.annotate(EduTwoTime, (.02,.065), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='black')
    plt.annotate(SkillsDesc, (.7,.65), weight='regular', fontsize=10, color='black')
    # plt.annotate(ExtrasTitle, (.7,.43), weight='bold', fontsize=10, color='black')
    # plt.annotate(ExtrasDesc, (.7,.345), weight='regular', fontsize=10, color='black')
    # plt.annotate(CodeTitle, (.7,.2), weight='bold', fontsize=10, color='black')
    #add qr code
    from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
    import matplotlib.image as mpimg
    # arr_code = mpimg.imread('ekresumecode.png')
    # imagebox = OffsetImage(arr_code, zoom=0.5)
    # ab = AnnotationBbox(imagebox, (0.84, 0.12))
    # ax.add_artist(ab)
    plt.savefig(resume_nameEntry.get(), dpi=300, bbox_inches='tight')
        
signup()
# login_page()


