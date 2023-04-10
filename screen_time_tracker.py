# Tracks daily screen time + current session screentime usage
# 
# FIXES:
# - clunky window interactions - fix updating every second
# - Add button to hide timer and/or add option to remove second display

import tkinter as tk
from tkinter import *
from time import sleep
import datetime

root = Tk()

dailyTimes = {}

labels_on = False

#def toggle():
#    lambda:hide_widget(l1)

def getDate():
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    return month + '/' + day

def beginTimer():
    button.destroy()

    working = True

    while working:
        intSec = int(sec.get())
        intMins = int(mins.get())
        intHrs = int(hrs.get())
        intSec += 1

        if intSec >= 60:
            intMins += 1
            intSec = 0
            dailyTimes[getDate()] = dailyTimes.get(getDate(), 0) + 1
        
        if intMins >= 60:
            intHrs += 1
            intMins = 0
        
        screen_time = dailyTimes.get(getDate(), 0)

        daily_hours = str(int(screen_time / 60))
        daily_mins = str(int(screen_time % 60))
        
        output = [str(intHrs), str(intMins), str(intSec), daily_hours, daily_mins]

        for i in range(5):
            if len(output[i]) < 2:
                output[i] = '0' + output[i]       


        hrs.set(output[0])
        mins.set(output[1])
        sec.set(output[2])
        daily.set(f'{getDate()} Screen Time: {output[3]} hrs {output[4]} mins')        

        #print(getDate())

        sleep(1)

        root.update()

hrs = StringVar()
mins = StringVar()
sec = StringVar()
daily = StringVar() 

hrs.set('00')
mins.set('00')
sec.set('00')
daily.set(f'{getDate()} Screen Time: {dailyTimes.get(getDate(), 0)}')


canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

frame = LabelFrame(canvas)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

l1 = Label(frame, textvariable = hrs).place(relx = 0.1, rely = 0.4)
l2 = Label(frame, textvariable = mins).place(relx = 0.4, rely = 0.4)
l3 = Label(frame, textvariable = sec).place(relx = 0.7, rely = 0.4)
l4 = Label(frame, textvariable = daily).place(relx = 0.1, rely = 0.6)


button = Button(frame, command = beginTimer, text = 'Begin Timer')
button.pack()


mainloop()

