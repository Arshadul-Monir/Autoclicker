import tkinter as tk
from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
import time

top = tk.Tk()
top.resizable(False,False)

mouse = Controller()
playing = False

def click(event = None):
    global playing
    playing = not playing
    print(playing)
    while playing:
        mouse.click(Button.left)
        print("Clicked")
        time.sleep(1)
        
top.bind("<space>", click)

top.mainloop() 