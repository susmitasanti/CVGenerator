from tkinter import *
from PIL import ImageTk #pip install pillow
from tkinter import ttk


dashboard_window=Tk()

dashboard_window.geometry('990x660+50+50')
dashboard_window.resizable(0,0)
bgImage=ImageTk.PhotoImage(file='bg4.png')

bgLabel=Label(dashboard_window,image=bgImage)
bgLabel.pack()

menu_bar=Menu()


























dashboard_window.mainloop()