# features to add:
# - make timer reliant on datetime.now as opposed to counter (wastes cpu on program time)
# - keep screentime tracker on as timer stops
# - option to remove/hide timer aspect
# - abstract single-to-double-digit function
# - create "break" counter

from tkinter import *
from time import sleep
from os.path import *
import json
import datetime

root = Tk()
screen_times = {}
# work_sessions = {}
working = False

# loads days from dict.json
if isfile('dict.json'): # check if dict.json exists
    with open('dict.json') as f:
        screen_times = json.load(f)

# returns date in the format month/day
def getDate():
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    return month + '/' + day

# converts int to time
# input: num - number of seconds
# output: tuple formatted as (sec, min, hrs)
def intToTime(num):
    a = int(num % 60)
    b = int( (num % 3600)//60 )
    c = int( num//3600 )

    return (a, b, c)

def toDoubleDigits(tuple):
    output = ()

    for i in tuple:
        j = str(i)

        if len(j) < 2:
            j = '0' + j
        
        output += (j,)
    
    return output

# begins timer counting
def beginTimer():
    global working
    working = True
    # updates window every increment seconds. increase for time precision; decrease for lower latency
    increment = 0.25
    counter = 1

    # runs permanent loop until working is turned off via stopTimer()
    while working:
        counter += increment
        intSec, intMins, intHrs = intToTime(counter)

        if counter % 60 == 0:  # updates screen_times every minute, or every time counter reaches a multiple of 60
            screen_times[getDate()] = screen_times.get(getDate(), 0) + 1

        screen_time = screen_times.get(getDate(), 0) # gets current daily screen time for display
        daily_mins, daily_hours, _ = intToTime(screen_time)
        
        output = toDoubleDigits((intHrs, intMins, intSec, daily_hours, daily_mins))

        hrs.set(output[0])
        mins.set(output[1])
        sec.set(output[2])
        daily.set(f'{getDate()} Screen Time: {output[3]} hrs {output[4]} mins')        

        sleep(increment)
        root.update()

def stopTimer():
    global working
    working = False

def end():
    global working
    working = False
    print("closed window")
    root.destroy()

hrs = StringVar()
mins = StringVar()
sec = StringVar()
daily = StringVar() 

hrs.set('00')
mins.set('00')
sec.set('00')
daily.set(f'{getDate()} Screen Time: {screen_times.get(getDate(), 0)}')


canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

frame = LabelFrame(canvas)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

Label(frame, textvariable = hrs).place(relx = 0.1, rely = 0.4)
Label(frame, textvariable = mins).place(relx = 0.4, rely = 0.4)
Label(frame, textvariable = sec).place(relx = 0.7, rely = 0.4)
Label(frame, textvariable = daily).place(relx = 0.1, rely = 0.6)


button = Button(frame, command = beginTimer, text = 'Start Timer')
button.pack()

button1 = Button(frame, command = stopTimer, text = "Stop Timer")
button1.pack()

root.protocol("WM_DELETE_WINDOW", end)
mainloop()

save = json.dumps(screen_times)
with open('dict.json', 'w') as f:
    f.write(save)
    f.close()

