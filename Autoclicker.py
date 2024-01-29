import tkinter as tk
from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import threading

class GUI:
    def __init__(self):
        # Instance variables
        self.playing = False
        
        self.root = tk.Tk()
        self.root.geometry(f'{400}x{400}+{(self.root.winfo_screenwidth() - 400) // 2}+{(self.root.winfo_screenheight() - 400) // 2}')
        
        self.keyboard_listener = keyboard.Listener(on_press = self.toggle)
        self.keyboard_listener.start()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.root.mainloop()

    
    def click(self):
        # Continues clicking while global variable is set to true
        while self.playing:
            Controller().click(Button.left)
            print("Clicked")
            time.sleep(2)
 
            

    # Function to compare keypress with hotkey and toggles if matches
    def toggle(self,key):
        print(key)
        if key == keyboard.Key.space:
            self.playing = not self.playing 
            listen_thread = threading.Thread(target=self.click)
            listen_thread.start()
            
    
    
    def on_close(self):
        self.keyboard_listener.stop()
        self.root.destroy()
        
        
clicker = GUI()