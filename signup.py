from tkinter import *
from tkinter import messagebox
import tkinter as tk


import pymysql 
from PIL import ImageTk
# import pymysql

def clear():
    signup_emailEntry.delete(0,END)

    signup_passwordEntry.delete(0,END)
    signup_confirm_PasswordEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get("1.0","end-1c") == '' or nameEntry.get("1.0","end-1c") == '' or ageEntry.get("1.0","end-1c") == '' or phoneEntry.get("1.0","end-1c") == '' or genEntry.get("1.0","end-1c") == '' or branchEntry.get("1.0","end-1c")=='' or degreeEntry.get("1.0","end-1c")=='' or start_year.get("1.0","end-1c") == '' or end_year.get("1.0","end-1c") == '' or passwordEntry.get("1.0","end-1c")=='' or confirm_PasswordEntry.get("1.0","end-1c")=='':
        messagebox.showerror('Error','All fields are Required')
    elif signup_passwordEntry.get() !=signup_confirm_PasswordEntry.get():
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
        mycursor.execute(query,(signup_emailEntry.get()))

        row=mycursor.fetchone()

        if row !=None:
            messagebox.showerror('Error', 'Email Already exists')
        else:

            query='insert into registration13(email_id,name,age,phone_no,password,gender,branch,degree,from_date,to_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            mycursor.execute(query,(signup_emailEntry.get(),signup_nameEntry.get(),signup_ageEntry.get(),signup_phoneEntry.get(),signup_passwordEntry.get(),signup_genEntry.get(),signup_branchEntry.get(),signup_degreeEntry.get(),signup_start_year.get(),signup_end_year.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registration is successful")
            clear()
            signup_window.destroy()
            import signin







def login_page():
    signup_window.destroy()
    import signin










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
nameEntry=Entry(frame,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
nameEntry= tk.Text(frame, height=1, width=25, wrap='word')
nameEntry.place(x=80,y=200)
#nameEntry.grid(row=2,column=6,sticky='w',padx=25)
ageLabel=Label(frame,text='Age',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#ageLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
ageLabel.config(width=25,height=1)
ageLabel.place(x=500,y=170)
ageEntry=Spinbox(frame,width=10,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1',from_=12 ,to=30)
#ageEntry.grid(row=4,column=0,sticky='w',padx=25)
ageEntry = tk.Text(frame, height=1, width=25, wrap='word')
ageEntry.place(x=500,y=200)
emailLabel=Label(frame,text='Email',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#emailLabel.grid(row=0,column=0,sticky='w',padx=25,pady=(10,0))
emailLabel.config(width=25,height=1)
emailLabel.place(x=500,y=294)
emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
#emailEntry.grid(row=2,column=0,sticky='w',padx=25)
emailEntry = tk.Text(frame, height=1, width=25, wrap='word')
emailEntry.place(x=500,y=325)
phoneLabel=Label(frame,text='Phone No.',font=('Open Sans',15,'bold'),bg='Light blue',fg='black')
#phoneLabel.grid(row=3,column=5,sticky='w',padx=25,pady=(10,0))
phoneLabel.config(width=25,height=1)
phoneLabel.place(x=80,y=230)
phoneEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',10,'bold'),fg='black',bg='white')
#phoneEntry.grid(row=4,column=5,sticky='w',padx=25)
phoneEntry = tk.Text(frame, height=1, width=25, wrap='word')
phoneEntry.place(x=80,y=260)
genLabel=Label(frame,text='Gender',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#genLabel.grid(row=3,column=6,sticky='w',padx=25,pady=(10,0))
genLabel.config(width=25,height=1)
genLabel.place(x=480,y=230)
genEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',10,'bold'),fg='black',bg='white')
#genEntry.grid(row=4,column=6,sticky='w',padx=25)
genEntry = tk.Text(frame, height=1, width=25, wrap='word')
genEntry.place(x=500,y=260)
degreeLabel=Label(frame,text='Degree',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#degreeLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
degreeLabel.config(width=25,height=1)
degreeLabel.place(x=80,y=285)
degreeEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),fg='black',bg='white')
#degreeEntry.grid(row=6,column=0,sticky='w',padx=25)
degreeEntry = tk.Text(frame, height=1, width=25, wrap='word')
degreeEntry.place(x=80,y=325)
branchLabel=Label(frame,text='Branch',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#branchLabel.grid(row=5,column=5,sticky='w',padx=25,pady=(10,0))
branchLabel.config(width=25,height=1)
branchLabel.place(x=80,y=355)
branchEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),fg='black',bg='white')
#branchEntry.grid(row=6,column=5,sticky='w',padx=25)
branchEntry = tk.Text(frame, height=1, width=25, wrap='word')
branchEntry.place(x=80,y=380)
#fromLabel=Label(frame,text='From',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
#fromLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
#fromLabel.config(width=25,height=1)
#fromLabel.place(x=250,y=30)
start_year = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
#start_year.grid(row=8,column=0,sticky='w',padx=25)
start_year.config(width=9)
start_year.place(x=490,y=380)


# Create a Spinbox widget for the ending year
toLabel=Label(frame,text='To',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
toLabel.config(width=5,height=1)
toLabel.place(x=570,y=370)
end_year = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
#end_year.grid(row=8,column=5,sticky='w',padx=25)
end_year.config(width=9)
end_year.place(x=630,y=380)

start_year1 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
#start_year.grid(row=8,column=0,sticky='w',padx=25)
start_year1.config(width=9)
start_year1.place(x=490,y=510)


# Create a Spinbox widget for the ending year
toLabel1=Label(frame,text='To',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
toLabel1.config(width=5,height=1)
toLabel1.place(x=570,y=510)
end_year1 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
#end_year.grid(row=8,column=5,sticky='w',padx=25)
end_year1.config(width=9)
end_year1.place(x=630,y=510)

start_year2 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
#start_year.grid(row=8,column=0,sticky='w',padx=25)
start_year2.config(width=9)
start_year2.place(x=490,y=570)


# Create a Spinbox widget for the ending year
toLabel2=Label(frame,text='To',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
toLabel2.config(width=5,height=1)
toLabel2.place(x=570,y=570)
end_year2 = Spinbox(frame,width=10,font=('Open Sans',10,'bold'),fg='black',bg='white', from_=2015, to=2030)
#end_year.grid(row=8,column=5,sticky='w',padx=25)
end_year2.config(width=9)
end_year2.place(x=630,y=570)






# usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
# usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
#
# usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
# usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#passwordLabel.grid(row=9,column=6,sticky='w',padx=25,pady=(10,0))
passwordLabel.config(width=25,height=1)
passwordLabel.place(x=80,y=420)
passwordEntry=Entry(frame,width=25,font=('Open Sans',11,'bold'),fg='black',bg='white')
#passwordEntry.grid(row=10,column=6,sticky='w',padx=25)
PasswordEntry = tk.Text(frame, height=1, width=25, wrap='word')
passwordEntry.place(x=80,y=450)

confirm_PasswordLabel=Label(frame,text='Confirm Password',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#confirm_PasswordLabel.grid(row=40,column=6,sticky='w',padx=25,pady=(10,0))
confirm_PasswordLabel.config(width=20,height=1)
confirm_PasswordLabel.place(x=480,y=420)
confirm_PasswordEntry=Entry(frame,width=25,font=('Open Sans',10,'bold'),fg='black',bg='light blue')
#confirm_PasswordEntry.grid(row=45,column=6,sticky='w',padx=25)
confirm_PasswordEntry = tk.Text(frame, height=1, width=25, wrap='word')
confirm_PasswordEntry.place(x=500,y=450)

school_nameLabel=Label(frame,text='School Name',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#confirm_PasswordLabel.grid(row=40,column=6,sticky='w',padx=25,pady=(10,0))
school_nameLabel.config(width=20,height=1)
school_nameLabel.place(x=85,y=480)
school_nameEntry=Entry(frame,width=25,font=('Open Sans',10,'bold'),fg='black',bg='light blue')
#confirm_PasswordEntry.grid(row=45,column=6,sticky='w',padx=25)
school_nameEntry = tk.Text(frame, height=1, width=25, wrap='word')
school_nameEntry.place(x=80,y=510)

college_nameLabel=Label(frame,text='College Name',font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#confirm_PasswordLabel.grid(row=40,column=6,sticky='w',padx=25,pady=(10,0))
college_nameLabel.config(width=20,height=1)
college_nameLabel.place(x=85,y=540)
college_nameEntry=Entry(frame,width=25,font=('Open Sans',10,'bold'),fg='black',bg='light blue')
#confirm_PasswordEntry.grid(row=45,column=6,sticky='w',padx=25)
college_nameEntry = tk.Text(frame, height=1, width=25, wrap='word')
college_nameEntry.place(x=80,y=570)



#confirm_PasswordEntry.place(x=250,y=30)
check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Open Sans',12,'bold'),fg='black',bg='light blue',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
#termsandconditions.grid(row=51,column=5,pady=0,padx=5)
termsandconditions.place(x=230,y=600)
signupButton=Button(frame,text='Sign up',font=('Open Sans',15,'bold'),bd=0,bg='white',
                    fg='black',activebackground='light blue',activeforeground='black',width=17,
                    command=connect_database)
signupButton.place(x=300,y=650)
signupButton.config(height=1,width=10)

#signupButton.grid(row=50,column=5,pady=(90,30))

alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans',15,'bold'),bg='light blue',fg='black')
#alreadyaccount.grid(row=60,column=5,sticky='w',padx=10,pady=65)
alreadyaccount.config(height=1,width=20)
alreadyaccount.place(x=270,y=700)
loginButton=Button(frame,text='Log in',font=('Open Sans',15,'bold underline'),bg='light blue',fg='black',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=330,y=740)

signup_window.mainloop()