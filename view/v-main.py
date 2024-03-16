from tkinter import *
from datetime import datetime
import pytz




root = Tk()
root.geometry("800x600")
root.resizable(width=False, height=False)



# Disable resizing of the window
root.resizable(width=False, height=False)
def defaultFontTitle():
    return ("Helvetica",20,"bold")

def defaultFontSubTitle():
    return ("Helvetica",17,"bold")

def defaultCountry():
    return pytz.timezone('Asia/Manila')

def currentTime(defaultCountry):
    return datetime.now(defaultCountry)

def currentDate(defaultCountry):
    return datetime.now(defaultCountry)



label_ToDoListTitle = Label(root,text="To Do List",font=defaultFontTitle())
label_CurrentTime = Label(root,font= defaultFontTitle(),text=currentDate(defaultCountry()).strftime("%B - %d - %Y"))
label_list = Label(root,font=defaultFontSubTitle(),text="List of things to do")

input_task = Entry()
button_addTask = Button(text="Add Task")





label_ToDoListTitle.grid(column=0,row=0)
label_CurrentTime.grid(column=0,row=1)
label_list.grid(column=0,row=2)
input_task.grid(column=0,row=3)
button_addTask.grid(column=1,row=3)

root.mainloop()