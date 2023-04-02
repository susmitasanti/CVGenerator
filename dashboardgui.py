
from tkinter import *
from tkinter import Tk

import pymysql
from PIL import ImageTk #pip install pillow
# import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.ttk import Combobox



dashboard_window = Tk()

#dashboard_window.geometry('990x660+50+50')
dashboard_window.geometry("{0}x{1}+0+0".format(dashboard_window.winfo_screenwidth(), dashboard_window.winfo_screenheight()))
dashboard_window.resizable(0,0)
dashboard_window.configure(bg='light grey')
background=ImageTk.PhotoImage(file='dashboard.png')

bgLabel=Label(dashboard_window,image=background)
bgLabel.config(width=800, height=800)
bgLabel.place(x=0,y=0)


img = Image.open("plus_sign.jpg")

img_tk = ImageTk.PhotoImage(img)


# Create a frame to hold the navbar buttons
navbar_frame = Frame(dashboard_window,bg="light grey")
navbar_frame.config(height=700,width=600)
navbar_frame.place(x=500,y=500)
# Create a button for each page
dashboard_button=  Button(navbar_frame, text="Dashboard",width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
cocurricular_button = Button(navbar_frame, text="Co-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
extracurricular_button = Button(navbar_frame, text="Extra-Curricular", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
internships_button = Button(navbar_frame, text="Internships",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
projects_button = Button(navbar_frame, text="Projects", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
button = Button(navbar_frame, text="Create", compound="left", width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
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
# connection = pymysql.connect(
# host="127.0.0.1",
# user="root",
# password="Harshita@030712",
# database="cv_generator"    
#     )
# # Create a cursor object
# cursor = connection.cursor()

# # Execute a SELECT statement to fetch data
# cursor.execute('''SELECT  `name`, `age`, `phone_no`, `gender`, `branch`, `degree`, `from_date`, `to_date` FROM `registration13` WHERE email_id=%s''', (username_))

# # Fetch all the rows using fetchall() method
# result = cursor.fetchone()

   # Create a frame for the main content of the window
content_frame = Frame(dashboard_window,bg="light blue")
content_frame.config(height=60,width=50)
content_frame.place(x=100,y=200)
# name = result[0]
# age = result[1]
# phone_no = result[2]
# gender = result[3]
# branch = result[4]
# degree= result[5]
# from_date= result[6]
# to_date= result[7]


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




name_value = Label(content_frame, text="name",font="35",bg="light blue")
name_value.place(x=350,y=150)
age_value = Label(content_frame, text="age",font="35",bg="light blue")
age_value.place(x=350,y=200)
phone_value = Label(content_frame, text="phone",font="35",bg="light blue")
phone_value.place(x=350,y=250)
gender_value = Label(content_frame, text="gender",font="35",bg="light blue")
gender_value.place(x=350,y=300)
branch_value = Label(content_frame, text="branch",font="35",bg="light blue")
branch_value.place(x=350,y=350)
degree_value = Label(content_frame, text="degree",font="35",bg="light blue")
degree_value.place(x=350,y=400)
from_value = Label(content_frame, text="from_date",font="35",bg="light blue")
from_value.place(x=350,y=450)
to_value = Label(content_frame, text="to_date",font="35",bg="light blue")
to_value.place(x=350,y=500)


#name_label.grid(row=0, column=0)
#name_value.grid(row=0, column=5)

#age_label.grid(row=1, column=0)
#age_value.grid(row=1, column=1)

#phone_label.grid(row=2, column=0)
#phone_value.grid(row=2, column=1)

#gender_label.grid(row=3, column=0)
#gender_value.grid(row=3, column=1)

#branch_label.grid(row=4, column=0)
#branch_value.grid(row=4, column=1)

#degree_label.grid(row=5, column=0)
#degree_value.grid(row=5, column=1)

#from_label.grid(row=6, column=0)
#from_value.grid(row=6, column=1)

#to_label.grid(row=7, column=0)
#to_value.grid(row=80, column=50)


# Pack the main content frame
content_frame.pack(expand=True, fill="both")

# Run the Tkinter event loop
dashboard_window.mainloop()