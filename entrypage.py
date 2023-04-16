import sys
from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk
from tkinter import ttk


entryPage = Tk()
def login_page():
    entryPage.destroy()
    import signin1

entryPage.geometry("{0}x{1}+0+0".format(entryPage.winfo_screenwidth(), entryPage.winfo_screenheight()))
entryPage.overrideredirect(1)
background=ImageTk.PhotoImage(file='Student Edge (1290 × 750 px).png')
bgLabel= Label(entryPage, image=background)
bgLabel.grid()

entryPage.wm_attributes('-topmost',True)
entryPage.wm_attributes('-alpha',0.8)
exitbtn=Button(entryPage,text='X',command=lambda:exit_window(),font=('yu gothic ui',17,'bold'),fg='yellow',bd=0)
exitbtn.place(x=1260,y=0)
progressLabel=Label(entryPage,text='Please Wait...',font=('yu gothic ui',13,'bold'),bg='#DCDCDC')

progressLabel.place(x=800,y=500)
progress=Progressbar(entryPage,orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=600,y=540)


def exit_window():
    sys.exit(entryPage.destroy())


i=0
def load():
    global i
    if(i <=10):
        txt='Please Wait... '+ (str(10*i)+'%')
        progressLabel.config(text=txt)
        progressLabel.after(500,load)
        progress['value']=10*i
        i += 1
    else:
        login_page()


load()




entryPage.mainloop()