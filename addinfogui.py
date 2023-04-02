from tkinter import *
from tkinter import Tk

import pymysql
from PIL import ImageTk #pip install pillow
# import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.ttk import Combobox


add_information=Tk()    #700x400+300+200
add_information.title("Extra Curricular")
#add_information.geometry('800x800+300+200')
add_information.geometry("{0}x{1}+0+0".format(add_information.winfo_screenwidth(), add_information.winfo_screenheight()))
add_information.resizable(False,False)
add_information.configure(bg='light blue')
# icon_image=PhotoImage(file="extra.png")
# add_information.iconphoto(False,icon_image)


Label(add_information,text='Additional Information',font=("arial 13",16,'bold'),bg="light blue",fg="black").place(x=100,y=20)

titleLabel=Label(add_information,text='Job Title',font=('sifon',15,'bold'),bg='light blue',fg='black')
titleLabel.place(x=50,y=100)
titleEntry=Entry(add_information,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
titleEntry.place(x=200,y=100)

addressLabel=Label(add_information,text='Address',font=('sifon',15,'bold'),bg='light blue',fg='black')
addressLabel.place(x=50,y=150)
addressEntry=Entry(add_information,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
addressEntry.place(x=200,y=150)

gitLabel=Label(add_information,text='Github Link',font=('sifon',15,'bold'),bg='light blue',fg='black')
gitLabel.place(x=50,y=200)
gitEntry=Entry(add_information,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
gitEntry.place(x=200,y=200)

linkedInLabel=Label(add_information,text='LinkedIn Link',font=('sifon',15,'bold'),bg='light blue',fg='black')
linkedInLabel.place(x=50,y=250)
linkedInEntry=Entry(add_information,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
linkedInEntry.place(x=200,y=250)

skill1_Label=Label(add_information,text='Skill 1',font=('sifon',15,'bold'),bg='light blue',fg='black')
skill1_Label.place(x=100,y=300)
skill1_Entry=Entry(add_information,width=15,font=('sifon',15,'bold'),fg='black',bg='white')
skill1_Entry.place(x=200,y=300)

skill2_Label=Label(add_information,text='Skill 2',font=('sifon',15,'bold'),bg='light blue',fg='black')
skill2_Label.place(x=370,y=300)
skill2_Entry=Entry(add_information,width=15,font=('sifon',15,'bold'),fg='black',bg='white')
skill2_Entry.place(x=470,y=300)

skill3_Label=Label(add_information,text='Skill 3',font=('sifon',15,'bold'),bg='light blue',fg='black')
skill3_Label.place(x=100,y=350)
skill3_Entry=Entry(add_information,width=15,font=('sifon',15,'bold'),fg='black',bg='white')
skill3_Entry.place(x=200,y=350)

skill4_Label=Label(add_information,text='Skill 4',font=('sifon',15,'bold'),bg='light blue',fg='black')
skill4_Label.place(x=370,y=350)
skill4_Entry=Entry(add_information,width=15,font=('sifon',15,'bold'),fg='black',bg='white')
skill4_Entry.place(x=470,y=350)

skill5_Label=Label(add_information,text='Skill 5',font=('sifon',15,'bold'),bg='light blue',fg='black')
skill5_Label.place(x=100,y=400)
skill5_Entry=Entry(add_information,width=15,font=('sifon',15,'bold'),fg='black',bg='white')
skill5_Entry.place(x=200,y=400)

skill6_Label=Label(add_information,text='Skill 6',font=('sifon',15,'bold'),bg='light blue',fg='black')
skill6_Label.place(x=370,y=400)
skill6_Entry=Entry(add_information,width=15,font=('sifon',15,'bold'),fg='black',bg='white')
skill6_Entry.place(x=470,y=400)


resume_nameLabel=Label(add_information,text='Resume Name',font=('sifon',15,'bold'),bg='light blue',fg='black')
resume_nameLabel.place(x=50,y=450)
resume_nameEntry=Entry(add_information,width=45,font=('sifon',15,'bold'),fg='black',bg='white')
resume_nameEntry.place(x=200,y=450)

addButton=Button(add_information,text='Add',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                fg='white',activebackground='blue',activeforeground='white',width=10)

addButton.place(x=200,y=500)


createButton=Button(add_information,text='Create',font=('Open Sans',16,'bold'),bd=0,bg='blue',
                fg='white',activebackground='blue',activeforeground='white',width=10)

createButton.place(x=300,y=500)


add_information.mainloop()