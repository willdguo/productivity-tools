# Reminds you to drink water every 15 minutes. Simple as that.
# Stay hydrated, folks

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from time import sleep
import random

def minToString(i):
    hrs = int(i/60)
    mins = int(i % 60)

    output = ""

    if hrs == 0:
        output = f'{mins} mins'
    else:
        output = f'{hrs} hrs {mins} mins'
    
    return output


def newSession():
    global counter
    global duration

    root.wm_attributes("-topmost", 1)

    working = True

    if(input.get()):
        duration = int(input.get())

    while(working):
        root.deiconify()

        update()
        messagebox.showinfo('Drink Water', msg[random.randint(0, len(msg) - 1)], parent = root)
        counter += 1
        
        root.withdraw()
        sleep(duration)

def update():
    global duration
    global counter

    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text = f"Water breaks: {counter}").pack()

    #Label(frame, text = 'Working time: ' + minToString(counter * duration / 60)).pack()

counter = 0
duration = 900
msg = ['Time to drink water!', 'Stay hydrated!', "Don't forget to drink water!"]

root = Tk()

canvas = Canvas(root)
canvas.pack()

frame = Frame(canvas)
frame.pack()

Label(frame, text = "Work time (sec):").pack()

input = Entry(frame, width = 8)
input.pack()

Button(frame, text = "Begin Session", command = newSession).pack()
mainloop()




