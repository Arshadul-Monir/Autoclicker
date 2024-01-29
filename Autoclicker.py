import tkinter as tk
from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import threading


# Global variables
playing = False
cps = 10


def click():
    global cps
    # Continues clicking while global variable is set to true
    while playing:
        Controller().click(Button.left)
        print("Clicked")
        if cps != 0:
            time.sleep(1/cps)

        

# Function to compare keypress with hotkey and toggles if matches
def toggle(key):
    global playing
    print(key, not playing)
    if key == keyboard.Key.space:
        playing = not playing 
        listen_thread = threading.Thread(target=click)
        listen_thread.start()

# Sets clicking speed when submit button is pressed
def submit_speed():
    global cps
    try:
        cps = int(speed.get())
    except ValueError:
        print("Invalid input. Please enter a valid number for CPS.")

# Stops the listener and closes the window
def on_close():
    keyboard_listener.stop()  
    root.destroy()
    
# Returns if entry if integer for speed input field
def validate(P):
    return P.isdigit() or P == ""

root = tk.Tk()
root.title("Auto Clicker")

root.geometry(f'{400}x{400}+{(root.winfo_screenwidth() - 400) // 2}+{(root.winfo_screenheight() - 400) // 2}')
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

instructions_label = tk.Label(frame, text="Press the spacebar to toggle auto-clicking")
instructions_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

speed_label = tk.Label(frame, text="Clicks per Second (CPS):")
speed_label.grid(row=1, column=0, sticky="E", pady=(0, 10))

speed = tk.Entry(frame, validate='all', validatecommand=(frame.register(validate), '%P'))
speed.grid(row=1, column=1, pady=(0, 10))

speed_button = tk.Button(root, text = "Submit CPS", command = submit_speed)
speed_button.pack()
root.protocol("WM_DELETE_WINDOW", on_close)


keyboard_listener = keyboard.Listener(on_press = toggle)
keyboard_listener.start()

root.mainloop()



