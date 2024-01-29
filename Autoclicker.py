import tkinter as tk
from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import threading

class GUI:
    def __init__(self):
        # Instance variables
        self.playing = False
        # self.listen_thread = None
        
        root = tk.Tk()
        root.geometry(f'{400}x{400}+{(root.winfo_screenwidth() - 400) // 2}+{(root.winfo_screenheight() - 400) // 2}')
        
        keyboard_listener = keyboard.Listener(on_press = self.toggle)
        keyboard_listener.start()
        root.mainloop()

    
    def click(self):
        # Continues clicking while global variable is set to true
        while self.playing:
            Controller().click(Button.left)
            print("Clicked")
            time.sleep(1/100)
 
            

    # Function to compare keypress with hotkey and toggles if matches
    def toggle(self,key):
        print(key)
        if key == keyboard.Key.space:
            self.playing = not self.playing 
            listen_thread = threading.Thread(target=self.click)
            listen_thread.start()
            
    
    
    def __del__(self):
        keyboard.Listener.stop()
        
        
clicker = GUI()