import tkinter as tk    
from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import threading


# Global variables
playing = False
cps = 10
keybinds = {
    "pause_unpause": keyboard.Key.space,
    "increment_speed": keyboard.Key.up,     # to be implemented
    "decrement_speed": keyboard.Key.down,   # to be implemented
}
current_binding_key = None
hotkey_listener = None

# Starts a new keyboard Listener in the choose_key function
def bind(keybind):
    global current_binding_key, hotkey_listener
    current_binding_key = keybind
    hotkey_listener = keyboard.Listener(on_press=choose_key)
    hotkey_listener.start()    

# Takes listened key 
def choose_key(key):
    print("you pressed", key)
    global current_binding_key
    if current_binding_key:
        keybinds[current_binding_key] = key
        current_binding_key = None
        hotkey_listener.stop()
        print("Binding complete.")
    
    

def click():
    global cps
    # Continues clicking while global variable is set to true
    while playing:
        Controller().click(Button.left)
        print("Clicked")
        if cps != 0:
            time.sleep(1/cps)


# Stops the listener and closes the window
def on_close():
    global keyboard_listener
    keyboard_listener.stop()  
    root.destroy()

# Sets clicking speed when submit button is pressed
def submit_speed():
    global cps
    if int(speed.get()) == 0 or int(speed.get()) > 100:
        print("Invalid input. Please enter a valid number for CPS")
        return
    cps = int(speed.get())


# Function to compare keypress with hotkey and toggles if matches
def toggle(key):    
    global playing
    print(key, not playing)
    if key == keyboard.Key.space:
        playing = not playing 
        listen_thread = threading.Thread(target=click)
        listen_thread.start()
    
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

# No work yet
# binding_button = tk.Button(root, text="Bind Hotkey", command=lambda: bind("pause_unpause"))
# binding_button.pack()

# position_button = tk.Button(root, text="Choose Position", command=click_position)
# position_button.pack()

keyboard_listener = keyboard.Listener(on_press = toggle)
keyboard_listener.start()

tk.mainloop()