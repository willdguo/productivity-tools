# BUG FIXES:
# - deiconify makes it regain focus, even when offscreen --> lost characters counted for
# - mouse will sometimes trigger buttons to activated when hovered over
# - cross-key issues: left window key triggers q
# - double counting keys [partially resolved by setting increment to 0.5, not 1]
#
# GENERL IMPROVEMENTS:
# - color gradient based on frequency
# - entire keyboard
# - make a class for each individual key -> a) easy to manage; b) rearrange into a non-grid format



import tkinter as tk
import pynput
from pynput.keyboard import Listener
from tkinter import *
import keyboard

root = Tk()
freqs = {}

alph = 'qwertyuiopasdfghjkl;zxcvbnm,./'

def key_press(key):
    # print(key.char, " press")

    freqs[key.char] = freqs.get(key.char, 0) + 1

    if key.char in alph:
        i = alph.index(key.char)
        layout[int(i / 10)][i % 10].config(state = "disabled", background = "lightgreen", text = key.char + '\n' + str(freqs[key.char]))

def key_release(key):
    # print(key.char, " release")

    if key.char in alph:
        i = alph.index(key.char)
        layout[int(i / 10)][i % 10].config(state = "active")

def off_screen(e):
    #root.withdraw()

    input = keyboard.read_key()
    print(input)


    # abstract this into a better function for better readability + stuff
    freqs[input] = freqs.get(input, 0) + 1

    if input in alph:
        i = alph.index(input)
        layout[int(i / 10)][i % 10].config(text = input + '\n' + str(freqs[input]))

    if input == "space":
        #root.deiconify
        return
    
    root.update_idletasks()

    off_screen(e)

#/////////////

layout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(3):
    for j in range(10):
        layout[i][j] = Button(root, width = 3, height = 3, text = alph[10 * i + j], font = ('Arial', 18))
        layout[i][j].grid(row = i, column = j)

root.bind('<KeyPress>', key_press)
root.bind('<KeyRelease>', key_release)
root.bind('<FocusOut>', off_screen)

#button = Button(frame, text = "Begin Sesh", command = newSession)
#button.pack()

mainloop()

print(freqs)


