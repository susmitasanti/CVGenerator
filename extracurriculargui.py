
from tkinter import *
from tkinter import Tk

import pymysql
from PIL import ImageTk #pip install pillow
# import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.ttk import Combobox

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
dashboard_button=  Button(navbar_frame, text="Dashboard",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
academics_button = Button(navbar_frame, text="Academics",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
cocurricular_button = Button(navbar_frame, text="Co-Curricular",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
extracurricular_button = Button(navbar_frame, text="Extra-Curricular",  width=15,height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
internships_button = Button(navbar_frame, text="Internships",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
projects_button = Button(navbar_frame, text="Projects",  width=15, height=5, bg='white',fg='black',font=('Open Sans',10,'bold'))
button = Button(navbar_frame, image=img_tk, compound="left", width=60, height=65, bg='white',fg='black',font=('Open Sans',10,'bold'))

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
# cursor = connection.cursor()

# # Execute a SELECT statement to fetch data
# cursor.execute("SELECT `event_name`, `activity_name`, `participation_level`, `rank` FROM `extra_curricular` WHERE email_id=%s", (username_))

# # Fetch all the rows using fetchall() method
# data = cursor.fetchall()

# Create a frame for the main content of the window
content_frame = Frame(extracurricular_window,bg="light blue")

# Create a Treeview widget
tree = ttk.Treeview(extracurricular_window,height=30)

# Define columns
tree["columns"] = ("column1", "column2", "column3", "column4")

# Format columns
tree.column("#0", width=0, stretch=NO)
tree.column("column1", width=300, anchor=CENTER)
tree.column("column2", width=300, anchor=CENTER)
tree.column("column3", width=300, anchor=CENTER)
tree.column("column4", width=300, anchor=CENTER)


# Add headings
tree.heading("#0", text="", anchor=CENTER)
tree.heading("column1", text="Event Name", anchor=CENTER,)
tree.heading("column2", text="Activity Name", anchor=CENTER)
tree.heading("column3", text="Participation Level", anchor=CENTER)
tree.heading("column4", text="Rank", anchor=CENTER)


# Add data to treeview
# for row in data:
tree.insert("", END, text="")



# Pack the Treeview widget
tree.pack()

# Pack the main content frame
content_frame.pack(expand=True, fill="both")


# Run the Tkinter event loop
extracurricular_window.mainloop()
