import string
from time import strftime
import tkinter as tk
from tkinter import CENTER, Toplevel, ttk
import os

window = tk.Tk()
window.title("Simple_Assistant")
window.geometry("640x480")
window.minsize(400, 400)

name = os.getlogin()
task_var = tk.StringVar()
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
    button_submit = ttk.Button(new_window,
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

button1 = ttk.Button (window, text = "Task 1", command = updateTask1)
button1.place(x = 320, y = 200,
             anchor = CENTER)

button2 = ttk.Button (window, text = "Task 2", command = updateTask2)
button2.place(x = 320, y = 240,
             anchor = CENTER)

button3 = ttk.Button (window, text = "Task 3", command = updateTask3)
button3.place(x = 320, y = 280,
             anchor = CENTER)


mainClock()
greeting()

window.mainloop()
