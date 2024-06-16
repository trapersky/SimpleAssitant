import string
from time import strftime
import tkinter as tk
import os

window = tk.Tk()
window.title("Simple_Assistant")
window.geometry("640x480")
window.minsize(400, 400)

name = os.getlogin()

def greeting():
    string = f"Hello {name}!"
    hello.config(text = string)
    
hello = tk.Label(font=("Arial", 20))
hello.place(relx=0,
            rely=0,
            anchor=tk.NW)

def clock():
    string = strftime('%H:%M:%S')
    timer.config(text = string)
    timer.after(1000, clock)

timer = tk.Label(font=('Arial',20))
timer.place(relx = 1,
            rely=0,
            anchor=tk.NE)

clock()
greeting()

window.mainloop()
