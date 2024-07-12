from asyncio.windows_events import NULL
import string
import time
from time import strftime, strptime
import tkinter as tk
from tkinter import ANCHOR, CENTER, LEFT, ON, StringVar, Toplevel, ttk
import os

window = tk.Tk()
window.title("Simple_Assistant")
window.geometry("640x480")
window.minsize(640, 480)
window.maxsize(640, 480)

name = os.getlogin()
task_var = tk.StringVar()
time_var = tk.StringVar()
clock1_var = tk.StringVar()
clock1_var.set("00:00:00")
clock2_var = tk.StringVar()
clock2_var.set("00:00:00")
clock3_var = tk.StringVar()
clock3_var.set("00:00:00")
tasks = ""
bclick = 0
tclick = 0
countdown_timer = ""

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
    window.withdraw()
    new_window.minsize(400, 200)
    task_instruction = tk.Label (new_window,font=("Arial", 10), text = "Insert name of task")
    task_instruction.place (x = 200, y = 60,
                            anchor = tk.CENTER)
    task_entry = tk.Entry(new_window, textvariable = task_var, font=("Arial", 20))
    task_entry.place(x = 200, y = 100,
                     anchor = tk.CENTER)
    button_submit = tk.Button(new_window,
                              text = "Submit",
                              command = lambda: [submit(), new_window.destroy()])
    button_submit.place(x = 200, y = 160,
                        anchor = tk.CENTER)

def createTimeWindow():
    new_window = tk.Toplevel()
    new_window.title("Declare time")
    window.withdraw()
    new_window.minsize(400, 200)
    time_instruction = tk.Label (new_window,font=("Arial", 10), text = "Insert time in format HH:MM:SS")
    time_instruction.place (x = 200, y = 60,
                            anchor = tk.CENTER)
    time_entry = tk.Entry(new_window, validate="key", validatecommand = (window.register(validateTimeInput), "%P"), textvariable = time_var, font=("Arial", 20))
    time_entry.place(x = 200, y = 100,
                     anchor = tk.CENTER)
    button_submit = tk.Button(new_window,
                              text = "Set",
                              command = lambda: [assignTime(), new_window.destroy()])
    button_submit.place(x = 200, y = 160,
                        anchor = tk.CENTER)

def validateTimeInput(time_input):
    if len(time_input) > 8:
        return False
    checks = []
    for i, char in enumerate (time_input):
        if i in (2,5):
            checks.append(char == ":")
        elif i in (3,6):
            checks.append(char < "6")
        elif i == 0:
            checks.append(char < "3")
        else:
            checks.append(char.isdecimal())
    return all(checks)

def submit():
    tasks = task_var.get()
    if bclick == 0: button1 ["text"] = tasks
    elif bclick == 1: button2 ["text"] = tasks
    elif bclick == 2: button3 ["text"] = tasks
    window.deiconify()

def assignTime():
    countdown_timer = time_var.get()
    if tclick == 0:        
        clock1_var.set(countdown_timer)
    elif tclick == 1:
        clock2_var.set(countdown_timer)
    elif tclick == 2:
        clock3_var.set(countdown_timer)
    window.deiconify()
    
       
def mainClock():
    string = strftime('%H:%M:%S')
    primary_timer.config(text = string)
    window.after(1000, mainClock)

primary_timer = tk.Label(font=('Arial',20))
primary_timer.place(relx = 1,
            rely = 0,
            anchor=tk.NE)

def updateTimer1():
    if clock1_var.get() == "00:00:00":
        global tclick
        tclick = 0
        createTimeWindow()
        
def updateTimer2():
    if clock2_var.get() == "00:00:00":
        global tclick
        tclick = 1
        createTimeWindow()
        
def updateTimer3():
    if clock3_var.get() == "00:00:00":
        global tclick
        tclick = 2
        createTimeWindow()

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

class Countdown:
    def __init__ (self, name):
        self.name = name
        self.countdown1_running = False
        self.countdown2_running = False
        self.countdown3_running = False

    def countdown1(self):
        self.countdown1_running = True
        hours = tk.StringVar()
        minutes = tk.StringVar()
        seconds = tk.StringVar()
        i = clock1_var.get()
        hours.set(i[:2])
        minutes.set(i[3:5])
        seconds.set(i[-2:])
        try:
            temp = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())
        except:
            print("Error")
        while self.countdown1_running == True:
                mins, secs = divmod (temp, 60)
                hrs, mins = divmod (mins, 60)                               
                timer = f"{hrs:02}:{mins:02}:{secs:02}"
                clock1_var.set(str(timer))
                window.after(1000, window.update())                
                if temp == 0: self.countdown1_running = False
                else: temp -=1
                
    def countdown2(self):
        self.countdown2_running = True
        hours = tk.StringVar()
        minutes = tk.StringVar()
        seconds = tk.StringVar()
        i = clock2_var.get()
        hours.set(i[:2])
        minutes.set(i[3:5])
        seconds.set(i[-2:])
        try:
            temp = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())
        except:
            print("Error")
        while self.countdown2_running == True:
                mins, secs = divmod (temp, 60)
                hrs, mins = divmod (mins, 60)                               
                timer = f"{hrs:02}:{mins:02}:{secs:02}"
                clock2_var.set(str(timer))
                window.after(1000, window.update())                
                if temp == 0: self.countdown2_running = False
                else: temp -=1
                
    def countdown3(self):
        self.countdown3_running = True
        hours = tk.StringVar()
        minutes = tk.StringVar()
        seconds = tk.StringVar()
        i = clock3_var.get()
        hours.set(i[:2])
        minutes.set(i[3:5])
        seconds.set(i[-2:])
        try:
            temp = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())
        except:
            print("Error")
        while self.countdown3_running == True:
                mins, secs = divmod (temp, 60)
                hrs, mins = divmod (mins, 60)                               
                timer = f"{hrs:02}:{mins:02}:{secs:02}"
                clock3_var.set(str(timer))
                window.after(1000, window.update())                
                if temp == 0: self.countdown3_running = False
                else: temp -=1
                
Count = Countdown("Count")

def stopTime1():
    Count.countdown1_running = False
    
def stopTime2():
    Count.countdown2_running = False
    
def stopTime3():
    Count.countdown3_running = False
    
def clearTimer1():
     clock1_var.set("00:00:00")
     Count.countdown1_running = False
    
def clearTimer2():
    clock2_var.set("00:00:00")
    Count.countdown2_running = False

def clearTimer3():
    clock3_var.set("00:00:00")
    Count.countdown3_running = False

    
button1 = tk.Button (window, text = "Task 1", command = updateTask1, width = 30)
button1.place(x = 120, y = 200)

button2 = tk.Button (window, text = "Task 2", command = updateTask2, width = 30)
button2.place(x = 120, y = 240)

button3 = tk.Button (window, text = "Task 3", command = updateTask3, width = 30)
button3.place(x = 120, y = 280) 

timer1 = tk.Button (window, textvariable = clock1_var, command = updateTimer1)
timer1.place(x = 340, y = 200)

timer2 = tk.Button (window, textvariable = clock2_var, command = updateTimer2)
timer2.place(x = 340, y = 240)

timer3 = tk.Button (window, textvariable = clock3_var, command = updateTimer3)
timer3.place(x = 340, y = 280)

pause1 = tk.Button (window, text = 'P', width = 2, command = stopTime1)
pause1.place(x = 390, y = 200)

pause2 = tk.Button (window, text = 'P', width = 2, command = stopTime2)
pause2.place(x = 390, y = 240)

pause3 = tk.Button (window, text = 'P', width = 2, command = stopTime3)
pause3.place(x = 390, y = 280)

start1 = tk.Button (window, text = 'S', width = 2, command = Count.countdown1)
start1.place(x = 412, y = 200)

start2 = tk.Button (window, text = 'S', width = 2, command = Count.countdown2)
start2.place(x = 412, y = 240)

start3 = tk.Button (window, text = 'S', width = 2, command = Count.countdown3)
start3.place(x = 412, y = 280)

clear1 = tk.Button (window, text = 'C', width = 2, command = clearTimer1)
clear1.place(x = 434, y = 200)

clear2 = tk.Button (window, text = 'C', width = 2, command = clearTimer2)
clear2.place(x = 434, y = 240)

clear3 = tk.Button (window, text = 'C', width = 2, command = clearTimer3)
clear3.place(x = 434, y = 280)

mainClock()
greeting()

window.mainloop()
