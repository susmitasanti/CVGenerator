from tkinter import *
from tkinter import messagebox

import pymysql 
from PIL import ImageTk
# import pymysql

def clear():
    emailEntry.delete(0,END)

    passwordEntry.delete(0,END)
    confirm_PasswordEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or nameEntry.get() == '' or ageEntry.get() == '' or phoneEntry.get() == '' or genEntry.get() == '' or branchEntry.get()=='' or degreeEntry.get()=='' or start_year.get() == '' or end_year.get() == '' or passwordEntry.get()=='' or confirm_PasswordEntry.get()=='':
        messagebox.showerror('Error','All fields are Required')
    elif passwordEntry.get() !=confirm_PasswordEntry.get():
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
        mycursor.execute(query,(emailEntry.get()))

        row=mycursor.fetchone()

        if row !=None:
            messagebox.showerror('Error', 'Email Already exists')
        else:

            query='insert into registration13(email_id,name,age,phone_no,password,gender,branch,degree,from_date,to_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            mycursor.execute(query,(emailEntry.get(),nameEntry.get(),ageEntry.get(),phoneEntry.get(),passwordEntry.get(),genEntry.get(),branchEntry.get(),degreeEntry.get(),start_year.get(),end_year.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registration is successful")
            clear()
            window.destroy()
            import signin







def login_page():
    window.destroy()
    import signin










window=Tk()
window.title('Signup Page')
window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=background)
bgLabel.grid()
frame=Frame(window,bg='white')
frame.place(x=60,y=60)
heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=5,padx=10,pady=10)


nameLabel=Label(frame,text='Name',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
nameLabel.grid(row=1,column=6,sticky='w',padx=25,pady=(10,0))
nameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
nameEntry.grid(row=2,column=6,sticky='w',padx=25)
ageLabel=Label(frame,text='Age',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
ageLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
ageEntry=Spinbox(frame,width=10,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1',from_=12 ,to=30)
ageEntry.grid(row=4,column=0,sticky='w',padx=25)


emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)
phoneLabel=Label(frame,text='Phone No.',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
phoneLabel.grid(row=3,column=5,sticky='w',padx=25,pady=(10,0))

phoneEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
phoneEntry.grid(row=4,column=5,sticky='w',padx=25)
genLabel=Label(frame,text='Gender',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
genLabel.grid(row=3,column=6,sticky='w',padx=25,pady=(10,0))
genEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
genEntry.grid(row=4,column=6,sticky='w',padx=25)
degreeLabel=Label(frame,text='Degree',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
degreeLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

degreeEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
degreeEntry.grid(row=6,column=0,sticky='w',padx=25)
branchLabel=Label(frame,text='Branch',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
branchLabel.grid(row=5,column=5,sticky='w',padx=25,pady=(10,0))

branchEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
branchEntry.grid(row=6,column=5,sticky='w',padx=25)
fromLabel=Label(frame,text='From',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
fromLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
start_year = Spinbox(frame,width=10,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1', from_=2015, to=2030)
start_year.grid(row=8,column=0,sticky='w',padx=25)

# Create a Spinbox widget for the ending year
toLabel=Label(frame,text='To',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
toLabel.grid(row=7,column=5,sticky='w',padx=25,pady=(10,0))
end_year = Spinbox(frame,width=10,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1', from_=2015, to=2030)
end_year.grid(row=8,column=5,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=9,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=10,column=0,sticky='w',padx=25)

confirm_PasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirm_PasswordLabel.grid(row=9,column=6,sticky='w',padx=25,pady=(10,0))

confirm_PasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirm_PasswordEntry.grid(row=10,column=6,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandconditions.grid(row=11,column=0,pady=10,padx=15)
signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',
                    fg='white',activebackground='firebrick1',activeforeground='white',width=17,
                    command=connect_database)

signupButton.grid(row=12,column=5,pady=10)

alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=15,column=6,sticky='w',padx=25,pady=10)
loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=750,y=460)

window.mainloop()