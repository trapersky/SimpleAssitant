import string
import time
from time import strftime
import tkinter as tk
from tkinter.ttk import *
from tkinter import ANCHOR, CENTER, LEFT, Toplevel, ttk
import os

window = tk.Tk()
window.title("Simple_Assistant")
window.geometry("640x480")
window.minsize(640, 480)
window.maxsize(640, 480)

name = os.getlogin()
task_var = tk.StringVar()
time_var = tk.StringVar()
tasks = ""
bclick = 0

def greeting():
    string = f"Hello {name}!"
    hello.config(text = string)
    
hello = tk.Label(font=("Arial", 20))
hello.place(relx = 0,
            rely = 0,
            anchor=tk.NW)    

def createTaskWindow():
    new_window = tk.Toplevel()
    new_window.title("Enter Task")
    new_window.minsize(400, 200)
    task_entry = tk.Entry(new_window, textvariable = task_var, font=("Arial", 20))
    task_entry.place(x = 200, y = 100,
                     anchor = tk.CENTER)
    button_submit = tk.Button(new_window,
                              text = "Submit",
                              command = lambda: [submit(), new_window.destroy()])
    button_submit.place(x = 200, y = 160,
                        anchor = tk.CENTER)

def submit():
    tasks = task_var.get()
    if bclick == 0: button1 ["text"] = tasks
    elif bclick == 1: button2 ["text"] = tasks
    elif bclick == 2: button3 ["text"] = tasks
        
def mainClock():
    string = strftime('%H:%M:%S')
    primary_timer.config(text = string)
    primary_timer.after(1000, mainClock)

primary_timer = tk.Label(font=('Arial',20))
primary_timer.place(relx = 1,
            rely = 0,
            anchor=tk.NE)

def updateTask1():
    if button1 ["text"] == "Task 1":
        global bclick
        bclick = 0
        createTaskWindow()
    else:
        button1 ["text"] = "Task 1"        

def updateTask2():
    if button2 ["text"] == "Task 2":
        global bclick
        bclick = 1
        createTaskWindow()
    else:
        button2 ["text"] = "Task 2"

def updateTask3():
    if button3 ["text"] == "Task 3":
        global bclick
        bclick = 2
        createTaskWindow()
    else:
        button3 ["text"] = "Task 3"

button1 = tk.Button (window, text = "Task 1", command = updateTask1, width = 30)
button1.place(x = 120, y = 200)

button2 = tk.Button (window, text = "Task 2", command = updateTask2, width = 30)
button2.place(x = 120, y = 240)

button3 = tk.Button (window, text = "Task 3", command = updateTask3, width = 30)
button3.place(x = 120, y = 280) 

timer1 = tk.Button (window, text = '00:00:00')
timer1.place(x = 340, y = 200)

timer2 = tk.Button (window, text = '00:00:00')
timer2.place(x = 340, y = 240)

timer3 = tk.Button (window, text = '00:00:00')
timer3.place(x = 340, y = 280)

pause1 = tk.Button (window, text = 'P', width = 2)
pause1.place(x = 390, y = 200)

pause2 = tk.Button (window, text = 'P', width = 2)
pause2.place(x = 390, y = 240)

pause3 = tk.Button (window, text = 'P', width = 2)
pause3.place(x = 390, y = 280)

start1 = tk.Button (window, text = 'S', width = 2)
start1.place(x = 412, y = 200)

start2 = tk.Button (window, text = 'S', width = 2)
start2.place(x = 412, y = 240)

start3 = tk.Button (window, text = 'S', width = 2)
start3.place(x = 412, y = 280)

clear1 = tk.Button (window, text = 'C', width = 2)
clear1.place(x = 434, y = 200)

clear2 = tk.Button (window, text = 'C', width = 2)
clear2.place(x = 434, y = 240)

clear3 = tk.Button (window, text = 'C', width = 2)
clear3.place(x = 434, y = 280)

mainClock()
greeting()

window.mainloop()
