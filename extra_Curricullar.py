from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox

import pathlib

academic=Tk()
academic.title("Academics")
academic.geometry('700x400+300+200')
academic.resizable(False,False)
academic.configure(bg='#326273')

Label(academic,text='Please fill Your Academic Details',font="arial 13",bg="#326273",fg="#fff").place(x=20,y=20)

Label(academic,text='Name',font=23,bg='#326273',fg="#fff").place(x=50,y=100)

academic.mainloop()


