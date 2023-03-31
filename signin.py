# signin.py

from tkinter import *

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

login_window=""



internship_page=""
internship_window=""

academics_page=""
academics_window=""

cocurricular_page=""
cocurricular_window=""

extracurricular_page=""
extracurricular_window=""

projects_page=""
projects_window=""

activity_Combobox=""
conductEntry=""
part_Combobox=""
rankEntry=""


def forms_connection():
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO `cocurricular`(`email_id`, `activity_name`, `conducted_by`, `participation_level`, `rank`) VALUES (%s,%s,%s,%s,%s)''', (username_), activity_Combobox.get(), conductEntry.get(), part_Combobox.get(), rankEntry.get() )

    connection.commit()    
    
def set_username(name):
    global signin
    global username
    username = name
    print(name)

def signup_page():
        global login_window
        login_window.destroy()
        import signup   

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

def handle_click1(page):
            global academics_window
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

def handle_click2(page):
            global cocurricular_window
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

def handle_click3(page):
    global extracurricular_window
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

def handle_click4(page):
    global internship_window
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

def handle_click5(page):
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
    else:
        projects_window.destroy()
        projects_page()
     

def plus_cocurricular():
        cocurricular=Tk()    #700x400+300+200
        cocurricular.title("Co-Curricular")
        cocurricular.geometry('700x400+300+200')
        cocurricular.resizable(False,False)
        cocurricular.configure(bg='#FF3030')
        # icon_image=PhotoImage(file="co.png")
        # cocurricular.iconphoto(False,icon_image)
        activityLabel=Label(cocurricular,text='Activity',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
        activityLabel.place(x=50,y=100)
        activity_Combobox=Combobox(cocurricular,values=['Workshop','Hackathon'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
        activity_Combobox.place(x=200,y=100)
        activity_Combobox.set('Workshop')
        Label(cocurricular,text='Co-curricular – discovering what’s possible....',font=('arial 13',16,'bold'),bg="#FF3030",fg="#fff").place(x=150,y=20)
        conductLabel=Label(cocurricular,text='Conducted By ',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
        conductLabel.place(x=50,y=150)
        conductEntry=Entry(cocurricular,width=45,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
        conductEntry.place(x=200,y=150)
        participationLabel=Label(cocurricular,text='Participation Level',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
        participationLabel.place(x=40,y=200)
        part_Combobox=Combobox(cocurricular,values=['Volunteer','Participant'],font=('Microsoft Yahei UI Light',10,'bold'),state='r',width=14)
        part_Combobox.place(x=210,y=200)
        part_Combobox.set('Participant')
        rankLabel=Label(cocurricular,text='Rank',font=('Microsoft Yahei UI Light',12,'bold'),bg='#FF3030',fg='#fff')
        rankLabel.place(x=50,y=250)
        rankEntry=Entry(cocurricular,width=10,font=('Microsoft Yahei UI Light',12,'bold'),fg='black',bg='white')
        rankEntry.place(x=200,y=250)

        signupButton=Button(cocurricular,text='Submit',font=('Open Sans',16,'bold'),bd=0,bg='blue',fg='white',activebackground='blue',activeforeground='white',width=10, command=cocurricular_execute)
        signupButton.place(x=300,y=350)

        cocurricular.mainloop()

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

                

def login_page():
        global usernameEntry
        global login_window
        global openeye
        global passwordEntry
        global eyeButton
        login_window=Tk()
        login_window.geometry('990x660+50+50')
        login_window.resizable(0,0)
        bgImage=ImageTk.PhotoImage(file='bg.jpg')
        # login_window.state("zoom")

        bgLabel=Label(login_window,image=bgImage)
        bgLabel.place(x=0,y=0)
        heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
        heading.place(x=605,y=120)
        usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
        usernameEntry.place(x=580,y=200)
        usernameEntry.insert(0,'Email-id')
        usernameEntry.bind('<FocusIn>',user_enter)

        frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
        frame1.place(x=580,y=222)

        passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
        passwordEntry.place(x=580,y=260)
        passwordEntry.insert(0,'Password')
        passwordEntry.bind('<FocusIn>',password_enter)
        frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
        frame2.place(x=580,y=282)

        openeye=PhotoImage(file='openeye.png')
        eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
        eyeButton.place(x=800,y=255)

        forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1')

        forgetButton.place(x=715,y=295)

        loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
        loginButton.place(x=578,y=350)

        orlabel=Label(login_window,text="----------------OR---------------",font=('Open Sans',16),fg='firebrick1',bg='white')
        orlabel.place(x=583,y=400)

        facebook_logo=PhotoImage(file='facebook.png')
        fblabel=Label(login_window,image=facebook_logo,bg='white')
        fblabel.place(x=640,y=440)
        google_logo=PhotoImage(file='google.png')
        googlelabel=Label(login_window,image=google_logo,bg='white')
        googlelabel.place(x=690,y=440)
        twitter_logo=PhotoImage(file='twitter.png')
        twitterlabel=Label(login_window,image=twitter_logo,bg='white')
        twitterlabel.place(x=740,y=440)

        signuplabel=Label(login_window,text="Dont have an account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
        signuplabel.place(x=590,y=500)
        newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='firebrick1',cursor='hand2',bd=0,command=signup_page)
        newaccountButton.place(x=727,y=500)

        login_window.mainloop()

def dashboard_page():
        global connection
        global cursor
        global data
        global username_
        global dashboard_window
        global tree

        dashboard_window = Tk()

        dashboard_window.geometry('990x660+50+50')
        dashboard_window.resizable(0,0)
        

        img = Image.open("plus_sign.jpg")

        img_tk = ImageTk.PhotoImage(img)


        # Create a frame to hold the navbar buttons
        navbar_frame = Frame(dashboard_window, padx=15, pady=15)

    # Create a button for each page
        academics_button = Button(navbar_frame, text="Academics", command=lambda: handle_click("academics_page"), width=15, height=5)
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", command=lambda: handle_click("cocurricular_page"), width=15, height=5)
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular", command=lambda: handle_click("extracurricular_page"), width=15, height=5)
        internships_button = Button(navbar_frame, text="Internships", command=lambda: handle_click("internship_page"), width=15, height=5)
        projects_button = Button(navbar_frame, text="Projects", command=lambda: handle_click("projects_page"), width=15, height=5)
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65)
        # button = Button(navbar_frame, compound="left", width=5, height=5)



    # Pack the navbar buttons horizontally
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
        content_frame = Frame(dashboard_window)

        name = result[0]
        age = result[1]
        phone_no = result[2]
        gender = result[3]
        branch = result[4]
        degree= result[5]
        from_date= result[6]
        to_date= result[7]


        name_label = Label(content_frame, text="Name: ")
        age_label = Label(content_frame, text="Age: ")
        phone_label = Label(content_frame, text="Phone No.: ")
        gender_label = Label(content_frame, text="Gender: ")
        branch_label= Label(content_frame, text="Branch: ")
        degree_label= Label(content_frame, text="Degree: ")
        from_label= Label(content_frame, text="From: ")
        to_label= Label(content_frame, text="To: ")




        name_value = Label(content_frame, text=name)
        age_value = Label(content_frame, text=age)
        phone_value = Label(content_frame, text=phone_no)
        gender_value = Label(content_frame, text=gender)
        branch_value = Label(content_frame, text=branch)
        degree_value = Label(content_frame, text=degree)
        from_value = Label(content_frame, text=from_date)
        to_value = Label(content_frame, text=to_date)

        
        name_label.grid(row=0, column=0)
        name_value.grid(row=0, column=1)

        age_label.grid(row=1, column=0)
        age_value.grid(row=1, column=1)

        phone_label.grid(row=2, column=0)
        phone_value.grid(row=2, column=1)

        gender_label.grid(row=3, column=0)
        gender_value.grid(row=3, column=1)

        branch_label.grid(row=4, column=0)
        branch_value.grid(row=4, column=1)

        degree_label.grid(row=5, column=0)
        degree_value.grid(row=5, column=1)

        from_label.grid(row=6, column=0)
        from_value.grid(row=6, column=1)

        to_label.grid(row=7, column=0)
        to_value.grid(row=7, column=1)


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

            academics_window.geometry('990x660+50+50')
            academics_window.resizable(0,0)

            img = Image.open("plus_sign.jpg")

            img_tk = ImageTk.PhotoImage(img)


            # Create a frame to hold the navbar buttons
            navbar_frame = Frame(academics_window, padx=15, pady=15)

            # Create a button for each page
            academics_button = Button(navbar_frame, text="Academics", command=lambda: handle_click1("academics_page"), width=15, height=5, bg="firebrick1")
            cocurricular_button = Button(navbar_frame, text="Co-Curricular", command=lambda: handle_click1("cocurricular_page"), width=15, height=5)
            extracurricular_button = Button(navbar_frame, text="Extra-Curricular", command=lambda: handle_click1("extracurricular_page"), width=15, height=5)
            internships_button = Button(navbar_frame, text="Internships", command=lambda: handle_click1("internship_page"), width=15, height=5)
            projects_button = Button(navbar_frame, text="Projects", command=lambda: handle_click1("projects_page"), width=15, height=5)
            button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65)

            # Pack the navbar buttons horizontally
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
            cursor.execute('''SELECT * FROM internship WHERE email_id=%s''', (username_))
            # Fetch all the rows using fetchall() method
            data = cursor.fetchall()

            # Create a frame for the main content of the window
            content_frame = Frame(academics_window)

            # Create a Treeview widget
            tree = ttk.Treeview(academics_window)

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
            tree.heading("column1", text="Internship Name", anchor=CENTER)
            tree.heading("column2", text="Domain", anchor=CENTER)
            tree.heading("column3", text="From", anchor=CENTER)
            tree.heading("column4", text="To", anchor=CENTER)


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

        cocurricular_window.geometry('990x660+50+50')
        cocurricular_window.resizable(0,0)

        img = Image.open("plus_sign.jpg")

        img_tk = ImageTk.PhotoImage(img)


        # Create a frame to hold the navbar buttons
        navbar_frame = Frame(cocurricular_window, padx=15, pady=15)

        # Create a button for each page
        academics_button = Button(navbar_frame, text="Academics", command=lambda: handle_click2("academics_page"), width=15, height=5)
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", command=lambda: handle_click2("cocurricular_page"), width=15, height=5, bg="firebrick1")
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular", command=lambda: handle_click2("extracurricular_page"), width=15, height=5)
        internships_button = Button(navbar_frame, text="Internships", command=lambda: handle_click2("internship_page"), width=15, height=5)
        projects_button = Button(navbar_frame, text="Projects", command=lambda: handle_click2("projects_page"), width=15, height=5)
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, command=plus_cocurricular)

        # Pack the navbar buttons horizontally
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
        cursor.execute('''SELECT  `activity_name`, `conducted_by`, `participation_level`, `rank` FROM `cocurricular` WHERE email_id=%s''', (username_))

        # Fetch all the rows using fetchall() method
        data = cursor.fetchall()

        # Create a frame for the main content of the window
        content_frame = Frame(cocurricular_window)

        # Create a Treeview widget
        tree = ttk.Treeview(cocurricular_window)

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
        tree.heading("column1", text="Activity Name", anchor=CENTER)
        tree.heading("column2", text="Conducted by", anchor=CENTER)
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
        cocurricular_window.mainloop()

def extracurricular_page():
        global connection
        global cursor
        global data
        global username_
        global extracurricular_window
        global tree

        extracurricular_window = Tk()

        extracurricular_window.geometry('990x660+50+50')
        extracurricular_window.resizable(0,0)

        img = Image.open("plus_sign.jpg")

        img_tk = ImageTk.PhotoImage(img)


        # Create a frame to hold the navbar buttons
        navbar_frame = Frame(extracurricular_window, padx=15, pady=15)

        # Create a button for each page
        academics_button = Button(navbar_frame, text="Academics", command=lambda: handle_click3("academics_page"), width=15, height=5)
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", command=lambda: handle_click3("cocurricular_page"), width=15, height=5)
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular", command=lambda: handle_click3("extracurricular_page"), width=15, height=5, bg="firebrick1")
        internships_button = Button(navbar_frame, text="Internships", command=lambda: handle_click3("internship_page"), width=15, height=5)
        projects_button = Button(navbar_frame, text="Projects", command=lambda: handle_click3("projects_page"), width=15, height=5)
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65)

        # Pack the navbar buttons horizontally
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
        content_frame = Frame(extracurricular_window)

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

        internship_window.geometry('990x660+50+50')
        internship_window.resizable(0,0)

        img = Image.open("plus_sign.jpg")

        img_tk = ImageTk.PhotoImage(img)


            # Create a frame to hold the navbar buttons
        navbar_frame = Frame(internship_window, padx=15, pady=15)

            # Create a button for each page
        academics_button = Button(navbar_frame, text="Academics", command=lambda: handle_click4("academics_page"), width=15, height=5)
        cocurricular_button = Button(navbar_frame, text="Co-Curricular", command=lambda: handle_click4("cocurricular_page"), width=15, height=5)
        extracurricular_button = Button(navbar_frame, text="Extra-Curricular", command=lambda: handle_click4("extracurricular_page"), width=15, height=5)
        internships_button = Button(navbar_frame, text="Internships", command=lambda: handle_click4("internship_page"), width=15, height=5, bg="firebrick1")
        projects_button = Button(navbar_frame, text="Projects", command=lambda: handle_click4("projects_page"), width=15, height=5)
        button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65)
        # button = tk.Button(navbar_frame, compound="left", width=60, height=65)


            # Pack the navbar buttons horizontally
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
        cursor.execute('''SELECT `name`, `domain`, `from_date`, `to_date` FROM `internship` WHERE email_id=%s''', (username_))
            

            # Fetch all the rows using fetchall() method
        data = cursor.fetchall()

            # Create a frame for the main content of the window
        content_frame = Frame(internship_window)

            # Create a Treeview widget
        tree = ttk.Treeview(internship_window)

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
        tree.heading("column1", text="Name", anchor=CENTER)
        tree.heading("column2", text="Domain", anchor=CENTER)
        tree.heading("column3", text="From", anchor=CENTER)
        tree.heading("column4", text="To", anchor=CENTER)


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
    projects_window = Tk()

    projects_window.geometry('990x660+50+50')
    projects_window.resizable(0,0)

    img = Image.open("plus_sign.jpg")

    img_tk = ImageTk.PhotoImage(img)


    # Create a frame to hold the navbar buttons
    navbar_frame = Frame(projects_window, padx=15, pady=15)

    # Create a button for each page
    academics_button = Button(navbar_frame, text="Academics", command=lambda: handle_click5("academics_page"), width=15, height=5)
    cocurricular_button = Button(navbar_frame, text="Co-Curricular", command=lambda: handle_click5("cocurricular_page"), width=15, height=5)
    extracurricular_button = Button(navbar_frame, text="Extra-Curricular", command=lambda: handle_click5("extracurricular_page"), width=15, height=5)
    internships_button = Button(navbar_frame, text="Internships", command=lambda: handle_click5("internship_page"), width=15, height=5)
    projects_button = Button(navbar_frame, text="Projects", command=lambda: handle_click5("projects_page"), width=15, height=5, bg="firebrick1")
    button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65)

    # Pack the navbar buttons horizontally
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
    content_frame = Frame(projects_window)

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




      

login_page()




